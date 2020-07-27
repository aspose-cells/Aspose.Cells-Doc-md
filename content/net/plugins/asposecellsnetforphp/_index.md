+++
title = "Aspose.Cells .NET for PHP" 
description = "" 
weight = 8893 
+++

Aspose.Cells for .NET : Aspose.Cells .NET for PHP  

# Aspose.Cells for .NET : Aspose.Cells .NET for PHP


{{< panel title="Contents Summary" style="primary" >}}
*   [Getting Started](#Aspose.Cells.NETforPHP-GettingStarted)
    *   [Introduction](#Aspose.Cells.NETforPHP-Introduction)
    *   [System Requirements and Supported Platforms](#Aspose.Cells.NETforPHP-SystemRequirementsandSupportedPlatforms)
        *   [System Requirements](#Aspose.Cells.NETforPHP-SystemRequirements)
        *   [Supported Platforms](#Aspose.Cells.NETforPHP-SupportedPlatforms)
    *   [Download and Configure](#Aspose.Cells.NETforPHP-DownloadandConfigure)
        *   [Download Required Libraries](#Aspose.Cells.NETforPHP-DownloadRequiredLibraries)
        *   [Download Examples from Social Coding Sites](#Aspose.Cells.NETforPHP-DownloadExamplesfromSocialCodingSites)
            *   [GitHub](#Aspose.Cells.NETforPHP-GitHub)
        *   [How to configure the source code on Windows Platform](#Aspose.Cells.NETforPHP-HowtoconfigurethesourcecodeonWindowsPlatform)
            *   [1\. Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.](#Aspose.Cells.NETforPHP-1.Registerbothdllandinterop.dllfilese.g.Aspose.Cells.dllandAspose.Cells.Interop.dll.)
            *   [2\. Enable COM and DOTNET Extensions in PHP.](#Aspose.Cells.NETforPHP-2.EnableCOMandDOTNETExtensionsinPHP.)
            *   [3\. Configure Aspose.Cells Java for PHP Examples](#Aspose.Cells.NETforPHP-3.ConfigureAspose.CellsJavaforPHPExamples)
                *   [Method 1](#Aspose.Cells.NETforPHP-Method1)
                *   [Method 2](#Aspose.Cells.NETforPHP-Method2)
    *   [Support Extend and Contribute](#Aspose.Cells.NETforPHP-SupportExtendandContribute)
        *   [Support](#Aspose.Cells.NETforPHP-Support)
        *   [Extend and Contribute](#Aspose.Cells.NETforPHP-ExtendandContribute)
        *   [Source Code](#Aspose.Cells.NETforPHP-SourceCode)
*   [Sample Code Examples](#Aspose.Cells.NETforPHP-SampleCodeExamples)
{{< /panel >}}
## Getting Started

### Introduction

### System Requirements and Supported Platforms

#### System Requirements

**Following are the system requirements to use Aspose.Cells .NET for PHP:**

*   IIS with PHP and PHP Manager installed.
*   Aspose.Total APIs.
*   Aspose.Cells the Interop dll and tlb file.

#### Supported Platforms

**Following are the supported platforms:**

*   PHP 5.3 or above
*   Windows OS

### Download and Configure

#### Download Required Libraries

Download required libraries mentioned below. These are the required for executing Aspose.Cells Java for PHP examples.

*   [Download Aspose.Cells for .NET (DLL or MSI) files from download section](http://www.aspose.com/community/files/51/.net-components/aspose.cells-for-.net/category1084.aspx)

*   [Download Aspose.Cells for .NET interop dll](http://www.aspose.com/community/files/51/.net-components/aspose.cells-for-.net/entry651498.aspx)

If you download msi version, you will find Aspose.Cells.dll in installed location which is C:\\Program Files (x86)\\Aspose\\Aspose.Cells for .NET\\Bin\\net2.0 folder by default.  
However in case you have downloaded DLL version you can extract it and then copy Aspose.Cells.dll from .NET 2.0 folder to your c:\\temp folder for ease of use.  
Similarly extract interop zip file and copy Aspose.Inteop.dll to c:\\temp

#### Download Examples from Social Coding Sites

Following releases of running examples are available to download on below mentioned social coding sites:

---

##### GitHub

*   **Aspose.Cells .NET for PHP Examples**
    *   [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### How to configure the source code on Windows Platform

Please follow these simple steps in order to open and extend the source code while using:

##### 1\. Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

{{< code lang="cs" >}}
Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.
C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase
Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905
Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.
Types registered successfully
C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase
{{< /code >}}

##### 2\. Enable COM and DOTNET Extensions in PHP.

In IIS open PHP Manager and then Click ‘Enable to Disable and Extension‘. Find php\_com\_dotnet.dll and make sure it is enabled.

##### 3\. Configure Aspose.Cells Java for PHP Examples

###### Method 1

Clone PHP Examples from [github](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)  
and run the following command

{{< code lang="cs" >}}
composer install
{{< /code >}}

###### Method 2

In your PHP Project's composer.json file add following lines

{{< code lang="cs" >}}
{
    "require": {
        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"
    }
}
{{< /code >}}

and run the install command

{{< code lang="cs" >}}
composer install
{{< /code >}}

To read about composer visit [https://getcomposer.org/](https://getcomposer.org/)

### Support Extend and Contribute

#### Support

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to Aspose.Cells .NET for PHP using any of the following platforms:

*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### Extend and Contribute

Aspose.Cells .NET for PHP is open source and its source code is available on the major social coding websites listed below. Developers are encouraged to download the source code and contribute by suggesting or adding new feature or improving the existing ones, so that others could also benefit from it.

#### Source Code

You can get the latest source code from one of the following locations

*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## Sample Code Examples

This section includes the following topics

*   [PHP Programmers Guide](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/)
    *   [Working With Files in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/)
        *   [File Handling Features in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/filehandlingfeaturesinphp/)
            *   [Opening Files in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/filehandlingfeaturesinphp/opening+files+in+php)
            *   [Saving Files in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/filehandlingfeaturesinphp/saving+files+in+php)
        *   [Utility Features in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/utilityfeaturesinphp/)
            *   [Encrypting Files in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/utilityfeaturesinphp/encrypting+files+in+php)
            *   [Excel to PDF Conversion in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/utilityfeaturesinphp/excel+to+pdf+conversion+in+php)
            *   [Managing Document Properties in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/utilityfeaturesinphp/managing+document+properties+in+php)
            *   [Worksheet to Image Conversion in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithfilesinphp/utilityfeaturesinphp/worksheet+to+image+conversion+in+php)
    *   [Working With Formulas in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithformulasinphp/)
        *   [Calculating Formulas in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithformulasinphp/calculating+formulas+in+php)
    *   [Working With Worksheets in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/)
        *   [Management Features in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/managementfeaturesinphp/)
            *   [Managing Worksheets in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/managementfeaturesinphp/managingworksheetsinphp/)
                *   [Add Worksheets to Existing Excel File in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/managementfeaturesinphp/managingworksheetsinphp/add+worksheets+to+existing+excel+file+in+php)
                *   [Add Worksheets to New Excel File in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/managementfeaturesinphp/managingworksheetsinphp/add+worksheets+to+new+excel+file+in+php)
                *   [Removing Worksheets Using Sheet Index in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/managementfeaturesinphp/managingworksheetsinphp/removing+worksheets+using+sheet+index+in+php)
                *   [Removing Worksheets Using Sheet Name in PHP](https://docs2.aspose.com/cells/net/plugins/asposecellsnetforphp/phpprogrammersguide/workingwithworksheetsinphp/managementfeaturesinphp/managingworksheetsinphp/removing+worksheets+using+sheet+name+in+php)

