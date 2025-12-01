---
title: Assign and Validate Digital Signatures
linktitle: Signature
type: docs
weight: 140
url: /python-net/assign-and-validate-digital-signatures/
description: Excel file digital signature, verification. To protect the authenticity of a workbook's content of Excel file, you can add a digital signature using C# codes with Aspose.Cells for Python via .NET.
keywords: Excel file digital signature, Add digital signature for Excel, How to validate digital signature.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

A digital signature provides assurance that a workbook file is valid and no one has altered it. You can create a personal digital signature by using the **Microsoft Selfcert.exe** or any other tool, or you can purchase a digital signature. After you create a digital signature, you must attach it to your workbook. Attaching a digital signature is similar to sealing an envelope. If an envelope arrives sealed, you have some level of assurance that no one has tampered with its contents.

{{% /alert %}}

## **Introduction**

Use the Digital Signature dialog to attach a digital signature. The Digital Signature dialog lists valid certificates. You can use the Digital Signature dialog to view certificates and to select the one you want to use. If a workbook has a digital signature, the name of the signature appears in the **Certificate Name** field. If you click the **Remove** button in the Digital Signature dialog, Microsoft Excel removes the digital signature as well.

## **How to Add Digital Signature for Excel**

Aspose.Cells for Python via .NET provides the [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/python-net/aspose.cells.digitalsignatures/digitalsignature) namespace to perform the job (assign and validate digital signatures). The namespace has some useful features for adding and validating digital signatures.

Please see the following sample code that describes how you can perform the task using the Aspose.Cells for Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AssignAndValidateDigitalSignatures.py" >}}



## **Advance topics**
- [Add Digital Signature to an already signed Excel file](/cells/python-net/add-digital-signature-to-an-already-signed-excel-file/)
- [Add Signature line to the worksheet](/cells/python-net/add-signature-line/)
- [Support for XAdES Signature](/cells/python-net/support-for-xades-signature/)

{{< app/cells/assistant language="python-net" >}}
