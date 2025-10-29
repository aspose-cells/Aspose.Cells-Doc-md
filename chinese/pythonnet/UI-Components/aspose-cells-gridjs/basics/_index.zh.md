---
title: Aspose.Cells.GridJs 基础
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## GridJs 基础

Aspose.Cells.GridJs 是一个允许用户快速轻松地开发跨平台 web 应用程序以查看或编辑电子表格文件的库。 

## 为什么使用 Aspose.Cells.GridJs


- 它使用户能够创建、编辑、格式化、协作和安全共享带有实时更新、公式支持和丰富数据可视化工具的电子表格，类似于传统的桌面应用程序。
- 它支持数据输入和编辑、格式、电子表格导航、公式计算、数据操作、图表和可视化、导入和导出、安全性、开发人员的插件和定制，以满足特定业务需求。

## 特性


- 导入、查看和编辑流行的电子表格格式。
- 将电子表格导出为各种支持的文件格式。
- 显示和管理图像、形状或图表文件。
- 执行网格设计和布局定制。
- 多工作表管理。
- 创建和计算 Excel® 公式。

## 支持的文件格式

https://docs.aspose.com/cells/python-net/supported-file-formats/

## 通用用法

下面是开发 GridJs web 应用程序的基本流程步骤。

- 通过 Config.set_file_cache_directory(`你的存储路径`) 设置缓存存储目录
- 通过 Config.set_license(`你的许可路径`) 设置许可证
- 设置图像路由URL GridJsWorkbook.set_image_url_base(`查看图像的路由`);
- 设置一个路由操作以获取来自电子表格文件的`json`。您可以使用`GridJsWorkbook.ImportExcelFile`和`GridJsWorkbook.ExportToJson` API，`GridJs`将自动将电子表格文件存储在缓存中。
- 设置一个路由操作以获取更新操作的`json`。您可以使用`GridJsWorkbook.UpdateCell` `API，GridJs`将在缓存中执行更新操作并返回更新后的`json`。
- 设置一个路由操作以获取缓存中的文件，从而可以获取缓存中的图像/形状zip文件或电子表格文件。
- 设置一个路由操作以下载电子表格。您可以使用`GridJsWorkbook.SaveToCacheWithFileName` API。

以下是用于展示Aspose.Cells.GridJs用法的基本演示：

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs

在演示中，我们使用 [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) 来呈现客户端页面。

如果您有任何疑问、需求或需要帮助，请反馈到以下网站 https://forum.aspose.com/c/cells/9
