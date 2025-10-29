---
title: 使用 C++ 更改外部链接数据源文件的绝对路径
linktitle: 更改外部链接数据源文件的绝对路径
type: docs
weight: 290
url: /zh/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: 在 Aspose.Cells 中用 C++ 更改外部链接数据源文件的绝对路径。
---

## 可能的使用场景

 如果你想更改外部链接数据源的绝对路径，请使用 [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) 方法。最初，该属性会设置为加载Excel文件的路径。但你可以将其设置为空字符串，或者设置为某个本地文件夹路径或远程网络路径。每次更改此属性时，外部链接数据源的路径也会随之更改。

## 更改外部链接数据源文件的绝对路径

 以下示例加载了包含外部链接的[示例Excel文件](5115146.xlsx)，它首先打印外部链接数据源（显示远程路径），然后移除远程路径并再次打印（显示本地路径），最后将 [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) 方法更改为本地和远程路径，再次打印外部链接数据源，示意更改已在控制台反映出来。

这是执行上述示例代码后的控制台或调试输出，使用[示例Excel文件](5115146.xlsx)。

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
