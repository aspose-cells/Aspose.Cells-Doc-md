﻿---
title: 为什么不自动化
type: docs
weight: 20
url: /zh/java/why-not-automation/
---
{{% alert color="primary" %}}

为什么 Aspose 组件是比 Microsoft 办公自动化更好的选择？*

我们在 Aspose 上最常听到两个问题：

1. **您的产品是否需要安装 Microsoft Office 才能运行？** 
简单回答是不。 Aspose 组件是完全独立的，不隶属于 Microsoft Corporation，也不由其授权、赞助或以其他方式批准。
1. **为什么要使用Aspose产品而不是利用Microsoft办公自动化？**
我们能给出的最简短的回答是，原因有很多，其中最主要的一个是 Microsoft 本身强烈建议不要通过软件解决方案实现 Office 自动化：[Office 服务器端自动化的注意事项](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Aspose 组件是自动化的更好替代方案有几个原因。一些关键原因是：

- [安全](/cells/zh/java/why-not-automation/#security)
- [稳定](/cells/zh/java/why-not-automation/#security)
- [可扩展性/速度](/cells/zh/java/why-not-automation/#security)
- [价格](/cells/zh/java/why-not-automation/#security)
- [特征](/cells/zh/java/why-not-automation/#security)

下面介绍其中的要点。此外，请务必访问本节末尾的链接。

{{% /alert %}}

## **安全**

以下是上述引用的 Microsoft 文章的直接引用：*“Office 应用程序从未打算在服务器端使用，因此没有考虑分布式组件所面临的安全问题。Office 不会对传入请求进行身份验证，也不会保护您免受无意中运行宏或启动另一台服务器的影响可能会从您的服务器端代码运行宏。不要打开从匿名 Web 上传到服务器的文件！根据最后设置的安全设置，服务器可以在管理员或系统上下文下运行宏完全权限并危及您的网络！此外，Office 使用许多客户端组件（例如 Simple MAPI、WinInet 和 MSDAIPP），这些组件可以缓存客户端身份验证信息以加快处理速度。如果 Office 在服务器端自动化，一个实例可能服务多个客户端，并且因为已经为该会话缓存了身份验证信息，所以一个客户端可以使用缓存d 另一个客户端的凭据，从而通过模拟其他用户获得未授予的访问权限。”*

Aspose 产品非常安全。 Aspose 组件在与所有 ASP.NET 应用程序相同的用户上下文中运行，在 ASPNET 用户下。因此，Aspose 组件不会对重要系统资源构成潜在风险。此外，当 Aspose 组件打开文档时，宏不会自动运行。 Aspose 组件的构建目标是允许开发人员创建、操作和保存 Office 文件。与 Microsoft Office 软件包相关的任何风险都不是 Aspose 组件固有的。

## **稳定**

以下是直接引用上面引用的 Microsoft 文章：*“Office 2000、Office XP 和 Office 2003 使用 Microsoft Windows Installer (MSI) 技术使最终用户的安装和自我修复更容易。MSI 引入了“首次使用时安装”的概念，它允许动态地安装功能在运行时安装或配置（针对系统，或更常见的是针对特定用户）。在服务器端环境中，这既会降低性能，又会增加出现要求用户批准安装的对话框的可能性或提供适当的安装盘。虽然它旨在提高 Office 作为最终用户产品的弹性，但 Office 对 MSI 功能的实施在服务器端环境中适得其反。此外，Office 的稳定性通常, 在服务器端运行时无法保证，因为它尚未针对此类用途进行设计或测试。在网络服务器上将 Office 作为服务组件使用可能会降低该机器的稳定性，并且结果是您的整个网络。如果您计划自动化 Office 服务器端，请尝试将程序隔离到一台不会影响关键功能的专用计算机上，并且可以根据需要重新启动。”*

由于 Aspose 组件被打包到一个 DLL 中，因此永远不需要安装任何额外的部件或组件来运行它们。 Aspose 组件仅由 .NET 应用程序使用，并且组件代码中没有任何部分旨在等待人类响应。 Aspose 组件已经过全面测试。 Aspose 组件被 IBM、希尔顿、读者文摘、美国银行等公司使用。

## **可扩展性/速度**

以下是直接引用上面引用的 Microsoft 文章：*“服务器端组件需要是高度可重入的多线程 COM 组件，对多个客户端具有最小的开销和高吞吐量。Office 应用程序几乎在所有方面都完全相反。它们是不可重入的、基于 STA 的自动化服务器旨在为单个客户端提供多样化但资源密集型的功能。它们作为服务器端解决方案几乎没有可扩展性，并且对重要元素（例如内存）有固定限制，不能通过配置更改。更重要的是，它们使用全局资源（例如内存映射文件、全局加载项或模板以及共享的自动化服务器），如果它们是在多客户端环境中配置的，这可能会限制可以并发运行的实例数量并导致竞争条件。计划同时运行任何 Office 应用程序的多个实例需要考虑“池化”或序列化对 Office 应用程序的访问以避免潜在的死机锁定或数据损坏。”*

Aspose 组件具有高度可扩展性和闪电般的速度。 Office 应用程序并非设计用于同时供成百上千用户使用；然而，Aspose 组件正是为此而设计的。我们的组件是真正的 .NET 解决方案，无论是在为单个应用程序提供支持的单个服务器上，还是在为企业范围的应用程序提供支持的负载平衡网络场上，都能完美运行。

## **价格**

当应用程序使用 Microsoft Office 自动化时，必须为每台运行该应用程序的机器购买 Microsoft Office 的副本。很多时候，应用程序可能需要创建或操作 office 文件，但并不要求用户拥有 Office。 Aspose 提供了一个非常[性价比高](https://purchase.aspose.com/buy)，免版税的再分发许可证，允许部署到无限数量的用户而无需担心许可问题。

创建基于 Web 的应用程序时，务必了解 Microsoft Office 自动化组件未针对服务器端解决方案定价或获得许可；因此，没有好的许可解决方案来部署使用 Microsoft Office 组件的 Web 应用程序。 Aspose 也为基于服务器的应用程序提供了一种非常经济高效的解决方案。

## **特征**

 Aspose 组件提供了管理 Office 文件所需的一切，还有很多很多。它们的设计理念是让开发人员以最少的工作量取得最大的成果。与 Office 自动化不同，Aspose 组件提供了许多强大、省时的功能。例如，[Aspose.Cells](https://products.aspose.com/cells/java/)为开发人员提供从**数据表**要么**数据视图**直接导入Excel文件。[每个组件](https://products.aspose.com/total/)Aspose 系列提供了自己的一套独特的强大功能。

购买 Aspose 组件或组件套件的最佳部分是可以访问我们的开发团队。我们的开发团队意识到，如果您的公司需要某项功能，那么其他公司很可能也需要它。虽然并非每个功能请求都可以添加，但我们的团队在提供帮助时会尽量保持开放和灵活的态度。这种心态帮助 Aspose 组件变得如此强大。如果您需要 Office 自动化对象的其他功能，那么添加它们的机会非常非常低。

## **结论**

{{% alert color="primary" %}}

本文涵盖了为什么 Aspose 组件比 Office 自动化更好的选择的要点。所有不同的 Aspose 组件提供无风险、无义务[评估版本](https://products.aspose.com/total/).我们鼓励您利用该评估，以便更好地了解 Aspose 可以为您的应用程序做些什么。

有关详细信息，请参阅以下 Internet 文章：

- [Office 服务器端自动化的注意事项](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}