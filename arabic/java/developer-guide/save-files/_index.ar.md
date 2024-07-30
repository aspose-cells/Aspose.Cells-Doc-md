---
title: حفظ ملفات Excel في تنسيق CSV، PDF وتنسيقات أخرى
linktitle: حفظ الملفات
type: docs
weight: 20
url: /ar/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** يسمح للمطورين بإنشاء ملفات Excel من الصفر باستخدام واجهة برمجة التطبيقات المرنة الخاصة به. عند إنشاء ملفات Excel، سيكون لديك أيضًا حاجة لحفظ دفتر العمل الخاص بك (الملف). توفر Aspose.Cells مجموعة متنوعة من الطرق لحفظ هذه الملفات. في هذا الموضوع، سنناقش جميع تلك الطرق الممكن اعتمادها من قبل المطورين لحفظ ملفاتهم.

{{% /alert %}}

## **طرق مختلفة لحفظ ملفاتك**

يوفر Aspose.Cells API فئة تسمى [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) تمثل ملف Excel وتوفر جميع الخصائص والأساليب اللازمة التي قد يحتاجها المطورون للعمل مع ملفات Excel الخاصة بهم. توفر فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) أسلوبًا [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) يستخدم لحفظ ملفات Excel. يحتوي الأسلوب [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) على العديد من التحميلات التي تستخدم لحفظ ملفات Excel بطرق مختلفة.

يمكن للمطورين أيضًا تحديد تنسيق الملف الذي يجب حفظ ملفاتهم فيه. يمكن حفظ الملفات في عدة تنسيقات مثل XLS، SpreadsheetML، CSV، مقسم بالجدول وبيانات مفصولة بفواصل TSV، XPS والعديد من التنسيقات الأخرى. يتم تحديد هذه التنسيقات باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat).

يحتوي تعداد [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) على العديد من تنسيقات الملفات المحددة مسبقًا (التي يمكن اختيارها من قبلك) على النحو التالي:

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|يحاول واجهة برمجة التطبيقات (API) التعرف على التنسيق المناسب من امتداد الملف المحدد في المعلمة الأولى لطريقة الحفظ|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|يمثل ملف CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|يمثل ملف شريحة Excel المفتوح لـOffice Open XML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|يمثل ملف XLSM بناءً على XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|يمثل ملف قالب Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|يمثل ملف قالب ممكن تنفيذه لبرامج Excel|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|يمثل ملف XLAM لبرنامج Excel|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|يمثل ملف قيم مفصولة بفواصل|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|يمثل ملف نصي مفصول بواسطة علامات التبويب|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|يمثل ملف(ات) HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|يمثل ملف(ات) MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)| يمثل ملف جدول بيانات OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)| يمثل ملف XLS الذي هو التنسيق الافتراضي لإصدارات Excel من عام 1997 إلى 2003|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)| يمثل ملف SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)| يمثل ملف Excel 2007 الثنائي XLSB|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)| يمثل تنسيق غير معترف به، لا يمكن حفظه|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)| يمثل مستند PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)| يمثل ملف مواصفات ورقة XML (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)| يمثل ملف نوع الصورة المعبرة (TIFF)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)| يمثل ملف SVG (الرسومات المتجهة قابلة للتوسيع على أساس XML)|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)| يمثل تنسيق تبادل البيانات|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)| يمثل ملف أرقام|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)| يمثل مستند markdown|
**عادةً، هناك طريقتان لحفظ ملفات Excel على النحو التالي:**

1. **حفظ الملف في موقع معين**
1. **حفظ الملف في تيار بيانات**

## **حفظ ملف في موقع معين**

إذا كان المطورون بحاجة إلى حفظ ملفاتهم في موقع تخزين ما ، فيمكنهم ببساطة تحديد اسم الملف (مع مسار تخزينه الكامل) وتنسيق الملف المطلوب (باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) أثناء استدعاء الأسلوب [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) في [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook).

**مثال:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **حفظ دفتر العمل إلى تنسيق نصي أو CSV**

في بعض الأحيان، ترغب في تحويل أو حفظ دفتر عمل يحتوي على عدة أوراق عمل إلى شكل نصي. في حالات الشكل النصي (على سبيل المثال TXT, TabDelim, CSV الخ)، فإن كل من مايكروسوفت إكسل وAspose.Cells تحفظان افتراضيًا محتويات الورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود، يحول بيانات جميع الأوراق في كتاب العمل إلى تنسيق نصي.

يمكنك تعديل نفس المثال لحفظ ملفك إلى CSV. افتراضيًا، [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) هو فاصلة، لذلك لا تحدد فاصلة عند الحفظ بتنسيق CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى إذا تم تعيين معلمة الأسلوب [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) على القيمة true، فإن البرنامج سيقوم فقط بتصدير ورقة عمل واحدة.

**مثال:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **حفظ ملفات النص بفاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **حفظ ملف في تيار**

إذا كان المطورون بحاجة إلى حفظ ملفاتهم في **Stream** ، فيجب عليهم إنشاء كائن **FileOutputStream** ثم حفظ الملف في ذلك **Stream** عن طريق استدعاء الأسلوب [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) في [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). يمكن للمطورين أيضًا تحديد تنسيق الملف المطلوب (باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) أثناء استدعاء الأسلوب [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

**مثال:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **حفظ الملف بتنسيق آخر**

### **ملفات XLS**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **ملفات XLSX**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **ملفات PDF**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **تعيين خيار ContentCopyForAccessibility**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)، يمكنك الحصول على أو تعيين خيار PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) للتحكم في الوصول إلى المحتوى في ملف PDF المحول. هذا يعني أنه يسمح لبرامج قراءة الشاشة باستخدام النص داخل ملف PDF لقراءة الملف. يمكنك تعطيله عن طريق تطبيق كلمة مرور لتغيير الأذونات وإلغاء اختيار العنصرين في اللقطة الشاشية [هنا](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **تصدير الخصائص المخصصة إلى ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)، يمكنك تصدير الخصائص المخصصة في جدول البيانات المصدري إلى ملف PDF. تم توفير معيار التصنيف [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) لتحديد الطريقة التي تتم بها تصدير الخصائص. يمكن رؤية هذه الخصائص في برنامج Adobe Acrobat Reader عن طريق النقر على ملف ومن ثم الخيارات كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx" من [هنا](sourceWithCustProps.xlsx) للاختبار وملف PDF الناتج "outSourceWithCustProps" متاح من [هنا](outSourceWithCustProps.pdf) للتحليل.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **تحويل دفتر العمل إكسل إلى Markdown**

توفر Aspose.Cells API دعمًا لتصدير الأوراق الجدولية إلى تنسيق Markdown. لتصدير الورقة الجدولية النشطة إلى Markdown، قم بتمرير [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) كالمعلمة الثانية لأسلوب [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). يمكنك أيضًا استخدام فئة [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) لتحديد الإعدادات الإضافية لتصدير الورقة الجدولية إلى Markdown.

يوضح المثال التالي تصدير ورقة البيانات النشطة إلى Markdown باستخدام عضو تصنيف [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN). يرجى الاطلاع على [ملف Markdown الناتج](Book1.txt) الذي تم إنشاؤه من قبل الكود للإشارة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/java/adjust-workbook-compression-level/)
- [تحويل جدول البيانات إلى تنسيقات مختلفة](/cells/ar/java/converting-workbook-to-different-formats/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [تتبع تقدّم تحويل Excel إلى TIFF](/cells/ar/java/track-conversion-progress-of-excel-to-tiff/)
- [تتبع تقدم تحويل الوثائق](/cells/ar/java/track-document-conversion-progress/)
