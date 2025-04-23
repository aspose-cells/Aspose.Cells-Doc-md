---
title: Pdf
type: docs
weight: 220
url: /ar/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تحويل سجل العمل في Excel إلى PDF. في هذا المثال، سنرى التحويل الكامل لسجل عمل Excel إلى PDF.

{{% /alert %}}

## **تحويل سجل عمل Excel إلى PDF**

تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

{{% alert color="primary" %}}

يكتب Aspose.Cells for .NET مباشرة المعلومات حول الواجهة البرمجية ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند تقديم مستند إلى PDF، يملأ Aspose.Cells for .NET حقل **PDF Producer** بالقيمة، على سبيل المثال 'Aspose.Cells v23.2'.

يرجى ملاحظة أنه يمكنك تغيير هذه المعلومات في مستندات الإخراج عن طريق خاصية [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **التحويل المباشر**

يدعم Aspose.Cells for .NET التحويل من جداول البيانات إلى ملف PDF بشكل مستقل عن البرمجيات الأخرى. ما عليك سوى حفظ ملف Excel كملف PDF باستخدام طريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) في فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). طريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) توفر عضو تعداد [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) الذي يحول الملفات الأصلية للExcel إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. قم بإنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) بالاتصال ببنائه الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. أدخل أي عمل (البيانات الدخلية، تطبيق التنسيق، ضبط الصيغ، إدراج الصور أو كائنات الرسم الأخرى، وما إلى ذلك) على ورق العمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1. عند اكتمال رمز الجداول، اتصل بطريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) في فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) لحفظ الجدول.

يجب أن يكون تنسيق الملف PDF، لذا حدد *Pdf* (قيمة محددة مسبقًا) من تعداد [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) لتوليد مستند PDF النهائي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **التحويل المتقدم**

يمكنك أيضًا استخدام الفصيلة [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) لتعيين خصائص مختلفة للتحويل. تعيين خصائص مختلفة للفصيلة [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لمخرج PDF. 

أهم خاصية هي [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) التي تمكّنك من تعيين مستوى الامتثال لمعايير PDF. حاليًا، يمكنك حفظ إلى صيغ PDF 1.4، PDF 1.5، PDF 1.6، PDF 1.7، PDF/A-1a، PDF/A-1b، PDF/A-2a، PDF/A-2b، PDF/A-2u، PDF/A-3a، PDF/A-2ab، وصيغ PDF/A-3u. يرجى ملاحظة أنه مع صيغة PDF/A، يكون حجم الملف الناتج أكبر من حجم ملف PDF عادي.

#### **حفظ جدول البيانات إلى ملف PDF/A المتوافق**

مقطع الرمز المقدم أدناه يوضح كيفية استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) لحفظ ملفات Excel إلى تنسيق PDF/A متوافق مع PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أن تمت إضافة خاصية [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) مع إصدار Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **تعيين وقت إنشاء ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)، يمكنك الحصول على أو تعيين وقت إنشاء PDF. يوضح الرمز التالي استخدام الخاصية [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) لتعيين وقت إنشاء ملف PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **تعيين خيار ContentCopyForAccessibility**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)، يمكنك الحصول على أو تعيين خيار [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) للتحكم في وصول المحتوى في ملف PDF المحول.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **تصدير الخصائص المخصصة إلى ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)، يمكنك تصدير الخصائص المخصصة في دفتر العمل المصدر إلى PDF. وتوفر مُعدّلة [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport) لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader بالنقر فوق ملف ثم الخصائص كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx" من [هنا](sourceWithCustProps.xlsx) للفحص وملف PDF الناتج "outSourceWithCustProps" متاح [هنا](outSourceWithCustProps.pdf) للتحليل.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **سمات التحويل**

نحن نعمل على تعزيز ميزات التحويل مع كل إصدار جديد. لا تزال عملية تحويل Excel إلى PDF من Aspose.Cells تحتوي على بعض القيود. لا يتم دعم MapChart عند التحويل إلى تنسيق PDF. أيضًا، بعض الكائنات الرسومية لا تتمتع بدعم جيد.

الجدول التالي يقوم بسرد جميع الميزات المدعومة جزئيًا أو بالكامل عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع خصائص جدول البيانات ولكنه يحدد تلك الميزات التي لا تتم دعمها أو يتم دعمها جزئيًا للتحويل إلى PDF.

