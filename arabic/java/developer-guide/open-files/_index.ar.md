---
title: فتح الملفات بتنسيقات مختلفة
linktitle: فتح الملفات
type: docs
weight: 10
url: /ar/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

يستخدم المطورون Aspose.Cells لفتح الملفات لأغراض مختلفة. على سبيل المثال، فتح ملف لاسترداد البيانات منه، أو استخدام ملف جدول بيانات محدد مُعرف مسبقًا لتسريع عملية التطوير الخاصة بك. يسمح Aspose.Cells للمطورين بفتح أنواع مختلفة من ملفات المصدر. يمكن أن تكون هذه الملفات ملفات تقارير Microsoft Excel، SpreadsheetML، قيم مفصولة بالفواصل (CSV)، ملفات قيم مفصولة بعلامات التبويب (TSV) أو ملفات قيم مفصولة بتنسيق الجدول (Tab Delimited). يناقش هذا المقال فتح هذه الملفات المصدرية المختلفة باستخدام Aspose.Cells.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة، يرجى الرجوع إلى الصفحات التالية:
[صيغ الملفات المدعومة](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **طرق بسيطة لفتح ملفات Excel**

### **الفتح عبر المسار**

لفتح ملف Microsoft Excel باستخدام مسار الملف، يمكنك تمرير مسار الملف كمعلمة أثناء إنشاء مثيل الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). يوضح الكود العيني التالي فتح ملف Excel باستخدام مسار الملف.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **الفتح عبر التيار**

في بعض الأحيان، يتم تخزين ملف Excel الذي تريد فتحه كتيار. في هذه الحالة، مماثلة لفتح ملف باستخدام مسار الملف، يمكنك تمرير التيار كمعلمة أثناء إنشاء مثيل الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). يوضح الكود العيني التالي فتح ملف Excel باستخدام التيار.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **فتح ملفات إصدارات Microsoft Excel المختلفة**

يمكن للمستخدم استخدام فئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) لتحديد شكل ملف Excel باستخدام تعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

تحتوي فئة [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) على العديد من تنسيقات الملفات المحددة مسبقًا بعضها مذكور أدناه.

|**أنواع التنسيق**|**الوصف**|
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

لفتح ملفات Microsoft Excel 95، قم بإنشاء مثيل [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) مع مسار أو تيار الملف القالب. يمكن تحميل الملف العيني لاختبار الشيفرة من الرابط التالي:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **فتح ملفات Microsoft Excel 97 أو إصدارات لاحقة من XLS**

لفتح ملفات XLS لـ Microsoft Excel إصدار XLS 97 أو الإصدارات اللاحقة، قم بإنشاء مثيل [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) مع مسار أو تيار الملف القالب. أو استخدم الطريقة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد قيمة [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003) في تعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **فتح ملفات Microsoft Excel 2007 أو إصدارات لاحقة من ملفات XLSX**

لفتح ملفات XLSX لـ Microsoft Excel 2007 أو الإصدارات اللاحقة، قم بإنشاء مثيل [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) مع مسار أو تيار الملف القالب. أو استخدم فئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد قيمة [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) في تعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **فتح الملفات بتنسيقات مختلفة**

تُتيح Aspose.Cells للمطورين فتح ملفات جداول البيانات بتنسيقات مختلفة مثل SpreadsheetML، CSV، وملفات محددة بأدوات التبويب. لفتح مثل هذه الملفات، يمكن للمطورين استخدام نفس النهج الذي يستخدمونه لفتح ملفات إصدارات مختلفة من Microsoft Excel.

### **فتح ملفات SpreadsheetML**

ملفات SpreadsheetML هي التمثيلات الخاصة باللغة تعريف الوسائط القابلة للتوسع (XML) لجداول البيانات الخاصة بك وتشمل جميع المعلومات حول جداول البيانات الخاصة بك مثل التنسيق، والصيغ، وما إلى ذلك. منذ Microsoft Excel XP، تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يصدر جداول بياناتك إلى ملفات SpreadsheetML.

لفتح ملفات SpreadsheetML، استخدم فئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد القيمة [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML) في تعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **فتح ملفات CSV**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات يتم فصل قيمها أو تقسيمها بواسطة فواصل. في ملفات CSV، يتم تخزين البيانات في تنسيق جدولي يحتوي على حقول مفصولة بحرف الفاصلة ومحاطة بحرف الاقتباس المزدوج. إذا احتوت قيمة الحقل على حرف الاقتباس المزدوج فيجب تهريبها بزوج من أحرف الاقتباس المزدوج. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات الخاصة بك إلى ملف CSV.

