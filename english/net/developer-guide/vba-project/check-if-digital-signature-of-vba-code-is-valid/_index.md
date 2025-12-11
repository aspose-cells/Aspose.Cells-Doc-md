---
title: Check if Digital Signature of VBA Code is Valid
type: docs
weight: 120
url: /net/check-if-digital-signature-of-vba-code-is-valid/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to check if the digital signature of the VBA code is valid using the [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) property. It will return **true** if the signature is valid, otherwise it will return **false**. The digital signature of the VBA code becomes invalid when you change the VBA code.

{{% /alert %}}

## **Check if Digital Signature of VBA Code is Valid in C#**

The following code demonstrates the usage of this property using the [sample Excel file](5115030.xlsm), which you can download from the provided link. The same Excel file has a valid signature, but when we modify its VBA code, save the workbook, and then recheck, we find that its signature has become invalid.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
{{< app/cells/assistant language="csharp" >}}
