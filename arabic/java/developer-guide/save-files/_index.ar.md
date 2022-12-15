---
title: حفظ ملفات Excel إلى CSV و PDF وتنسيقات أخرى
linktitle: احفظ الملفات
type: docs
weight: 20
url: /ar/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**يسمح للمطورين بإنشاء ملفات Excel من البداية باستخدام API. بمجرد إنشاء ملفات Excel ، ستحتاج أيضًا إلى حفظ المصنف الخاص بك (ملف). يوفر Aspose.Cells طرقًا متنوعة لحفظ هذه الملفات. في هذا الموضوع ، سنناقش كل تلك الطرق الممكنة التي يمكن للمطورين اتباعها لحفظ ملفاتهم.

{{% /alert %}}

## **طرق مختلفة لحفظ ملفاتك**

 يوفر Aspose.Cells API فئة مسماة[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)يمثل ملف Excel ويوفر جميع الخصائص والأساليب الضرورية التي قد يحتاجها المطورون للعمل مع ملفات Excel الخاصة بهم. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) فئة توفر أ[**حفظ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) الطريقة المستخدمة لحفظ ملفات Excel. ال[**حفظ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) يحتوي الأسلوب على العديد من التحميلات الزائدة التي تُستخدم لحفظ ملفات Excel بطرق مختلفة.

 يمكن للمطورين أيضًا تحديد تنسيق الملف الذي يجب حفظ ملفاتهم به. يمكن حفظ الملفات بتنسيقات متعددة مثل XLS و SpreadsheetML و CSV و Tab Delimited والقيم المفصولة بعلامات جدولة TSV و XPS وغيرها الكثير. يتم تحديد تنسيقات الملفات هذه باستخدام الامتداد[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) تعداد.

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)يحتوي التعداد على العديد من تنسيقات الملفات المحددة مسبقًا (التي يمكن أن تختارها أنت) على النحو التالي:

