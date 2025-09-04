---
title: Aspose.Cells.GridJs Basics
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## Basics of GridJs

Aspose.Cells.GridJs is a library that allows users to develop cross-platform web application to view or edit spreadsheet file quickly and easily. 

## Why Use Aspose.Cells.GridJs


- It enable users to create, edit, format, collaborate on, and securely share spreadsheets with real-time updates, formula support, and rich data visualization tools, akin to traditional desktop applications.
- It supports Data Input and Editing,Format,Spreadsheet Navigation,Formula Calculation,Data Manipulation,Charts and Visualizations,Import and Export,Security,Add-ons and Customization for developers to tailor the editor to specific business needs.

## Features


- Import, view and edit the popular spreadsheet formats.
- Export the spreadsheets to various supported file formats.
- Display and manage the image or shape or chart files.
- Perform Grid design and layout customization.
- Multiple worksheet management.
- Creation and calculation of Excel® formulas.

## Supported File Formats

https://docs.aspose.com/cells/python-net/supported-file-formats/

## General Usage

Below is the basic process steps to develop a web application of GridJs.

- Set cache storage directory by  Config.set_file_cache_directory(`you storage path`)
- Set License by  Config.set_license(`you license path`)
- Set image route url GridJsWorkbook.set_image_url_base(`route for view image`);
- Set up a route action to get `json` from the spreadsheet file. You can use `GridJsWorkbook.ImportExcelFile` and `GridJsWorkbook.ExportToJson` APIs, `GridJs` will automatically store the spread file in cache.
- Set up a route action to get `json` for the update operation.You can use `GridJsWorkbook.UpdateCell` `API,GridJs` will do update operation in cache and return the updated `json`.
- Set up a route action to get file in cache,thus we can get the images/shapes zip file or the spreadsheet file in cache.
- Set up a route action to download the spreadsheet.You can use `GridJsWorkbook.SaveToCacheWithFileName` API.

Below is a basic demo to show the usage of Aspose.Cells.GridJs :

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs

In the demo we use  [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) for the render of client side  page.

If you have any questions,requirements or need help, please feedback to the following website https://forum.aspose.com/c/cells/9