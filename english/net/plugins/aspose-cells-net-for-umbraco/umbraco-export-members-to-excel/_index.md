---
title: Umbraco Export Members to Excel
type: docs
weight: 10
url: /net/umbraco-export-members-to-excel/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Export Members to Excel is an add‑on for Umbraco which allows you to export members from your Umbraco CMS to an Excel or OpenDocument Spreadsheet using [Aspose.Cells](https://products.aspose.com/cells/net/). A new node titled **Export Members To Excel** appears under the **Members** tree in the Umbraco backend after installation, where you can simply select members to export and the output format to get members in the selected document format.

### **Module Features**

This initial version of the add‑on has the following features:

- Export members to Microsoft Excel documents (.xls, .xlsx and .xlsb)  
- Export members to tab‑delimited text document (.txt)  
- Export members to CSV (comma‑delimited) (*.csv)  
- Export members to OpenDocument Spreadsheet (*.ods)  
- Option to select the desired output format before exporting  
- Option to export all or selected members to the chosen output document format  
- Works with all .NET versions starting from .NET 2.0  
- Exported document is automatically sent to the browser for download  
- If selected, a copy of the exported document is saved in the **App_Data/AsposeMemberExport** folder on the server for later use  
- Compatible with a wide range of Umbraco versions **4.5**+ **including versions 6 and 7**

## **System Requirements and Supported Platforms**

### **System Requirements**

In order to set up this module you need to have the following requirement met:

- Umbraco 6.0+

Please feel free to contact us if you wish to install this module on other versions of Umbraco.

### **Supported Platforms**

The module is supported on all versions of Umbraco running on ASP.NET 4.0.

## **Downloading**

You can download the Export Members to Excel add‑on from one of the following locations:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installing**

Once downloaded, please follow these steps to install this package into your Umbraco website:

1. Log in to the Umbraco **Developer** section, for example `http://www.myblog.com/umbraco/`.  
2. From the tree, expand the **Packages** folder.  
3. From here there are two ways to install a package: select **Install local package** or browse the **Umbraco Package Repository**.  
4. If you install the **local package**, do not unzip the package but load the ZIP into Umbraco.  
5. Follow the instructions on screen.

**Note:** You may get a “Maximum request length exceeded” error when installing. You can easily fix this issue by updating the `maxRequestLength` value in your Umbraco `web.config` file.

{{< highlight xml >}}
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
{{< /highlight >}}

## **Using**

After you have installed the macro, it is really simple to start using it on your website:

1. Make sure you are logged in to the Umbraco **Developer** section, for example `http://www.myblog.com/umbraco/`.  
2. Click **Members** in the list of sections at the bottom left of the screen.  
3. At the end of the tree, you will see a node titled **Export Members To Excel**; click on it to launch the Export to Excel add‑on.  
4. Select your desired output document format and select members to export. If you wish to export all members, leave the member selection empty or click the checkbox in the header row.  
5. Click the **Export** button at the bottom and you will be prompted to download the exported file.

## **Video Demo**

Please check [the video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) below to see the module in action.

## **Support, Extend and Contribute**

### **Support**

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought it or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to Aspose.Cells .NET for Umbraco modules using any of the following platforms:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Extend and Contribute**

Export Members to Excel is an open‑source add‑on and its source code is available on the major social‑coding websites listed below. Developers are encouraged to download the source code and extend the functionality as per their own requirements.

#### **Source Code**

You can get the latest source code from one of the following locations:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **How to Configure the Source Code**

You need to have the following installed in order to open and extend the source code:

- Visual Studio 2010 or higher

Please follow these simple steps to get started:

1. Download/clone the source code.  
2. Open Visual Studio 2010 and choose **File > Open > Project/Solution**.  
3. Browse to the folder that contains the source code you have downloaded and open, for example, **Aspose.UmbracoMemberExportToExcel.sln**.
