---
title: Aspose.Cells.GridJs Basics
type: docs
weight: 250
url: /net/aspose-cells-gridjs/basics/
keywords: GridJs
description: This article introduce the basic steps to set up a web application for GridJs.
---

## Basics of GridJs

Aspose.Cells.GridJs is a .NET standard library that allows users to develop web application to show/edit spreadsheet quickly and easily. 

Aspose.Cells.GridJs supports import the popular spreadsheet (XLS, XLSX, XLSM, XLSB,  CSV, SpreadsheetML, ODS) file formats.

It also allows exporting Excel files to PDF, HTML .etc. Below is the basic process steps to develop a web application of GridJs.

- Implement GridCacheForStream to write you own business logic for cache storage.
- Set up a controller action to get json from the spreadsheet file. You can use GridJsWorkbook.ImportExcelFile and GridJsWorkbook.ExportToJson APIs, GridJs will automatically store the spread file in cache.
- Set up a controller action to get json for the update operation.You can use GridJsWorkbook.UpdateCell API，GridJs will do update operation in cache and return the updated json.
- Set up a controller action to get the images/shapes files url in the spreadsheet ,GridJs will automatically zip all the images/shapes in cache .It will use GridCacheForStream.GetFileUrl API.
- Set up a controller action to get file in cache,thus we can get the images/shapes zip file or the spreadsheet file in cache.It will use GridCacheForStream.LoadStream API.
- Set up a controller action to download the spreadsheet.You can use GridJsWorkbook.SaveToCacheWithFileName API.

Belowis a basic demo to show the usage of Aspose.Cells.GridJs : https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs 

If you have any questions,requirements or need help, please feedback to the following website https://forum.aspose.com/c/cells/9