---
title: Ottieni il numero di versione dell'applicazione che ha creato il documento Excel
type: docs
weight: 150
url: /it/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

 Spesso è necessario conoscere il numero di versione dell'applicazione che ha creato un documento Microsoft Excel. Aspose.Cells fornisce il[**Cartella di lavoro.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) proprietà a tale scopo.

{{% /alert %}}

 Il codice di esempio seguente illustra l'utilizzo di[**Cartella di lavoro.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)proprietà. Carica i file Excel creati con Microsoft Excel 2003, 2007, 2010 e 2013 e stampa il numero di versione dell'applicazione che ha creato questi documenti Excel.

Per tuo riferimento, di seguito è riportato l'output della console creato dal codice di esempio.

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
