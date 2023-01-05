---
title: بي دي إف
type: docs
weight: 220
url: /ar/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل مصنف Excel إلى PDF. في هذا المثال ، سنرى التحويل الكامل لمصنف Excel إلى PDF.

{{% /alert %}}

## **تحويل مصنف Excel إلى PDF**

يتم استخدام ملفات PDF على نطاق واسع لتبادل المستندات بين المنظمات والقطاعات الحكومية والأفراد. إنه تنسيق مستند قياسي وغالبًا ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات Excel Microsoft إلى مستندات PDF.

يدعم Aspose.Cells تحويل ملفات Excel إلى PDF ويحافظ على الدقة المرئية العالية في التحويل.

{{% alert color="primary" %}}

 Aspose.Cells for .NET يكتب مباشرة المعلومات حول API ورقم الإصدار في وثائق المخرجات. على سبيل المثال ، عند تقديم المستند إلى PDF ، يتم تعبئة Aspose.Cells for .NET**تطبيق** حقل بقيمة "Aspose.Cells" و**PDF منتج**حقل ذو قيمة ، على سبيل المثال "Aspose.Cells v17.9".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for .NET لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}}

### **التحويل المباشر**

 Aspose.Cells for .NET يدعم التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ما عليك سوى حفظ ملف Excel في PDF باستخدام امتداد**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** صف دراسي'**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** طريقة. ال**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** طريقة توفر**[SaveFormat.Pdf] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**عضو التعداد الذي يحول ملفات Excel الأصلية إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل جداول بيانات Excel مباشرة إلى تنسيق PDF:

1.  إنشاء كائن من**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)**فئة عن طريق استدعاء مُنشئها الفارغ.
1. يمكنك فتح / تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء المصنف من البداية.
1. قم بأي عمل (إدخال البيانات ، وتطبيق التنسيق ، وتعيين الصيغ ، وإدراج الصور أو الكائنات الرسومية الأخرى ، وما إلى ذلك) في جدول البيانات باستخدام واجهات برمجة التطبيقات Aspose.Cells '.
1.  عند اكتمال كود جدول البيانات ، اتصل بـ**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** صف دراسي'**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**طريقة لحفظ جدول البيانات.

 يجب أن يكون تنسيق الملف PDF لذا اختر*بي دي إف* (قيمة محددة مسبقًا) من**[SaveFormat] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**تعداد لتوليد وثيقة PDF النهائية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **التحويل المتقدم**

 يمكنك أيضًا اختيار استخدام ملف**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** فئة لتعيين سمات مختلفة للتحويل. تعيين خصائص مختلفة لملف**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** تمنحك class التحكم في إعدادات الطباعة والخط والأمان والضغط للمخرج PDF. الخاصية الأكثر أهمية هي**[الامتثال] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**والتي تمكنك من حفظ ملفات Excel في PDF / A متوافق مع ملفات PDF.

#### **حفظ المصنف في PDF / A الملفات المتوافقة**

 يوضح مقتطف الشفرة الوارد أدناه كيفية استخدام ملف**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**فئة لحفظ ملفات Excel بتنسيق PDF متوافق مع PDF / A.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 يرجى ملاحظة أن**[الامتثال] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**تمت إضافة الخاصية مع إصدار Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **قم بتعيين PDF وقت الإنشاء**

 مع ال**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**فئة ، يمكنك الحصول على وقت إنشاء PDF أو تعيينه. يوضح الكود التالي استخدام**[PdfSaveOptions.CreatedTime] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** الخاصية لتعيين وقت إنشاء ملف PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **قم بتعيين خيار ContentCopyForAccessibility**

