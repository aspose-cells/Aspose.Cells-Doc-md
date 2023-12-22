---
title: Sichere PDF-Dokumente
type: docs
weight: 260
url: /de/java/secure-pdf-documents/
description: Sichern Sie PDF-Dateien beim Konvertieren von Excel-Dateien. In diesem Artikel wird die Erstellung einer sicheren PDF-Datei aus Excel mit Aspose.Cells for Java API veranschaulicht.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerkennwörtern, damit nicht jeder sie öffnen kann.
- Legen Sie Einschränkungen oder Berechtigungen für das Dokument fest, nachdem das Dokument geöffnet wurde. Sie können beispielsweise einschränken, ob der Inhalt des Dokuments gedruckt oder extrahiert werden kann.

In diesem Artikel wird erläutert, wie Sie beim Speichern von Tabellenkalkulationen in PDF Sicherheitsoptionen für PDF übergeben.

{{% /alert %}}

 Aspose.Cells bietet[**PDFSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)für die Arbeit mit Sicherheit. Sie können beim Speichern unter PDF Eigentümer- und Benutzerkennwörter festlegen. Das Eigentümerkennwort oder Benutzerkennwort ist erforderlich, um das verschlüsselte Dokument PDF zum Anzeigen zu öffnen.

- Das Benutzerkennwort kann null oder eine leere Zeichenfolge sein. In diesem Fall ist beim Öffnen des Dokuments PDF kein Kennwort vom Benutzer erforderlich.
- Das Öffnen des Dokuments PDF mit dem richtigen Besitzerpasswort ermöglicht den vollständigen Zugriff (ohne Angabe von Zugriffsbeschränkungen) auf das Dokument.
- Das Öffnen des Dokuments PDF mit dem richtigen Benutzerkennwort (oder das Öffnen eines Dokuments ohne Benutzerkennwort) ermöglicht einen eingeschränkten Zugriff entsprechend den angegebenen Berechtigungen.

Der folgende Beispielcode beschreibt, wie Sie gesicherte PDF-Dateien mit Aspose.Cells for Java API erstellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()kurz vor dem Rendern in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
