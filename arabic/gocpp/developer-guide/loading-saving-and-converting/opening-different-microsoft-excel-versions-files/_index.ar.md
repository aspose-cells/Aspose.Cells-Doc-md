---
title: فتح ملفات إكسل المختلفة طرازات Microsoft
type: docs
weight: 20
url: /ar/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة متنوعة من ملفات إكسل المختلفة ، مثل إكسل 95/97 - 2003 ، SpreadsheetML ، فتح ملفات إكسل 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات إكسل المشفرة.

{{% /alert %}}

## **فتح ملفات إصدارات Microsoft Excel المختلفة**

غالبًا ما يتعين على التطبيق أن يكون قادرًا على فتح ملفات Microsoft Excel التي تم إنشاؤها بإصدارات مختلفة، على سبيل المثال، Microsoft Excel 95، 97، أو Microsoft Excel 2007/2010/2013/2016/2019 و Office 365. قد تحتاج إلى تحميل ملف بأي من عدة تنسيقات، بما في ذلك XLS، XLSX، XLSM، XLSB، SpreadsheetML، TabDelimited أو TSV، CSV، ODS، وغير ذلك. استخدم المنشئ أو حدد طريقة [**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/) لفئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) لتحديد التنسيق باستخدام تعداد [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/).

تحتوي تعداد [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) على العديد من تنسيقات الملفات المعرفة مسبقًا، وبعضها مذكور أدناه.

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|FileFormatType_CSV|يُمثل ملف CSV|
|FileFormatType_Excel97To2003|يُمثل ملف Excel 97 - 2003|
|FileFormatType_Xlsx|يُمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSX|
|FileFormatType_Xlsm|يمثل ملف Excel XLSM لعامي 2007/2010/2013/2016/2019 وOffice 365|
|FileFormatType_Xltx|يمثل ملف XLTX النموذجي لعام 2007/2010/2013/2016/2019 وOffice 365 لبرنامج Excel|
|FileFormatType_Xltm|يمثل ملف XLTM القابل للتشغيل لعام 2007/2010/2013/2016/2019 وOffice 365 لبرنامج Excel|
|FileFormatType_Xlsb|يمثل ملف XLSB الثنائي لعام 2007/2010/2013/2016/2019 وOffice 365 لبرنامج Excel|
|FileFormatType_SpreadsheetML|يمثل ملف SpreadsheetML|
|FileFormatType_Tsv|يمثل ملف قيم مفصولة بواسطة علامة جدول طابقة|
|FileFormatType_TabDelimited|يمثل ملف نصي مفصول بواسطة علامات طابقة|
|FileFormatType_Ods|يمثل ملف ODS|
|FileFormatType_Html|يمثل ملف HTML|
|FileFormatType_MHtml|يمثل ملف MHTML|

### **فتح ملفات Microsoft Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) وقم بتعيين السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) لقالب الملف الذي سيتم تحميله. يمكن تنزيل ملف عيني لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **فتح ملفات Microsoft Excel 97 - 2003**

لفتح ملف Microsoft Excel 97 - 2003، استخدم [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) وقم بتعيين السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **فتح ملفات Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX**

لفتح تنسيق ملف Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365، أي XLSX أو XLSB، حدد مسار الملف. يمكنك أيضًا استخدام [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) وتعيين السمة/الخيارات ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

يدعم Aspose.Cells أيضًا فتح ملفات Microsoft Excel محمية بكلمة مرور لعام 2007، 2010، 2013، 2016، 2019، وOffice 365.
