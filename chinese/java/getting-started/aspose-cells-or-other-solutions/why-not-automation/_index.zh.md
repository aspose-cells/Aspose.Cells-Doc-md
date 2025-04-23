---
title: 为什么不自动化
type: docs
weight: 20
url: /zh/java/why-not-automation/
---

{{% alert color="primary" %}}

为什么Aspose组件比Microsoft Office自动化更好？*

在Aspose，我们经常听到两个问题：

1. **您的产品是否需要安装Microsoft Office才能运行？** 
   简单的答案是否定的。Aspose组件完全独立，与Microsoft Corporation没有附属关系，也未经授权、赞助或其他方式获得 Microsoft Corporation 批准。
1. **为什么我们应该使用Aspose产品而不是利用Microsoft Office自动化？**
   我们能给出的最简短答案是有很多原因，主要原因是Microsoft自己强烈建议不要使用软件解决方案的Office自动化：[Office服务器端自动化的注意事项](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)。

Aspose组件比自动化有几个很好的替代方案。一些关键原因包括：

- [安全性](/cells/zh/java/why-not-automation/#security)
- [稳定性](/cells/zh/java/why-not-automation/#security)
- [可伸缩性/速度](/cells/zh/java/why-not-automation/#security)
- [价格](/cells/zh/java/why-not-automation/#security)
- [功能](/cells/zh/java/why-not-automation/#security)

以下是关键点的描述。此外，请务必访问本节末尾的链接。

{{% /alert %}}

## **安全性**

以下是上述微软文章的直接引用：“办公应用程序从未打算用于服务器端使用，因此并未考虑分布式组件面临的安全问题。Office不会对传入的请求进行身份验证，也无法保护你免受意外运行宏或启动另一个可能从服务器端代码运行宏的服务器的影响。不要从匿名Web上传到服务器的文件。基于上次设置的安全设置，服务器可以以管理员或系统上下文运行宏，并威胁您的网络！此外，Office使用许多客户端组件（例如简单MAPI、WinInet和MSDAIPP），这些组件可以在缓存客户端身份验证信息以加快处理。如果Office被服务器端自动化，一个实例可以为多个客户端提供服务，并且因为认证信息已为该会话进行了缓存，所以一个客户端可以使用另一个客户端的缓存凭据，并由此冒充其他用户获得未授予权限。”

Aspose产品非常安全。Aspose组件在与所有ASP.NET应用程序相同的用户上下文下运行，即ASPNET用户。因此，Aspose组件不会对重要的系统资源构成潜在风险。此外，当由Aspose组件打开文档时，宏不会自动运行。Aspose组件的目标是让开发人员能够创建、操作和保存Office文件。与Microsoft Office套件相关的风险对Aspose组件并不固有。

## **稳定性**

以下是引用上述微软文章的直接引用：*“Office 2000、Office XP 和 Office 2003 使用 Microsoft Windows Installer (MSI) 技术，以使安装和自我修复更容易对最终用户。MSI 引入了“首次使用时安装”的概念，允许在运行时（用于系统，或更常见的是针对特定用户）动态安装或配置功能。在服务器端环境中，这既会降低性能，也会增加用户批准安装或提供适当安装磁盘的对话框出现的可能性。虽然它的设计目的是增加 Office 作为最终用户产品的弹性，但 Office 对 MSI 功能的实现在服务器端环境中是适得其反的。此外，由于 Office 未针对此类用途进行设计或测试，因此无法保证 Office 整体的稳定性在服务器端运行。在网络服务器作为服务组件使用 Office 可能会降低该计算机的稳定性，从而影响整个网络。如果打算自动化 Office 服务器端，尝试将程序隔离到专用计算机上，这不会影响关键功能，并且可以根据需要重新启动。”*

由于 Aspose 组件被打包到一个单独的 DLL 中，因此永远不需要安装任何其他部分或组件才能使其正常工作。Aspose 组件仅由 .NET 应用程序使用，没有任何部分设计成等待用户响应。Aspose 组件经过了彻底的测试。Aspose 组件被 IBM、希尔顿、读者文摘、美国银行等公司使用。

## **可伸缩性/速度**

以下是引用上述微软文章的直接引用：*“服务器端组件需要高度可重入、多线程的 COM 组件，具有最小的开销和多客户端的高吞吐量。Office 应用程序在几乎所有方面都刚好相反。它们是非可重入的、基于STA的自动化服务器，旨在为单个客户端提供多样但资源密集型的功能。它们提供了很少可伸缩性作为服务器端解决方案，并对重要元素（如内存）有固定限制，无法通过配置更改。更重要的是，它们使用全局资源（如内存映射文件、全局加载项或模板以及共享的自动化服务器），这可能会限制可同时运行的实例数量，并导致在多客户端环境中配置时出现竞争条件。计划同时运行任何 Office 应用程序的开发人员，需要考虑“池化”或串行化访问 Office 应用程序，以避免潜在的死锁或数据损坏。”*

Aspose 组件具有高度可伸缩性和极快的速度。Office 应用程序不是设计用于同时被数百甚至数千用户使用；然而，Aspose 组件就是为此而设计的。我们的组件是真正的 .NET 解决方案，在单个服务器上运行单个应用程序或在负载平衡的 Web 农场上运行企业范围的应用程序时都能完美执行。

## **价格**

当应用程序使用 Microsoft Office 自动化时，必须为运行该应用程序的每台计算机购买 Microsoft Office 的副本。许多时候，应用程序可能需要创建或操纵 Office 文件，但不需要用户拥有 Office。Aspose 提供了一种非常[具有成本效益的](https://purchase.aspose.com/buy)，免版税的重新分发许可证，允许向无限数量的用户部署，无须担心许可问题。

创建基于 Web 的应用程序时，重要的是要知道，Microsoft Office 自动化组件无法用于服务器端解决方案，因此没有用于部署使用 Microsoft Office 组件的 Web 应用程序的良好许可解决方案。Aspose 也为基于服务器的应用程序提供了一个非常具有成本效益的解决方案。

## **功能**

Aspose 组件提供管理 Office 文件所需的一切，以及更多。它们的设计理念是允许开发人员以最少的工作量实现最大的结果。与 Office 自动化不同，Aspose 组件提供许多强大而节省时间的功能。例如，[Aspose.Cells](https://products.aspose.com/cells/java/) 提供了直接将 **DataTable** 或 **DataView** 导出到 Excel 文件的功能。[Aspose 家族](https://products.aspose.com/total/)中的每个组件都提供其独特而强大的功能。

购买 Aspose 组件或组件套件最好的部分是可以使用我们的开发团队。我们的开发团队意识到，如果您的公司需要某种功能，很可能其他公司也需要。尽管不能添加每个功能请求，但我们的团队在提供帮助时会非常开放心态和灵活。这种心态帮助 Aspose 组件变得如此强大。如果您需要 Office 自动化对象的其他功能，那么它们被添加的可能性是非常低的。

## **结论**

{{% alert color="primary" %}}

本文涵盖了为什么 Aspose 组件是比 Office 自动化更好的选择的关键要点。所有不同的 Aspose 组件都提供了无风险、无义务的[评估版本](https://products.aspose.com/total/)。我们鼓励您利用该评估版本，以更好地了解 Aspose 对您的应用程序可以做些什么。

更多信息，请参阅以下 Internet 文章：

- [考虑服务器端自动化 Office 的因素](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
