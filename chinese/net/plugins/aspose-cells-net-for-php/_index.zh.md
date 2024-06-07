---
title: Aspose.Cells的PHP.NET
type: docs
weight: 40
url: /zh/net/aspose-cells-net-for-php/
---

## **入门指南**

### **介绍**

### **系统要求和支持的平台**

#### **系统要求**

**以下是使用Aspose.Cells .NET for PHP的系统要求:**

- 安装了PHP和PHP管理器的IIS。
- Aspose.Total API。
- Aspose.Cells的Interop dll和tlb文件。

#### **支持的平台**

**以下是支持的平台:**

- PHP 5.3或更高版本
- Windows操作系统

### **下载和配置**

#### **下载所需库**

下载下面提到的必需库。这些是执行Aspose.Cells Java for PHP示例所需的库。

- [从下载部分下载Aspose.Cells for .NET(DLL或MSI)文件](https://downloads.aspose.com/cells/net)
- [下载Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

如果您下载了MSI版本，则默认情况下会在安装位置找到Aspose.Cells.dll，即C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0文件夹。
然而，如果您下载了DLL版本，您可以将其提取然后将Aspose.Cells.dll从.NET 2.0文件夹复制到c:\temp文件夹以便使用。
同样，提取Interop zip文件并将Aspose.Inteop.dll复制到c:\temp

#### **从社交编码网站下载示例**

以下版本的正在运行的示例可在下面提到的社交编码网站上下载:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP示例**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **如何在Windows平台上配置源代码**

请按照以下简单步骤进行，以在使用时打开和扩展源代码：

##### **1. 注册dll和interop.dll文件，例如Aspose.Cells.dll和Aspose.Cells.Interop.dll**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. 在PHP中启用COM和DOTNET扩展**

在IIS中打开PHP Manager，然后点击'启用和禁用扩展'。找到php_com_dotnet.dll并确保其已启用。

##### **3. 配置Aspose.Cells .NET for PHP示例**

###### **方法1**

从[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)克隆PHP示例
然后运行以下命令

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **方法2**

在您的PHP项目的composer.json文件中添加以下行

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

然后运行安装命令

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **支持扩展和贡献**

#### **支持**

自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。

您可以使用以下任何平台上的任何问题或建议来记录与Aspose.Cells .NET for PHP相关的问题。 

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **扩展和贡献**

Aspose.Cells .NET for PHP是开源的，其源代码可以在下面列出的主要社交编码网站上找到。鼓励开发人员下载源代码，并通过建议或添加新功能或改进现有功能来做出贡献，以使其他人也能从中受益。

#### **源代码**

您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **示例代码**

本节包括以下主题

- [PHP程序员指南](/cells/zh/net/php-programmers-guide/)
  - [在PHP中处理文件](/cells/zh/net/working-with-files-in-php/)
    - [PHP中的文件处理功能](/cells/zh/net/file-handling-features-in-php/)
      - [在PHP中打开文件](/cells/zh/net/opening-files-in-php/)
      - [在PHP中保存文件](/cells/zh/net/saving-files-in-php/)
    - [PHP中的实用功能](/cells/zh/net/utility-features-in-php/)
      - [在PHP中加密文件](/cells/zh/net/encrypting-files-in-php/)
      - [在PHP中进行Excel到PDF的转换](/cells/zh/net/excel-to-pdf-conversion-in-php/)
      - [在PHP中管理文档属性](/cells/zh/net/managing-document-properties-in-php/)
      - [在PHP中进行工作表到图像的转换](/cells/zh/net/worksheet-to-image-conversion-in-php/)
  - [在PHP中处理公式](/cells/zh/net/working-with-formulas-in-php/)
    - [在PHP中计算公式](/cells/zh/net/calculating-formulas-in-php/)
  - [在PHP中处理工作表](/cells/zh/net/working-with-worksheets-in-php/)
    - [在PHP中的管理功能](/cells/zh/net/management-features-in-php/)
      - [在PHP中管理工作表](/cells/zh/net/managing-worksheets-in-php/)
        - [在PHP中向现有Excel文件添加工作表](/cells/zh/net/add-worksheets-to-existing-excel-file-in-php/)
        - [在PHP中向新Excel文件添加工作表](/cells/zh/net/add-worksheets-to-new-excel-file-in-php/)
        - [在PHP中使用工作表索引删除工作表](/cells/zh/net/removing-worksheets-using-sheet-index-in-php/)
        - [在PHP中使用工作表名称删除工作表](/cells/zh/net/removing-worksheets-using-sheet-name-in-php/)
