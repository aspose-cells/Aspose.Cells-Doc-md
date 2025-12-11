---
title: Import data from document
type: docs
weight: 20
url: /net/import-data-from-document/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Data is a collection of raw facts, and we create spreadsheet documents or reports to present these raw facts in a more meaningful manner. Normally we add data to spreadsheets ourselves, but sometimes we need to reuse existing data resources, and here comes the need to import data into spreadsheets from different data sources. In this topic, we will discuss some techniques to import data into worksheets from different data sources.

**Importing Data Using Aspose.Cells**  
When you use **Aspose.Cells** to open an Excel file, all data in the file is automatically imported, but Aspose.Cells also supports importing data from different data sources. A few of these data sources are listed below:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells provides a class, **Workbook**, that represents an Excel file. The Workbook class contains a Worksheets collection that allows access to each worksheet in the Excel file. A worksheet is represented by the Worksheet class. The Worksheet class provides a Cells collection.

The Cells collection provides very useful methods for importing data from different data sources.

This section has the following topics:

- [Importing from Array](/cells/net/importing-from-array/)
- [Importing from ArrayList](/cells/net/importing-from-arraylist/)
- [Importing from Custom Objects](/cells/net/importing-from-custom-objects/)
- [Importing from DataTable](/cells/net/importing-from-datatable/)
{{< app/cells/assistant language="csharp" >}}
