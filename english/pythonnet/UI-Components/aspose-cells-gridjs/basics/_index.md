---  
title: Aspose.Cells.GridJs Basics  
type: docs  
weight: 250  
url: /python-net/aspose-cells-gridjs/basics/  
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

## Basics of GridJs  

Aspose.Cells.GridJs is a library that allows users to develop cross‑platform web applications to view or edit spreadsheet files quickly and easily.  

## Why Use Aspose.Cells.GridJs  

- It enables users to create, edit, format, collaborate on, and securely share spreadsheets with real‑time updates, formula support, and rich data‑visualization tools, akin to traditional desktop applications.  
- It supports Data Input and Editing, Format, Spreadsheet Navigation, Formula Calculation, Data Manipulation, Charts and Visualizations, Import and Export, Security, Add‑ons and Customization for developers to tailor the editor to specific business needs.  

## Features  

- Import, view and edit the popular spreadsheet formats.  
- Export the spreadsheets to various supported file formats.  
- Display and manage image, shape, or chart files.  
- Perform grid design and layout customization.  
- Multiple worksheet management.  
- Creation and calculation of Excel® formulas.  

## Supported File Formats  

https://docs.aspose.com/cells/python-net/supported-file-formats/  

## General Usage  

Below are the basic process steps to develop a web application with GridJs.  

- Set cache storage directory by `Config.set_file_cache_directory('your storage path')`.  
- Set license by `Config.set_license('your license path')`.  
- Set image route URL with `GridJsWorkbook.set_image_url_base('route for view image')`.  
- Set up a route action to get JSON from the spreadsheet file. You can use `GridJsWorkbook.ImportExcelFile` and `GridJsWorkbook.ExportToJson` APIs; GridJs will automatically store the spreadsheet file in cache.  
- Set up a route action to get JSON for the update operation. You can use the `GridJsWorkbook.UpdateCell` API; GridJs will perform the update operation in cache and return the updated JSON.  
- Set up a route action to get a file from cache, thus we can retrieve the images/shapes zip file or the spreadsheet file from the cache.  
- Set up a route action to download the spreadsheet. You can use the `GridJsWorkbook.SaveToCacheWithFileName` API.  

Below is a basic demo to show the usage of Aspose.Cells.GridJs:  

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs  

In the demo we use [gridjs‑spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) for rendering the client‑side page.  

If you have any questions, requirements, or need help, please provide feedback at the following website: https://forum.aspose.com/c/cells/9  
