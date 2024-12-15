import scrapy
import json
import os
import re

class FeiyiSpider(scrapy.Spider):
    name = 'feiyi'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/wikitag/api/getlemmas']

    def start_requests(self):
        # 初始请求的负载数据，设置适当的过滤器以获取非遗项目
        payload = {
            "limit": 20,  # 你可以增加这个值来获取更多项目
            "timeout": 3000,
            "filterTags": '["71377",0]',
            "tagId": 71394,
            "fromLemma": False,
            "contentLength": 40,
            "page": 0  # 根据需要修改分页
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        yield scrapy.FormRequest(
            url=self.start_urls[0],
            method="POST",
            formdata={key: str(value) for key, value in payload.items()},
            headers=headers,
            callback=self.parse
        )

    def parse(self, response):
        # 解析返回的 JSON 数据
        data = json.loads(response.text)
     #   self.log(json.dumps(data, indent=4, ensure_ascii=False))  # 打印调试信息
        items = data.get("lemmaList", [])  # 获取项目列表，调整获取条目的数量

        for item in items[:5]:
            name = item.get("lemmaTitle")
            detail_url = item.get("lemmaUrl")
            if detail_url and not detail_url.startswith("http"):
                detail_url = "https://baike.baidu.com" + detail_url
            if name and detail_url:
                # 对每个项目，发送请求去抓取详细页面
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.parse_detail,
                    meta={"project_name": name}
                )
            

    def parse_detail(self, response):
        name = response.meta["project_name"]
        # 获取项目的详细介绍
        content = ''.join(response.xpath('//span[@class="text_sCq_F"]//text()').getall()).strip()
        url = response.url

        # 确认抓取到内容
        if content:
            # 替换多余的空白字符和格式化段落
            content = content.replace('\n', '\n\n')  # 保证段落间有空行
            content = re.sub(r'\s+', ' ', content)  # 替换多余的空格为单个空格
            # 格式化文件内容，添加项目名称和 URL
            header = f"Project Name: {name}\nURL: {url}\n\n"
            full_content = header + content
            # 创建输出目录
            output_dir = os.path.join(os.getcwd(), "output_files")
            self.log(f"Current working directory: {os.getcwd()}")

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                self.log(f"Created directory: {output_dir}")  # 调试信息，确保目录创建成功

            # 生成合法的文件名
            filename = self.clean_filename(name) + ".txt"
            file_path = os.path.join(output_dir, filename)

            self.log(f"Trying to write to: {file_path}")  # 确认生成的文件路径

            # 保存文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(full_content)

            self.log(f"Saved file: {file_path}")
        else:
            self.log(f"No content for project: {name}")

    def clean_filename(self, filename):
        # 清理文件名中的非法字符，例如：/ \ : * ? " < > | 等
        return re.sub(r'[\\/:*?"<>|]', '_', filename)