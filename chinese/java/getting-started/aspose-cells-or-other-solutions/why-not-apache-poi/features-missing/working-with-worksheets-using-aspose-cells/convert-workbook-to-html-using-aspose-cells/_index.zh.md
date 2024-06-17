---
title: 使用Aspose.Cells将工作簿转换为HTML
type: docs
weight: 20
url: /zh/java/convert-workbook-to-html-using-aspose-cells/
---

## **Aspose.Cells - 将工作簿转换为HTML**
Aspose.Cells的API支持将电子表格导出为HTML格式。为此，**Aspose.Cells**使用**HtmlSaveOptions**类，该类允许开发人员控制输出HTML的多个方面。

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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

更多详情，请访问[将Excel文件转换为HTML](/cells/zh/java/converting-workbook-to-different-formats/)。

{{% /alert %}}
