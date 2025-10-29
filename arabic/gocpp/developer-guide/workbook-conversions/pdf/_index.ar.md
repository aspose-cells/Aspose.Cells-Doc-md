---
title: تحويل إكسل إلى PDF مع Golang عبر C++
linktitle: تحويل Excel إلى PDF
type: docs
weight: 220
url: /ar/go-cpp/convert-excel-to-pdf/
description: تعلم كيفية تحويل دفاتر عمل إكسل إلى صيغة PDF باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل دفاتر عمل Excel إلى PDF. في هذا المثال، سنقوم بمشاهدة التحويل الكامل لدفتر عمل Excel إلى PDF.

{{% /alert %}}

## **تحويل سجل عمل Excel إلى PDF**

ملفات PDF مستخدمة على نطاق واسع لتبادل الوثائق بين المؤسسات والقطاعات الحكومية والأفراد. هو صيغة وثيقة قياسية، وغالباً ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات إكسل إلى وثائق PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

{{% alert color="primary" %}}

تكتب Aspose.Cells for C++ مباشرة المعلومات حول API ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند تصيير مستند إلى PDF، تملأ Aspose.Cells for C++ حقل **منتج PDF** بقيمة، مثلاً 'Aspose.Cells v23.2'.

يرجى ملاحظة أنه يمكنك تغيير هذه المعلومات في المستندات الناتجة باستخدام خاصية [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **التحويل المباشر**

يدعم Aspose.Cells for C++ التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ببساطة، احفظ ملف Excel كملف PDF باستخدام طريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) من فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/). تقدم طريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) عضو التعداد [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) الذي يحول ملفات Excel الأصلية إلى صيغة PDF.

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. أنشئ كائن من فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) عن طريق استدعاء منشئها الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. قم بأي عمل (إدخال بيانات، تطبيق التنسيق، تعيين الصيغ، إدراج الصور، أو أشكال الرسم الأخرى، وهلم جرا) على جدول البيانات باستخدام واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells.
1. عند اكتمال رمز جدول البيانات، استدعي طريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) من فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) لحفظ جدول البيانات.

يجب أن يكون تنسيق الملف PDF، لذلك اختر *Pdf* (قيمة معرفة مسبقًا) من التعداد [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) لإنشاء المستند النهائي بصيغة PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf.go" >}}
### **التحويل المتقدم**

يمكنك أيضًا اختيار استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) لضبط خصائص مختلفة للتحويل. يتيح ضبط خصائص مختلفة لفئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) السيطرة على إعدادات الطباعة، والخط، والأمان، وضغوط البيانات لإخراج PDF.

أهم خاصية هي [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/)، التي تمكنك من تحديد مستوى الامتثال لمعايير PDF. حاليًا، يمكنك الحفظ بصيغ PDF 1.4، PDF 1.5، PDF 1.6، PDF 1.7، PDF/A-1a، PDF/A-1b، PDF/A-2a، PDF/A-2b، PDF/A-2u، PDF/A-3a، PDF/A-2ab، و PDF/A-3u. لاحظ أن حجم ملف الإخراج يكون أكبر عند استخدام تنسيق PDF/A.

#### **حفظ جدول البيانات إلى ملف PDF/A المتوافق**

يوضح الشفرة البرمجية أدناه كيفية استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) لحفظ ملفات Excel بصيغة PDF / PDF/A متوافقة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-1.go" >}}
{{% alert color="primary" %}}

يرجى ملاحظة، تمت إضافة خاصية [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) مع إصدار Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **تعيين وقت إنشاء ملف PDF**

باستخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)، يمكنك الحصول على وقت إنشاء ملف PDF أو ضبطه. تظهر الشفرة التالية استخدام خاصية [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcreatedtime/) لضبط وقت إنشاء ملف PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-2.go" >}}
#### **تعيين خيار ContentCopyForAccessibility**

باستخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)، يمكنك الحصول على أو ضبط خيار [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) لملف PDF للتحكم في الوصول إلى المحتوى في PDF المحول.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-3.go" >}}
#### **تصدير الخصائص المخصصة إلى ملف PDF**

باستخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)، يمكنك تصدير الخصائص المخصصة في دفتر المصدر إلى PDF. يتم توفير التعداد [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader بالنقر على ملف ثم خيار خصائص كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx" [من هنا](sourceWithCustProps.xlsx) للاختبار، وملف PDF الناتج "outSourceWithCustProps" متوفر [هنا](outSourceWithCustProps.pdf) للتحليل.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-4.go" >}}
### **سمات التحويل**

