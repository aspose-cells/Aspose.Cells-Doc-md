---
title: Umbraco Database Data Exporter to Excel
type: docs
weight: 20
url: /net/umbraco-database-data-exporter-to-excel/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
Aspose .NET Database Data Exporter to Excel for Umbraco Module allows users to export data directly from local or remote database tables, views, and by a custom query into Microsoft Excel or OpenOffice Spreadsheet. This module demonstrates the powerful spreadsheet‑building feature provided by Aspose.Cells. This initial version of the module is enriched with the following cool features to make the export process simple and easy to use.

### **Module Features**
This initial version of the add‑on has the following features:

- Allow connecting to a local MS SQL Server database  
- Allow connecting to a remote MS SQL Server database  
- Populate all tables from the connected database  
- Populate all views from the connected database  
- Allow writing a custom query  
- Auto‑fit columns to content length.  
- Allow skipping strings longer than 32 KB in Excel cells (LoadOptions)  
- Apply header column formatting as bold text  
- Allow using as data source (table, view, custom query)  
- Export data to Microsoft Excel documents (.xls, .xlsx and .xlsb)  
- Export data to tab‑delimited text document (*.txt)  
- Export data to CSV (comma‑delimited) (*.csv)  
- Export data to OpenDocument Spreadsheet (*.ods)  
- Option to select desired output format before exporting.  
- Exported document is automatically sent to the browser for downloading.  

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

## **System Requirements and Supported Platforms**
### **System Requirements**
In order to set up Aspose .NET Database Data Exporter to Excel for Umbraco module you need to have the following requirements met:

- Umbraco 6.2.5 & Umbraco 6 versions  
- Umbraco with MS SQL Server  
- Microsoft .NET Framework 4.0  

**Note:** Umbraco 7 and above are not supported in this release. We look forward to hearing your feedback and adding support for Umbraco 7 in the next version.  

### **Supported Platforms**
The module is supported on all versions of  

- Umbraco 6.0 running on ASP.NET 4.0  

## **Downloading**
You can download Aspose .NET Cells Database Data Exporter to Excel for Umbraco module from one of the following locations:

- [Umbraco Projects](https://goo.gl/BPrWm2)  
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)  

## **Installing**
Once downloaded, please follow these steps to install this package into your Umbraco website:

1. Log in to the Umbraco **Developer** section, for example `http://www.myblog.com/umbraco`  
2. From the tree, expand the **Packages** folder.  
3. From here there are two ways to install a package: select **Install local package** or browse the **Umbraco Package Repository**.  
4. If you install **local package**, do not unzip the package but load the ZIP into Umbraco.  
5. Follow the instructions on screen.  

**Note:** You may get a ‘Maximum request length exceeded’ error when installing. You can easily fix this issue by updating the `maxRequestLength` value in your Umbraco `web.config` file.  

```xml
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```  

## **Using**
After you have installed Aspose .NET Database Data Exporter to Excel for Umbraco module it is really simple to start using it on your website. Please follow these simple steps to get started:

1. Make sure you are logged in to the Umbraco **Developer** section, for example `http://www.myblog.com/umbraco/`  
2. Click **Settings** in the list of sections in the bottom left of the screen.  
3. Expand the **Templates** node and select the template that you want to add to, for example Textpage.  
4. Select the position in the selected template where you want the export button to be added. Usually you may want to add it to the top right of the page, or the bottom of the page.  
5. Click **Insert Macro** on the top ribbon.  
6. From **Choose a macro** (Aspose .NET Database Data Exporter to Excel for Umbraco), select the recently installed Aspose .NET Database Data Exporter to Excel for Umbraco macro and click **OK**.  

Please check the screenshot below for details.  

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

You have successfully added Aspose .NET Database Data Exporter to Excel module to your page.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. Enter or use pre‑populated MS SQL Server connection string  
2. Select Data Source Type (Table, View, Custom Query)  
3. Select or enter Data Source (Table, View, Custom Query)  
4. Select Export Type  
5. Click **Export Data**  
6. Desired file will be downloaded automatically.  

## **Video Demo**
Please check [the video](https://www.youtube.com/watch?v=MkfKyeLTauE) below to see the module in action.

## **Support, Extend and Contribute**
### **Support**
From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought it or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to Aspose.Words .NET for Umbraco Modules using any of the following platforms:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)  

### **Extend and Contribute**
Export Members to Excel is an open‑source add‑on and its source code is available on the major social‑coding websites listed below. Developers are encouraged to download the source code and extend the functionality as per their own requirements.

#### **Source Code**
You can get the latest source code from one of the following locations:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)  

#### **How to configure the source code**
You need to have the following installed in order to open and extend the source code:

- Visual Studio 2010 or higher  

Please follow these simple steps to get started:

1. Download/clone the source code.  
2. Open Visual Studio 2010 and choose **File** > **Open Project**.  
3. Browse to the latest source code that you have downloaded and open, e.g., `Aspose.DatabaseDataExportertoExcel.sln`.
