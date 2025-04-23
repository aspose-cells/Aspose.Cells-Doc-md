---
title: الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور
type: docs
weight: 280
url: /ar/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

من الممكن حماية مصنفات العمل وأوراق العمل بشكل منفصل. على سبيل المثال، قد تحتوي جدول بيانات على ورقة عمل أو أكثر محمية بكلمة مرور، ومع ذلك، قد تكون جدول البيانات ذاته محمياً أو قد لا يكون كذلك. توفر واجهات برمجة التطبيقات Aspose.Cells الوسائل للكشف ما إذا كانت ورقة العمل المعطاة محمية بكلمة مرور أم لا. يوضح هذا المقال استخدام Aspose.Cells for Java API لتحقيق النتيجة نفسها.

{{% /alert %}}

## **الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور**

Aspose.Cells for Java 8.7.0 قد عرض الخاصية [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) للكشف ما إذا كانت ورقة العمل محمية بكلمة مرور أم لا. تعيد الحقل البولياني [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) **صحيح** إذا كانت [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) محمية بكلمة مرور و**خاطئة** إذا لم تكن محمية بكلمة مرور.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
{{< app/cells/assistant language="java" >}}
