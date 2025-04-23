---
title: تحويل مصنف Excel إلى PDF
type: docs
weight: 80
url: /ar/go-cpp/convert-excel-workbook-to-pdf/
---

## **تحويل سجل عمل Excel إلى PDF**

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

{{% alert color="primary" %}}

يكتب Aspose.Cells مباشرةً المعلومات حول API ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند عرض المستند في PDF، Aspose.Cells for Go via C++ يملأ حقل **التطبيق** بالقيمة 'Aspose.Cells' وحقل **منتج PDF** بقيمة، مثل 'Aspose.Cells v24.12.0'.

يرجى ملاحظة أنك لا تستطيع توجيه Aspose.Cells for Go via C++ لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}}

### **التحويل المباشر**

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. أنشئ كائن من فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) عن طريق استدعاء منشئه الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. أدخل أي عمل (البيانات الدخلية، تطبيق التنسيق، ضبط الصيغ، إدراج الصور أو كائنات الرسم الأخرى، وما إلى ذلك) على ورق العمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1. عند الانتهاء من رمز جدول البيانات، استدعِ طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) لفئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) لحفظ جدول البيانات.

يجب أن يكون تنسيق الملف PDF، لذلك اختر قيمة [SaveFormat](https://reference.aspose.com/cells/go-cpp/workbook/saveformat/) ذات الصلة لإنشاء مستند PDF النهائي.

يرجى الاطلاع على الكود النموذجي التالي، وملف Excel العيني الخاص به [ملف Excel النموذجي](67338368.xlsx) وملف PDF الناتج [PDF الناتج](67338369.pdf) للمرجع الخاص بك.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
