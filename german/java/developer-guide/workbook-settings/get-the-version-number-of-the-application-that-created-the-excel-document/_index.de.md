---
title: Rufen Sie die Versionsnummer der Anwendung ab, die das Excel-Dokument erstellt hat
type: docs
weight: 150
url: /de/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

 Häufig müssen Sie die Versionsnummer der Anwendung kennen, die ein Microsoft-Excel-Dokument erstellt hat. Aspose.Cells bietet die[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) Eigentum für diesen Zweck.

{{% /alert %}}

 Der folgende Beispielcode demonstriert die Verwendung von[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)Eigentum. Es lädt Excel-Dateien, die mit Microsoft Excel 2003, 2007, 2010 und 2013 erstellt wurden, und druckt die Versionsnummer der Anwendung, die diese Excel-Dokumente erstellt hat.

Als Referenz finden Sie unten die Konsolenausgabe, die der Beispielcode erstellt.

{{< highlight "java" >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
