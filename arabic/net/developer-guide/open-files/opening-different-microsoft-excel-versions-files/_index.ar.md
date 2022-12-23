---
title: فتح ملفات إصدارات Excel Microsoft المختلفة
type: docs
weight: 20
url: /ar/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح نطاق من ملفات إصدارات Excel Microsoft المختلفة ، مثل Microsoft Excel 95/97-2003 ، SpreadsheetML ، فتح Microsoft Excel 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات Excel المشفرة.

{{% /alert %}}

## **فتح ملفات مختلفة من إصدارات إكسل Microsoft**

 غالبًا ما يجب أن يكون التطبيق قادرًا على فتح ملفات Excel Microsoft التي تم إنشاؤها في إصدارات مختلفة ، على سبيل المثال ، Microsoft Excel 95،97 أو Microsoft Excel 2007/2010/2013/2016/2019 و Office 365. قد تحتاج إلى تحميل ملف بأي من التنسيقات المتعددة ، بما في ذلك XLS ، XLSX ، XLSM ، XLSB ، SpreadsheetML ، TabDelimited أو TSV ، CSV ، ODS وما إلى ذلك. استخدم المنشئ أو حدد**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** صف دراسي'**[تنسيق الملف] (https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)**نوع السمة التي تحدد التنسيق باستخدام**[FileFormatType] (https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**تعداد.

 ال**[FileFormatType] (https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا والتي يرد بعضها أدناه.

|**أنواع تنسيق الملف**|**وصف**|
|:- |:- |
|Csv|يمثل ملف CSV|
|إكسل 97 إلى 2003|يمثل ملف Excel 97 - 2003|
|xlsx|يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSX|
|Xlsm|يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSM|
|Xltx|يمثل ملف Excel 2007/2010/2013/2016/2019 ونموذج Office 365 XLTX|
|Xltm|يمثل ملف XLTM ممكّن للماكرو في Excel 2007/2010/2013/2016/2019 و Office 365|
|Xlsb|يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 ثنائي XLSB|
|SpreadsheetML|يمثل ملف SpreadsheetML|
|Tsv|يمثل ملف قيم مفصولة بعلامات جدولة|
|TabDelimited|يمثل ملفًا نصيًا محددًا بعلامات جدولة|
|أود|يمثل ملف ODS|
|لغة البرمجة|يمثل ملف HTML|
|Mhtml|يمثل ملف MHTML|

### **فتح Microsoft ملفات Excel 95 / 5.0**

لفتح ملف Microsoft Excel 95 / 5.0 ، استخدم**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**وقم بتعيين السمة ذات الصلة لـ**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**فئة ملف القالب المراد تحميله. يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **فتح Microsoft ملفات Excel 97-2003**

 لفتح ملف Microsoft Excel 97-2003 ، استخدم**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** وقم بتعيين السمة ذات الصلة لـ**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**فئة ملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **فتح Microsoft Excel 2007/2010/2013/2016/2019 وملفات Office 365 XLSX**

لفتح تنسيق Microsoft Excel 2007/2010/2013/2016/2019 وتنسيق Office 365 ، أي XLSX أو XLSB ، حدد مسار الملف. تستطيع ايضا استخذام**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** وقم بتعيين السمة / الخيارات ذات الصلة لـ**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**فئة ملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **فتح ملفات اكسل المشفرة**

 من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر ، استخدم ملحق**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**وقم بتعيين سماته وخياراته (على سبيل المثال ، أعط كلمة مرور) لملف القالب المراد تحميله.
يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الرابط التالي:

[اكسل مشفر](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

يدعم Aspose.Cells أيضًا فتح ملفات Microsoft المحمية بكلمة مرور في Excel 2007 و 2010 و 2013 و 2016 و 2019 و Office 365.


