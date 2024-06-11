---
title: 通过IFilePathProvider接口提供导出的工作表html文件路径
type: docs
weight: 70
url: /zh/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能的使用场景**
假设您有一个包含多个工作表的excel文件，并且您想要将每个工作表导出为单独的HTML文件。如果您的任何工作表具有指向其他工作表的链接，则这些链接将在导出的HTML中断开。为解决此问题，Aspose.Cells提供了[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)接口，您可以实现该接口以修复这些中断的链接。
## **通过IFilePathProvider接口提供导出的工作表HTML文件路径**
请下载以下代码中使用的[示例excel文件](5115213.zip)及其导出的HTML文件。所有这些文件都在Temp目录中。您应该将其提取到C:驱动器中。然后它将变为C:\Temp目录。然后您将在浏览器中打开Sheet1.html文件，并单击其中的两个链接。这些链接指向C:\Temp\OtherSheets目录中的这两个导出的HTML工作表。

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

以下截图显示了C:\Temp\Sheet1.html及其链接的外观

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下截图显示了HTML源代码。如您所见，现在链接指向C:\Temp\OtherSheets目录。通过使用[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)接口实现了这一点。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **示例代码**
请注意C:\Temp目录仅用于举例。您可以使用任何选择的目录，并将[sample excel文件](5115211.xlsx)放入其中，并执行提供的示例代码。然后，它将在您的目录中创建OtherSheets子目录，并在其中导出第二和第三个工作表的HTML。在执行之前，请更改提供的代码中的dirPath变量并将其指向您选择的目录。

{{% alert color="primary" %}} 

当设置Aspose.Cells许可证时，示例代码才能正常工作。如果在未设置许可证的情况下尝试运行代码，它将陷入无限循环。因此，我们已经添加了一个检查来打印一条消息并停止执行，以防止许可证未设置。您可以购买许可证，也可以向Aspose.Purchase团队申请30天临时许可证。

{{% /alert %}} 

请注意，注释掉代码中的这些行将会导致Sheet1.html中的链接断开，Sheet2.html或Sheet3.html将无法在其中单击链接打开



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



以下是您可以通过提供的[示例excel文件](5115211.xlsx) 执行的完整样本代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
