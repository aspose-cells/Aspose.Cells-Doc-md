---
title: Verify Password Used to Protect the Worksheet with Golang via C++
linktitle: Verify Password Used to Protect the Worksheet
type: docs
weight: 370
url: /go-cpp/verify-password-used-to-protect-the-worksheet/
description: Learn how to verify the password used to protect a worksheet using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

Aspose.Cells APIs have enhanced the [**Protection**](https://reference.aspose.com/cells/go-cpp/protection/) class by introducing some useful properties and methods. One such method is the [**VerifyPassword**](https://reference.aspose.com/cells/go-cpp/protection/verifypassword/) which allows specifying a password as an instance of a string and verifies if the same password has been used to protect the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/).

{{% /alert %}}

The [**Protection.VerifyPassword**](https://reference.aspose.com/cells/go-cpp/protection/verifypassword/) method returns **true** if the specified password matches the password used to protect the given worksheet and **false** if the specified password does not match. The following piece of code uses the [**Protection.VerifyPassword**](https://reference.aspose.com/cells/go-cpp/protection/verifypassword/) method in conjunction with the [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/go-cpp/protection/isprotectedwithpassword/) property to detect whether the worksheet is protected with a password and to verify the password.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyPasswordUsedToProtectTheWorksheet.go" >}}
{{< app/cells/assistant language="go" >}}
