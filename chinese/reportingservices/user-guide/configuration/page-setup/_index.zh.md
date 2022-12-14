---
title: 页面设置
type: docs
weight: 80
url: /zh/reportingservices/page-setup/
---
该配置包括两个部分和 8 种页面设置属性。这些属性包括名称、索引、FitToPagesTall、FitToPagesWide、TopMargin、FooterMargin、HeaderMargin、BottomMargin、LeftMargin 和 RightMargin。

- **姓名**代表报表名称，当name为空时代表整个报表。
- **指数**表示导出的 Excel 文件的工作表索引。
- **适合页面高**表示工作表在打印时将缩放到的页数。
- **适合页面宽度**表示工作表在打印时将缩放到的页宽数。
- **页脚边距**表示页面底部到页脚的距离，单位为厘米。
- **页眉边距**表示从页面顶部到页眉的距离，以厘米为单位。
- **左边距**表示左边距的大小，以厘米为单位。
- **右边距**表示右边距的大小，以厘米为单位。
- **顶边距**表示上边距的大小，单位为厘米。
- **底边距**表示下边距的大小，以厘米为单位。

PageSetup 配置示例：

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
