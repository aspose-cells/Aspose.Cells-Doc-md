---
title: 通过Node.js和C++更改外部链接数据源文件的绝对路径
linktitle: 更改外部链接数据源文件的绝对路径
type: docs
weight: 290
url: /zh/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: 学习如何使用Aspose.Cells for Node.js via C++更改外部链接数据源文件的绝对路径。 
---

## 可能的使用场景

如果你想更改外部链接数据源文件的绝对路径，请使用[**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--)属性。最初，该属性将设置为加载Excel文件的路径。但你可以将其设置为空字符串，或设置为本地文件夹路径或远程网络路径。每当你更改此属性，外部链接数据源的路径也会相应更改。

## 更改外部链接数据源文件的绝对路径

以下示例代码加载包含外部链接的[样例Excel文件](5115146.xlsx)。它首先打印外部链接数据源，显示远程路径，然后删除远程路径并再次打印，此时显示本地路径的外部链接数据源。接着，它将[**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--)属性更改为本地和远程路径并再次打印外部链接数据源，变化会反映在控制台输出中。

这是执行上述示例代码后，使用[样例Excel文件](5115146.xlsx)的控制台或调试输出。

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
