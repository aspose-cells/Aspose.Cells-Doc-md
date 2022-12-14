---
title: تحويل المصنف إلى HTML باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/convert-workbook-to-html-using-aspose-cells/
---
## **Aspose.Cells - تحويل المصنف إلى HTML**
 توفر واجهات برمجة التطبيقات Aspose.Cells دعمًا لتصدير جداول البيانات إلى تنسيق HTML. لهذا الغرض،**Aspose.Cells** يستخدم**خيارات HtmlSave** فئة تسمح للمطورين بالتحكم في العديد من جوانب HTML الناتج.

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تحويل ملفات Excel إلى HTML](/cells/ar/java/converting-workbook-to-different-formats/).

{{% /alert %}}
