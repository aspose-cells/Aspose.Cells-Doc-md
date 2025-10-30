---
title: Sichere PDF Dokumente
type: docs
weight: 120
url: /de/python-net/secure-pdf-documents/
description: Erfahren Sie, wie Sie beim Speichern von Tabellenkalkulationen als PDF mit Aspose.Cells for Python via .NET API Sicherheitsoptionen für PDF übergeben können.
keywords: Python Sicherheitsoptionen in PDF schreiben, PDF Dokument verschlüsseln 
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells for Python via .NET bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) zum Arbeiten mit Sicherheit. Sie können Benutzer- und Besitzerkennwörter beim Speichern als PDF festlegen. Das Besitzerkennwort oder Benutzerkennwort wird benötigt, um das verschlüsselte PDF-Dokument zur Anzeige zu öffnen.

- Das Benutzerpasswort kann null oder leer sein. In diesem Fall ist kein Passwort vom Benutzer erforderlich, wenn das PDF-Dokument geöffnet wird.
- Das Öffnen des PDF-Dokuments mit dem korrekten Besitzerpasswort ermöglicht vollen Zugriff (ohne Einschränkungen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der unten stehende Beispielcode beschreibt, wie PDFs mit Aspose.Cells für Python via .NET gesichert werden können.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die richtigen Werte im PDF dargestellt.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
