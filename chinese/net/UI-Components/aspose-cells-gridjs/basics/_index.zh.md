---
title: Aspose.Cells.GridJs 基础
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: 本文介绍了为 GridJs 设置 Web 应用程序的基本步骤。
---

## GridJs 基础

Aspose.Cells.GridJs 是一个 .NET 标准库，允许用户快速轻松地开发 Web 应用程序以显示/编辑电子表格。 

Aspose.Cells.GridJs 支持导入流行的电子表格（XLS、XLSX、XLSM、XLSB、CSV、SpreadsheetML、ODS）文件格式。

它还允许将 Excel 文件导出为 PDF、HTML 等。以下是开发 GridJs Web 应用程序的基本过程步骤。

- 实现GridCacheForStream,编写自己的缓存存储业务逻辑。
- 设置控制器动作以从电子表格文件中获取JSON。您可以使用GridJsWorkbook.ImportExcelFile和GridJsWorkbook.ExportToJson APIs，GridJs将自动将电子表格文件存储在缓存中。
- 设置控制器动作以获取更新操作的JSON。您可以使用GridJsWorkbook.UpdateCell API，在缓存中进行更新操作并返回更新后的JSON。
- 设置控制器动作以获取电子表格中的图像/形状文件URL，GridJs将自动在缓存中压缩所有图像/形状。将使用GridCacheForStream.GetFileUrl API。
- 设置控制器动作以获取缓存中的文件，从而可以在缓存中获取图像/形状压缩文件或电子表格文件。它将使用GridCacheForStream.LoadStream API。
- 设置控制器动作以下载电子表格。您可以使用GridJsWorkbook.SaveToCacheWithFileName API。

以下是显示Aspose.Cells.GridJs用法的基本演示：https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs 

如果您有任何疑问、需求或需要帮助，请反馈到以下网站 https://forum.aspose.com/c/cells/9
