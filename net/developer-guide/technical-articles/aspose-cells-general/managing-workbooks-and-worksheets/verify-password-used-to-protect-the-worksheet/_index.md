---
title: Verify Password Used to Protect the Worksheet
type: docs
weight: 370
url: /net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs have enhanced the [Protection](https://apireference.aspose.com/net/cells/aspose.cells/protection) class by introducing some useful properties & methods. One such method is the [VerifyPassword](https://apireference.aspose.com/net/cells/aspose.cells/protection/methods/verifypassword) which allows specifying a password as an instance of *string* and verifies if the same password has been used to protect the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet).

{{% /alert %}} 

The [Protection.VerifyPassword](https://apireference.aspose.com/net/cells/aspose.cells/protection/methods/verifypassword) method returns **true** if the specified password matches the password used to protect the given worksheet and **false** if the specified password does not match. Following piece of code uses the [Protection.VerifyPassword](https://apireference.aspose.com/net/cells/aspose.cells/protection/methods/verifypassword) method in conjunction with [Protection.IsProtectedWithPassword](https://apireference.aspose.com/net/cells/aspose.cells/protection/properties/isprotectedwithpassword) property to detect the password protection, and verifies the password.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
