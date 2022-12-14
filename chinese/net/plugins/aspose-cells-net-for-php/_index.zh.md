---
title: Aspose.Cells .NET 用于 PHP
type: docs
weight: 40
url: /zh/net/aspose-cells-net-for-php/
---
## **入门**

### **介绍**

### **系统要求和支持的平台**

#### **系统要求**

**以下是对 PHP 使用 Aspose.Cells .NET 的系统要求：**

- 安装了 PHP 和 PHP 管理器的 IIS。
- Aspose.Total API。
- Aspose.Cells Interop dll 和 tlb 文件。

#### **支持的平台**

**以下是支持的平台：**

- PHP 5.3 或以上
- Windows操作系统

### **下载和配置**

#### **下载所需的库**

下载下面提到的所需库。这些是执行 Aspose.Cells Java PHP 示例所必需的。

- [从下载部分下载 Aspose.Cells for .NET（DLL 或 MSI）文件](https://downloads.aspose.com/cells/net)
- [下载 Aspose.Cells for .NET 互操作 dll](https://downloads.aspose.com/cells/net)

如果你下载MSI版本，你会在安装位置找到Aspose.Cells.dll，默认是C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0文件夹。
但是，如果您下载了 DLL 版本，则可以将其解压缩，然后将 Aspose.Cells.dll 从 .NET 2.0 文件夹复制到您的 c:\temp 文件夹以便于使用。
同样提取 interop zip 文件并将 Aspose.Inteop.dll 复制到 c:\temp

#### **从社交编码网站下载示例**

以下版本的运行示例可在下面提到的社交编码网站上下载：

-----

##### **GitHub**

- **Aspose.Cells .NET 用于 PHP 示例**

  - [Aspose.Cells .NET 用于 PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Windows平台源码配置方法**

请按照以下简单步骤在使用时打开和扩展源代码：

##### **1. 注册 dll 和 interop.dll 文件，例如 Aspose.Cells.dll 和 Aspose.Cells.Interop.dll。**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. 在 PHP 中启用 COM 和 DOTNET 扩展。**

在 IIS 中打开 PHP 管理器，然后单击“启用禁用和扩展”。查找 php_com_dotnet.dll 并确保它已启用。

##### **3.为PHP示例配置Aspose.Cells .NET**

###### **方法一**

从中克隆 PHP 示例[知乎](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
并运行以下命令

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **方法二**

在您的 PHP 项目的 composer.json 文件中添加以下行

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

并运行安装命令

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

要阅读有关作曲家的信息，请访问<https://getcomposer.org/>

### **支持扩展和贡献**

#### **支持**

从 Aspose 成立之初，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，并且了解当技术问题或软件中的怪癖阻止您做您需要做的事情时是多么令人沮丧。我们来这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。凡是使用过我们产品的人，无论是购买过的还是正在评价中的，都值得我们充分的关注和尊重。

您可以使用以下任何平台记录与 Aspose.Cells .NET for PHP 相关的任何问题或建议：

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **扩展和贡献**

Aspose.Cells .NET for PHP 是开源的，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码并通过建议或添加新功能或改进现有功能来做出贡献，以便其他人也可以从中受益。

#### **源代码**

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **示例代码示例**

本节包括以下主题

- [PHP 程序员指南](/cells/zh/net/php-programmers-guide/)
  - [在 PHP 中处理文件](/cells/zh/net/working-with-files-in-php/)
    - [PHP 中的文件处理功能](/cells/zh/net/file-handling-features-in-php/)
      - [在 PHP 中打开文件](/cells/zh/net/opening-files-in-php/)
      - [在 PHP 中保存文件](/cells/zh/net/saving-files-in-php/)
    - [PHP 中的实用功能](/cells/zh/net/utility-features-in-php/)
      - [在 PHP 中加密文件](/cells/zh/net/encrypting-files-in-php/)
      - [在 PHP 中将 Excel 转换为 PDF](/cells/zh/net/excel-to-pdf-conversion-in-php/)
      - [在 PHP 中管理文档属性](/cells/zh/net/managing-document-properties-in-php/)
      - [在 PHP 中将工作表转换为图像](/cells/zh/net/worksheet-to-image-conversion-in-php/)
  - [在 PHP 中使用公式](/cells/zh/net/working-with-formulas-in-php/)
    - [在 PHP 中计算公式](/cells/zh/net/calculating-formulas-in-php/)
  - [在 PHP 中使用工作表](/cells/zh/net/working-with-worksheets-in-php/)
    - [PHP 中的管理功能](/cells/zh/net/management-features-in-php/)
      - [在 PHP 中管理工作表](/cells/zh/net/managing-worksheets-in-php/)
        - [在 PHP 中将工作表添加到现有的 Excel 文件](/cells/zh/net/add-worksheets-to-existing-excel-file-in-php/)
        - [在 PHP 中将工作表添加到新的 Excel 文件](/cells/zh/net/add-worksheets-to-new-excel-file-in-php/)
        - [在 PHP 中使用工作表索引删除工作表](/cells/zh/net/removing-worksheets-using-sheet-index-in-php/)
        - [在 PHP 中使用工作表名称删除工作表](/cells/zh/net/removing-worksheets-using-sheet-name-in-php/)