نحن نعمل على تعزيز ميزات التحويل مع كل إصدار جديد. لا تزال عملية تحويل Excel إلى PDF في Aspose.Cells تحتوي على بعض القيود. MapChart غير مدعوم عند التحويل إلى تنسيق PDF. كما أن بعض كائنات الرسم غير مدعومة بشكل جيد.

تدرج الجدول التالي جميع الميزات المدعومة كليًا أو جزئيًا عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع سمات جدول البيانات، لكنه يحدد الميزات التي لا تدعم أو تدعم جزئيًا للتحويل إلى PDF.

| عنصر المستند | الخاصية | مدعوم | ملاحظات |
| :- | :- | :- | :- |
| المحاذاة |  | نعم |  |
| إعدادات الخلفية |  | نعم |  |
| الحد | اللون | نعم |  |
| الحد | نوع الخط | نعم |  |
| الحد | عرض الخط | نعم |  |
| بيانات الخلية |  | نعم |  |
| التعليقات |  | نعم |  |
| التنسيق الشرطي |  | نعم |  |
| خصائص المستند |  | نعم |  |
| كائنات الرسم |  | جزئيا | الظلال والتأثيرات ثلاثية الأبعاد لكائنات الرسم غير مدعومة بشكل جيد؛ WordArt و SmartArt مدعومان جزئيا. |
| الخط | الحجم | نعم |  |
| الخط | اللون | نعم |  |
| الخط | النمط | نعم |  |
| الخط | التسطير | نعم |  |
| الخط | التأثيرات | نعم |  |
| الصور |  | نعم |  |
| الرابط التشعبي |  | نعم |  |
| الرسوم البيانية |  | جزئيا | مخطط الخريطة غير مدعوم. |
| خلايا مدمجة |  | نعم |  |
| فاصل الصفحة |  | نعم |  |
| إعداد الصفحة | رأس/تذييل | نعم |  |
| إعداد الصفحة | الهوامش | نعم |  |
| إعداد الصفحة | اتجاه الصفحة | نعم |  |
| إعداد الصفحة | حجم الصفحة | نعم |  |
| إعداد الصفحة | منطقة الطباعة | نعم |  |
| إعداد الصفحة | عناوين الطباعة | نعم |  |
| إعداد الصفحة | المقياس | نعم |  |
| ارتفاع الصف/عرض العمود |  | نعم |  |
| لغة من اليمين إلى اليسار |  | نعم |  |

{{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، فمن الأفضل الاتصال بـ [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) قبل تصيير الجدول إلى PDF. سيساعد ذلك على إعادة حساب القيم المعتمدة على الصيغ، وإظهار القيم الصحيحة في PDF.

{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة](/cells/ar/cpp/add-pdf-bookmarks-with-named-destinations/)
- [تغيير الخط المستخدم للرموز اليونيكود الخاصة عند حفظ الملف إلى PDF](/cells/ar/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [تحويل ملف XLSX إلى تنسيق PDF](/cells/ar/cpp/convert-xlsx-file-to-pdf-format/)
- [تحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [تحويل ملف XLS مع صور أو رسوم بيانية إلى تنسيق PDF](/cells/ar/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [إنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة](/cells/ar/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [الحصول على DrawObject والحدود أثناء تقديمها إلى PDF باستخدام فئة DrawObjectEventHandler](/cells/ar/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [الحصول على تحذيرات بديلة للخط أثناء تحويل ملف Excel إلى PDF](/cells/ar/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [تجاهل الأخطاء أثناء تحويل Excel إلى PDF](/cells/ar/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [تحديد عدد الصفحات التي يتم إنشاؤها – تحويل من Excel إلى PDF](/cells/ar/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [طباعة التعليقات عند الحفظ إلى PDF](/cells/ar/cpp/print-comments-while-saving-to-pdf/)
- [تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF](/cells/ar/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم صفحة PDF واحدة لكل ورقة عمل إكسل - تحويل إكسل إلى PDF](/cells/ar/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [عرض الحروف اليونيكود الإضافية في ملف PDF الناتج باستخدام Aspose.Cells](/cells/ar/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة عينات الصور المضافة - تحويل إكسل إلى PDF](/cells/ar/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [حفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [حفظ إكسل في ملف PDF بحجم قياسي أو حد أدنى](/cells/ar/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [حفظ ورقات العمل المحددة في ملف PDF](/cells/ar/cpp/save-specified-worksheets-to-pdf/)
- [مستندات PDF آمنة](/cells/ar/cpp/secure-pdf-documents/)
- [تحديد كيفية عبور السلسلة في ملف PDF والصورة](/cells/ar/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
