---
title: التحقق من الكلمة المستخدمة لحماية ورقة العمل
type: docs
weight: 370
url: /ar/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

قدم Aspose.Cells لبايثون via .NET تحسينات على فئة [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) من خلال تقديم بعض الخصائص والطرق المفيدة. واحدة من هذه الطرق هي [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) التي تسمح بتحديد كلمة مرور ككائن *سلسلة* والتحقق مما إذا تم استخدام نفس كلمة المرور لحماية [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

تُرجع الوسيلة [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) **true** إذا تطابقت كلمة المرور المحددة مع كلمة المرور المستخدمة لحماية ورقة العمل المعطاة و**false** إذا لم تتطابق كلمة المرور المحددة. يستخدم شريحة الرمز التالية الوسيلة [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) مع خاصية [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) لاكتشاف حماية كلمة المرور والتحقق منها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

{{< app/cells/assistant language="python-net" >}}
