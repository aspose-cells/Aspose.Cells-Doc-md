---
title: Überprüfen, ob die digitale Signatur des VBA Codes gültig ist, mit Golang via C++
linktitle: Prüfen, ob die digitale Signatur des VBA Codes gültig ist
type: docs
weight: 120
url: /de/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Erfahren Sie, wie man die Gültigkeit einer digitalen Signatur im VBA Code mit Aspose.Cells und Golang via C++ überprüft.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es, zu überprüfen, ob die digitale Signatur des VBA-Codes mit der [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/)-Eigenschaft gültig ist. Es gibt **true** zurück, wenn die Signatur gültig ist; andernfalls gibt es **false** zurück. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfen, ob die Digitale Signatur des VBA-Codes in C++ gültig ist**

Der folgende Code demonstriert die Verwendung dieser Eigenschaft anhand der [Beispiel-Excel-Datei](5115030.xlsm), die Sie über den bereitgestellten Link herunterladen können. Die gleiche Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern, die Arbeitsmappe speichern und erneut überprüfen, stellen wir fest, dass ihre Signatur ungültig geworden ist.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
