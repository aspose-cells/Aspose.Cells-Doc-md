---
title: 在Windows上安装Aspose.Cells
type: docs
weight: 20
url: /zh/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

有时候您可能在Windows Vista上安装Aspose.Cells时遇到一些问题。这篇文档解释了我们如何应对这些问题，并成功安装组件。实际上，Aspose.Cells安装程序需要在IIS上创建一个虚拟文件夹，以便在您的计算机上部署Web演示（Asp.NET演示），因此您需要在使用其安装程序安装Aspose.Cells之前具有管理权限。

{{% /alert %}} 
## **可能的因素**
通常，在Windows Vista中，您安装/使用的产品/组件始终在"普通用户"权限下实施，即使您是管理员。即使以管理员身份登录，程序也只被允许对文件系统进行有限访问。这导致了一些不幸的副作用，在Windows XP中，以管理员身份登录时，您通常不会遇到这些副作用。
## **UAC（用户帐户控制）**
UAC是Windows Vista的一部分，它要求您的权限。UAC模式（也称为管理员批准模式）主要影响管理员帐户的工作方式。当UAC启用（默认情况下启用）时，您必须明确授予任何想使用"管理员"权限的程序权限。任何未经您许可尝试使用管理员权限的程序都将被拒绝访问。UAC还是Windows Vista的其他安全功能的必需组成部分，包括Internet Explorer中的受保护模式。Internet Explorer受保护模式可保护计算机免受恶意网页等网络相关漏洞的影响，包括未知漏洞。

启用UAC模式后，您运行的每个程序只能获得系统的"标准用户"访问权限，即使您以管理员身份登录。Windows Vista具有内置功能，可以自动减少系统中安全漏洞的潜在性。它通过自动启用名为用户帐户控制（或简称UAC）的功能来达到这一点。UAC迫使作为本地管理员组成员的用户以无管理权限的常规用户方式运行。尽管UAC显然改善了Windows Vista的安全性，在某些情况下，您可能希望将其禁用，例如在观众面前进行演示（例如，与安全无关的演示）。一些家庭用户可能想要禁用UAC，因为这会使用系统的额外资源。
## **成功安装组件的步骤**
- 请确保在Vista上安装了IIS，然后再安装Aspose.Cells。这是强制性的，因为Aspose.Cells安装程序需要在IIS上创建一个虚拟文件夹，用于部署Web演示（Asp.NET演示）。
- 您需要禁用UAC（用户帐户控制）。在安装Aspose.Cells之前，您必须确保拥有对系统的完全控制的"管理权限"。否则，在使用其安装程序安装Aspose.Cells时，可能会遇到错误＃2869。

以下是实现此操作的一些方法。
### **使用命令行**
1. 搜索cmd.exe在您的Windows目录中，然后右键单击它，选择使用"管理员"身份运行。
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **使用控制面板**
- 单击开始
- 单击控制面板
- 单击用户帐户和家庭安全
- 单击用户帐户
- 单击打开或关闭用户帐户控制
-取消复选框
-点击确定

{{% alert color="primary" %}} 

您需要重新启动计算机以使更改生效。此更改影响计算机上的所有账户，而不仅仅是您的账户。

{{% /alert %}}
