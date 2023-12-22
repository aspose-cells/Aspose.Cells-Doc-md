---
title: Sichere PDF-Dokumente
type: docs
weight: 120
url: /de/python-net/secure-pdf-documents/
description: Erfahren Sie, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF mit Aspose.Cells for Python via .NET API übergeben.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerkennwörtern, damit nicht jeder sie öffnen kann.
- Legen Sie Einschränkungen oder Berechtigungen für das Dokument fest, nachdem das Dokument geöffnet wurde. Sie können beispielsweise einschränken, ob der Inhalt des Dokuments gedruckt oder extrahiert werden kann.

In diesem Artikel wird erläutert, wie Sie beim Speichern von Tabellenkalkulationen in PDF Sicherheitsoptionen für PDF übergeben.

{{% /alert %}}

 Aspose.Cells for Python via .NET bietet[**PDFSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)für die Arbeit mit Sicherheit. Sie können beim Speichern unter PDF Eigentümer- und Benutzerkennwörter festlegen. Das Eigentümerkennwort oder Benutzerkennwort ist erforderlich, um das verschlüsselte Dokument PDF zum Anzeigen zu öffnen.

- Das Benutzerkennwort kann null oder eine leere Zeichenfolge sein. In diesem Fall ist beim Öffnen des Dokuments PDF kein Kennwort vom Benutzer erforderlich.
- Das Öffnen des Dokuments PDF mit dem richtigen Besitzerpasswort ermöglicht den vollständigen Zugriff (ohne Angabe von Zugriffsbeschränkungen) auf das Dokument.
- Das Öffnen des Dokuments PDF mit dem richtigen Benutzerkennwort (oder das Öffnen eines Dokuments ohne Benutzerkennwort) ermöglicht einen eingeschränkten Zugriff entsprechend den angegebenen Berechtigungen.

Der folgende Beispielcode beschreibt, wie PDFs mit Aspose.Cells for Python via .NET gesichert werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz bevor es in PDF gerendert wird. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte in PDF gerendert werden.

{{% /alert %}}
