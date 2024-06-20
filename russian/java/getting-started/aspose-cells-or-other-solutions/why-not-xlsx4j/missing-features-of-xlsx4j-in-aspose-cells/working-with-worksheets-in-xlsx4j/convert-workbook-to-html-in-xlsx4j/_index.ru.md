---
title: Преобразовать книгу в формат HTML в xlsx4j
type: docs
weight: 10
url: /ru/java/convert-workbook-to-html-in-xlsx4j/
---

## **Aspose.Cells - Преобразование книги в формат HTML**
API Aspose.Cells обеспечивает поддержку экспорта электронных таблиц в формат HTML. Для этой цели **Aspose.Cells** использует класс **HtmlSaveOptions**, который позволяет разработчикам контролировать несколько аспектов выходного HTML.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

Дополнительные сведения см. на странице [Преобразование файлов Excel в HTML](/cells/ru/java/converting-workbook-to-different-formats/).

{{% /alert %}}
