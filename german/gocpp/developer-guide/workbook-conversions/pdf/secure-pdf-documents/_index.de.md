---
title: Sichere PDF Dokumente mit Golang via C++
linktitle: Sichere PDF Dokumente
type: docs
weight: 120
url: /de/go-cpp/secure-pdf-documents/
description: Lernen Sie, wie Sie PDF Dokumente mit Besitzer und Benutzers Passwort mithilfe von Aspose.Cells mit Golang via C++ sichern.
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/) für die Arbeit mit Sicherheit. Sie können Besitzer- und Benutzerkennwörter beim Speichern in PDF festlegen. Das Besitzer- oder Benutzerkennwort ist erforderlich, um das verschlüsselte PDF-Dokument zu öffnen.

- Das Benutzerpasswort kann null oder leer sein. In diesem Fall ist kein Passwort vom Benutzer erforderlich, wenn das PDF-Dokument geöffnet wird.
- Das Öffnen des PDF-Dokuments mit dem richtigen Besitzerkennwort gewährt vollen Zugriff (ohne Zugriffsrestriktionen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der unten stehende Beispielcode beschreibt, wie PDFs mit Aspose.Cells gesichert werden können.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) direkt vor dem Rendern in PDF aufzurufen. Dadurch werden die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}
