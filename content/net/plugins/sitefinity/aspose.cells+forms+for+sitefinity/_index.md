---
title : "Aspose.Cells Forms for Sitefinity" 
description : "" 
weight : 12963 
toc : false
type: docs
url: /net/plugins/sitefinity/aspose.cells+forms+for+sitefinity/
---

# Aspose.Cells for .NET : Aspose.Cells Forms for Sitefinity


{{< panel title="Contents Summary" style="primary" >}}
*   [Introduction](#introduction)
    *   [Module Features](#module-features)
*   [System Requirements and Supported Platforms](#system-requirements-and-supported-platforms)
*   [Downloading and Installing](#downloading-and-installing)
    *   [Downloading](#downloading)
    *   [Installing](#installing)
*   [Using and Video Demo](#using-and-video-demo)
    *   [Using](#using)
        *   [How to apply Aspose License?](#how-to-apply-aspose-license?)
        *   [Dynamic Forms Settings](#dynamic-forms-settings)
        *   [Dynamic Form Submit](#dynamic-form-submit)
        *   [Export Saved Data](#export-saved-data)
    *   [Video Demo](#video-demo)
*   [Support, Extend and Contribute](#support,-extend-and-contribute)
    *   [Support](#support)
    *   [Extend and Contribute](#extend-and-contribute)
        *   [Source Code](#source-code)
        *   [How to configure source code](#how-to-configure-source-code)
{{< /panel >}}
## Introduction

Aspose.Cells Dynamic Forms for Sitefinity Module allows users to Generate Dynamic Questionnaire and Surveys, save user input into Excel Spreadsheet and Export the results into Excel, Text, CSV and OpenDocument Spreadsheet using Aspose.Cells. This module demonstrates the powerful spreadsheet building feature provided by Aspose.Cells for .NET.

![image](https://docs2.aspose.com/cells/net/attachments/thumbnails/5023902/5115561)  

### Module Features

This initial version of the module is enriched with the following features to make the Forms Building and Export process simple and easy to use

*   Save Form Field Settings in Excel
*   Save Form’s User Input Data in to Excel
*   Allow to Add new and Update existing Form Fields
*   Allow to Add TextBox, Multiline TextBox, RadioButtons, CheckBox and DropDownList, DropDownList Items type Fields
*   Allow to Add/Update Label for each Fields
*   Allow to Show/Hide Form Fields
*   Auto Fit Columns to contents length and apply Header Column formatting as Bold Text
*   Export Data to Microsoft Excel Documents (.xls, .xlsx and .xlsb)
*   Export Data to Tab delimited text document (\*.txt)
*   Export Data to CSV (Comma delimited) (\*.csv)
*   Export Data to OpenDocument Spreadsheet (\*.ods)
*   Option to select desired output format before exporting.
*   Exported document is automatically sent to browser for downloading.

## System Requirements and Supported Platforms

In order to setup Aspose.Cells .NET for Sitefinity add-ons you need to have the following requirements met:

*   Sitefinity CMS running on ASP.NET 4.0

Please feel free to contact us if you have any issues setting up this Sitefinity Add-on.

The Add-on is supported on all versions of

*   Sitefinity CMS running on ASP.NET 4.0

## Downloading and Installing

### Downloading

You can download Aspose .NET Content Exporter for Sitefinity module from one of the following locations

*   [CodePlex](https://asposecellssitefinity.codeplex.com/releases/view/620241)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)
*   [Microsoft Developer Network](https://code.msdn.microsoft.com/Sitefinity-Dynamic-Forms-93656293)

### Installing

Once downloaded, please follow these steps to install the Add-on into your Sitefinity website:

**Step 1: Copy files to your Sitefinity installation**

Please extract the downloaded ZIP file. You will need FTP or direct access to the Sitefinity installation folder on the server to perform the following:

1.  Copy **Aspose.Cells.dll** & **Aspose.Sitefinity.FormBuilder.dll** into the bin folder  folder of the Sitefinity installation.
2.  Copy the **Addons** folder on the root of the Sitefinity installation where the **bin** folder is located.

**Step 2: Register the Aspose Sitefinity Content Export add-on in Sitefinity**

1.  Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by [http://www.mywebsite.com/sitefinity](http://www.mywebsite.com/sitefinity)
2.  Click **Administration** and then **Settings**.  
    The Basic Settings page appears.
3.  Click the **Advanced** link.  
    The Settings page appears.
4.  In the left pane, click **Toolboxes** followed by **Toolboxes**, then **PageControls**, **Sections** and **ContentToolboxSection**, then **Tools.**
5.  Click **Create new**.  
    The widget registration form appears.
6.  Fill the form fields as follows:
    1.  Make sure **Enabled** is selected.
        1.  In the **Control CLR Type or Virtual Path** field.
            1.  Add **~/Addons/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx**
        2.  Add **Name**, **Title** and **Description** as follows:
            1.  Aspose  **PageName **(like Edit,View,Export) form to SiteFinity Users
            2.  Aspose **PageName** Form (like Aspose Edit Form , Aspose View Form , Aspose Export Form)
            3.  **PageName** Form Builder & Exporter for Sitefinity.
        3.  You may leave all other fields as they are.
        4.  When finished, click **Save changes**.
        5.  The widget is registered in the toolbox and can be used in Sitefinity. (**See** **below**** Image**)

![image](download/thumbnails/5023902/685775646)  

## Using and Video Demo

### Using

After you have installed and configured the Aspose.Cells Dynamic Forms Builder for Sitefinity Users add-on it is really simple to start using it on your website. Please follow these simple steps to get started:

1.  Make sure you are logged-in to Sitefinity with an Administrator level account.
2.  Navigate to the page where you want to add the plugin. Make sure the page is opened in edit mode.
3.  From the **Drag Widgets** menu on the right, select Aspose Edit/View/Export Form and drag it into position. (**See** **below ****Image** )

![image](https://docs2.aspose.com/cells/net/attachments/thumbnails/5023902/5115562)  

You have successfully added Aspose.Cells Dynamic Form Builder for Sitefinity module to your page.

#### How to apply Aspose License?

This Plugin uses an evaluation version of Aspose.Cells. Once you are happy with your evaluation, you can purchase a license at the [Aspose website](http://www.aspose.com/purchase/default.aspx).  
To remove evaluation message and feature limitations, product license should be applied. You will receive a license file after you have purchased the product. Please follow the steps below to apply the license

*   Make sure the license file is named as **Aspose.Total.lic**
*   Place **Aspose.Total.lic** file in **App\_Data** folder of your Sitefinity website e.g. "Sitefinity Root Folder/App\_Data/Aspose.Total.lic"

#### Dynamic Forms Settings

1.  Make sure you are logged-in click on Page menu click on first row **View** option button near **Action column.**  
2.  Click **Edit** button available near option label.
3.  There are few pre-defined fields, you can edit/hide just by clicking **Edit** in grid.
4.  You can create/delete/update new fields of any type **(TextBox, MultiLineTextBox, RadioButton, Checkboxes, DropdownList, Title, Success Message)**

#### Dynamic Form Submit

1.  Fill in the fields.
2.  Click **Submit** button to save data.
3.  Each **Submit** button click will save new record in to excel.

#### Export Saved Data

1.  Make sure you are logged-in , go to Pages menu and click on first row view option button near action column
2.  Mouse Over **Export Icon** and Click **onit** export page will be open 
3.  Select **Export Type**
4.  Click **Export Data**
5.  Exported data file as per export type will poupup to download/open

You have successfully added Aspose Sitefinity Export Users to Excel.

### Video Demo

Please check [the video](https://www.youtube.com/watch?v=La5WMCvafR0) below to see the module in action.

## Support, Extend and Contribute

### Support

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.  
You can log any issues or suggestions related to Aspose.Cells .NET for Sitefinity Modules using any of the following platforms

*   [CodePlex](https://asposecellssitefinity.codeplex.com/workitem/list/basic)
*   [Github](https://github.com/asposecells/Aspose.Cells-for-.NET/issues)
*   [Microsoft Developer Network](https://code.msdn.microsoft.com/Sitefinity-Dynamic-Forms-93656293/view/Discussions#content)

### Extend and Contribute

#### Source Code

You can download the latest source code at:

*   [Codeplex](https://asposecellssitefinity.codeplex.com/SourceControl/latest)
*   [Github](https://github.com/asposecells/Aspose.Cells-for-.NET)
*   [Microsoft Developer Network](https://code.msdn.microsoft.com/Sitefinity-Dynamic-Forms-93656293)

#### How to configure source code

You need to have the following installed in order to open and extend the source code

*   Visual Studio 2013 or higher

Please follow these simple steps to get started

1.  Download/Clone the source code.
2.  Open Visual Studio 2013 and Choose **File** > **Open Project**
3.  Browse to the latest source code that you have downloaded and open the **.sln** file.

