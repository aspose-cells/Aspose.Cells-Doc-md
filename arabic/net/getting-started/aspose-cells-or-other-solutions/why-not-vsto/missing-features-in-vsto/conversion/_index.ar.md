---
title: تحويل
type: docs
weight: 30
url: /ar/net/conversion/
---

ميزة فريدة من نوعها في Aspose.Cells التي توفر مرونة في تحويل الإصدارات دون التأثير على العمل.
SaveFormat هو تعداد يمكنه تحويل المستند في الامتدادات المذكورة أدناه في الجدول.

|**اسم العضو** |**القيمة** |**الوصف** |
| :- | :- | :- |
|CSV |1 |يمثل ملف CSV. |
|Xlsx |6 |يمثل ملف xlsx. |
|Xlsm |7 |يمثل ملف xlsm الذي يتيح الماكرو. |
|Xltx |8 |يمثل ملف xltx. |
|Xltm |9 |يمثل ملف xltm الذي يتيح الماكرو. |
|TabDelimited |11 |يمثل ملف نص محدد بواسطة الألسنة. |
|Html |12 |يمثل ملف HTML. |
|MHtml |17 |يمثل ملف MHTML. |
|ODS |14 |يمثل ملف ods. |
|Excel97To2003 |5 |يمثل ملف Excel97-2003 xls. |
|SpreadsheetML |15 |يمثل ملف Excel 2003 xml. |
|Xlsb |16 |يمثل ملف xlsb. |
|Auto |0 |في حال حفظ الملف على القرص، يتم تنسيق الملف وفقًا للاسم النهائي للملف. <br> إذا تم حفظ الملف على التيار، يكون تنسيق الملف هو xlsx. |
|Unknown |255 |يمثل تنسيق غير معترف به، لا يمكن حفظه. |
|Pdf |13 | يمثل ملف Pdf. |
|XPS |20 | يمثل ملف XPS. |
|TIFF |21 | يمثل ملف TIFF. |
|SVG |22 | يمثل ملف SVG. |
|Dif |30 | تنسيق تبادل البيانات. |
أدناه مقتطف من الكود يظهر تحويل من xls إلى xlsx يمكنك القيام به بالعكس أيضًا

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **تحميل رمز عينة**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
