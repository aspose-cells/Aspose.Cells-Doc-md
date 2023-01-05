---
title: فتح ملفات بتنسيقات مختلفة
linktitle: الملفات المفتوحة
type: docs
weight: 10
url: /ar/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

يستخدم المطورون Aspose.Cells لفتح الملفات لأغراض مختلفة. على سبيل المثال ، افتح ملفًا لاسترداد البيانات منه ، أو استخدم ملف جدول بيانات مصمم مسبقًا لتسريع عملية التطوير لديك. Aspose.Cells يسمح للمطورين بفتح أنواع مختلفة من الملفات المصدر. يمكن أن تكون ملفات المصدر هذه Microsoft تقارير Excel أو SpreadsheetML أو قيم مفصولة بفواصل (CSV) أو ملفات مفصولة بعلامات جدولة أو قيم مفصولة بعلامات جدولة (TSV). تتناول هذه المقالة فتح هذه الملفات المصدر المختلفة باستخدام Aspose.Cells.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة ، فيرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **طرق بسيطة لفتح ملفات Excel**

### **فتح طريق**

لفتح ملف Excel Microsoft باستخدام مسار الملف ، قم بتمرير مسار الملف كمعامل أثناء إنشاء مثيل لـ**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**صف دراسي. يوضح نموذج التعليمات البرمجية التالي فتح ملف Excel باستخدام مسار الملف.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **فتح من خلال تيار**

في بعض الأحيان ، يتم تخزين ملف Excel الذي تريد فتحه كتدفق. في هذه الحالة ، على غرار فتح ملف باستخدام مسار الملف ، قم بتمرير الدفق كمعامل أثناء إنشاء ملف**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** صف دراسي. يوضح نموذج التعليمات البرمجية التالي فتح ملف Excel باستخدام دفق.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **فتح ملفات مختلفة من إصدارات إكسل Microsoft**

 يجوز للمستخدم استخدام**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة لتحديد تنسيق ملف Excel باستخدام امتداد**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

 ال**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا والتي يرد بعضها أدناه.

|**أنواع التنسيق**|**وصف**|
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

 لفتح ملفات Microsoft Excel 95 ، قم بإنشاء مثيل لملف**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**المثيل مع مسار أو دفق ملف القالب. يمكن تنزيل ملف نموذج لاختبار الكود من الرابط التالي:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **فتح Microsoft Excel 97 أو الإصدارات الأحدث XLS الملفات**

 لفتح XLS ملفات Microsoft Excel XLS 97 أو الإصدارات الأحدث ، قم بإنشاء مثيل لـ**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**المثيل مع مسار أو دفق ملف القالب. أو استخدم ملف**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** الطريقة وحدد**[EXCEL_97_TO_2003] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** قيمة في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **فتح Microsoft Excel 2007 أو الإصدارات الأحدث XLSX الملفات**

 لفتح XLSX ملفات Microsoft Excel 2007 أو الإصدارات الأحدث ، قم بإنشاء مثيل**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**المثيل مع مسار أو دفق ملف القالب. أو استخدم ملف**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة واختيار**[XLSX] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** قيمة في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **فتح ملفات بتنسيقات مختلفة**

Aspose.Cells يسمح للمطورين بفتح ملفات جداول البيانات بتنسيقات مختلفة مثل SpreadsheetML ، CSV ، الملفات المحددة بعلامات جدولة. لفتح مثل هذه الملفات ، يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات مختلفة من إصدارات Microsoft Excel.

### **فتح SpreadsheetML الملفات**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات الخاصة بك بما في ذلك جميع المعلومات حول جدول البيانات مثل التنسيق والصيغ وما إلى ذلك. منذ Microsoft Excel XP ، تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يقوم بتصدير جداول البيانات الخاصة بك إلى ملفات SpreadsheetML.

لفتح SpreadsheetML ملفات ، استخدم امتداد**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة واختيار**[SPREADSHEET_ML] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** قيمة في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **فتح CSV الملفات**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات محددة قيمها أو مفصولة بفواصل. في ملفات CSV ، يتم تخزين البيانات في تنسيق جدولي يحتوي على حقول مفصولة بفاصلة ويتم اقتباسها بحرف اقتباس مزدوج. إذا احتوت قيمة الحقل على علامة اقتباس مزدوجة ، يتم تخطيها بزوج من علامات الاقتباس المزدوجة. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى ملف CSV.

لفتح CSV ملفات ، استخدم امتداد**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة واختيار**[CSV] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** القيمة المحددة مسبقًا في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **فتح CSV الملفات واستبدال الحروف غير الصالحة**