|**عنصر المستند**|**السمة**|**مدعوم**|**ملاحظات**|
| :- | :- | :- | :- |
|المحاذاة| |نعم| |
|إعدادات الخلفية| |نعم| |
|الحدود|لون|نعم| |
|الحدود|نمط الخط|نعم| |
|الحدود|سمك الخط|نعم| |
|بيانات الخلية| |نعم| |
|التعليقات| |نعم| |
|تنسيق شرطي| |نعم| |
|خصائص المستند| |نعم| |
|كائنات الرسم| |جزئيا|لا يتم دعم الظل والتأثيرات ثلاثية الأبعاد لكائنات الرسم بشكل جيد؛ WordArt و SmartArt يتم دعمهما جزئيا.|
|الخط|الحجم|نعم| |
|الخط|اللون|نعم| |
|الخط|النمط|نعم| |
|الخط|التسطير|نعم| |
|الخط|التأثيرات|نعم||
|الصور| |نعم| |
|الارتباط| |نعم| |
|الرسوم البيانية| |جزئيا|لم يتم دعم MapChart.|
|الخلايا المدمجة| |نعم| |
|فاصل الصفحة| |نعم| |
|إعداد الصفحة|الرأس/التذييل|نعم| |
|إعداد الصفحة|الهوامش|نعم| |
|إعداد الصفحة|اتجاه الصفحة|نعم| |
|إعداد الصفحة|حجم الصفحة|نعم| |
|إعداد الصفحة|منطقة الطباعة|نعم| |
|إعداد الصفحة|عناوين الطباعة|نعم| |
|إعداد الصفحة|تحجيم|نعم| |
|ارتفاع الصف/عرض العمود| |نعم| |
|لغة من اليمين إلى اليسار| |نعم| |

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل عرض الجدول في تنسيق PDF. هذا سيضمن إعادة حساب القيم المعتمدة على الصيغ، وعرض القيم الصحيحة في ملف PDF.

{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة علامات مرجعية لملف PDF](/cells/ar/net/add-pdf-bookmarks/)
- [إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة](/cells/ar/net/add-pdf-bookmarks-with-named-destinations/)
- [تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة](/cells/ar/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [تغيير الخط المستخدم للرموز اليونيكود الخاصة عند حفظ الملف إلى PDF](/cells/ar/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [التحكم في تحميل الموارد الخارجية في دفتر العمل في MS Excel أثناء تحويله إلى PDF](/cells/ar/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [تحويل ملف XLSX إلى تنسيق PDF](/cells/ar/net/convert-xlsx-file-to-pdf-format/)
- [تحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [تحويل ملف XLS مع صور أو رسوم بيانية إلى تنسيق PDF](/cells/ar/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [إنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/net/create-pdfbookmarkentry-for-chart-sheet/)
- [تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة](/cells/ar/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [الحصول على DrawObject والحدود أثناء تقديمها إلى PDF باستخدام فئة DrawObjectEventHandler](/cells/ar/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [الحصول على تحذيرات بديلة للخط أثناء تحويل ملف Excel إلى PDF](/cells/ar/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [تجاهل الأخطاء أثناء تحويل Excel إلى PDF](/cells/ar/net/ignore-errors-while-rendering-excel-to-pdf/)
- [تحديد عدد الصفحات التي يتم إنشاؤها – تحويل من Excel إلى PDF](/cells/ar/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [طباعة التعليقات عند الحفظ إلى PDF](/cells/ar/net/print-comments-while-saving-to-pdf/)
- [تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF](/cells/ar/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم صفحة PDF واحدة لكل ورقة عمل إكسل - تحويل إكسل إلى PDF](/cells/ar/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [عرض الحروف اليونيكود الإضافية في ملف PDF الناتج باستخدام Aspose.Cells](/cells/ar/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة عينات الصور المضافة - تحويل إكسل إلى PDF](/cells/ar/net/resampling-added-images-excel-to-pdf-conversion/)
- [حفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/net/save-each-worksheet-to-a-different-pdf-file/)
- [حفظ إكسل في ملف PDF بحجم قياسي أو حد أدنى](/cells/ar/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [حفظ ورقات العمل المحددة في ملف PDF](/cells/ar/net/save-specified-worksheets-to-pdf/)
- [مستندات PDF آمنة](/cells/ar/net/secure-pdf-documents/)
- [تحديد كيفية عبور السلسلة في ملف PDF والصورة](/cells/ar/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
