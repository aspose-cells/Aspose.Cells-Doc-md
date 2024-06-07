---
title: Aspose.Cells.GridJs基础知识
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: 本文介绍了为GridJs设置Web应用程序的基本步骤。
---

## GridJs基础

Aspose.Cells.GridJs是一个.NET标准库，允许用户快速简便地开发Web应用程序来显示/编辑电子表格。 

Aspose.Cells.GridJs支持导入流行的电子表格（XLS、XLSX、XLSM、XLSB、CSV、SpreadsheetML、ODS）文件格式。

它还允许将Excel文件导出为PDF、HTML等。以下是开发GridJs Web应用程序的基本流程步骤。

- 实现GridCacheForStream以编写自己的缓存存储业务逻辑。
- 设置一个控制器动作来从电子表格文件获取JSON。您可以使用GridJsWorkbook.ImportExcelFile和GridJsWorkbook.ExportToJson API，GridJs会自动将电子表格文件存储在缓存中。
- 设置一个控制器动作来获取用于更新操作的JSON。您可以使用GridJsWorkbook.UpdateCell API，GridJs会在缓存中执行更新操作并返回更新后的JSON。
- 设置一个控制器动作来获取电子表格中的图像/形状文件URL，GridJs将自动将所有图像/形状压缩到缓存中。它将使用GridCacheForStream.GetFileUrl API。
- 设置一个控制器动作来获取缓存中的文件，这样我们就可以获取缓存中的图像/形状压缩文件或电子表格文件。它将使用GridCacheForStream.LoadStream API。
- 设置一个控制器动作来下载电子表格。您可以使用GridJsWorkbook.SaveToCacheWithFileName API。

以下是一个演示Aspose.Cells.GridJs用法的基本演示：https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs 

如果您有任何问题、需求或需要帮助，请反馈到以下网站https://forum.aspose.com/c/cells/9
