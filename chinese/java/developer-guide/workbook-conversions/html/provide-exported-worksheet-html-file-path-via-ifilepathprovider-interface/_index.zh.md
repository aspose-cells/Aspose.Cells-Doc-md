---
title: 通过IFilePathProvider接口提供导出工作表HTML文件路径
type: docs
weight: 870
url: /zh/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **可能的使用场景**
假设，您有一个包含多个工作表的 Excel 文件，并且您想要将每个工作表导出到单独的 HTML 文件。如果您的任何工作表有指向其他工作表的链接，那么这些链接将在导出的 HTML 中断开。为了解决这个问题，Aspose.Cells 提供[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)您可以实现该接口来修复损坏的链接。
## **通过IFilePathProvider接口提供导出工作表HTML文件路径**
请下载[示例 excel 文件](5473417.zip)在以下代码及其导出的 HTML 文件中使用。所有这些文件都在*温度*目录。你应该提取它*C：*驾驶。然后就会变成*C:\温度*目录。然后你会打开*Sheet1.html*在浏览器中打开文件，然后单击其中的两个链接。这些链接指的是这两个导出的 HTML 工作表，它们位于*C:\Temp\OtherSheets*目录。

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下屏幕截图显示了如何*C:\Temp\Sheet1.html*它的链接看起来像

![待办事项：图片_替代_文本](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下屏幕截图显示了 HTML 源。如您所见，链接现在指的是*C:\Temp\OtherSheets*目录。这是通过使用[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)界面。

![待办事项：图片_替代_文本](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **示例代码**
请注意*C:\温度*目录仅用于说明目的。您可以使用您选择和放置的任何目录[示例 excel 文件](5473414.xlsx)在那里并执行提供的示例代码。然后它将创建*其他床单*您的目录中的子目录，并在其中导出第二个和第三个工作表 HTML。请更改*目录路径*在提供的代码中添加变量，并在执行前将其引用到您选择的目录。

{{% alert color="primary" %}} 

示例代码仅在您设置 Aspose.Cells 许可证时才有效。如果您尝试在未设置许可证的情况下运行代码，它将进入无限循环。因此，我们添加了一个检查以在未设置许可证时打印消息并停止执行。您可以购买许可证或向 Aspose.Purchase 团队申请 30 天的临时许可证。

{{% /alert %}} 

请参阅在代码中注释这些行将破坏链接*Sheet1.html*和*Sheet2.html*要么*Sheet3.html*当他们的链接在里面被点击时不会打开*Sheet1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



这是您可以使用提供的执行的完整示例代码[示例 excel 文件](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
