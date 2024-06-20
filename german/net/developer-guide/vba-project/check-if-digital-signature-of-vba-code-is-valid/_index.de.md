---
title: Prüfen, ob die digitale Signatur des VBA Codes gültig ist
type: docs
weight: 120
url: /de/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, mithilfe der [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned)-Eigenschaft zu überprüfen, ob die digitale Signatur des VBA-Codes gültig ist. Es gibt **true** zurück, wenn die Signatur gültig ist, andernfalls **false**. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfen Sie, ob die digitale Signatur des VBA-Codes in C# gültig ist**

Der folgende Code demonstriert die Verwendung dieser Eigenschaft anhand der [Beispieldatei](5115030.xlsm), die Sie über den bereitgestellten Link herunterladen können. Die gleiche Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern und die Arbeitsmappe speichern, finden wir heraus, dass ihre Signatur ungültig geworden ist.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
