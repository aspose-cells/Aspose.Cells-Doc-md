---
title: Hämta versionsnumret för programmet som skapade Excel-dokumentet
type: docs
weight: 150
url: /sv/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

 Ofta behöver du veta versionsnumret för programmet som skapade ett Microsoft Excel-dokument. Aspose.Cells tillhandahåller[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) egendom för detta ändamål.

{{% /alert %}}

 Följande exempelkod visar användningen av[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)fast egendom. Den laddar Excel-filer skapade med Microsoft Excel 2003, 2007, 2010 och 2013 och skriver ut versionsnumret för programmet som skapade dessa Excel-dokument.

För din referens, nedan är konsolutgången som exempelkoden skapar.

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
