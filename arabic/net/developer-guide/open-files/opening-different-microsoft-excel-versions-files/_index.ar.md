---
title: افتح ملفات إصدارات Excel المختلفة Microsoft
type: docs
weight: 20
url: /ar/net/opening-different-microsoft-excel-versions-files/
description: يشرح هذا المقال كيفية فتح ملفات إصدارات Excel المختلفة باستخدام Aspose.Cells for .NET API.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة من ملفات إصدارات Excel المختلفة Microsoft، مثل Microsoft Excel 95/97 - 2003، SpreadsheetML، فتح Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX أو ملفات Excel المشفرة.

{{% /alert %}}

##  **كيفية فتح ملفات مختلفة Microsoft إصدارات Excel**

 غالبًا ما يجب أن يكون التطبيق قادرًا على فتح Microsoft من ملفات Excel التي تم إنشاؤها في إصدارات مختلفة، على سبيل المثال، Microsoft Excel 95,97، أو Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365. قد تحتاج إلى تحميل ملف بأي من التنسيقات المتعددة، بما في ذلك XLS أو XLSX أو XLSM أو XLSB أو SpreadsheetML أو TabDelimited أو TSV أو CSV أو ODS وما إلى ذلك. استخدم المنشئ، أو حدد**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**فصل'**[تنسيق الملف](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** سمة الكتابة التي تحدد التنسيق باستخدام**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**تعداد.

 ال**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا والتي يرد بعضها أدناه.

|**أنواع تنسيقات الملفات**|**وصف**|
| :- | :- |
|ملف CSV|يمثل ملف CSV|
|Excel97To2003|يمثل ملف Excel 97 - 2003|
|XLSX|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSX|
|XLSM|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSM|
|XLTX|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLTX|
|XLTM|يمثل ملف Excel 2007/2010/2013/2016/2019 وOffice 365 الممكّن بماكرو XLTM|
|XLSB|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 الثنائي XLSB|
|SpreadsheetML|يمثل ملف SpreadsheetML|
|تسف|يمثل ملف قيم مفصولة بعلامات جدولة|
|TabDelimited|يمثل ملف نصي محدد بعلامات جدولة|
|احتمالات|يمثل ملف ODS|
|لغة البرمجة|يمثل ملف HTML|
|م أتش تي أم أل|يمثل ملف MHTML|

###  **افتح Microsoft ملفات Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**وقم بتعيين السمة ذات الصلة لـ**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**فئة ملف القالب الذي سيتم تحميله. يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **افتح Microsoft ملفات Excel 97 - 2003**

 لفتح ملف Microsoft Excel 97 - 2003، استخدم**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** وقم بتعيين السمة ذات الصلة لـ**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**فئة ملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **فتح Microsoft ملفات Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX**

لفتح تنسيق Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365، أي XLSX أو XLSB، حدد مسار الملف. تستطيع ايضا استخذام**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** وقم بتعيين السمة/الخيارات ذات الصلة لـ**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**فئة ملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **فتح ملفات Excel المشفرة**

 من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر، استخدم**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**وقم بتعيين سماته وخياراته (على سبيل المثال، إعطاء كلمة مرور) لتحميل ملف القالب.
يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[إكسل مشفرة](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells يدعم أيضًا فتح ملفات Microsoft Excel 2007 و 2010 و 2013 و 2016 و 2019 و Office 365 المحمية بكلمة مرور.


