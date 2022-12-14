---
title: فتح ملفات إصدارات Excel Microsoft المختلفة
type: docs
weight: 20
url: /ar/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح نطاق من ملفات إصدارات Excel Microsoft المختلفة ، مثل Microsoft Excel 95/97-2003 ، SpreadsheetML ، فتح Microsoft Excel 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات Excel المشفرة.

{{% /alert %}}

## **فتح ملفات مختلفة من إصدارات إكسل Microsoft**

 غالبًا ما يجب أن يكون التطبيق قادرًا على فتح ملفات Excel Microsoft التي تم إنشاؤها في إصدارات مختلفة ، على سبيل المثال ، Microsoft Excel 95،97 أو Microsoft Excel 2007/2010/2013/2016/2019 و Office 365. قد تحتاج إلى تحميل ملف بأي تنسيق من عدة تنسيقات ، بما في ذلك XLS و XLSX و XLSM و XLSB و SpreadsheetML و TabDelimited أو TSV و CSV و ODS وما إلى ذلك. استخدم المنشئ أو حدد**دفتر العمل** صف دراسي'**تنسيق الملف** نوع السمة التي تحدد التنسيق باستخدام**نوع الملف**تعداد.

 ال**نوع الملف**يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا والتي يرد بعضها أدناه.

|**أنواع تنسيق الملف**|**وصف**|
|:- |:- |
|CSV|يمثل ملف CSV|
|اكسل_97_TO_2003|يمثل ملف Excel 97 - 2003|
|XLSX|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSX|
|XLSM|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSM|
|Xltx|يمثل ملف Excel 2007/2010/2013/2016/2019 وقالب Office 365 XLTX|
|XLTX|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف XLTM ممكّن للماكرو في Office 365|
|XLSB|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 الثنائي XLSB|
|SPREADSHEET_ML|يمثل ملف SpreadsheetML|
|ملف TSV|يمثل ملف قيم مفصولة بعلامات جدولة|
|علامة التبويب محدد|يمثل ملفًا نصيًا محددًا بعلامات جدولة|
|المواد المستنفدة للأوزون|يمثل ملف ODS|
|لغة البرمجة|يمثل ملف HTML|
|M_HTML|يمثل ملف MHTML|

### **فتح Microsoft ملفات Excel 95 / 5.0**

لفتح ملف Microsoft Excel 95 / 5.0 ، استخدم**LoadOptions**وقم بتعيين السمة ذات الصلة لـ**LoadOptions**فئة ملف القالب المراد تحميله. يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **فتح Microsoft ملفات Excel 97-2003**

 لفتح ملف Microsoft Excel 97-2003 ، استخدم**LoadOptions** وقم بتعيين السمة ذات الصلة لـ**LoadOptions**فئة ملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **فتح Microsoft Excel 2007/2010/2013/2016/2019 وملفات Office 365 XLSX**

 لفتح تنسيق Microsoft Excel 2007/2010/2013/2016/2019 وتنسيق Office 365 ، أي XLSX أو XLSB ، حدد مسار الملف. تستطيع ايضا استخذام**LoadOptions** وقم بتعيين السمة / الخيارات ذات الصلة لـ**LoadOptions**فئة ملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **فتح ملفات اكسل المشفرة**

 من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر ، استخدم ملحق**LoadOptions**وقم بتعيين سماته وخياراته (على سبيل المثال ، أعط كلمة مرور) لملف القالب المراد تحميله.
يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الرابط التالي:

[اكسل مشفر](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

يدعم Aspose.Cells أيضًا فتح ملفات Microsoft المحمية بكلمة مرور في Excel 2007 و 2010 و 2013 و 2016 و 2019 و Office 365.


