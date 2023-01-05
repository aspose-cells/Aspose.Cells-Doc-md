---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /net/aspose-cells-net-for-php/
---

## **Getting Started**

### **Introduction**

### **System Requirements and Supported Platforms**

#### **System Requirements**

**Following are the system requirements to use Aspose.Cells .NET for PHP:**

- IIS with PHP and PHP Manager installed.
- Aspose.Total APIs.
- Aspose.Cells the Interop dll and tlb file.

#### **Supported Platforms**

**Following are the supported platforms:**

- PHP 5.3 or above
- Windows OS

### **Download and Configure**

#### **Download Required Libraries**

Download required libraries mentioned below. These are the required for executing Aspose.Cells Java for PHP examples.

- [Download Aspose.Cells for .NET (DLL or MSI) files from download section](https://downloads.aspose.com/cells/net)
- [Download Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

If you download MSI version, you will find Aspose.Cells.dll in installed location which is C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 folder by default.
However in case you have downloaded DLL version you can extract it and then copy Aspose.Cells.dll from .NET 2.0 folder to your c:\temp folder for ease of use.
Similarly extract interop zip file and copy Aspose.Inteop.dll to c:\temp

#### **Download Examples from Social Coding Sites**

Following releases of running examples are available to download on below mentioned social coding sites:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **How to configure the source code on Windows Platform**

Please follow these simple steps in order to open and extend the source code while using:

##### **1. Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Enable COM and DOTNET Extensions in PHP.**

In IIS open PHP Manager and then Click ‘Enable to Disable and Extension‘. Find php_com_dotnet.dll and make sure it is enabled.

##### **3. Configure Aspose.Cells .NET for PHP Examples**

###### **Method 1**

Clone PHP Examples from [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
and run the following command

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Method 2**

In your PHP Project's composer.json file add following lines

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

and run the install command

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Support Extend and Contribute**

#### **Support**

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to Aspose.Cells .NET for PHP using any of the following platforms:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Extend and Contribute**

Aspose.Cells .NET for PHP is open source and its source code is available on the major social coding websites listed below. Developers are encouraged to download the source code and contribute by suggesting or adding new feature or improving the existing ones, so that others could also benefit from it.

#### **Source Code**

You can get the latest source code from one of the following locations

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Sample Code Examples**

This section includes the following topics

- [PHP Programmers Guide](/cells/net/php-programmers-guide/)
  - [Working With Files in PHP](/cells/net/working-with-files-in-php/)
    - [File Handling Features in PHP](/cells/net/file-handling-features-in-php/)
      - [Opening Files in PHP](/cells/net/opening-files-in-php/)
      - [Saving Files in PHP](/cells/net/saving-files-in-php/)
    - [Utility Features in PHP](/cells/net/utility-features-in-php/)
      - [Encrypting Files in PHP](/cells/net/encrypting-files-in-php/)
      - [Excel to PDF Conversion in PHP](/cells/net/excel-to-pdf-conversion-in-php/)
      - [Managing Document Properties in PHP](/cells/net/managing-document-properties-in-php/)
      - [Worksheet to Image Conversion in PHP](/cells/net/worksheet-to-image-conversion-in-php/)
  - [Working With Formulas in PHP](/cells/net/working-with-formulas-in-php/)
    - [Calculating Formulas in PHP](/cells/net/calculating-formulas-in-php/)
  - [Working With Worksheets in PHP](/cells/net/working-with-worksheets-in-php/)
    - [Management Features in PHP](/cells/net/management-features-in-php/)
      - [Managing Worksheets in PHP](/cells/net/managing-worksheets-in-php/)
        - [Add Worksheets to Existing Excel File in PHP](/cells/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Add Worksheets to New Excel File in PHP](/cells/net/add-worksheets-to-new-excel-file-in-php/)
        - [Removing Worksheets Using Sheet Index in PHP](/cells/net/removing-worksheets-using-sheet-index-in-php/)
        - [Removing Worksheets Using Sheet Name in PHP](/cells/net/removing-worksheets-using-sheet-name-in-php/)
