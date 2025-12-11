---
title: Filter objects while loading workbook in GridDesktop
type: docs
weight: 1060
url: /net/aspose-cells-griddesktop/loading-filter
description: This article describes how to use loading filter in GridDesktop.
keywords: GridDesktop,loading,loading filter,filter
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Please use [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter) property while filtering data from the workbook.

The [GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) enumeration has the following values.
- All
- BookSettings
- CellBlank
- CellBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Chart
- ConditionalFormatting
- DataValidation
- DefinedNames
- DocumentProperties
- Formula
- Hyperlinks
- MergedArea
- PivotTable
- Settings
- Shape
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap

## **Filter data while Loading Workbook**
The following sample code illustrates how to filter drawings from the workbook. Please check the [sample Excel file](5472489.xlsx). As you can see, all charts/shapes/images have been filtered out of the workbook.

![workbook without image](nodrawing.png)

### **Sample Code**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}
