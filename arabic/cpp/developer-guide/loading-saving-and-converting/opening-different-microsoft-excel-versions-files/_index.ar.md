---
title: فتح ملفات إصدارات Excel Microsoft المختلفة
type: docs
weight: 20
url: /ar/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح نطاق من ملفات إصدارات Excel Microsoft المختلفة ، مثل Microsoft Excel 95/97-2003 ، SpreadsheetML ، فتح Microsoft Excel 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات Excel المشفرة.

{{% /alert %}}

## **فتح ملفات مختلفة من إصدارات إكسل Microsoft**

 غالبًا ما يجب أن يكون التطبيق قادرًا على فتح ملفات Excel Microsoft التي تم إنشاؤها في إصدارات مختلفة ، على سبيل المثال ، Microsoft Excel 95،97 أو Microsoft Excel 2007/2010/2013/2016/2019 و Office 365. قد تحتاج إلى تحميل ملف بأي تنسيق من عدة تنسيقات ، بما في ذلك XLS و XLSX و XLSM و XLSB و SpreadsheetML و TabDelimited أو TSV و CSV و ODS وما إلى ذلك. استخدم المنشئ أو حدد**[IWorkbook] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** صف دراسي'**[SetFileFormat] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)** طريقة لتحديد التنسيق باستخدام**[FileFormatType] (https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**تعداد.
	
 ال**[FileFormatType] (https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا والتي يرد بعضها أدناه.

|**أنواع تنسيق الملف**|**وصف**|
|:- |:- |
|FileFormatType_CSV|يمثل ملف CSV|
|FileFormatType_Excel97To2003|يمثل ملف Excel 97 - 2003|
|FileFormatType_Xlsx|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSX|
|FileFormatType_Xlsm|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 XLSM|
|FileFormatType_Xltx|يمثل ملف Excel 2007/2010/2013/2016/2019 وقالب Office 365 XLTX|
|FileFormatType_Xltm|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف XLTM ممكّن للماكرو في Office 365|
|FileFormatType_Xlsb|يمثل ملف Excel 2007/2010/2013/2016/2019 وملف Office 365 الثنائي XLSB|
|FileFormatType_SpreadsheetML|يمثل ملف SpreadsheetML|
|FileFormatType_Tsv|يمثل ملف قيم مفصولة بعلامات جدولة|
|FileFormatType_Tab محدد|يمثل ملفًا نصيًا محددًا بعلامات جدولة|
|FileFormatType_Ods|يمثل ملف ODS|
|FileFormatType_Html|يمثل ملف HTML|
|FileFormatType_MHtml|يمثل ملف MHTML|

### **فتح Microsoft ملفات Excel 95 / 5.0**

لفتح ملف Microsoft Excel 95 / 5.0 ، استخدم**[ILoadOptions] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**وقم بتعيين السمة ذات الصلة لـ**ILoadOptions**فئة ملف القالب المراد تحميله. يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **فتح Microsoft ملفات Excel 97-2003**

 لفتح ملف Microsoft Excel 97-2003 ، استخدم**[ILoadOptions] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** وقم بتعيين السمة ذات الصلة لـ**ILoadOptions**فئة ملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **فتح Microsoft Excel 2007/2010/2013/2016/2019 وملفات Office 365 XLSX**

 لفتح تنسيق Microsoft Excel 2007/2010/2013/2016/2019 وتنسيق Office 365 ، أي XLSX أو XLSB ، حدد مسار الملف. تستطيع ايضا استخذام**[ILoadOptions] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** وقم بتعيين السمة / الخيارات ذات الصلة لـ**ILoadOptions**فئة ملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

يدعم Aspose.Cells أيضًا فتح ملفات Microsoft المحمية بكلمة مرور في Excel 2007 و 2010 و 2013 و 2016 و 2019 و Office 365.


