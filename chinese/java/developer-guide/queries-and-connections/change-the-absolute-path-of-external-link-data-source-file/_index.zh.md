---
title: 更改外部链接数据源文件的绝对路径
type: docs
weight: 1020
url: /zh/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **可能的使用场景**
如果您想要更改外部链接数据源文件的绝对路径，那么请使用 [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) 属性。最初，此属性将设置为加载Excel文件的路径。但您可以将其设置为空字符串，或者您可以将其设置为某个本地文件夹路径或远程网络路径。每当您更改此属性时，外部链接数据源文件的路径也将被更改。
## **更改外部链接数据源文件的绝对路径**
以下示例代码加载包含外部链接的 [示例excel文件](5472589.xlsx)。首先打印外部链接数据源，打印远程路径。然后删除远程路径再次打印，这次打印本地路径的外部链接数据源。然后更改 [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) 属性为本地和远程路径，并再次打印外部链接数据源，更改会反映在控制台输出中。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **控制台输出**
以下是执行上述示例代码时的控制台或调试输出 [示例excel文件](5472589.xlsx)。

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
