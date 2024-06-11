---
title: 转换Excel为JSON
type: docs
weight: 20
url: /zh/java/convert-excel-to-json/
description: 了解如何使用 Aspose.Cells for Java API 将Excel文件转换为JSON。
keywords: Java将工作簿导出为json，使用Java将Excel转换为JSON，在Java中保存Excel为JSON，使用Java将工作簿转换为JSON，在Java中保存工作簿为JSON，导出Excel为JSON via Java。
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为Json(JavaScript对象表示)文件。

{{% /alert %}}

## **如何将Excel工作簿转换为JSON**

不用纠结如何将Excel工作簿转换为JSON，因为Aspose.Cells Java库拥有最佳解决方案。Aspose.Cells Java API支持将电子表格转换为JSON格式。要将工作簿导出为JSON，请将[**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)作为[**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)方法的第二个参数传递。您还可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions)类指定导出工作表到JSON的附加设置。

以下代码示例演示了将Excel工作簿导出为Json。请查看代码将[源文件](sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

以下代码示例示范了使用JsonSaveOptions类指定附加设置，从而导出Excel工作簿为Json。请参阅转换[源文件](sample.xlsx)到代码生成的Json文件的代码以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
