---
title: 在 xlsx4j 中将工作簿转换为 HTML
type: docs
weight: 10
url: /zh/java/convert-workbook-to-html-in-xlsx4j/
---
## **Aspose.Cells - 将工作簿转换为 HTML**
 Aspose.Cells API 支持将电子表格导出为 HTML 格式。以此目的，**Aspose.Cells**使用**HtmlSave选项**允许开发人员控制输出 HTML 的几个方面的类。

**Java**

{{< highlight "java" >}}

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

欲了解更多详情，请访问[将 Excel 文件转换为 HTML](/cells/zh/java/converting-workbook-to-different-formats/).

{{% /alert %}}