|**أنواع تنسيق الملف**|**وصف**|
|:- |:- |
|[**تلقاءي**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|يحاول API اكتشاف النسق المناسب من امتداد الملف المحدد في المعامل الأول لطريقة الحفظ|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|يمثل ملف CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|يمثل ملف Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|يمثل ملف XLSM المستند إلى XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|يمثل ملف قالب Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|يمثل ملف قالب ممكّن لـ Excel Macro|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|يمثل ملف Excel XLAM|
|[**ملف TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|يمثل ملف قيم مفصولة بعلامات جدولة|
|[**علامة التبويب محدد**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|يمثل ملفًا نصيًا محددًا بعلامات جدولة|
|[**لغة البرمجة**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|يمثل ملف (ملفات) HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|يمثل ملف (ملفات) MHTML|
|[**المواد المستنفدة للأوزون**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|يمثل ملف جدول بيانات OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|يمثل ملف XLS وهو التنسيق الافتراضي لمراجعات Excel 1997 إلى 2003|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|يمثل ملف SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|يمثل ملف Excel 2007 ثنائي XLSB|
|[**مجهول**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|يمثل تنسيقًا غير معروف ، لا يمكن حفظه.|
|[**بي دي إف**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|يمثل وثيقة PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|يمثل ملف مواصفات ورق XML (XPS)|
|[**شجار**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|يمثل ملف تنسيق ملف صور ذي علامات (TIFF)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|يمثل ملف Scalable Vector Graphics (SVG) المستند إلى XML|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|يمثل تنسيق تبادل البيانات.|
|[**أعداد**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|يمثل ملف أرقام.|
|[**تخفيض السعر**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|يمثل وثيقة تخفيض السعر.|
**عادة ، هناك طريقتان لحفظ ملفات Excel على النحو التالي:**

1. **حفظ الملف في مكان ما**
1. **حفظ الملف في دفق**

## **حفظ الملف في بعض المواقع**

 إذا احتاج المطورون إلى حفظ ملفاتهم في بعض مواقع التخزين ، فيمكنهم ببساطة تحديد اسم الملف (بمسار التخزين الكامل) وتنسيق الملف المطلوب (باستخدام[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) تعداد) أثناء استدعاء[**حفظ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) طريقة[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)هدف.

**مثال:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **حفظ المصنف إلى نص أو تنسيق CSV**

في بعض الأحيان ، تريد تحويل مصنف أو حفظه باستخدام أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT و TabDelim و CSV وما إلى ذلك) ، بشكل افتراضي ، يقوم كل من Microsoft Excel و Aspose.Cells بحفظ محتويات ورقة العمل النشطة فقط.

يوضح المثال التالي من التعليمات البرمجية كيفية حفظ مصنف بأكمله في تنسيق نصي. قم بتحميل المصنف المصدر الذي يمكن أن يكون أي ملف جدول بيانات Microsoft Excel أو OpenOffice (مثل XLS و XLSX و XLSM و XLSB و ODS وما إلى ذلك) بأي عدد من أوراق العمل.

عندما يتم تنفيذ الكود ، فإنه يحول بيانات جميع الأوراق في المصنف إلى تنسيق TXT.

 يمكنك تعديل نفس المثال لحفظ ملفك في CSV. بشكل افتراضي،[**TxtSaveOptions. فاصل**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) هي فاصلة ، لذلك لا تحدد فاصلًا في حالة الحفظ بتنسيق CSV.

**مثال:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **حفظ الملفات النصية باستخدام فاصل مخصص**

تحتوي الملفات النصية على بيانات جدول بيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **حفظ الملف في دفق**

 إذا احتاج المطورون إلى حفظ ملفاتهم في ملف**مجرى** ثم يجب عليهم إنشاء ملف**FileOutputStream** الكائن ثم احفظ الملف على ذلك**مجرى** عن طريق استدعاء[**حفظ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) طريقة[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)هدف. يمكن للمطورين أيضًا تحديد تنسيق الملف المطلوب (باستخدام امتداد[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) تعداد) أثناء استدعاء[**حفظ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) طريقة.

**مثال:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **حفظ الملف في تنسيق آخر**

### **ملفات XLS**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **ملفات XLSX**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **ملفات PDF**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **قم بتعيين خيار ContentCopyForAccessibility**

 مع ال[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) فئة ، يمكنك الحصول على ملف PDF أو تعيينه[**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) خيار للتحكم في الوصول إلى المحتوى في ملف PDF المحول. هذا يعني أنه يسمح لبرنامج قارئ الشاشة باستخدام النص الموجود في ملف PDF لقراءة ملف PDF. يمكنك تعطيله عن طريق تطبيق تغيير أذونات كلمة المرور وإلغاء تحديد العنصرين الموجودين في لقطة الشاشة[هنا](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **تصدير الخصائص المخصصة إلى PDF**

مع ال[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class ، يمكنك تصدير الخصائص المخصصة في المصنف المصدر إلى PDF.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)يتم توفير العداد لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader من خلال النقر على ملف ثم خيار الخصائص كما هو موضح في الصورة التالية. يمكن تحميل ملف القالب "sourceWithCustProps.xlsx"[هنا](sourceWithCustProps.xlsx)للاختبار وإخراج ملف PDF "outSourceWithCustProps" متاح[هنا](outSourceWithCustProps.pdf)للتحليل.

![ما يجب القيام به: image_بديل_نص](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **تحويل مصنف Excel إلى Markdown**

يوفر Aspose.Cells API دعمًا لتصدير جداول البيانات إلى تنسيق Markdown. لتصدير ورقة العمل النشطة إلى Markdown ، قم بتمرير[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)كمعامل ثاني لـ[**المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) طريقة. يمكنك أيضًا استخدام ملفات[**Markdown حفظ الخيارات**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)فئة لتحديد إعدادات إضافية لتصدير ورقة العمل إلى Markdown.

يوضح المثال التالي من التعليمات البرمجية تصدير ورقة العمل النشطة إلى Markdown باستخدام[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)عضو التعداد. الرجاء مراجعة[إخراج ملف Markdown](Book1.txt)التي تم إنشاؤها بواسطة رمز كمرجع.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **موضوعات مسبقة**
- [ضبط مستوى ضغط المصنف](/cells/ar/java/adjust-workbook-compression-level/)
- [تحويل المصنف إلى تنسيقات مختلفة](/cells/ar/java/converting-workbook-to-different-formats/)
- [حفظ المصنف لتقييد تنسيق جدول بيانات XML المفتوح](/cells/ar/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [تتبع تقدم التحويل من Excel إلى TIFF](/cells/ar/java/track-conversion-progress-of-excel-to-tiff/)
- [تتبع تقدم تحويل المستند](/cells/ar/java/track-document-conversion-progress/)
