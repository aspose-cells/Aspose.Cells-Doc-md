---
title: Check if Digital Signature of VBA Code is Valid
type: docs
weight: 120
url: /python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET allows you to check if the digital signature of the VBA code is valid using the [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed) property. It will return **true** if the signature is valid otherwise it will return **false**. The digital signature of the VBA code becomes invalid when you change the VBA code.

{{% /alert %}}

## **Check if Digital Signature of VBA Code is Valid in Python**

The following code demonstrates the usage of this property using the [sample excel file](5115030.xlsm) which you can download from the provided link. The same excel file has a valid signature but when we modify its VBA code and save the workbook and then recheck, we find its signature has become invalid.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

