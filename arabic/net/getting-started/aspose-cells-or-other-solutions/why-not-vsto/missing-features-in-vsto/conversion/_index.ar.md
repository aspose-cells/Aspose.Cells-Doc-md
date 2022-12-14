---
title: تحويلات
type: docs
weight: 30
url: /ar/net/conversion/
---
Aspose.Cells ميزة فريدة توفر مرونة في تحويلات الإصدارات دون التأثير على العمل.
SaveFormat هو تعداد يمكنه تحويل المستند في الامتدادات الواردة أدناه في الجدول.

|**اسم عضو** |**قيمة** |**وصف** |
|:- |:- |:- |
| CSV|1 | يمثل ملف CSV.|
| xlsx|6 | يمثل ملف xlsx.|
| Xlsm|7 | يمثل ملف xlsm الذي يمكّن وحدات الماكرو.|
| Xltx|8 | يمثل ملف xltx.|
| Xltm|9 | يمثل ملف xltm الذي يمكّن وحدات الماكرو.|
| علامة التبويب محدد|11 | يمثل ملفًا نصيًا محددًا بعلامات جدولة.|
| لغة البرمجة|12 | يمثل ملف html.|
| هتمل|17 | يمثل ملف mhtml.|
| المواد المستنفدة للأوزون|14 | يمثل ملف ods.|
| إكسل 97 إلى 2003|5 | يمثل ملف Excel97-2003 xls.|
| SpreadsheetML|15 | يمثل ملف Excel 2003 xml.|
| Xlsb|16 | يمثل ملف xlsb.|
| آلي|0 |في حالة حفظ الملف على القرص ، يتوافق تنسيق تنسيق الملف مع امتداد اسم الملف.<br> في حالة حفظ الملف في الدفق ، يكون تنسيق الملف هو xlsx.|
| مجهول|255 | يمثل تنسيقًا غير معروف ، لا يمكن حفظه.|
| بي دي إف|13 | يمثل ملف PDF.|
| XPS|20 | يمثل ملف XPS.|
| شجار|21 | يمثل ملف TIFF.|
| SVG|22 | يمثل ملف SVG.|
| فرق|30 | تنسيق تبادل البيانات.|
يوجد أدناه مقتطف الشفرة الذي يعرض التحويل من xls إلى xlsx ، ويمكنك القيام بذلك أيضًا بالعكس

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
