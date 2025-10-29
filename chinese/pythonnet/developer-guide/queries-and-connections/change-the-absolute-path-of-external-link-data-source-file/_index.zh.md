---
title: 更改外部链接数据源文件的绝对路径
type: docs
weight: 290
url: /zh/python-net/change-the-absolute-path-of-external-link-data-source-file/
---

## 可能的使用场景

如果您想更改外部链接数据源文件的绝对路径，请使用[**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path)属性。最初，此属性将设置为加载Excel文件的路径。但您可以将其设置为空字符串，或者可以将其设置为某个本地文件夹路径或远程网络路径。每当更改此属性时，外部链接数据源文件的路径也将更改。

## 更改外部链接数据源文件的绝对路径

以下示例代码加载包含外部链接的[示例Excel文件](5115146.xlsx)。首先打印外部链接数据源，该外部链接数据源打印远程路径。然后删除远程路径并再次打印，此时，打印外部链接数据源与本地路径。然后更改[**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path)属性为本地和远程路径，并再次打印外部链接数据源，更改会在控制台输出中反映出来。

这是执行上述示例代码后的控制台或调试输出，使用[示例Excel文件](5115146.xlsx)。

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
