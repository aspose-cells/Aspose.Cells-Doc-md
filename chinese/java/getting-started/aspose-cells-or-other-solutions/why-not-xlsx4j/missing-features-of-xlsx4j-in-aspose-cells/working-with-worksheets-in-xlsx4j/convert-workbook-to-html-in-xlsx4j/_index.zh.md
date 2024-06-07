---
title: 在xlsx4j中将电子表格转换为HTML
type: docs
weight: 10
url: /zh/java/convert-workbook-to-html-in-xlsx4j/
---

## **Aspose.Cells - 将工作簿转换为HTML**
Aspose.Cells API提供了将电子表格导出为HTML格式的支持。为此, **Aspose.Cells**使用 **HtmlSaveOptions** 类，允许开发人员控制输出HTML的多个方面。

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[将Excel文件转换为HTML](/cells/zh/java/converting-workbook-to-different-formats/)

{{% /alert %}}