مع ال**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** فئة ، يمكنك الحصول على PDF أو تعيينه**[AccessibilityExtractContent] (https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** خيار للتحكم في الوصول إلى المحتوى في PDF المحول.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **تصدير الخصائص المخصصة إلى PDF**

مع ال**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** فئة ، يمكنك تصدير الخصائص المخصصة في المصنف المصدر إلى PDF.**[PdfCustomPropertiesExport] (https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**يتم توفير العداد لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader من خلال النقر على ملف ثم خيار الخصائص كما هو موضح في الصورة التالية. يمكن تحميل ملف القالب "sourceWithCustProps.xlsx"[هنا](sourceWithCustProps.xlsx) للاختبار والإخراج PDF يتوفر ملف "outSourceWithCustProps"[هنا](outSourceWithCustProps.pdf) للتحليل.

![ما يجب القيام به: image_بديل_نص](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **سمات التحويل**

نعمل على تحسين ميزات التحويل مع كل إصدار جديد. لا يزال تحويل Aspose.Cell من Excel إلى PDF به بعض القيود. قد يتم فقد بعض تنسيقات جدول البيانات عند التحويل إلى تنسيق PDF. أيضًا ، بعض الكائنات الرسومية غير مدعومة بعد.

يسرد الجدول التالي جميع الميزات المدعومة كليًا أو جزئيًا عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع سمات جدول البيانات ولكنه يحدد تلك الميزات غير المدعومة أو المدعومة جزئيًا للتحويل إلى PDF .

|**عنصر المستند**|**ينسب**|**أيد**|**ملاحظات**|
|:- |:- |:- |:- |
|التوافق||نعم||
|إعدادات الخلفية||نعم||
|الحدود|اللون|نعم||
|الحدود|أسلوب الخط|نعم||
|الحدود|عرض الخط|نعم||
|Cell البيانات||نعم||
|تعليقات||نعم||
|تنسيق مشروط||نعم||
|خصائص المستند||نعم||
|كائنات الرسم||جزئيا|الكائنات المدعومة: TextBox ، Line ، Rectangle ، Oval ، GroupBox ، Button ، CheckBox ، RadioButton ، ListBox ، ComboBox ، Label|
|الخط|بحجم|نعم||
|الخط|اللون|نعم||
|الخط|أسلوب|نعم||
|الخط|تسطير|نعم||
|الخط|تأثيرات|جزئيا|يتم دعم الخط من خلال التأثير فقط|
|الصور||نعم||
|ارتباط تشعبي||نعم||
|الرسوم البيانية||جزئيا||
|اندمجت Cells||نعم||
|فاصل صفحة||نعم||
|اعداد الصفحة|تذييل الرأس|نعم||
|اعداد الصفحة|الهوامش|نعم||
|اعداد الصفحة|اتجاه الصفحة|نعم||
|اعداد الصفحة|مقاس الصفحه|نعم||
|اعداد الصفحة|منطقة الطباعة|نعم||
|اعداد الصفحة|عناوين الطباعة|نعم||
|اعداد الصفحة|تحجيم|نعم||
|ارتفاع الصف / عرض العمود||نعم||
|لغة RTL (من اليمين إلى اليسار)||نعم||

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال**[Workbook.CalculateFormula ()] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**مباشرة قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

## **موضوعات مسبقة**
- [أضف PDF إشارات مرجعية](/cells/ar/net/add-pdf-bookmarks/)
- [قم بإضافة PDF إشارات مرجعية ذات الوجهات المحددة](/cells/ar/net/add-pdf-bookmarks-with-named-destinations/)
- [تجنب الصفحة الفارغة في الإخراج PDF عندما لا يوجد شيء للطباعة](/cells/ar/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [قم بتغيير الخط على أحرف Unicode المحددة فقط أثناء الحفظ في PDF](/cells/ar/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [التحكم في تحميل الموارد الخارجية في مصنف MS Excel أثناء التقديم إلى PDF](/cells/ar/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [قم بتحويل ملف XLS إلى تنسيق PDF](/cells/ar/net/convert-an-xls-file-to-pdf-format/)
- [قم بتحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [قم بتحويل XLS ملف مع صور أو مخططات إلى PDF](/cells/ar/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [قم بإنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/net/create-pdfbookmarkentry-for-chart-sheet/)
- [احتواء كافة أعمدة ورقة العمل على PDF صفحة واحدة](/cells/ar/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [احصل على DrawObject و Bound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler](/cells/ar/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [احصل على تحذيرات لاستبدال الخط أثناء عرض ملف Excel](/cells/ar/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [تجاهل الأخطاء أثناء تقديم Excel إلى PDF](/cells/ar/net/ignore-errors-while-rendering-excel-to-pdf/)
- [حدد عدد الصفحات التي تم إنشاؤها - Excel بتحويل PDF](/cells/ar/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [طباعة التعليقات أثناء الحفظ في PDF](/cells/ar/net/print-comments-while-saving-to-pdf/)
- [عرض وظائف Office الإضافية أثناء تحويل Excel إلى PDF](/cells/ar/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم واحد PDF صفحة لكل ورقة عمل Excel - تحويل Excel إلى PDF](/cells/ar/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [تقديم أحرف تكميلية Unicode في الإخراج PDF بواسطة Aspose.Cells](/cells/ar/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة أخذ عينات الصور المضافة - من Excel إلى تحويل PDF](/cells/ar/net/resampling-added-images-excel-to-pdf-conversion/)
- [احفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/net/save-each-worksheet-to-a-different-pdf-file/)
- [احفظ ملف Excel في PDF بالحجم القياسي أو الأدنى](/cells/ar/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [تأمين وثائق PDF](/cells/ar/net/secure-pdf-documents/)
- [حدد كيفية عبور السلسلة في الإخراج PDF والصورة](/cells/ar/net/specify-how-to-cross-string-in-output-pdf-and-image/)
