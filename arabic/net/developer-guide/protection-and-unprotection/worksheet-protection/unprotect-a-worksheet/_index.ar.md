---
title: إلغاء حماية ورقة العمل
type: docs
weight: 20
url: /ar/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

إذا كان هناك حاجة لإزالة الحماية من ورقة العمل المحمية في وقت التشغيل بحيث يمكن إجراء بعض التغييرات على الملف؟ يمكن القيام بذلك بسهولة مع Aspose.Cells.

{{% /alert %}}

## **إلغاء حماية ورقة العمل**

### **استخدام Microsoft Excel**

لإزالة الحماية من ورقة العمل:

من قائمة الـ**أدوات**, حدد **الحماية** ثم اختر **إلغاء حماية الورقة**. سيتم إزالة الحماية ما لم تكن ورقة العمل محمية بكلمة مرور. في هذه الحالة، سيظهر مربع حوار لإدخال كلمة المرور. أدخل كلمة المرور وسيتم إزالة حماية ورقة العمل بعد ذلك.

### **إزالة الحماية من ورقة العمل المحمية بشكل بسيط باستخدام Aspose.Cells**

يمكن إلغاء حماية ورقة العمل عن طريق استدعاء الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الوسيلة [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index).
ورقة العمل المحمية بسيطة هي تلك التي لا يتم حمايتها بكلمة المرور. يمكن إلغاء حماية مثل تلك الأوراق العمل عن طريق استدعاء الوسيلة [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) دون تمرير معلمة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **إلغاء حماية ورقة العمل المحمية بكلمة المرور باستخدام Aspose.Cells**

ورقة العمل المحمية بكلمة المرور هي تلك التي تم حمايتها بكلمة مرور. يمكن إلغاء حماية مثل تلك الأوراق العمل عن طريق استدعاء النسخة المتجاوبة للوسيلة [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) التي تأخذ كلمة المرور كمعلمة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
