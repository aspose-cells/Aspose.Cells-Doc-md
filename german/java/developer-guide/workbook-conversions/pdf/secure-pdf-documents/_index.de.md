---
title: PDF Dokumente sichern
type: docs
weight: 260
url: /de/java/secure-pdf-documents/
description: Sichern Sie PDF-Dateien beim Konvertieren von Excel-Dateien. Dieser Artikel demonstriert das Generieren einer sicheren PDF-Datei aus Excel mit Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Beispielsweise müssen sie Dokumente mit Benutzer- und Eigentümerkennwörtern sichern, damit nicht jeder sie öffnen kann, oder sie möchten einschränken, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erläutert, wie Sie PDF-Sicherheitsoptionen übergeben, wenn Sie Tabellenkalkulationen unter PDF speichern.

{{% /alert %}} 

 Aspose.Cells APIs bieten die[**PdfSicherheitsoptionen**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)Klasse für die Arbeit mit der Sicherheit des Dateiformats PDF. Der folgende Beispielcode beschreibt, wie gesicherte PDF-Dateien mit Aspose.Cells for Java API erstellt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) kurz vor dem Rendern in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die richtigen Werte in PDF gerendert werden.

{{% /alert %}}
