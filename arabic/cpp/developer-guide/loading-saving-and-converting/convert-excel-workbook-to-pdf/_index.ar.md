---
title: تحويل مصنف Excel إلى PDF
type: docs
weight: 80
url: /ar/cpp/convert-excel-workbook-to-pdf/
---
##  **تحويل مصنف Excel إلى PDF**
تُستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنه تنسيق مستند قياسي وغالبًا ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات Excel Microsoft إلى PDF مستندًا.

Aspose.Cells يدعم تحويل ملفات Excel إلى PDF ويحافظ على دقة بصرية عالية في التحويل.

{{% alert color="primary" %}} 

 Aspose.Cells يكتب مباشرة المعلومات حول API ورقم الإصدار في مستندات الإخراج. على سبيل المثال، عند تقديم المستند إلى PDF، Aspose.Cells for C++ يملأ**طلب** الحقل بقيمة "Aspose.Cells" و**PDF منتج** حقل ذو قيمة، على سبيل المثال "Aspose.Cells v18.5.0".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for C++ لتغيير هذه المعلومات أو إزالتها من المستندات الناتجة.

{{% /alert %}} 
###  **التحويل المباشر**
Aspose.Cells يدعم التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ما عليك سوى حفظ ملف Excel على الرقم PDF باستخدام ملف[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)فصل'[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)طريقة. ال[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)توفر الطريقة[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)عضو التعداد الذي يحول ملفات Excel الأصلية إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل جداول بيانات Excel مباشرة إلى تنسيق PDF:

1.  إنشاء مثيل لكائن من[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)فئة عن طريق استدعاء منشئها الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء المصنف من البداية.
1. قم بأي عمل (إدخال البيانات، وتطبيق التنسيق، وتعيين الصيغ، وإدراج الصور أو الكائنات الرسومية الأخرى، وما إلى ذلك) في جدول البيانات باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1.  عند اكتمال رمز جدول البيانات، اتصل بـ[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)فصل'[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)طريقة حفظ جدول البيانات.

يجب أن يكون تنسيق الملف هو PDF، لذا حدد PDF ذات الصلة (قيمة محددة مسبقًا) من تعداد SaveFormat لإنشاء مستند PDF النهائي

 الرجاء مراجعة نموذج التعليمات البرمجية التالي، الخاص به[عينة من ملف إكسل](67338368.xlsx) و[الإخراج PDF](67338369.pdf) للرجوع اليها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **التحويل المتقدم**
يمكنك أيضًا اختيار استخدام[خيارات حفظ PDF](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)class لتعيين سمات مختلفة للتحويل. تحديد خصائص مختلفة لل**خيارات حفظ PDF** تمنحك الفئة التحكم في إعدادات الطباعة والخط والأمان والضغط للإخراج PDF. الخاصية الأكثر أهمية هي[SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)والتي تمكنك من حفظ ملفات Excel إلى ملفات PDF/A المتوافقة مع PDF.
####  **حفظ المصنف في PDF/A الملفات الممتثلة**
يوضح مقتطف التعليمات البرمجية التالي كيفية استخدام**خيارات حفظ PDF**فئة لحفظ ملفات Excel بتنسيق PDF/A المتوافق مع PDF

 الرجاء مراجعة نموذج التعليمات البرمجية التالي و[الإخراج PDF](67338370.pdf) للرجوع اليها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **اضبط وقت الإنشاء PDF**
مع ال**IPdfSaveOptions** فئة، يمكنك الحصول على أو ضبط وقت الإنشاء PDF.

 الرجاء مراجعة نموذج التعليمات البرمجية التالي و[الإخراج PDF](67338371.pdf) للرجوع اليها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
