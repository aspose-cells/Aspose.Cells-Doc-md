---
title: Pdf
type: docs
weight: 220
url: /ar/python-net/convert-excel-to-pdf/
description: تعلم كيفية تحويل إكسل إلى PDF باستخدام Aspose.Cells for Python via .NET API.
keywords: بايثون تحويل Excel إلى PDF، تحويل Excel إلى PDF باستخدام بايثون، بايثون حفظ Excel إلى PDF، Excel إلى PDF في بايثون
---

{{% alert color="primary" %}}

تدعم Aspose.Cells for Python via .NET تحويل مصنف Excel إلى PDF. في هذا المثال، سنرى تحويل كامل لمصنف Excel إلى PDF.

{{% /alert %}}

## **تحويل سجل عمل Excel إلى PDF**

تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.

يدعم Aspose.Cells for Python via .NET تحويل ملفات Excel إلى PDF ويحتفظ بالمظهر البصري العالي خلال التحويل.

{{% alert color="primary" %}}

تكتب Aspose.Cells for Python via .NET مباشرة معلومات حول واجهة برمجة التطبيقات ورقم الإصدار في وثائق الإخراج. على سبيل المثال، عند تقديم مستند إلى PDF، يملأ Aspose.Cells for Python via .NET حقل **منتج PDF** بالقيمة، مثل 'Aspose.Cells for Python via .NET v23.2'.

يرجى ملاحظة أنه يمكنك تغيير هذه المعلومات في مستندات الإخراج عن طريق خاصية [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **التحويل المباشر**

تدعم Aspose.Cells for Python via .NET التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرمجيات الأخرى. قم ببساطة بحفظ ملف Excel إلى PDF باستخدام فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) وطريقة [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) لهذه الفئة. توفر الطريقة [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) عضو فئة التعداد الذي يحول الملفات الأصلية بتنسيق Excel إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. قم بإنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) بالاتصال ببنائه الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. اقم بفعل أي عمل (إدخال بيانات، تطبيق التنسيق، تعيين الصيغ، إدراج الصور أو أجسام الرسم الأخرى، وما إلى ذلك) على جدول البيانات باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells for Python via .NET.
1. عند اكتمال رمز الجداول، اتصل بطريقة [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) في فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) لحفظ الجدول.

يمكنك أيضًا اختيار استخدام فئة {0} لتعيين خصائص مختلفة للتحويل. تعيين خصائص مختلفة لفئة {1} يمنحك التحكم في الطباعة والخط وإعدادات الأمان والضغط لملف PDF الناتج. الخاصية الأكثر أهمية هي {2} التي تمكّنك من حفظ ملفات Excel إلى ملفات PDF/A متوافقة مع PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **التحويل المتقدم**

يمكنك أيضًا اختيار استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) لتعيين خصائص مختلفة للتحويل. تعيين خصائص مختلفة لفئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) يمنحك التحكم في إعدادات الطباعة والخط والأمان وضغط الإخراج PDF. أهم خاصية هي [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) التي تمكنك من حفظ ملفات Excel إلى ملفات PDF/A متوافقة مع PDF.

#### **حفظ جدول البيانات إلى ملف PDF/A المتوافق**

مقطع الرمز المقدم أدناه يوضح كيفية استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) لحفظ ملفات Excel إلى تنسيق PDF/A متوافق مع PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أن خاصية [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) تمت إضافتها مع إصدار Aspose.Cells for Python via .NET لـ .NET 5.3.0.

{{% /alert %}}

#### **تعيين وقت إنشاء ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)، يمكنك الحصول على أو تعيين وقت إنشاء PDF. يوضح الرمز التالي استخدام الخاصية [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) لتعيين وقت إنشاء ملف PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **تعيين خيار ContentCopyForAccessibility**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)، يمكنك الحصول على أو تعيين خيار [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) للتحكم في وصول المحتوى في ملف PDF المحول.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **تصدير الخصائص المخصصة إلى ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)، يمكنك تصدير الخصائص المخصصة في دفتر العمل المصدر إلى PDF. وتوفر مُعدّلة [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader بالنقر فوق ملف ثم الخصائص كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx" من [هنا](sourceWithCustProps.xlsx) للفحص وملف PDF الناتج "outSourceWithCustProps" متاح [هنا](outSourceWithCustProps.pdf) للتحليل.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **سمات التحويل**

نحن نعمل على تعزيز ميزات التحويل مع كل إصدار جديد. لا تزال عملية تحويل Excel إلى PDF من Aspose.Cells تحتوي على بعض القيود. لا يتم دعم MapChart عند التحويل إلى تنسيق PDF. أيضًا، بعض الكائنات الرسومية لا تتمتع بدعم جيد.

الجدول التالي يقوم بتسريد جميع الميزات التي يتم دعمها جزئيا أو بالكامل عند التصدير إلى PDF باستخدام Aspose.Cells for Python via .NET. هذا الجدول ليس نهائيًا ولا يغطي جميع سمات جداول البيانات ولكنه يحدد تلك الميزات التي غير مدعومة جزئيا أو غير معتمدة للتحويل إلى PDF.

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

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فإن الأفضلية لاصدار [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) الأمر مباشرةً قبل تقديم جدول البيانات إلى تنسيق PDF. سيؤدي ذلك إلى ضمان إعادة حساب قيم الصيغة التي تعتمد عليها، وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة علامات مرجعية لملف PDF](/cells/ar/python-net/add-pdf-bookmarks/)
- [إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة](/cells/ar/python-net/add-pdf-bookmarks-with-named-destinations/)
- [تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة](/cells/ar/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [تحويل ملف XLSX إلى تنسيق PDF](/cells/ar/python-net/convert-xlsx-file-to-pdf-format/)
- [تحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [تحويل ملف XLS مع صور أو رسوم بيانية إلى تنسيق PDF](/cells/ar/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [إنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة](/cells/ar/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [تجاهل الأخطاء أثناء تحويل Excel إلى PDF](/cells/ar/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [تحديد عدد الصفحات التي يتم إنشاؤها – تحويل من Excel إلى PDF](/cells/ar/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [طباعة التعليقات عند الحفظ إلى PDF](/cells/ar/python-net/print-comments-while-saving-to-pdf/)
- [تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF](/cells/ar/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم صفحة PDF واحدة لكل ورقة عمل إكسل - تحويل إكسل إلى PDF](/cells/ar/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [عرض الحروف اليونيكود الإضافية في ملف PDF الناتج باستخدام Aspose.Cells](/cells/ar/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة عينات الصور المضافة - تحويل إكسل إلى PDF](/cells/ar/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [حفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [حفظ إكسل في ملف PDF بحجم قياسي أو حد أدنى](/cells/ar/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [حفظ ورقات العمل المحددة في ملف PDF](/cells/ar/python-net/save-specified-worksheets-to-pdf/)
- [مستندات PDF آمنة](/cells/ar/python-net/secure-pdf-documents/)
- [تحديد كيفية عبور السلسلة في ملف PDF والصورة](/cells/ar/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="python-net" >}}
