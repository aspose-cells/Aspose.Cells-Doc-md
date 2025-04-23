---
title: Sichere PDF Dokumente
type: docs
weight: 120
url: /de/net/secure-pdf-documents/
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) zur Arbeit mit Sicherheit. Sie können Besitzer- und Benutzerpasswörter beim Speichern in PDF festlegen. Das Besitzerpasswort oder das Benutzerpasswort wird beim Öffnen des verschlüsselten PDF-Dokuments zur Anzeige benötigt.

- Das Benutzerpasswort kann null oder leer sein. In diesem Fall ist kein Passwort vom Benutzer erforderlich, wenn das PDF-Dokument geöffnet wird.
- Das Öffnen des PDF-Dokuments mit dem korrekten Besitzerpasswort ermöglicht vollen Zugriff (ohne Einschränkungen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der unten stehende Beispielcode beschreibt, wie PDFs mit Aspose.Cells gesichert werden können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die richtigen Werte im PDF dargestellt.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
