---
title: Aspose.Cells.GridJs基础
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/basics/
---
## GridJs 基础知识

Aspose.Cells.GridJs 是一个 .NET 标准库，允许用户开发 Web 应用程序以快速轻松地显示/编辑电子表格。

Aspose.Cells.GridJs支持导入流行的电子表格（XLS、XLSX、XLSM、XLSB、CSV、SpreadsheetML、ODS）文件格式。

它还允许将 Excel 文件导出到 PDF、HTML 等。以下是开发 GridJs Web 应用程序的基本流程步骤。

- 实施 GridCacheForStream 以编写您自己的缓存存储业务逻辑。
- 设置控制器操作以从电子表格文件中获取 json。您可以使用 GridJsWorkbook.ImportExcelFile 和 GridJsWorkbook.ExportToJson API，GridJs 会自动将传播文件存储在缓存中。
- 设置一个controller action来获取更新操作的json。可以使用GridJsWorkbook.UpdateCell API，GridJs会在缓存中做更新操作并返回更新后的json。
- 设置控制器操作以获取电子表格中的图像/形状文件 url，GridJs 将自动将所有图像/形状压缩到缓存中。它将使用 GridCacheForStream.GetFileUrl API。
- 设置一个控制器操作来获取缓存中的文件，这样我们就可以获取缓存中的图像/形状 zip 文件或电子表格文件。它将使用 GridCacheForStream.LoadStream API。
- 设置控制器操作以下载电子表格。您可以使用 GridJsWorkbook.SaveToCacheWithFileName API。

下面是一个显示 Aspose.Cells.GridJs 用法的基本演示：https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

如果您有任何问题、需求或需要帮助，请反馈至以下网站https://forum.aspose.com/c/cells/9