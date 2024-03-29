---
title: Aspose.Cells.GridJs Basics
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/basics/
---

## Basics of GridJs

Aspose.Cells.GridJs is a .NET standard library that allows users to develop web application to show/edit spreadsheet quickly and easily. 

Aspose.Cells.GridJs supports import the popular spreadsheet (XLS, XLSX, XLSM, XLSB,  CSV, SpreadsheetML, ODS) file formats.

It also allows exporting Excel files to PDF, HTML .etc. Below is the basic process steps to develop a web application of GridJs.


- Set cache storage directory by  Config.set_file_cache_directory('you storage path')
- Set License by  Config.set_license('you license path')
- Set image route url GridJsWorkbook.set_image_url_base('route for view image');
- Set up a route action to get json from the spreadsheet file. You can use GridJsWorkbook.ImportExcelFile and GridJsWorkbook.ExportToJson APIs, GridJs will automatically store the spread file in cache.
- Set up a route action to get json for the update operation.You can use GridJsWorkbook.UpdateCell API，GridJs will do update operation in cache and return the updated json.
- Set up a route action to get the images/shapes files url in the spreadsheet ,GridJs will automatically zip all the images/shapes in cache .It will use GridCacheForStream.GetFileUrl API.
- Set up a route action to get file in cache,thus we can get the images/shapes zip file or the spreadsheet file in cache.It will use GridCacheForStream.LoadStream API.
- Set up a route action to download the spreadsheet.You can use GridJsWorkbook.SaveToCacheWithFileName API.

Below is a basic demo to show the usage of Aspose.Cells.GridJs :
https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 
in the demo we use  [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) for the render of client side  page.

If you have any questions,requirements or need help, please feedback to the following website https://forum.aspose.com/c/cells/9