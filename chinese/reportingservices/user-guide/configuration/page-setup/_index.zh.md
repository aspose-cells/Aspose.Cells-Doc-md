---
title: 页面设置
type: docs
weight: 80
url: /zh/reportingservices/page-setup/
---

配置包括两个部分和 8 种页面设置属性。这些属性包括名称、索引、FitToPagesTall、FitToPagesWide、上边距、底部边距、页眉边距、页脚边距、左边距和右边距。

- **名称** 表示报告名称，当名称为空时表示整个报告。
- **索引** 表示导出的 Excel 文件的工作表索引。
- **FitToPagesTall** 表示打印时工作表将被缩放到的页面高度。
- **FitToPagesWide** 表示打印工作表时将被缩放到的页面宽度。
- **FooterMargin** 表示页脚距离页面底部的距离，以厘米为单位。
- **HeaderMargin** 表示页眉距离页面顶部的距离，以厘米为单位。
- **LeftMargin** 表示左边距的大小，以厘米为单位。
- **RightMargin** 表示右边距的大小，以厘米为单位。
- **TopMargin** 表示顶部边距的大小，以厘米为单位。
- **BottomMargin** 表示底部边距的大小，以厘米为单位。

PageSetup 配置示例：

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
