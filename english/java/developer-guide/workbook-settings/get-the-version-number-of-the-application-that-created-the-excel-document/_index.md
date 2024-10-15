---
title: Get the Version Number of the Application that Created the Excel Document
type: docs
weight: 150
url: /java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Often you need to know the version number of the application that created a Microsoft Excel document. Aspose.Cells provides the [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) property for this purpose.

{{% /alert %}}

The following sample code demonstrates the use of the [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) property. It loads Excel files created with Microsoft Excel 2003, 2007, 2010 and 2013 and prints the version number of the application that created these Excel documents.

For your reference, below is the console output the sample code creates.

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