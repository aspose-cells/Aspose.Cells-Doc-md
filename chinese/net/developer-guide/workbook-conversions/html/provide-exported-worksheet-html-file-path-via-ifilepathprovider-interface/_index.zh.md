---
title: 通过 IFilePathProvider 接口提供导出的工作表 HTML 文件路径
type: docs
weight: 70
url: /zh/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能的使用场景**
假设您有一个包含多个工作表的 Excel 文件，并且您希望将每个工作表导出为单独的 HTML 文件。如果您的某些工作表存在到其他工作表的链接，则这些链接在导出的 HTML 中将会失效。为解决此问题，Aspose.Cells 提供了[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)接口，您可以实现该接口来修复这些错误的链接。
## **通过 IFilePathProvider 接口提供导出的工作表 HTML 文件路径**
请下载以下代码中使用的[示例 Excel 文件](5115213.zip)以及其导出的 HTML 文件。所有这些文件都在 Temp 目录中。您应当将其解压到 C 盘。然后它将成为 C:\Temp 目录。然后您将在浏览器中打开 Sheet1.html 文件，并点击其内部的两个链接。这些链接指向位于 C:\Temp\OtherSheets 目录中的两个导出的 HTML 工作表。

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下屏幕截图显示了 C:\Temp\Sheet1.html 及其链接的样子

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下屏幕截图显示了 HTML 源代码。您可以看到链接现在指向 C:\Temp\OtherSheets 目录。这是通过[使用 IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)接口实现的。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **示例代码**
请注意 C:\Temp 目录仅用于说明目的。您可以使用自己选择的任何目录，并将 [示例 Excel 文件](5115211.xlsx) 放入其中，并执行提供的示例代码。然后它将在您选择的目录内创建 OtherSheets 子目录，并将其中的第二个和第三个工作表导出为 HTML。请在执行之前更改所提供代码中的 dirPath 变量并将其指向您选择的目录。

{{% alert color="primary" %}} 

只有在设置 Aspose.Cells 许可证后，示例代码才能运行。如果尝试在没有设置许可证的情况下运行代码，则会陷入无限循环。因此，我们已添加了一个检查来打印消息并在未设置许可证时停止执行。您可以购买许可证或从 Aspose.Purchase 团队申请一个 30 天的临时许可证。

{{% /alert %}} 

请注意，在代码内将这些行注释掉将会使 Sheet1.html 中的链接失效，当单击其链接时，Sheet2.html 或 Sheet3.html 将无法打开



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



这是您可以使用提供的[示例 Excel 文件](5115211.xlsx)执行的完整示例代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
