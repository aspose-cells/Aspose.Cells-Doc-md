---
title: التحقق من الكلمة المستخدمة لحماية ورقة العمل
type: docs
weight: 370
url: /ar/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

قد قامت واجهات برمجة التطبيقات Aspose.Cells بتعزيز فئة [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) من خلال إدخال بعض الخصائص والوسائل المفيدة. إحدى هذه الوسائل هي [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) التي تسمح بتحديد كلمة مرور كنسخة من *string* والتحقق مما إذا كانت نفس كلمة المرور تم استخدامها لحماية [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

تُرجع الوسيلة [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) **true** إذا تطابقت كلمة المرور المحددة مع كلمة المرور المستخدمة لحماية ورقة العمل المعطاة و**false** إذا لم تتطابق كلمة المرور المحددة. يستخدم شريحة الرمز التالية الوسيلة [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) مع خاصية [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) لاكتشاف حماية كلمة المرور والتحقق منها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