في Excel ، عند فتح ملف CSV بأحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بنفس الشيء بواسطة Aspose.Cells API والذي هو موضح في مثال الكود الموضح أدناه.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **فتح CSV الملفات باستخدام المحلل اللغوي المفضل**

هذا ليس ضروريًا دائمًا لاستخدام إعدادات المحلل اللغوي الافتراضية لفتح ملفات CSV. في بعض الأحيان ، لا يؤدي استيراد ملف CSV إلى إنشاء الإخراج المتوقع مثل تنسيق التاريخ ليس كما هو متوقع أو يتم التعامل مع الحقول الفارغة بشكل مختلف. لهذا الغرض**[TxtLoadOptions.PreferredParsers] (https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**متاح لتوفير المحلل اللغوي المفضل لتحليل أنواع البيانات المختلفة حسب المتطلبات. يوضح نموذج التعليمات البرمجية التالي استخدام المحلل اللغوي المفضل.

يمكن تنزيل نموذج ملف المصدر وملفات الإخراج من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **فتح ملفات TSV (محدد بعلامات جدولة)**

تحتوي الملفات المحددة بعلامات جدولة على بيانات جدول بيانات ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثل الجداول وجداول البيانات. باختصار ، الملف المحدد بعلامات جدولة هو نوع خاص من ملفات النص العادي بعلامة جدولة بين كل عمود في النص.

لفتح ملفات محددة بعلامات جدولة ، يجب على المطورين استخدام الامتداد**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة واختيار**[TSV] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** القيمة المحددة مسبقًا في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **فتح ملفات اكسل المشفرة**

نعلم أنه من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح مثل هذه الملفات المشفرة ، يجب على المطورين استدعاء طريقة LoadOptions خاصة محملة بشكل زائد وتحديد قيمة DEFAULT المحددة مسبقًا في تعداد FileFormatType. ستأخذ هذه الطريقة أيضًا كلمة المرور للملف المشفر كما هو موضح أدناه في المثال.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

يدعم Aspose.Cells أيضًا فتح ملفات MS Excel 2013 المحمية بكلمة مرور.

{{% alert color="primary" %}}

هناك فرص معقولة في أن يقوم مُنشئ المصنف بإلقاء System.OutOfMemoryException أثناء تحميل جداول بيانات كبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتوفرة غير كافية لتحميل جدول البيانات بالكامل في الذاكرة ، وبالتالي ، يجب تحميل جدول البيانات أثناء تمكين[تفضيلات الذاكرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **فتح SXC الملفات**

StarOffice Calc مشابه لـ Microsoft Excel ويدعم الصيغ والمخططات والوظائف ووحدات الماكرو. يتم حفظ جداول البيانات التي تم إنشاؤها باستخدام هذا البرنامج بالملحق SXC. يتم استخدام ملف SXC أيضًا لملفات جداول بيانات OpenOffice.org Calc. يمكن Aspose.Cells قراءة ملفات SXC كما هو موضح في نموذج التعليمات البرمجية التالي.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **فتح FODS الملفات**

الملف FODS هو جدول بيانات محفوظ في OpenDocument XML بدون أي ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS كما هو موضح في نموذج التعليمات البرمجية التالي.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **موضوعات مسبقة**
- [تصفية الأسماء المعرفة أثناء تحميل المصنف](/cells/ar/java/filter-defined-names-while-loading-workbook/)
- [تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل](/cells/ar/java/filter-objects-while-loading-workbook-or-worksheet/)
- [احصل على تحذيرات أثناء تحميل ملف Excel](/cells/ar/java/get-warnings-while-loading-excel-file/)
- [احتفظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات بتنسيق CSV](/cells/ar/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تحميل المصنف بحجم ورق طابعة محدد](/cells/ar/java/load-workbook-with-specified-printer-paper-size/)
- [فتح ملفات إصدارات Excel Microsoft المختلفة](/cells/ar/java/opening-different-microsoft-excel-versions-files/)
- [تحسين استخدام الذاكرة أثناء العمل مع الملفات الكبيرة التي تحتوي على مجموعات بيانات كبيرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [اقرأ جدول البيانات Numbers الذي طورته شركة Apple Inc. باستخدام Aspose.Cells](/cells/ar/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [قراءة CSV ملف ذو ترميزات متعددة](/cells/ar/java/reading-csv-file-with-multiple-encodings/)
- [أوقف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً](/cells/ar/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [باستخدام LightCells API](/cells/ar/java/using-lightcells-api/)
