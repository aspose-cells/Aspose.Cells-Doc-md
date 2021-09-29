---
title: Provide exported worksheet html file path via IFilePathProvider interface
type: docs
weight: 70
url: /net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Possible Usage Scenarios**
Suppose, you have an excel file with multiples sheets and you want to export each sheet to individual HTML file. If any of your sheets have links to other sheets, then those links will be broken in the exported HTML. To deal with this problem, Aspose.Cells provides [IFilePathProvider](https://apireference.aspose.com/cells/net/aspose.cells/ifilepathprovider) interface which you can implement to fix the broken links.
## **Provide exported worksheet HTML file path via IFilePathProvider interface**
Please download the [sample excel file](5115213.zip) used in the following code and its exported HTML files. All these files are inside the Temp directory. You should extract it on C: drive. Then it will become C:\Temp directory. Then you will open the Sheet1.html file in the browser and click the two links inside it. These links refer to these two exported HTML worksheets which are inside the C:\Temp\OtherSheets directory.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

The following screenshot shows how the C:\Temp\Sheet1.html and its links look like

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

The following screenshot shows the HTML source. As you can see that the links are now referring to C:\Temp\OtherSheets directory. This was achieved using the [IFilePathProvider](https://apireference.aspose.com/cells/net/aspose.cells/ifilepathprovider) interface.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Sample Code**
Please note C:\Temp directory is just for illustration purpose. You can use any directory of your choice and place [sample excel file](5115211.xlsx) inside there and execute the provided sample code. It will then create OtherSheets sub-directory inside your directory and export second and third worksheets HTML inside it. Please change the dirPath variable inside the provided code and refer it to the directory of your choice before execution.

{{% alert color="primary" %}} 

The sample code will only work when you will set Aspose.Cells license. If you will try to run the code without setting the license, it will go into an infinite loop. Therefore, we have added a check to print a message and stop execution when the license is not set. You can either purchase a license or request for a 30-day temporary license from Aspose.Purchase team.

{{% /alert %}} 

Please see commenting these lines inside the code will break the links in Sheet1.html and Sheet2.html or Sheet3.html will not open up when their links will be clicked inside the Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Here is the complete sample code which you can be executed with the provided [sample excel file](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
