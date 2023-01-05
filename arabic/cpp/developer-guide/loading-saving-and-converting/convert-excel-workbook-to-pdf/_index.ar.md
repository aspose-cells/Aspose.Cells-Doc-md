---
title: تحويل مصنف Excel إلى PDF
type: docs
weight: 80
url: /ar/cpp/convert-excel-workbook-to-pdf/
---
## **تحويل مصنف Excel إلى PDF**
يتم استخدام ملفات PDF على نطاق واسع لتبادل المستندات بين المنظمات والقطاعات الحكومية والأفراد. إنه تنسيق مستند قياسي وغالبًا ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات Excel Microsoft إلى مستندات PDF.

يدعم Aspose.Cells تحويل ملفات Excel إلى PDF ويحافظ على الدقة المرئية العالية في التحويل.

{{% alert color="primary" %}} 

 يقوم Aspose.Cells بكتابة المعلومات حول API ورقم الإصدار مباشرة في وثائق المخرجات. على سبيل المثال ، عند تقديم المستند إلى PDF ، يملأ Aspose.Cells for C++**تطبيق** حقل بقيمة "Aspose.Cells" و**PDF منتج** حقل بقيمة ، على سبيل المثال "Aspose.Cells v18.5.0".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for C++ لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}} 
### **التحويل المباشر**
Aspose.Cells يدعم التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ما عليك سوى حفظ ملف Excel في PDF باستخدام امتداد[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)صف دراسي'[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)طريقة. ال[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)طريقة توفر[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)عضو التعداد الذي يحول ملفات Excel الأصلية إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل جداول بيانات Excel مباشرة إلى تنسيق PDF:

1.  إنشاء كائن من[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)فئة عن طريق استدعاء مُنشئها الفارغ.
1. يمكنك فتح / تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء المصنف من البداية.
1. قم بأي عمل (إدخال البيانات ، وتطبيق التنسيق ، وتعيين الصيغ ، وإدراج الصور أو الكائنات الرسومية الأخرى ، وما إلى ذلك) في جدول البيانات باستخدام واجهات برمجة التطبيقات Aspose.Cells '.
1.  عند اكتمال كود جدول البيانات ، اتصل بـ[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)صف دراسي'[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)طريقة لحفظ جدول البيانات.

يجب أن يكون تنسيق الملف PDF ، لذا حدد PDF ذي الصلة (قيمة محددة مسبقًا) من تعداد SaveFormat لإنشاء مستند PDF النهائي

 يرجى الاطلاع على نموذج التعليمات البرمجية التالي ، الخاص به[نموذج لملف Excel](67338368.xlsx) و[الإخراج PDF](67338369.pdf) للرجوع اليها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **التحويل المتقدم**
يمكنك أيضًا اختيار استخدام ملف[IPdfSaveOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)فئة لتعيين سمات مختلفة للتحويل. تعيين خصائص مختلفة لملف**IPdfSaveOptions** تمنحك class التحكم في إعدادات الطباعة والخط والأمان والضغط للمخرج PDF. الخاصية الأكثر أهمية هي[SetCompliance](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)والتي تمكنك من حفظ ملفات Excel في PDF / A متوافق مع ملفات PDF.
#### **حفظ المصنف في PDF / A الملفات المتوافقة**
يوضح مقتطف الشفرة التالي كيفية استخدام ملف**IPdfSaveOptions**فئة لحفظ ملفات Excel بتنسيق PDF متوافق مع PDF / A

 يرجى الاطلاع على نموذج التعليمات البرمجية التالي وملف[الإخراج PDF](67338370.pdf) للرجوع اليها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **قم بتعيين PDF وقت الإنشاء**
مع ال**IPdfSaveOptions** فئة ، يمكنك الحصول على وقت إنشاء PDF أو تعيينه.

 يرجى الاطلاع على نموذج التعليمات البرمجية التالي وملف[الإخراج PDF](67338371.pdf) للرجوع اليها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
