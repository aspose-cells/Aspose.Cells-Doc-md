---
title: التحقق من الكلمة المستخدمة لحماية ورقة العمل
type: docs
weight: 290
url: /ar/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

تحسنت واجهة برمجة تطبيقات Aspose.Cells الفئة [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) من خلال إدخال بعض الخصائص والطرق المفيدة. إحدى هذه الطرق هي [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword-java.lang.String-) التي تسمح بتحديد كلمة مرور كنمط نصي والتحقق مما إذا كانت نفس كلمة المرور قد استخدمت لحماية ورقة العمل.

{{% /alert %}}

## **التحقق من الكلمة المستخدمة لحماية ورقة العمل**

يُعيد الطريقة [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword-java.lang.String-) قيمة **صحيح** إذا تطابقت كلمة المرور المحددة مع كلمة المرور المستخدمة لحماية الورقة العمل المعطاة، و**خاطئ** إذا لم تتطابق كلمة المرور المحددة. تستخدم القطعة التالية من الكود الطريقة [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword-java.lang.String-) بالاشتراك مع الخاصية [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) للكشف عن حماية كلمة المرور، والتحقق من كلمة المرور.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
