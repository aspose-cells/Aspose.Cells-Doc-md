---
title: 更改外部链接数据源文件的绝对路径
type: docs
weight: 1020
url: /zh/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **可能的使用场景**
如果要更改外部连接数据源文件的绝对路径，请使用 [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) 属性。最初，该属性将设置为加载 Excel 文件的路径。但是您可以将其设置为空字符串，或者将其设置为某个本地文件夹路径或远程网络路径。每当更改此属性时，外部连接数据源文件的路径也将被更改。
## **更改外部连接数据源文件的绝对路径**
以下示例代码加载了带有外部连接的 [示例 excel 文件](5472589.xlsx)。首先打印外部连接数据源，打印远程路径。然后删除远程路径，再次打印，这次打印外部连接数据源为本地路径。然后将 [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) 属性更改为本地和远程路径，并再次打印外部连接数据源，更改将反映在控制台输出中。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **控制台输出**
执行上述示例代码与 [示例 excel 文件](5472589.xlsx) 后的控制台或调试输出如下。

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
