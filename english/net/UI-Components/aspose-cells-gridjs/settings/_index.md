---  
title: Workbook Related Settings for GridJs  
type: docs  
weight: 250  
url: /net/aspose-cells-gridjs/settings/  
description: This article describes the workbook settings for GridJs.  
keywords: GridJs,settings,GridWorkbookSettings,workbook_settings  
aliases:  
  - /net/aspose-cells-gridjs/how-to-use-settings/  
  - /net/aspose-cells-gridjs/work-with-settings/  
  - /net/aspose-cells-gridjs/work-with-workbook-settings/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

# Settings for GridJs  

## Overview  

GridJs provides comprehensive configuration options through the `GridWorkbookSettings` class. These settings allow developers to customize various aspects of Excel file processing, including calculation behavior, metadata management, and performance optimization.  

## GridWorkbookSettings Class  

The [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings) class serves as the central configuration hub for GridJs operations.  

### Key Configuration Areas  

- **Calculation Settings**: Control formula recalculation behavior  
- **Metadata Management**: Set file properties and author information  
- **Performance Optimization**: Configure caching and resource management  

## Basic Usage Examples  

### Disabling Recalculation on File Open  

```csharp
GridJsWorkbook gw = new GridJsWorkbook();
GridWorkbookSettings gws = new GridWorkbookSettings();
// Do not re‑calculate all formulas on opening the file
gws.ReCalculateOnOpen = false;
gw.Settings = gws;
gw.ImportExcelFile(@"c:\test.xlsx");
```  

### Setting File Metadata  

```csharp
GridJsWorkbook gw = new GridJsWorkbook();
GridWorkbookSettings gws = new GridWorkbookSettings();
// Set author information
gws.Author = "peter";
gw.Settings = gws;
gw.ImportExcelFile(@"c:\test.xlsx");
```  

## Common Settings Reference  

### Calculation‑Related Settings  

- `ReCalculateOnOpen`: Controls whether formulas are recalculated when opening files; default is true.  
- `ForceFullCalculate`: Enables forced full calculation cycles.  
- `CreateCalcChain`: Controls whether to create a calculated formulas chain; default is false.  
- `Iteration`: Controls whether to use iteration to resolve circular references; default is true.  
- `MaxIteration`: Sets the maximum number of iterations to resolve circular references; the default value is 100.  

### Metadata Settings  

- `Author`: Specifies the file author.  

### Performance Settings  

- `CheckCustomNumberFormat`: Validates custom number format when setting `Style.Custom`.  
- `CheckExcelRestriction`: Controls whether to check restrictions of the Excel file when the user modifies cell‑related objects.  

## Advanced Configuration  

### Batch Settings Application  

```csharp
GridJsWorkbook gw = new GridJsWorkbook();
GridWorkbookSettings gws = new GridWorkbookSettings();

// Configure multiple settings simultaneously
gws.ReCalculateOnOpen = false;
gws.Author = "peter";
gws.CheckCustomNumberFormat = true;
gws.CheckExcelRestriction = true;
gw.Settings = gws;
gw.ImportExcelFile(@"c:\test.xlsx");
```  

## Demo and Examples  

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:  

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/main/Examples_GridJs>  

## Additional Resources  

- [GridJs Server API Documentation](https://reference.aspose.com/cells/net/aspose.cells.gridjs)  
- [GridJs Client API Documentation](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api)  
