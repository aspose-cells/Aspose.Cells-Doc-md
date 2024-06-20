---
title: Hämta versionssiffran för programmet som skapade Excel dokumentet
type: docs
weight: 210
url: /sv/net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Du behöver ofta veta versionsnumret för programmet som skapade ett Microsoft Excel-dokument. Aspose.Cells tillhandahåller egenskapen [**Workbook.BuiltInDocumentProperties.Version**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/version) för detta ändamål.

{{% /alert %}}

Följande exempelkod visar hur man använder egenskapen [**Workbook.BuiltInDocumentProperties.Version**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/version). Den läser in Excel-filer skapade med Microsoft Excel 2003, 2007, 2010 och 2013 och skriver ut versionsnumret för det program som skapade dessa Excel-dokument.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-GetApplicationVersion-1.cs" >}}
