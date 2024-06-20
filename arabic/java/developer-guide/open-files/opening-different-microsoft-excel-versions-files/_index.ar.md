---
title: فتح ملفات إكسل المختلفة طرازات Microsoft
type: docs
weight: 20
url: /ar/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة متنوعة من ملفات إكسل المختلفة ، مثل إكسل 95/97 - 2003 ، SpreadsheetML ، فتح ملفات إكسل 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات إكسل المشفرة.

{{% /alert %}}

## **فتح ملفات إصدارات Microsoft Excel المختلفة**

غالبًا ما يكون للتطبيق القدرة على فتح ملفات Microsoft Excel التي تم إنشاؤها في إصدارات مختلفة، على سبيل المثال، Microsoft Excel 95، 97، أو Microsoft Excel 2007/2010/2013/2016/2019 و Office 365. قد تحتاج إلى تحميل ملف في أيٍ من عدة تنسيقات، بما في ذلك XLS، XLSX، XLSM، XLSB، SpreadsheetML، TabDelimited أو TSV، CSV، ODS وغيرها. استخدم البناء، أو استخدم [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) لفئة [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat) لتحديد التنسيق باستخدام [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType).

تحتوي فئة [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) على العديد من تنسيقات الملفات المحددة مسبقًا بعضها مذكور أدناه.

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|EXCEL_97_TO_2003|تمثل ملف Excel 97 - 2003|
|XLSX|يمثل ملف Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX|
|XLSM|يمثل ملف Excel 2007/2010/2013/2016/2019 وOffice 365 XLSM|
|XLTX|يمثل ملف قالب Excel 2007/2010/2013/2016/2019 وOffice 365 XLTX|
|XLTM|يمثل ملف XLTM مع مكرو Excel 2007/2010/2013/2016/2019 وOffice 365|
|XLSB|يمثل ملف XLSB الثنائي من Excel 2007/2010/2013/2016/2019 وOffice 365|
|SPREADSHEET_ML|تمثل ملف SpreadsheetML|
|TSV|يمثل ملف قيم مفصولة بعلامة التبويب|
|TAB_DELIMITED| تمثل ملف نص مفصول بعلامة التبويب|
|ODS|يمثل ملف ODS|
|HTML|يمثل ملف HTML|
|M_HTML|تمثل ملف MHTML|

### **فتح ملفات Microsoft Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وقم بتعيين السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) لقالب الملف الذي سيتم تحميله. يمكن تنزيل ملف عيني لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **فتح ملفات Microsoft Excel 97 - 2003**

لفتح ملف Microsoft Excel 97 - 2003، استخدم [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وقم بتعيين السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **فتح ملفات Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX**

لفتح تنسيق ملف Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365، أي XLSX أو XLSB، حدد مسار الملف. يمكنك أيضًا استخدام [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وتعيين السمة/الخيارات ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **فتح ملفات إكسل المشفرة**

من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر، استخدم فئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وقم بتعيين سماته وخياراته (على سبيل المثال، إعطاء كلمة مرور) لقالب الملف الذي سيتم تحميله. 
يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

تدعم Aspose.Cells أيضًا فتح ملفات Microsoft Excel 2007، 2010، 2013، 2016، 2019، Office 365 المحمية بكلمة مرور.
