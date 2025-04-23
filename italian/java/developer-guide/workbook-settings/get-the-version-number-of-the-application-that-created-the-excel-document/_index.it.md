---
title: Ottieni il numero di versione dell applicazione che ha creato il documento di Excel
type: docs
weight: 150
url: /it/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Spesso è necessario conoscere il numero di versione dell'applicazione che ha creato un documento di Microsoft Excel. Aspose.Cells fornisce la proprietà [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) a questo scopo.

{{% /alert %}}

Il codice di esempio seguente dimostra l'uso della proprietà [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version). Carica file Excel creati con Microsoft Excel 2003, 2007, 2010 e 2013 e stampa il numero di versione dell'applicazione che ha creato questi documenti di Excel.

Per il riferimento, di seguito è riportato l'output della console che il codice di esempio crea.

{{< highlight java >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
{{< app/cells/assistant language="java" >}}
