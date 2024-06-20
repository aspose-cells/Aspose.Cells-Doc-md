---
title: فتح ملفات إكسل المختلفة طرازات Microsoft
type: docs
weight: 20
url: /ar/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة متنوعة من ملفات إكسل المختلفة ، مثل إكسل 95/97 - 2003 ، SpreadsheetML ، فتح ملفات إكسل 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات إكسل المشفرة.

{{% /alert %}}

## **فتح ملفات إصدارات Microsoft Excel المختلفة**

غالبًا ما يتعين على التطبيق أن يكون قادرًا على فتح ملفات مايكروسوفت إكسل التي تم إنشاؤها بإصدارات مختلفة؛ على سبيل المثال، مايكروسوفت إكسل 95 و97، أو مايكروسوفت إكسل 2007/2010/2013/2016/2019 وأوفيس 365. قد تحتاج إلى تحميل ملف بأي من الصيغ المتنوعة، بما في ذلك XLS و XLSX و XLSM و XLSB و SpreadsheetML و TabDelimited أو TSV و CSV و ODS وما إلى ذلك. استخدم المنشئ، أو حدد نوع الصيغة المستخدمة في الفئة **Workbook** بواسطة خاصية **file_format** بتعيينها باستخدام تعداد **FileFormatType**.

تحتوي تعداد **FileFormatType** على العديد من الصيغ المحددة مسبقًا، وأدناه بعض هذه الصيغ.

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|EXCEL_97_TO_2003|تمثل ملف Excel 97 - 2003|
|XLSX|يمثل ملف Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX|
|XLSM|يمثل ملف Excel 2007/2010/2013/2016/2019 وOffice 365 XLSM|
|Xltx|يمثل ملف XLTX قالب Excel 2007/2010/2013/2016/2019 و Office 365|
|XLTX|تمثل ملف إكسل 2007/2010/2013/2016/2019 وأوفيس 365 بصيغة XLTX مع ماكرو ممكّن|
|XLSB|يمثل ملف XLSB الثنائي من Excel 2007/2010/2013/2016/2019 وOffice 365|
|SPREADSHEET_ML|تمثل ملف SpreadsheetML|
|TSV|يمثل ملف قيم مفصولة بعلامة التبويب|
|TAB_DELIMITED| تمثل ملف نص مفصول بعلامة التبويب|
|ODS|يمثل ملف ODS|
|HTML|يمثل ملف HTML|
|M_HTML|تمثل ملف MHTML|

### **فتح ملفات Microsoft Excel 95/5.0**

لفتح ملف مايكروسوفت إكسل 95/5.0، استخدم **LoadOptions** وقم بتعيين الخاصية ذات الصلة لفئة **LoadOptions** لتحميل ملف القالب. يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **فتح ملفات Microsoft Excel 97 - 2003**

لفتح ملف Microsoft Excel 97 - 2003، استخدم **LoadOptions** واضبط السمة ذات الصلة للفئة **LoadOptions** لملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **فتح ملفات Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX**

لفتح ملف بتنسيق Microsoft Excel 2007/2010/2013/2016/2019 و Office 365، أي XLSX أو XLSB، حدد مسار الملف. يمكنك أيضًا استخدام **LoadOptions** واضبط السمات والخيارات ذات الصلة لفئة **LoadOptions** لملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **فتح ملفات إكسل المشفرة**

من الممكن إنشاء ملفات Excel مُشفرة باستخدام Microsoft Excel. لفتح ملف مشفر، استخدم **LoadOptions** واضبط سماتها وخياراتها (على سبيل المثال، أعطِ كلمة مرور) لملف القالب الذي سيتم تحميله.
يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

تدعم Aspose.Cells أيضًا فتح ملفات Microsoft Excel 2007، 2010، 2013، 2016، 2019، Office 365 المحمية بكلمة مرور.


