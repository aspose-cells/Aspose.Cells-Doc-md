---
title : "Visual Studio Export GridView To Excel Control" 
description : "" 
weight : 12955 
toc : false
type: docs
url: /net/plugins/visualstudio/visual+studio+export+gridview+to+excel+control/
---

# Aspose.Cells for .NET : Visual Studio Export GridView To Excel Control


{{< panel title="Contents Summary" style="primary" >}}
*   1 [**Introduction**](#**introduction**)
    *   1.1 [Module Features](#module-features)
*   2 [**System Requirements and Supported Platforms**](#**system-requirements-and-supported-platforms**)
    *   2.1 [System Requirements](#system-requirements)
    *   2.2 [Supported Platforms](#supported-platforms)
*   3 [**Downloading**](#**downloading**)
*   4 [**Installing**](#**installing**)
    *   4.1 [For Visual Studio 2010, 2012 and 2013](#for-visual-studio-2010,-2012-and-2013)
    *   4.2 [For Visual Studio 2005, 2008 and Express editions](#for-visual-studio-2005,-2008-and-express-editions)
*   5 [**Using**](#**using**)
    *   5.1 [Manually adding ExportGridViewToExcel control](#manually-adding-exportgridviewtoexcel-control)
    *   5.2 [FAQs](#faqs)
    *   5.3 [Aspose .NET Export GridView To Excel Control Properties](#aspose-.net-export-gridview-to-excel-control-properties)
*   6 [**Video Demo**](#**video-demo**)
*   7 [**Support, Extend and Contribute**](#**support,-extend-and-contribute**)
    *   7.1 [Support](#support)
    *   7.2 [Extend and Contribute](#extend-and-contribute)
        *   7.2.1 [Source Code](#source-code)
        *   7.2.2 [How to configure the source code](#how-to-configure-the-source-code)
        *   7.2.3 [Source code overview](#source-code-overview)
{{< /panel >}}
## **Introduction**

Export GridView To Excel Control is an ASP.NET server control which allows exporting contents of GridView into Microsoft Excel or OpenOffice Spreadsheets using [Aspose.Cells](http://www.aspose.com/.net/excel-component.aspx). It adds **Export to Excel** button on top of the GridView control. Clicking the button dynamically exports the content of the GridView control to a Microsoft Excel or OpenOffice Spreadsheet and then automatically downloads the exported file to the disk location selected by the user in just couple of seconds.

### Module Features

This initial version of the control provides the following features:

*   Get an offline copy of your favorite online GridView content for editing, sharing and printing.
*   Inherited from default ASP.NET GridView control and hence have all its features and properties.
*   Export GridView to Xlsx, Xlsb, Xls, Txt, Csv, Ods.
*   Works with all .NET versions starting from .NET 2.0.
*   Ability to customize/localize Export button text.
*   Apply look and feel of your own theme on Export button using css.
*   Option to add custom heading on top of the exported document
*   Option to save each exported document on server at configurable disk path
*   Option to export current page or all pages when paging is enabled

![](https://docs2.aspose.com/cells/net/attachments/5020349/5115269.png)

This control allows you to export GridView in the following different file formats.

1.  Export GridView to Excel
2.  Export GridView to Xlsx
3.  Export GridView to Xlsb
4.  Export GridView to Xls
5.  Export GridView to Txt
6.  Export GridView to Csv
7.  Export GridView to Ods

## **System Requirements and Supported Platforms**

### System Requirements

Export GridView To Excel Control for Visual Studio can be used on any system that have IIS and .NET framework 2.0 or greater installed.

### Supported Platforms

Export GridView To Excel Control for Visual Studio is supported of all version of ASP.NET running on .NET framework 2.0 or greater. You can use any of the following Visual Studio versions to use this control in your ASP.NET applications

*   Visual Studio 2005
*   Visual Studio 2008
*   Visual Studio 2010
*   Visual Studio 2012
*   Visual Studio 2013

## **Downloading**

You can download Export GridView To Excel Control from one of the following locations

*   [CodePlex](https://asposecellsnet.codeplex.com/releases/view/617433)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
*   [Visual Studio Gallery](https://visualstudiogallery.msdn.microsoft.com/ce6e61a8-da1b-4b16-8825-c2d7fa0f45be)

## **Installing**

It is very simple and easy to install Export GridView To Excel Control, please follow these simple steps

### For Visual Studio 2010, 2012 and 2013

1.  Extract the downloaded zip file
2.  Double click the VSIX file Aspose.Excel.GridViewExport.vsix
3.  A dialog will appear showing you the available and supported Visual Studio versions installed on your machine
4.  Select the ones you want to add the Export GridView To Excel Control to.
5.  Click Install

You will get a success dialog once the installation is completed.

**Note:** Please make sure to restart Visual Studio for the changes to take effect.

### For Visual Studio 2005, 2008 and Express editions

Please follow these steps to integrate Export GridView To Excel Control in Visual studio for easy drag and drop just like other ASP.NET controls

1.  Extract the downloaded zip file
2.  Make sure to run Visual Studio as Administrator

On the Tools menu, click Choose Toolbox Items.

1.  Click Browse.  
    The Open dialog box appears.
2.  Browse to the extracted folder and select Aspose.Excel.GridViewExport.dll
3.  Click OK.

When you open an aspx or ascx control in the left side Toolbox you will see ExportGridViewToWord under General Tab

![](https://docs2.aspose.com/cells/net/attachments/5020349/5115270.png)

## **Using**

Once installed, it is very easy to start using this control in your ASP.NET applications

For .NET framework 4.0 and above

For .NET framework 2.0 and above

For applications running in .NET framework 4.0 and above in Visual Studio 2010 and above, you should see **ExportGridViewToExcel** control in **Aspose** Tab in Toolbar as shown below. You can simply drag drop this control onto your ASP.NET page, control or master page just like any other .NET control and get started.

In order you use this control in applications running in .NET 2.0 in any visual studio version make sure that you have added ExportGridViewToExcel to your toolbox as per instructions on ﻿[8.1.2.1 Downloading and Installing](#) under heading **For Visual Studio 2005, 2008 and Express editions**  
You should see **ExportGridViewToExcel** control in **General** Tab in Toolbar as shown below. You can simply drag drop this control onto your ASP.NET page, control or master page just like any other .NET control and get started.

![](download/thumbnails/5020349/568878106)  

![](download/thumbnails/5020349/1489014690)  

### Manually adding ExportGridViewToExcel control

If you have any issues using the above methods which uses Visual Studio Toolbox, you can manually add this control to your ASP.NET application running on any .NET framework greater than 2.0

1.  If you are using Visual Studio make sure to Run it as Administrator
2.  Add reference to **Aspose.Excel.GridViewExport.dll** available in extracted download package in your ASP.NET project or web application. Make sure your web application/Visual Studio have full access to this folder otherwise you might get Access is denied exception.
3.  Add this line to the top of the page, control or MasterPage
    
    <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>
    
4.  Add the following to a place on your ASP.NET page, control or masterpage where you want the control to be added
    
    <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>
    

### FAQs

Common questions and issues you might face while using this Control

{{< table style="table-striped" >}}
|# |Question|Answer|
|:----|:----|:----|
|1|I cannot see ExportGridViewToExcel control in Toolbox|**Visual Studio 2010 and higher**    1.Make sure that you have installed this control using VSIX extension file found in downloaded package. To verify go to Tools -> Extension and Updates. Unders Installed you should see 'Aspose Export Export GridView To Excel Control'. If don't see it please try re-installing it    2.Make sure your web application is running in .NET framework 4.0 or higher, for lower versions of .NET framework please check the above alternate method.**Older Versions of Visual Studio**    3.Make sure that you have manually added this control to your Toolbox as per above instructions.|
|2|I am getting 'Access is denied' error when running the application|If you are experiencing this problem on production then make sure that you copy both Aspose.Excel.dll and Aspose.Excel.GridViewExport.dll to your bin folder.If you are using Visual Studio make sure to run it as Administrator even if you are already logged-in as administrator.|
{{< /table >}}

### Aspose .NET Export GridView To Excel Control Properties

The following properties are exposed to configure and use cool features provided by this control

{{< table style="table-striped" >}}
|Property Name |Type|Example/Possible values|Description|
|:----|:----|:----|:----|
|ExportButtonText|string  |Export to Excel|You can use this property to override existing default text  |
|ExportButtonCssClass|string  |btn btn-primary  |Css Class that is applied to the outer div of the export button. To apply css on button you can use .yourClass input|
|ExportFileHeading|string  |<h4>GridView Export Example Report</h4>|You can use html tags to add style to your heading  |
|ExportOutputFormat|enum|Xlsx, Xlsb, Xls, Txt, Csv, Ods|Output format of the exported document. Supported formats are Xlsx, Xlsb, Xls, Txt, Csv, Ods|
|ExportOutputPathOnServer|string  |c:  temp|Local output Disk path on server where a copy of the export is automatically saved. Application must have write access to this path.|
|ExportDataSource|object  |allRowsDataTable  |Sets the object from which this data-bind control retrieves its list of data items. The object must have all the data that need to be exported. This property is used in addition to normal DataSource property and is useful when custom paging is enabled and current page only fetches rows to be displayed on screen.  |
|LicenseFilePath|string| |Local path on server to the license file. For example c:  inetpub  Aspose.Cells.lic|
{{< /table >}}

An example of Export GridView to Excel control with all properties used is shown below

{{< code lang="xml" >}}
<aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"
    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"
    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"
    ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToExcel>
{{< /code >}}

## **Video Demo**

Please check [the video](https://www.youtube.com/watch?v=_fSq_3TP1oM) below to see the module in action.

![](https://www.youtube.com/embed/_fSq_3TP1oM?rel=0)

## **Support, Extend and Contribute**

### Support

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to this control using any of the following platforms

*   [CodePlex](https://asposecellsnet.codeplex.com/workitem/list/basic)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
*   [Visual Studio Gallery Q & A](https://visualstudiogallery.msdn.microsoft.com/ce6e61a8-da1b-4b16-8825-c2d7fa0f45be)
*   [Code.MSDN Q & A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-601e98b0)

### Extend and Contribute

Aspose .NET Export GridView To Excel Control for Visual Studio is open source and its source code is available on the major social coding websites listed below. Developers are encouraged to download the source code and extend the functionality as per their own requirements.

#### Source Code

You can get the latest source code from one of the following locations

*   [CodePlex](https://asposecellsnet.codeplex.com/SourceControl/latest#Plugins/VisualStudio/Aspose.Excel.GridViewExport/)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
*   [Code.MSDN](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-601e98b0)

#### How to configure the source code

You need to have the following installed in order to open and extend the source code

*   Visual Studio 2010

Please follow these simple steps to get started

1.  Download/Clone the source code.
2.  Open Visual Studio 2010 and Choose **File** > **Open Project**
3.  Browse to the latest source code that you have downloaded and open **Aspose.Excel.GridViewExport.sln**

#### Source code overview

There are three projects in the solution

*   Aspose.Excel.GridViewExport - Contains VSIX package and Server control for .NET 4.0.
*   Aspose.Excel.GridViewExport\_DotNet\_2.0 - Extended GridView control for .NET 2.0
*   Aspose.Excel.GridViewExport.Website - Web project for testing the Excel Exportable GridView control

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [previewExcel.png](https://docs2.aspose.com/cells/net/attachments/5020349/5115269.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [ExportGridViewToExcel added to Toolbox in Visual Studio 2005 and 2008.png](https://docs2.aspose.com/cells/net/attachments/5020349/5115271.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [ExportGridViewToExcel added to Toolbox in Visual Studio 2005 and 2008.png](https://docs2.aspose.com/cells/net/attachments/5020349/5115270.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [ExportGridViewToExcel .NET 4.0 and Above.png](https://docs2.aspose.com/cells/net/attachments/5020349/5115272.png) (image/png)  

