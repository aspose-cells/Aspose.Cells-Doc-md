---
title: Hämta versionssiffran för programmet som skapade Excel dokumentet
type: docs
weight: 210
url: /sv/python-net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Ofta behöver du veta versionsnumret för den applikation som skapade ett Microsoft Excel-dokument. Aspose.Cells för Python via .NET tillhandahåller egenskapen [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version) för detta ändamål.

{{% /alert %}}

Följande exempelkod visar hur man använder egenskapen [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version). Den läser in Excel-filer skapade med Microsoft Excel 2003, 2007, 2010 och 2013 och skriver ut versionsnumret för det program som skapade dessa Excel-dokument.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-GetApplicationVersion-1.py" >}}
