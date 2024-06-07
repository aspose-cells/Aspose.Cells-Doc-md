---
title: 页面设置
type: docs
weight: 80
url: /zh/reportingservices/page-setup/
---

配置包括两个部分和8种页面设置属性。这些属性包括名称、索引、FitToPagesTall、FitToPagesWide、TopMargin、FooterMargin、HeaderMargin、BottomMargin、LeftMargin、RightMargin。

- **name** 代表报告名称，当名称为空时代表整个报告。
- **index** 代表导出的 Excel 文件的工作表索引。
- **FitToPagesTall** 代表打印时工作表将按比例缩放到的纵向页面数。
- **FitToPagesWide** 代表打印时工作表将按比例缩放到的横向页面数。
- **FooterMargin** 代表页面底部到页脚的距离，以厘米为单位。
- **HeaderMargin** 代表页面顶部到页眉的距离，以厘米为单位。
- **LeftMargin** 代表左边距的大小，以厘米为单位。
- **RightMargin** 代表右边距的大小，以厘米为单位。
- **TopMargin** 代表顶部边距的大小，以厘米为单位。
- **BottomMargin** 代表底部边距的大小，以厘米为单位。

PageSetup 配置示例：

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
