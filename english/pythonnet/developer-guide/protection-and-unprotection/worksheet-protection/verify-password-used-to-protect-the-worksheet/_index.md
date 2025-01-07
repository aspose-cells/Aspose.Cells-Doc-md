---
title: Verify Password Used to Protect the Worksheet
type: docs
weight: 370
url: /python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET APIs have enhanced the [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) class by introducing some useful properties & methods. One such method is the [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) which allows specifying a password as an instance of *string* and verifies if the same password has been used to protect the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

The [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) method returns **true** if the specified password matches the password used to protect the given worksheet and **false** if the specified password does not match. Following piece of code uses the [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) method in conjunction with [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) property to detect the password protection, and verifies the password.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

