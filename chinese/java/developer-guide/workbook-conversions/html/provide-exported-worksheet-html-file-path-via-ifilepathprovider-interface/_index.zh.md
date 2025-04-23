---
title: 通过IFilePathProvider接口提供导出的工作表HTML文件路径
type: docs
weight: 870
url: /zh/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能的使用场景**
假设您有一个包含多个工作表的Excel文件，并且希望将每个工作表导出为单独的HTML文件。如果您的任何工作表都具有指向其他工作表的链接，那么这些链接在导出的HTML中将会断开。为了解决这个问题，Aspose.Cells提供了[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)接口，您可以实现该接口来修复断开的链接。
## **通过IFilePathProvider接口提供导出的工作表HTML文件路径**
请下载以下代码中使用的[示例Excel文件](5473417.zip)及其导出的HTML文件。所有这些文件都在*Temp*目录中。您应该将其解压缩到*C:*驱动器上。然后它将变为*C:\Temp*目录。然后您将在浏览器中打开*Sheet1.html*文件，并单击其中的两个链接。这些链接指向*C:\Temp\OtherSheets*目录中的这两个导出的HTML工作表。

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下截图显示了*C:\Temp\Sheet1.html*及其链接的外观

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下截图显示了HTML源代码。正如您所看到的，现在链接是指向*C:\Temp\OtherSheets*目录。这是通过[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)接口实现的。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **示例代码**
请注意，*C:\Temp*目录仅用于说明目的。您可以使用任何自己选择的目录，并将[示例Excel文件](5473414.xlsx)放在其中，并执行提供的示例代码。然后它将在您的目录内创建*OtherSheets*子目录，并在其中导出第二和第三个工作表的HTML。请在执行之前更改提供的代码中的*dirPath*变量并将其指向您选择的目录。

{{% alert color="primary" %}} 

当设置Aspose.Cells许可证时，示例代码才能正常工作。如果在未设置许可证的情况下尝试运行代码，它将陷入无限循环。因此，我们已经添加了一个检查来打印一条消息并停止执行，以防止许可证未设置。您可以购买许可证，也可以向Aspose.Purchase团队申请30天临时许可证。

{{% /alert %}} 

请注意，取消代码中这些行的注释将使*Sheet1.html*和*Sheet2.html*或*Sheet3.html*中的链接中断，或当单击*Sheet1.html*中的链接时将不会打开。



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



以下是您可以使用提供的[示例Excel文件](5473414.xlsx)执行的完整示例代码。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
{{< app/cells/assistant language="java" >}}
