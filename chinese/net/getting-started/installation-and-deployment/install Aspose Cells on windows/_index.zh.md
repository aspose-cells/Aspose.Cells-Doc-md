---
title: 在Windows上安装Aspose.Cells
type: docs
weight: 20
url: /zh/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

有时您可能在Windows Vista上安装Aspose.Cells时遇到问题。本文将解释如何解决这个问题，以及如何成功安装该组件。实际上，Aspose.Cells安装程序需要在IIS上为其Web演示(Asp.NET演示)部署创建一个虚拟文件夹，因此在使用其安装程序安装Aspose.Cells之前，您需要具有管理权限。安装程序必须显式允许对系统的管理员级访问。

{{% /alert %}} 
## **可能因素**
通常在Windows Vista中，无论您是管理员，您安装/使用的产品/组件始终在“普通用户”权限下实施。即使您以管理员身份登录，程序也只被允许对文件系统进行有限访问。这会产生一些不幸的副作用，在Windows XP中，当以管理员身份登录时通常不会遇到这些问题。
## **UAC(用户账户控制)**
**UAC**是Windows Vista的一部分，它会请求您的许可。**UAC**模式(也称为**管理员批准模式**)主要影响管理员帐户的工作方式。当**UAC**启用(默认情况下启用)时，必须明确允许任何要使用“管理员”权限的程序。任何未经您许可尝试使用管理员权限的程序都将被拒绝访问。**UAC**还用于**Windows Vista**的其他安全功能，包括Internet Explorer中的**保护模式**。Internet Explorer的保护模式可保护计算机免受恶意网页和其他与网络相关的漏洞的影响，包括未知漏洞。

**UAC**模式启用后，您运行的每个程序都只能以“标准用户”权限访问系统，即使您以管理员身份登录。**Windows Vista**具有自动减少系统安全漏洞潜在性的内置能力。它通过自动启用名为**用户账户控制**(或简称**UAC**)的功能来实现。**UAC**强制要求本地管理员组中的用户像没有管理权限的普通用户一样运行。尽管**UAC**显然提高了**Windows Vista**的安全性，但在某些情况下，您可能希望禁用它，例如，在观众面前展示演示(非安全相关的演示)时。一些家庭用户可能会因为系统资源的额外使用而诱使禁用**UAC**。
## **成功安装该组件的步骤**
- 请确保在安装**Aspose.Cells**之前在您的Vista上安装了IIS。这是强制性的，因为**Aspose.Cells**安装程序需要在IIS上为Web演示(Asp.NET演示)的部署创建一个虚拟文件夹。
- 您需要禁用**UAC**(用户账户控制)。在安装**Aspose.Cells**之前，您必须确保具有完全控制系统的**管理员权限**。否则，在使用其安装程序安装**Aspose.Cells**时可能会遇到2869错误。

以下是实现此目标的一些方法。
### **使用命令行**
1. 在Windows目录中搜索cmd.exe，然后右键单击它并选择**以管理员身份运行**。
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **使用控制面板**
- 点击开始
- 点击控制面板
- 点击用户帐户和家庭安全
- 点击用户帐户
- 点击打开或关闭用户帐户控制
- 取消复选框
- 点击确定

{{% alert color="primary" %}} 

您需要重新启动计算机才能使更改生效。此更改会影响计算机上的所有帐户，而不仅仅是您的。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
