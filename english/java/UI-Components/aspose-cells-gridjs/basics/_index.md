---
title: Aspose.Cells.GridJs Basics
type: docs
weight: 250
url: /net/aspose-cells-gridjs/basics/
keywords: GridJs
description: This article introduces the basic steps to set up a web application for GridJs.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Basics of GridJs

Aspose.Cells.GridJs is a .NET Standard library that allows users to develop web applications to show/edit spreadsheets quickly and easily.  

Aspose.Cells.GridJs supports importing the popular spreadsheet file formats (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).  

It also allows exporting Excel files to PDF, HTML, etc. Below is the basic process steps to develop a GridJs web application.

- Implement **GridCacheForStream** to write your own business logic for cache storage.  
- Set up a controller action to get JSON from the spreadsheet file. You can use `GridJsWorkbook.ImportExcelFile` and `GridJsWorkbook.ExportToJson` APIs; GridJs will automatically store the spreadsheet file in cache.  
- Set up a controller action to get JSON for the update operation. You can use `GridJsWorkbook.UpdateCell` API; GridJs will perform the update operation in cache and return the updated JSON.  
- Set up a controller action to get the images/shapes files URL in the spreadsheet. GridJs will automatically zip all the images/shapes in cache. It will use `GridCacheForStream.GetFileUrl` API.  
- Set up a controller action to get a file from cache, thus we can retrieve the images/shapes zip file or the spreadsheet file from cache. It will use `GridCacheForStream.LoadStream` API.  
- Set up a controller action to download the spreadsheet. You can use `GridJsWorkbook.SaveToCacheWithFileName` API.  

Below is a basic demo to show the usage of Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs  

If you have any questions, requirements, or need help, please provide feedback at the following website: https://forum.aspose.com/c/cells/9
