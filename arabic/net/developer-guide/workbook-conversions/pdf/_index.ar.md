---
title: Pdf
type: docs
weight: 220
url: /ar/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل مصنف Excel إلى PDF. في هذا المثال، سنرى التحويل الكامل لمصنف Excel إلى PDF.

{{% /alert %}}

##  **تحويل مصنف Excel إلى PDF**

تُستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنه تنسيق مستند قياسي وغالبًا ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات Excel Microsoft إلى PDF مستندًا.

Aspose.Cells يدعم تحويل ملفات Excel إلى PDF ويحافظ على دقة بصرية عالية في التحويل.

{{% alert color="primary" %}}

 Aspose.Cells for .NET يكتب مباشرة المعلومات حول API ورقم الإصدار في مستندات الإخراج. على سبيل المثال، عند تقديم المستند إلى PDF، تتم تعبئة Aspose.Cells for .NET**PDF منتج** حقل ذو قيمة، على سبيل المثال "Aspose.Cells v23.2".

 يرجى ملاحظة أنه يمكنك تغيير هذه المعلومات في المستندات الناتجة عن طريق**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)** ملكية.

{{% /alert %}}

###  **التحويل المباشر**

 Aspose.Cells for .NET يدعم التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ما عليك سوى حفظ ملف Excel على الرقم PDF باستخدام ملف**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**فصل'**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** طريقة. ال**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** توفر الطريقة**[حفظ التنسيق.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**عضو التعداد الذي يحول ملفات Excel الأصلية إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل جداول بيانات Excel مباشرة إلى تنسيق PDF:

