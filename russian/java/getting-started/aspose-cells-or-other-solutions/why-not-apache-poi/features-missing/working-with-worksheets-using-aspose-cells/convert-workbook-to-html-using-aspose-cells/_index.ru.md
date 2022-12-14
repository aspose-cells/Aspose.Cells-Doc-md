---
title: Преобразование рабочей книги в HTML с помощью Aspose.Cells
type: docs
weight: 20
url: /ru/java/convert-workbook-to-html-using-aspose-cells/
---
## **Aspose.Cells - Преобразование рабочей книги в HTML**
 API-интерфейсы Aspose.Cells обеспечивают поддержку экспорта электронных таблиц в формат HTML. Для этого**Aspose.Cells** использует**Хтмлсавеоптионс** class, который позволяет разработчикам контролировать несколько аспектов выходного HTML.

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Преобразование файлов Excel в HTML](/cells/ru/java/converting-workbook-to-different-formats/).

{{% /alert %}}
