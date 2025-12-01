
---
title: Workbook Related Settings for GridJs
type: docs
weight: 250
url: /java/aspose-cells-gridjs/settings/
description: This article describes the workbook settings for GridJs.
keywords: GridJs,settings,GridWorkbookSettings,workbook_settings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-settings/
  - /java/aspose-cells-gridjs/work-with-settings/
  - /java/aspose-cells-gridjs/work-with-workbook-settings/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Settings for GridJs

## Overview

GridJs provides comprehensive configuration options through the `GridWorkbookSettings` class. These settings allow developers to customize various aspects of Excel file processing, including calculation behavior, metadata management, and performance optimization.

## GridWorkbookSettings Class

The [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/com.aspose.gridjs/gridworkbooksettings) class serves as the central configuration hub for GridJs operations.

### Key Configuration Areas

- **Calculation Settings**: Control formula recalculation behavior
- **Metadata Management**: Set file properties and author information
- **Performance Optimization**: Configure caching and resource management


## Basic Usage Examples

### Disabling Recalculation on File Open

```java
GridJsWorkbook gw = new GridJsWorkbook();
GridWorkbookSettings gws = new GridWorkbookSettings();
// Do not re-calculate all formulas on opening the file
gws.setReCalculateOnOpen(false);
gw.setSettings(gws);
gw.importExcelFile(@"c:\test.xlsx");
```

### Setting File Metadata

```java
GridJsWorkbook gw = new GridJsWorkbook();
GridWorkbookSettings gws = new GridWorkbookSettings();
// Set author information
gws.setAuthor("peter");
gw.setSettings(gws);
gw.importExcelFile(@"c:\test.xlsx");
```

## Common Settings Reference

### Calculation-Related Settings

- `setReCalculateOnOpen`: Controls whether formulas are recalculated when opening files,default is true.
- `setForceFullCalculate`: Enables forced full calculation cycles
- `setCreateCalcChain`:  Controls whether create calculated formulas chain,default is false.
- `setIteration`:  Controls whether use iteration to resolve circular references,default is true.
- `setMaxIteration`: Set the maximum number of iterations to resolve a circular reference, the default value is 100.

### Metadata Settings

- `setAuthor`: Specifies the file author


### Performance Settings

- `setCheckCustomNumberFormat`: Validates custom number format when setting Style.Custom
- `setCheckExcelRestriction`: Controls Whether check restriction of excel file when user modify cells related objects


## Advanced Configuration

### Batch Settings Application

```java
GridJsWorkbook gw = new GridJsWorkbook();
GridWorkbookSettings gws = new GridWorkbookSettings();

// Configure multiple settings simultaneously
gws.setReCalculateOnOpen(false);
gws.setAuthor("peter");
gws.setCheckCustomNumberFormat(true);
gws.setCheckExcelRestriction(true);
gw.setSettings(gws);
gw.importExcelFile(@"c:\test.xlsx");
```

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs>


## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/java/com.aspose.gridjs)
- [GridJs Client API Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api)

---