لفتح ملفات CSV، استخدم فئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد قيمة [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) المحددة مسبقًا في فئة التعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

في Excel، عند فتح ملف CSV مع أحرف خاصة، يتم استبدال الأحرف تلقائيًا. ويتم نفس الأمر بواسطة واجهة برمجة التطبيقات Aspose.Cells التي يتم توضيحها في المثال البرمجي المعطى أدناه.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **فتح ملفات CSV باستخدام محلل الجاري التفضيلي**

غالبًا ما ليس من الضروري استخدام إعدادات محلل افتراضية لفتح ملفات CSV. في بعض الأحيان، قد لا ينتج استيراد ملف CSV الإخراج المتوقع مثل عدم تطابق تنسيق التاريخ المتوقع أو معالجة الحقول الفارغة بشكل مختلف. لهذا الغرض، تتاح فئة [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) لتوفير محلل مفضل لتوصيل مختلف أنواع البيانات حسب الحاجة. يوضح الكود عينة التالي استخدام المحلل المفضل.  

يمكن تنزيل ملف الشفرة المصدري وملفات الإخراج التجريبية من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **فتح ملفات TSV (مفصولة بالألسنة)**

تحتوي ملفات TSV على بيانات جدولية ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثل الجداول وأوراق العمل. بإيجاز، ملف TSV هو نوع خاص من ملف نصي عادي مع علامة تبويب بين كل عمود في النص.

لفتح ملفات مقسمة بواسطة العلامات، يجب على المطورين استخدام الفئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد القيمة [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) المحددة مسبقًا في فئة التعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **فتح ملفات إكسل المشفرة**

نحن نعلم أنه من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملفات المشفرة مثل هذه، يجب على المطورين استدعاء طريقة محددة محملة بالمعلومات وتحديد القيمة الافتراضية، المحددة مسبقًا في تعداد أنواع ملفات البيانات. كما سيتم أيضًا أخذ كلمة المرور للملف المشفر كما هو موضح في المثال أدناه.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

تدعم Aspose.Cells أيضًا فتح ملفات MS Excel 2013 المحمية بكلمة مرور.

{{% alert color="primary" %}}

هناك فرص عادلة لأن يقوم بناء الدفتر برمجيات بإلقاء استثناء System.OutOfMemoryException أثناء تحميل أوراق عمل كبيرة الحجم. يشير هذا الاستثناء إلى أن الذاكرة المتاحة غير كافية لتحميل الورقة الجداولية بالكامل إلى الذاكرة، وبالتالي يجب تحميل الورقة الجدولية بتمكين [تفضيلات الذاكرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **فتح ملفات SXC**

StarOffice Calc مماثل لـ Microsoft Excel ويدعم الصيغ والرسوم البيانية والوظائف والتوابع والماكرو. الجداول التي تم إنشاؤها باستخدام هذا البرنامج يتم حفظها بامتداد SXC.يُستخدم ملف SXC أيضاً لملفات جدول البيانات في OpenOffice.org Calc. يمكن لـ Aspose.Cells قراءة ملفات SXC كما هو موضح في الكود العيني التالي.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **فتح ملفات FODS**

ملف FODS هو جدول بيانات يتم حفظه في تنسيق OpenDocument XML دون أي ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS كما هو موضح في الكود العيني التالي.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **مواضيع متقدمة**
- [تصفية أسماء محددة أثناء تحميل المصنف](/cells/ar/java/filter-defined-names-while-loading-workbook/)
- [تصفية الكائنات أثناء تحميل مصنف العمل أو ورقة العمل](/cells/ar/java/filter-objects-while-loading-workbook-or-worksheet/)
- [الحصول على تحذيرات أثناء تحميل ملف إكسل](/cells/ar/java/get-warnings-while-loading-excel-file/)
- [الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تحميل الدفتر بحجم ورقة الطابعة المحدد](/cells/ar/java/load-workbook-with-specified-printer-paper-size/)
- [فتح ملفات Microsoft Excel مختلفة الإصدارات](/cells/ar/java/opening-different-microsoft-excel-versions-files/)
- [تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [قراءة جدول بيانات الأرقام المطور من قبل Apple Inc. باستخدام Aspose.Cells](/cells/ar/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [قراءة ملف CSV بعدة ترميزات](/cells/ar/java/reading-csv-file-with-multiple-encodings/)
- [توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً](/cells/ar/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [استخدام واجهة برمجة التطبيقات LightCells](/cells/ar/java/using-lightcells-api/)
