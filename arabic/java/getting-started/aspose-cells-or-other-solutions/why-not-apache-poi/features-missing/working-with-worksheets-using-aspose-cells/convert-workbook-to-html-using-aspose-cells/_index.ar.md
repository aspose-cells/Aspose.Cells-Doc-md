---
title: تحويل دفتر العمل إلى HTML باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/convert-workbook-to-html-using-aspose-cells/
---

## **Aspose.Cells - تحويل دفتر العمل إلى HTML**
توفر واجهات برمجة التطبيقات Aspose.Cells دعمًا لتصدير الجداول الإلكترونية إلى تنسيق HTML. لهذا الغرض، يستخدم **Aspose.Cells** فئة **HtmlSaveOptions** التي تسمح للمطورين بالتحكم في عدة جوانب من ال HTML الناتج.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تحويل ملفات Excel إلى HTML](/cells/ar/java/converting-workbook-to-different-formats/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
