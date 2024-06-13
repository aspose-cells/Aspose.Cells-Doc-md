---
title: 已知限制
type: docs
weight: 50
url: /zh/jasperreports/known-limitations/
---

{{% alert color="primary" %}} 

以下是目前不支持 Aspose.Cells for JasperReports 的功能列表：

- **没有自动安装程序**。Aspose.Cells for JasperReports 以ZIP存档方式分发。[要安装](/cells/zh/jasperreports/installation/)，请解压并将文件复制到适当位置，可能需要编辑一些XML配置文件。将来会提供自动安装程序。
- **Excel 不支持所有 JasperReports 图表类型**。JasperReports 中的某些图表类型与 Microsoft Excel 的图表不兼容，例如：XYBarChart、XYAreaChart、ThermometerChart、CandlestickChart、HighLowChart、MultipleAxisChart 和 MeterChart。这些图表将被导出为图片，与原始的 JasperReports XLS 导出器处理图表的方式相同。（其他图表将被导出为可编辑图表。）

{{% /alert %}}
