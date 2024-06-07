---
title: 更改外部链接数据源文件的绝对路径
type: docs
weight: 290
url: /zh/net/change-the-absolute-path-of-external-link-data-source-file/
---

## 可能的使用场景

如果要更改外部链接数据源文件的绝对路径，请使用[**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) 属性。最初，此属性将设置为加载Excel文件的路径。 但您可以将其设置为空字符串，也可以将其设置为某些本地文件夹路径或远程网络路径。 每当更改此属性时，外部链接数据源文件的路径也将更改。

## 更改外部链接数据源文件的绝对路径

以下示例代码加载包含外部链接的[示例Excel文件](5115146.xlsx)。 先打印外部链接数据源，该数据源会打印远程路径。 然后删除远程路径并重新打印，这次它将打印有本地路径的外部链接数据源。 然后将[**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) 属性更改为本地和远程路径，并重新打印外部链接数据源，变化将反映在控制台输出中。

这是在执行上述示例代码与[示例Excel文件](5115146.xlsx)之后的控制台或调试输出。

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