1.  إنشاء مثيل لكائن من**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**فئة عن طريق استدعاء منشئها الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء المصنف من البداية.
1. قم بأي عمل (إدخال البيانات، وتطبيق التنسيق، وتعيين الصيغ، وإدراج الصور أو الكائنات الرسومية الأخرى، وما إلى ذلك) في جدول البيانات باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1.  عند اكتمال رمز جدول البيانات، اتصل بـ**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**فصل'**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**طريقة حفظ جدول البيانات.

 يجب أن يكون تنسيق الملف PDF لذا اختر*Pdf* (قيمة محددة مسبقًا) من**[حفظ التنسيق](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**التعداد لإنشاء مستند PDF النهائي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **التحويل المتقدم**

 يمكنك أيضًا اختيار استخدام**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class لتعيين سمات مختلفة للتحويل. تحديد خصائص مختلفة لل**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** تمنحك الفئة التحكم في إعدادات الطباعة والخط والأمان والضغط للإخراج PDF. الخاصية الأكثر أهمية هي**[الامتثال](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**والتي تمكنك من حفظ ملفات Excel إلى ملفات PDF/A المتوافقة مع PDF.

####  **حفظ المصنف في PDF/A الملفات الممتثلة**

 يوضح مقتطف الكود المتوفر أدناه كيفية استخدام**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**فئة لحفظ ملفات Excel بتنسيق PDF/A المتوافق PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أن**[الامتثال](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**تمت إضافة الخاصية مع إصدار Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

####  **اضبط وقت الإنشاء PDF**

 مع ال**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**فئة، يمكنك الحصول على أو ضبط وقت الإنشاء PDF. الكود التالي يوضح استخدام**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** الخاصية لتعيين وقت إنشاء الملف PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **قم بتعيين خيار ContentCopyForAccessibility**

مع ال**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** فئة، يمكنك الحصول على أو تعيين PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** خيار للتحكم في الوصول إلى المحتوى في PDF المحول.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **تصدير الخصائص المخصصة إلى PDF**

مع ال**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** فئة، يمكنك تصدير الخصائص المخصصة في المصنف المصدر إلى PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**يتم توفير العداد لتحديد الطريقة التي يتم بها تصدير الخصائص. ويمكن ملاحظة هذه الخصائص في برنامج Adobe Acrobat Reader بالضغط على خيار File ثم خصائص كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx".[هنا](sourceWithCustProps.xlsx) للاختبار والإخراج PDF ملف "outSourceWithCustProps" متاح[هنا](outSourceWithCustProps.pdf) للتحليل.

![ما يجب القيام به:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **سمات التحويل**

نحن نعمل على تحسين ميزات التحويل مع كل إصدار جديد. لا يزال تحويل Aspose.Cell من Excel إلى PDF به بعض القيود. MapChart غير مدعوم عند التحويل إلى تنسيق PDF. كما أن بعض الكائنات الرسومية غير معتمدة بشكل جيد.

يسرد الجدول التالي جميع الميزات المدعومة كليًا أو جزئيًا عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع سمات جدول البيانات ولكنه يحدد الميزات غير المدعومة أو المدعومة جزئيًا للتحويل إلى PDF .

|**عنصر الوثيقة**|**يصف**|**أيد**|**ملحوظات**|
| :- | :- | :- | :- |
|تنسيق| |نعم| |
|إعدادات الخلفية| |نعم| |
|حدود|لون|نعم| |
|حدود|أسلوب الخط|نعم| |
|حدود|عرض الخط|نعم| |
|Cell بيانات| |نعم| |
|تعليقات| |نعم| |
|تنسيق مشروط| |نعم| |
|خصائص المستند| |نعم| |
|كائنات الرسم| |جزئيا|لا يتم دعم تأثيرات الظل والتأثيرات ثلاثية الأبعاد للكائنات الرسومية بشكل جيد؛ يتم دعم WordArt وSmartArt جزئيًا.|
|الخط|مقاس|نعم| |
|الخط|لون|نعم| |
|الخط|أسلوب|نعم| |
|الخط|تسطير|نعم| |
|الخط|تأثيرات|نعم||
|الصور| |نعم| |
|الارتباط التشعبي| |نعم| |
|الرسوم البيانية| |جزئيا|MapChart غير مدعوم.|
|تم الدمج Cells| |نعم| |
|فاصل صفحة| |نعم| |
|اعداد الصفحة|تذييل الرأس|نعم| |
|اعداد الصفحة|هوامش|نعم| |
|اعداد الصفحة|اتجاه الصفحة|نعم| |
|اعداد الصفحة|مقاس الصفحه|نعم| |
|اعداد الصفحة|منطقة الطباعة|نعم| |
|اعداد الصفحة|طباعة العناوين|نعم| |
|اعداد الصفحة|التحجيم|نعم| |
|ارتفاع الصف/عرض العمود| |نعم| |
|لغة RTL (من اليمين إلى اليسار).| |نعم| |

{{% alert color="primary" %}}

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل الاتصال به**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** مباشرة قبل تقديم جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

##  **مواضيع متقدمة**
- [إضافة PDF الإشارات المرجعية](/cells/ar/net/add-pdf-bookmarks/)
- [إضافة PDF الإشارات المرجعية مع الوجهات المسماة](/cells/ar/net/add-pdf-bookmarks-with-named-destinations/)
- [تجنب الصفحة الفارغة في الإخراج PDF عندما لا يكون هناك شيء للطباعة](/cells/ar/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [قم بتغيير الخط على أحرف Unicode المحددة فقط مع الحفظ في PDF](/cells/ar/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [التحكم في تحميل الموارد الخارجية في MS Excel Workbook أثناء العرض إلى PDF](/cells/ar/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [تحويل ملف XLSX إلى تنسيق PDF](/cells/ar/net/convert-xlsx-file-to-pdf-format/)
- [تحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [تحويل XLS ملف بالصور أو المخططات إلى PDF](/cells/ar/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [إنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/net/create-pdfbookmarkentry-for-chart-sheet/)
- [احتواء جميع أعمدة ورقة العمل في صفحة PDF واحدة](/cells/ar/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [احصل على DrawObject and Bound أثناء العرض إلى PDF باستخدام فئة DrawObjectEventHandler](/cells/ar/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [احصل على تحذيرات بشأن استبدال الخط أثناء عرض ملف Excel](/cells/ar/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [تجاهل الأخطاء أثناء تقديم Excel إلى PDF](/cells/ar/net/ignore-errors-while-rendering-excel-to-pdf/)
- [الحد من عدد الصفحات التي تم إنشاؤها - تحويل Excel إلى PDF](/cells/ar/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [اطبع التعليقات أثناء الحفظ في PDF](/cells/ar/net/print-comments-while-saving-to-pdf/)
- [عرض وظائف Office الإضافية أثناء تحويل Excel إلى PDF](/cells/ar/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم صفحة واحدة PDF لكل ورقة عمل Excel - تحويل Excel إلى PDF](/cells/ar/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [تقديم أحرف Unicode التكميلية في الإخراج PDF بواسطة Aspose.Cells](/cells/ar/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة تشكيل الصور المضافة - تحويل Excel إلى PDF](/cells/ar/net/resampling-added-images-excel-to-pdf-conversion/)
- [احفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/net/save-each-worksheet-to-a-different-pdf-file/)
- [احفظ Excel في PDF بالحجم القياسي أو الحد الأدنى](/cells/ar/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [احفظ أوراق العمل المحددة في PDF](/cells/ar/net/save-specified-worksheets-to-pdf/)
- [تأمين PDF الوثائق](/cells/ar/net/secure-pdf-documents/)
- [حدد كيفية عبور السلسلة في الإخراج PDF والصورة](/cells/ar/net/specify-how-to-cross-string-in-output-pdf-and-image/)
