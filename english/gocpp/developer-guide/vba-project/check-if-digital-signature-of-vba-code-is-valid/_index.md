---
title: Check if Digital Signature of VBA Code is Valid with Golang via C++
linktitle: Check if Digital Signature of VBA Code is Valid
type: docs
weight: 120
url: /go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Learn how to check the validity of a digital signature in VBA code using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to check if the digital signature of the VBA code is valid using the **Workbook.VbaProject.IsValidSigned** property. It will return **true** if the signature is valid; otherwise, it will return **false**. The digital signature of the VBA code becomes invalid when you change the VBA code.

{{% /alert %}}

## **Check if Digital Signature of VBA Code is Valid in C++**

The following code demonstrates the usage of this property using the sample **Excel** file (**5115030.xlsm**), which you can download from the provided link. The same Excel file has a valid signature, but when we modify its VBA code, save the workbook, and then re‑check, we find that its signature has become invalid.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}