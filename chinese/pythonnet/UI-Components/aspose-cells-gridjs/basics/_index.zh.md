---
title: Aspose.Cells.GridJs基础知识
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## GridJs基础

Aspose.Cells.GridJs是一个允许用户快速轻松开发用于查看或编辑电子表格文件的跨平台Web应用程序的库。 

## 为什么使用Aspose.Cells.GridJs


- 它使用户能够创建、编辑、格式化、协作，并安全地共享具有实时更新、公式支持和丰富数据可视化工具的电子表格，类似于传统桌面应用程序。
- 它支持数据输入和编辑、格式、电子表格导航、公式计算、数据操作、图表和可视化、导入和导出、安全、为开发人员提供附加组件和定制选项，以符合特定业务需求的编辑器。

## 特性


- 导入、查看和编辑流行的电子表格格式。
- 将电子表格导出到各种支持的文件格式。
- 显示和管理图像、形状或图表文件。
- 执行网格设计和布局定制。
- 多工作表管理。
- 创建和计算 Excel® 公式。

## 支持的文件格式

https://docs.aspose.com/cells/python-net/supported-file-formats/

## 通用用法

以下是开发 GridJs 网页应用程序的基本步骤。

- 通过 Config.set_file_cache_directory(`你的存储路径`) 设置缓存存储目录
- 通过 Config.set_license(`你的许可证路径`) 设置许可证
- 通过 GridJsWorkbook.set_image_url_base(`查看图像的路径`) 设置图像路由 URL
- 设置路由操作以从电子表格文件中获取 `json`。您可以使用 `GridJsWorkbook.ImportExcelFile` 和 `GridJsWorkbook.ExportToJson` API，`GridJs` 将自动将电子表存储在缓存中。
- 设置一个路由操作来获取更新操作的 `json`。您可以使用 `GridJsWorkbook.UpdateCell` API，`GridJs` 将在缓存中执行更新操作并返回更新后的 `json`。
- 设置一个路由操作以在缓存中获取文件，因此我们可以获取缓存中的图像/形状 zip 文件或电子表文件。
- 设置一个用于下载电子表的路由操作。您可以使用 `GridJsWorkbook.SaveToCacheWithFileName` API。

下面是展示 Aspose.Cells.GridJs 用法的基本演示：

https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 

在演示中，我们使用 [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) 来渲染客户端页面。

如果您有任何问题、需求或需要帮助，请反馈到以下网站https://forum.aspose.com/c/cells/9
