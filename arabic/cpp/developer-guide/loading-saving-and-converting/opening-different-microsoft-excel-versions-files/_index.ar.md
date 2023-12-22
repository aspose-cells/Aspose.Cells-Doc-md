---
title: فتح ملفات إصدارات Excel المختلفة Microsoft
type: docs
weight: 20
url: /ar/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة من ملفات إصدارات Excel المختلفة Microsoft، مثل Microsoft Excel 95/97 - 2003، SpreadsheetML، فتح Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX أو ملفات Excel المشفرة.

{{% /alert %}}

##  **فتح ملفات من إصدارات Excel المختلفة Microsoft**

 غالبًا ما يجب أن يكون التطبيق قادرًا على فتح Microsoft من ملفات Excel التي تم إنشاؤها في إصدارات مختلفة، على سبيل المثال، Microsoft Excel 95,97، أو Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365. قد تحتاج إلى تحميل ملف بأي من التنسيقات المتعددة، بما في ذلك XLS أو XLSX أو XLSM أو XLSB أو SpreadsheetML أو TabDelimited أو TSV أو CSV أو ODS وما إلى ذلك. استخدم المنشئ، أو حدد**[المصنف](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**فصل'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** طريقة لتحديد التنسيق باستخدام**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**تعداد.
	
 ال**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا والتي يرد بعضها أدناه.

|**أنواع تنسيقات الملفات**|**وصف**|
| :- | :- |
|FileFormatType_CSV|يمثل ملف CSV|
|FileFormatType_Excel97To2003|يمثل ملف Excel 97 - 2003|
|FileFormatType_Xlsx|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSX|
|FileFormatType_Xlsm|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSM|
|FileFormatType_Xltx|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLTX|
|FileFormatType_Xltm|يمثل ملف Excel 2007/2010/2013/2016/2019 وOffice 365 الممكّن بماكرو XLTM|
|FileFormatType_Xlsb|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 الثنائي XLSB|
|FileFormatType_SpreadsheetML|يمثل ملف SpreadsheetML|
|FileFormatType_Tsv|يمثل ملف قيم مفصولة بعلامات جدولة|
|FileFormatType_TabDelimited|يمثل ملف نصي محدد بعلامات جدولة|
|FileFormatType_Ods|يمثل ملف ODS|
|FileFormatType_Html|يمثل ملف HTML|
|FileFormatType_MHtml|يمثل ملف MHTML|

###  **فتح Microsoft ملفات Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم**[خيارات التحميل](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**وقم بتعيين السمة ذات الصلة لـ**خيارات التحميل**فئة ملف القالب الذي سيتم تحميله. يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **فتح Microsoft ملفات اكسل 97 - 2003**

 لفتح ملف Microsoft Excel 97 - 2003، استخدم**[خيارات التحميل](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** وقم بتعيين السمة ذات الصلة لـ**خيارات التحميل**فئة ملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **فتح Microsoft ملفات Excel 2007/2010/2013/2016/2019 وOffice 365 XLSX**

لفتح تنسيق Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365، أي XLSX أو XLSB، حدد مسار الملف. تستطيع ايضا استخذام**[خيارات التحميل](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** وقم بتعيين السمة/الخيارات ذات الصلة لـ**خيارات التحميل**فئة ملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells يدعم أيضًا فتح ملفات Microsoft Excel 2007 و 2010 و 2013 و 2016 و 2019 و Office 365 المحمية بكلمة مرور.


