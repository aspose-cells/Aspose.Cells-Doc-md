---
title: فتح ملفات إكسل من إصدارات مايكروسوفت المختلفة
type: docs
weight: 20
url: /ar/net/opening-different-microsoft-excel-versions-files/
description: يشرح هذا المقال كيفية فتح ملفات إكسل من إصدارات مختلفة باستخدام Aspose.Cells for .NET API.
keywords: C# فتح ملفات إكسل من إصدارات مايكروسوفت المختلفة، كيف يمكنني فتح ملفات إكسل المشفرة.
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة متنوعة من ملفات إكسل المختلفة ، مثل إكسل 95/97 - 2003 ، SpreadsheetML ، فتح ملفات إكسل 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات إكسل المشفرة.

{{% /alert %}}

## **كيفية فتح ملفات من إصدارات مايكروسوفت إكسل المختلفة**

غالبًا ما يجب على تطبيق أن يكون قادرًا على فتح ملفات Microsoft Excel التي تم إنشاؤها في إصدارات مختلفة، على سبيل المثال، Microsoft Excel 95،97، أو Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365. قد تحتاج إلى تحميل ملف بأحد صيغ متعددة، بما في ذلك XLS، XLSX، XLSM، XLSB، SpreadsheetML، تنسيق الجدول المفصول بالفواصل أو TSV، CSV، ODS، وما إلى ذلك. استخدم البناء، أو حدد نوع الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) باستخدام سمة [**FileFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat) التي تحدد التنسيق باستخدام فئة التعداد [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype).

تحتوي فئة [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) على العديد من تنسيقات الملفات المحددة مسبقًا بعضها مذكور أدناه.

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|Csv| يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
|Xlsx| يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSX|
|Xlsm| يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSM|
|Xltx|يمثل ملف XLTX قالب Excel 2007/2010/2013/2016/2019 و Office 365|
|Xltm|يمثل ملف XLTM Excel 2007/2010/2013/2016/2019 و Office 365 القادر على تشغيل الماكرو|
|Xlsb|يمثل ملف XLSB بتنسيق Excel 2007/2010/2013/2016/2019 و Office 365|
|SpreadsheetML|يمثل ملف SpreadsheetML|
|Tsv|يمثل ملف بقيم مفصولة بواسطة علامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|Ods|يمثل ملف ODS|
|Html|يمثل ملف HTML|
|Mhtml|يمثل ملف MHTML|

### **فتح ملفات Microsoft Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) وقم بتعيين السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) لقالب الملف الذي سيتم تحميله. يمكن تنزيل ملف عيني لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **فتح ملفات Microsoft Excel 97 - 2003**

لفتح ملف Microsoft Excel 97 - 2003، استخدم [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) وقم بتعيين السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **فتح ملفات Microsoft Excel 2007/2010/2013/2016/2019 و Office 365 بصيغة XLSX**

لفتح تنسيق ملف Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365، أي XLSX أو XLSB، حدد مسار الملف. يمكنك أيضًا استخدام [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) وتعيين السمة/الخيارات ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **فتح ملفات Excel المشفرة**

من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر، استخدم فئة [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) وقم بتعيين سماته وخياراته (على سبيل المثال، إعطاء كلمة مرور) لقالب الملف الذي سيتم تحميله.
يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

تدعم Aspose.Cells أيضًا فتح ملفات Microsoft Excel 2007، 2010، 2013، 2016، 2019، Office 365 المحمية بكلمة مرور.


{{< app/cells/assistant language="csharp" >}}
