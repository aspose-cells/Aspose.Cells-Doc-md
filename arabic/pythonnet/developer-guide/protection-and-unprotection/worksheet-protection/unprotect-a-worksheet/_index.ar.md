---
title: إلغاء حماية ورقة العمل
type: docs
weight: 20
url: /ar/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

إذا كان المطور بحاجة إلى إلغاء حماية ورقة عمل محمية أثناء التشغيل حتى يمكن إجراء بعض التغييرات على الملف، يمكن ذلك بسهولة باستخدام Aspose.Cells for Python via .NET.

{{% /alert %}}

## **إلغاء حماية ورقة العمل**

### **استخدام Microsoft Excel**

لإزالة الحماية من ورقة العمل:

من قائمة الـ**أدوات**, حدد **الحماية** ثم اختر **إلغاء حماية الورقة**. سيتم إزالة الحماية ما لم تكن ورقة العمل محمية بكلمة مرور. في هذه الحالة، سيظهر مربع حوار لإدخال كلمة المرور. أدخل كلمة المرور وسيتم إزالة حماية ورقة العمل بعد ذلك.

### **إلغاء حماية ورقة محمية ببساطة باستخدام Aspose.Cells لبايثون via .NET**

يمكن إلغاء حماية ورقة العمل عن طريق استدعاء الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الوسيلة [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect).
ورقة العمل المحمية بسيطة هي تلك التي لا يتم حمايتها بكلمة المرور. يمكن إلغاء حماية مثل تلك الأوراق العمل عن طريق استدعاء الوسيلة [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) دون تمرير معلمة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **إلغاء حماية ورقة محمية بكلمة مرور باستخدام Aspose.Cells لبايثون via .NET**

ورقة العمل المحمية بكلمة المرور هي تلك التي تم حمايتها بكلمة مرور. يمكن إلغاء حماية مثل تلك الأوراق العمل عن طريق استدعاء النسخة المتجاوبة للوسيلة [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) التي تأخذ كلمة المرور كمعلمة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

