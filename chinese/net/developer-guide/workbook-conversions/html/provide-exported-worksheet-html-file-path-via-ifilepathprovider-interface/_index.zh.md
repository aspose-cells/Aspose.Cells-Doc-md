---
title: 通过IFilePathProvider接口提供导出工作表html文件路径
type: docs
weight: 70
url: /zh/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **可能的使用场景**
假设，您有一个包含多个工作表的 Excel 文件，并且您想要将每个工作表导出到单独的 HTML 文件。如果您的任何工作表有指向其他工作表的链接，那么这些链接将在导出的 HTML 中被破坏。针对这个问题，Aspose.Cells提供[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)您可以实现该接口来修复损坏的链接。
## **通过 IFilePathProvider 接口提供导出的工作表 HTML 文件路径**
请下载[示例 excel 文件](5115213.zip)在以下代码及其导出的 HTML 文件中使用。所有这些文件都在 Temp 目录中。您应该将其解压缩到 C: 驱动器。然后它将成为 C:\Temp 目录。然后您将在浏览器中打开 Sheet1.html 文件并单击其中的两个链接。这些链接指向 C:\Temp\OtherSheets 目录中的这两个导出的 HTML 工作表。

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下屏幕截图显示了 C:\Temp\Sheet1.html 及其链接的外观

![待办事项：图片_替代_文本](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下屏幕截图显示了 HTML 源代码。如您所见，链接现在指向 C:\Temp\OtherSheets 目录。这是通过使用[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)界面。

![待办事项：图片_替代_文本](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **示例代码**
请注意 C:\Temp 目录仅用于说明目的。您可以使用您选择和放置的任何目录[示例 excel 文件](5115211.xlsx)在那里并执行提供的示例代码。然后它将在您的目录中创建 OtherSheets 子目录，并在其中导出第二个和第三个工作表 HTML。请在提供的代码中更改 dirPath 变量，并在执行前将其引用到您选择的目录。

{{% alert color="primary" %}} 

示例代码仅在您设置 Aspose.Cells 许可证时才有效。如果您尝试在未设置许可证的情况下运行代码，它将进入无限循环。因此，我们添加了一个检查以在未设置许可证时打印消息并停止执行。您可以购买许可证或向 Aspose.Purchase 团队申请 30 天的临时许可证。

{{% /alert %}} 

请参阅在代码中注释这些行将破坏 Sheet1.html 和 Sheet2.html 中的链接，或者在 Sheet1.html 中单击它们的链接时 Sheet3.html 将不会打开



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



这是完整的示例代码，您可以使用提供的代码执行[示例 excel 文件](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
