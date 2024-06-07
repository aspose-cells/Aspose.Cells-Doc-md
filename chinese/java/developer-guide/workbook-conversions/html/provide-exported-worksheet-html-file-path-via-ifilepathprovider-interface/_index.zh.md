---
title: 通过IFilePathProvider接口提供导出的工作表HTML文件路径
type: docs
weight: 870
url: /zh/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能的使用场景**
假设您有一个包含多个工作表的Excel文件，并且希望将每个工作表导出为单独的HTML文件。如果您的某些工作表链接到其他工作表，则这些链接将在导出的HTML中断开。为解决此问题，Aspose.Cells提供了[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)接口，您可以实现此接口以修复断开的链接。
## **通过 IFilePathProvider 接口提供导出的工作表 HTML 文件路径**
请下载以下代码中使用的[样本excel文件](5473417.zip)及其导出的HTML文件。所有这些文件都在*Temp*目录中。您应该将其解压到*C:*驱动器上。然后它将变为*C:\Temp*目录。然后您将在浏览器中打开*Sheet1.html*文件并单击其中的两个链接。这些链接指向位于*C:\Temp\OtherSheets*目录中的这两个导出的HTML工作表。

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下屏幕截图显示了*C:\Temp\Sheet1.html*及其链接的外观

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下屏幕截图显示了HTML源代码。正如您所看到的，这些链接现在指向*C:\Temp\OtherSheets*目录。这是使用[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)接口实现的。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **示例代码**
请注意，*C:\Temp*目录仅供说明目的。您可以选择任何目录，并将[样本excel文件](5473414.xlsx)放在其中，并在执行提供的示例代码之前创建*OtherSheets*子目录。请在执行之前更改提供的代码中的*dirPath*变量，并将其引用到您选择的目录。

{{% alert color="primary" %}} 

只有在设置 Aspose.Cells 许可证后，示例代码才能运行。如果尝试在没有设置许可证的情况下运行代码，则会陷入无限循环。因此，我们已添加了一个检查来打印消息并在未设置许可证时停止执行。您可以购买许可证或从 Aspose.Purchase 团队申请一个 30 天的临时许可证。

{{% /alert %}} 

请查看在代码中注释这些行将打断*Sheet1.html*中的链接，当单击内部链接时，*Sheet2.html*或*Sheet3.html*将不会打开。



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



以下是完整的示例代码，您可以使用提供的[样本excel文件](5473414.xlsx)执行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
