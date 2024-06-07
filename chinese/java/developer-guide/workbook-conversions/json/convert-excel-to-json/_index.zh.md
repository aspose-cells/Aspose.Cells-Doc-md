---
title: 将Excel转换为JSON
type: docs
weight: 20
url: /zh/java/convert-excel-to-json/
description: 学习如何使用 Aspose.Cells for Java API 将 excel 文件转换为 json。
keywords: Java 将工作簿导出为 JSON，使用 Java 将 Excel 转换为 JSON，保存 Excel 为 JSON 在 Java 中，使用 Java 将工作簿转换为 JSON，使用 Java 导出 Excel 为 JSON，使用 Java 通过 JSON 导出工作簿到 JSON。
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为JSON(JavaScript对象表示)文件。

{{% /alert %}}

## **如何将 Excel 工作簿转换为 JSON**

无需纠结如何将 Excel 工作簿转换为 JSON，因为 Aspose.Cells Java 库有最佳解决方案。Aspose.Cells Java API 支持将电子表格导出为 JSON 格式。要将工作簿导出到 JSON，请将 [**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) 作为 [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) 方法的第二个参数。也可以使用 [**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) 类来指定导出工作表到 JSON 的附加设置。

以下代码示例演示了将 Excel 工作簿导出为 JSON。请参阅用于将 [源文件](sample.xlsx) 转换为代码生成的 Json 文件的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

以下代码示例使用JsonSaveOptions类指定额外设置来演示将Excel工作簿导出为Json。请查看代码，将源文件(sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
