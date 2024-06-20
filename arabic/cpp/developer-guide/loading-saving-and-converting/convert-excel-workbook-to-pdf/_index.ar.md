---
title: تحويل مصنف Excel إلى PDF
type: docs
weight: 80
url: /ar/cpp/convert-excel-workbook-to-pdf/
---

## **تحويل سجل عمل Excel إلى PDF**
تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

{{% alert color="primary" %}} 

يكتب Aspose.Cells مباشرةً معلومات حول واجهة برمجة التطبيقات ورقم الإصدار في المستندات الناتجة. على سبيل المثال ، عند تقديم مستند إلى PDF ، يملأ Aspose.Cells for C++ الحقل **التطبيق** بالقيمة 'Aspose.Cells' وحقل **شركة الإنتاج بتنسيق PDF** بالقيمة ، مثل 'Aspose.Cells v18.5.0'.

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for C++ بتغيير أو إزالة هذه المعلومات من مستند الإخراج.

{{% /alert %}} 
### **التحويل المباشر**
Aspose.Cells يدعم التحويل من جداول البيانات إلى صيغة PDF بشكل مستقل عن البرمجيات الأخرى. قم ببساطة بحفظ ملف Excel إلى PDF باستخدام فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) وطريقة [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) . توفر طريقة [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) عضو تعداد [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) الذي يحول الملفات الأصلية من Excel إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. يتم إنشاء كائن من فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) باستدعاء بناءه الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. أدخل أي عمل (البيانات الدخلية، تطبيق التنسيق، ضبط الصيغ، إدراج الصور أو كائنات الرسم الأخرى، وما إلى ذلك) على ورق العمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1. عندما يكون رمز جدول البيانات كاملاً، قم بدعوة طريقة [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) لفئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) لحفظ جدول البيانات.

يجب أن يكون تنسيق الملف PDF، لذا حدد PDF ذو الصلة (قيمة محددة مسبقًا) من تعداد SaveFormat لتوليد مستند PDF النهائي

يرجى الاطلاع على الرمز البريدي الخاص، وملف Excel الخاص به [67338368.xlsx](sample Excel file) وملف الإخراج الخاص به [67338369.pdf](output PDF) للإشارة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **التحويل المتقدم**
يمكنك أيضًا اختيار استخدام فئة [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)  لتعيين سمات مختلفة للتحويل. يمنحك ضبط الخصائص المختلفة لفئة **PdfSaveOptions** السيطرة على الطباعة والخط وإعدادات الأمان والضغط لمستند PDF الناتج. أهم خاصية هي [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) التي تمكّنك من حفظ ملفات Excel كملفات PDF/A متوافقة.
#### **حفظ جدول البيانات إلى ملف PDF/A المتوافق**
يوضح كود الشفرة التالي كيفية استخدام فئة **PdfSaveOptions** لحفظ ملفات Excel إلى تنسيق PDF/A متوافق

يرجى الاطلاع على الرمز البريدي الخاص، وملف الإخراج الخاص به [67338370.pdf](output PDF) للإشارة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **تعيين وقت إنشاء ملف PDF**
باستخدام فئة **IPdfSaveOptions**، يمكنك الحصول على الوقت الخاص بإنشاء PDF أو تعيينه.

يرجى الاطلاع على الرمز الخاص بالعينة وملف الإخراج الخاص به [67338371.pdf](output PDF) للإشارة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
