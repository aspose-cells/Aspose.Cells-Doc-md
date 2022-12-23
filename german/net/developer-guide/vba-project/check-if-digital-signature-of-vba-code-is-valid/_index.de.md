---
title: Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist
type: docs
weight: 120
url: /de/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 Aspose.Cells können Sie überprüfen, ob die digitale Signatur des VBA-Codes gültig ist, indem Sie die[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) Eigentum. Es wird zurückkehren**wahr** Wenn die Signatur gültig ist, wird sie sonst zurückgegeben**FALSCH**. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfen Sie, ob die digitale Signatur des VBA-Codes in C# gültig ist**

 Der folgende Code demonstriert die Verwendung dieser Eigenschaft mit der[Excel-Beispieldatei](5115030.xlsm)die Sie über den angegebenen Link herunterladen können. Dieselbe Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern und die Arbeitsmappe speichern und dann erneut überprüfen, stellen wir fest, dass ihre Signatur ungültig geworden ist.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
