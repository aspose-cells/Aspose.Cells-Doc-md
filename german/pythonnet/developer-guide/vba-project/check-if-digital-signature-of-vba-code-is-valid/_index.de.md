---
title: Prüfen, ob die digitale Signatur des VBA Codes gültig ist
type: docs
weight: 120
url: /de/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET erlaubt es, zu überprüfen, ob die digitale Signatur des VBA-Codes gültig ist, mittels der [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed)-Eigenschaft. Es gibt **true** zurück, wenn die Signatur gültig ist, ansonsten **false**. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfen, ob die digitale Signatur von VBA-Code in Python gültig ist**

Der folgende Code demonstriert die Verwendung dieser Eigenschaft anhand der [Beispieldatei](5115030.xlsm), die Sie über den bereitgestellten Link herunterladen können. Die gleiche Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern und die Arbeitsmappe speichern, finden wir heraus, dass ihre Signatur ungültig geworden ist.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
