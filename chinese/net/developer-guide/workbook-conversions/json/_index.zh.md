---
title: Json
type: docs
weight: 300
url: /zh/net/convert-workbook-to-json/
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为Json（JavaScript对象表示）文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

Aspose.Cells API支持将电子表格转换为JSON格式。要将工作簿导出为JSON，请将[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法的第二个参数传递。您还可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)类来指定导出工作表到JSON的其他设置。

以下代码示例演示了如何使用[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出为Json。请查看用于参考的代码将[源文件](book1.xlsx)转换为[输出Json文件](book1.Json)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **高级主题**
- [将CSV转换为JSON](/cells/zh/net/convert-csv-to-json/)
- [将Excel转换为JSON](/cells/zh/net/convert-excel-to-json/)
- [将JSON转换为CSV](/cells/zh/net/convert-json-to-csv/)
- [将JSON转换为Excel](/cells/zh/net/convert-json-to-excel/)
{{< app/cells/assistant language="csharp" >}}
