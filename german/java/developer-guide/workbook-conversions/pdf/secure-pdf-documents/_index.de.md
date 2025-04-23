---
title: Sichere PDF Dokumente
type: docs
weight: 260
url: /de/java/secure-pdf-documents/
description: Sichern Sie PDF Dateien beim Konvertieren von Excel Dateien. Dieser Artikel zeigt, wie man eine gesicherte PDF Datei aus Excel mit Aspose.Cells for Java API generiert.
keywords: sichere PDF Dokumente java, sichere PDF Dokumente, Excel in sichere PDF Datei, Excel in sichere PDF Datei java, Konvertieren von Excel in sichere PDF, Konvertieren von Excel in sicheres PDF java, Konvertieren von Excel in passwortgeschütztes PDF, Konvertieren von Excel in passwortgeschütztes PDF java, Excel in passwortgeschütztes PDF java, Excel in passwortgeschütztes PDF
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) zur Arbeit mit Sicherheit. Sie können Besitzer- und Benutzerpasswörter beim Speichern in PDF festlegen. Das Besitzerpasswort oder das Benutzerpasswort wird beim Öffnen des verschlüsselten PDF-Dokuments zur Anzeige benötigt.

- Das Benutzerpasswort kann null oder leer sein. In diesem Fall ist kein Passwort vom Benutzer erforderlich, wenn das PDF-Dokument geöffnet wird.
- Das Öffnen des PDF-Dokuments mit dem korrekten Besitzerpasswort ermöglicht vollen Zugriff (ohne Einschränkungen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der nachstehende Beispielcode beschreibt, wie man mit Aspose.Cells for Java API gesicherte PDF-Dateien erstellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

Wenn die Tabellenkalkulation Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor dem Rendern in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet, und die korrekten Werte werden im PDF angezeigt.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
