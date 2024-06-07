---
title: 为何不自动化
type: docs
weight: 20
url: /zh/java/why-not-automation/
---

{{% alert color="primary" %}}

为什么Aspose组件比Microsoft Office自动化更好的选项？*

在Aspose，我们经常听到两个最常见的问题：

1. **您的产品是否需要安装Microsoft Office才能运行？** 
   简单的答案是否定的。 Aspose组件是完全独立的，与Microsoft Corporation无关，未经授权，赞助或以其他方式获得批准。
1. **我们为什么应该使用Aspose产品而非利用Microsoft Office自动化？**
   我们能给出的最简短答案是有很多原因，主要原因是微软强烈建议不要从软件解决方案进行Office自动化: [Office服务器端自动化注意事项](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)。

Aspose组件比自动化更好的替代方案有几个原因。一些关键原因包括:

- [安全性](/cells/zh/java/why-not-automation/#security)
- [稳定性](/cells/zh/java/why-not-automation/#security)
- [可扩展性/速度](/cells/zh/java/why-not-automation/#security)
- [价格](/cells/zh/java/why-not-automation/#security)
- [功能](/cells/zh/java/why-not-automation/#security)

关键点如下。此外，确保查看本节末尾的链接。

{{% /alert %}}

## **安全性**

以下是上述Microsoft文章的直接引用：*"办公应用程序从未打算用于服务器端使用，因此不考虑分布式组件面临的安全问题。Office不会对传入请求进行身份验证，并且不会保护您免受意外运行宏或从您服务器端代码启动可能运行宏的另一个服务器造成的危害。不要打开从匿名Web上传到服务器的文件！基于上次设置的安全设置，服务器可以在管理员或系统上下文中以完全特权运行宏并危及您的网络！此外，Office使用许多客户端组件（如Simple MAPI、WinInet和MSDAIPP），可以缓存客户端身份验证信息以加快处理速度。如果Office在服务器端自动化，一个实例可能为多个客户端提供服务，由于身份验证信息已为该会话缓存，因此可能一个客户端可以使用另一个客户端的缓存凭据并通过冒充其他用户获得未授予的访问权限。*"

Aspose产品非常安全。Aspose组件与所有ASP.NET应用程序一样在相同的用户环境中运行，即在ASPNET用户下。因此，Aspose组件不会对重要的系统资源构成潜在风险。此外，在Aspose组件打开文档时，不会自动运行宏。Aspose组件的目标是允许开发人员创建、操纵和保存Office文件。与Microsoft Office套件相关的风险对Aspose组件来说并不固有。

## **稳定性**

以下是上述Microsoft文章的直接引用：*"Office 2000、Office XP和Office 2003使用Microsoft Windows Installer (MSI) 技术，使安装和自我修复对最终用户更加便捷。MSI引入了"首次使用时安装"的概念，允许在运行时（对于系统，或者更常见的是对于特定用户）动态安装或配置功能。在服务器端环境中，这既降低了性能，又增加了出现对用户批准安装或提供适当安装磁盘的提示框的可能性。虽然它旨在增加Office作为最终用户产品的韧性，但Office对MSI能力的实现在服务器端环境是适得其反的。此外，总的来看，Office的稳定性在服务器端不能得到保证，因为它没有为这种使用方式而设计或测试。在网络服务器上将Office作为服务组件进行自动化可能会降低该计算机的稳定性，也因此可能影响您整个网络。如果您计划在服务器端自动化Office，尝试将该程序隔离到一个专用计算机上，该计算机不会影响关键功能，并且可以根据需要重新启动。*"

由于Aspose组件打包到单个DLL中，因此永远不需要安装任何额外的部件或部件来使其运行。Aspose组件仅由.NET应用程序使用，并且组件代码中没有设计等待人类响应的部分。Aspose组件经过了彻底测试。IBM、希尔顿、读者文摘、美国银行等公司都在使用Aspose组件。

## **可扩展性/速度**

以下是上述Microsoft文章的直接引用：*"服务器端组件需要是高度可重入的、多线程的COM组件，具有最小的开销和高吞吐量，以满足多客户端的需要。Office应用程序在几乎所有方面都是完全相反的。它们是非可重入的、基于STA的自动化服务器，旨在为单个客户端提供多样但资源密集的功能。它们提供了很少对于服务器端解决方案的可伸缩性，并且重要元素（如内存）的上限是固定的，这些上限无法通过配置进行更改。更重要的是，它们使用全局资源（如内存映射文件、全局加载项或模板，以及共享的自动化服务器），这些资源可以限制可以同时运行的实例数量，并且如果在多客户端环境中配置这些资源，可能导致竞态条件。计划同时运行一个Office应用程序的多个实例的开发人员需要考虑"池化"或串行化对Office应用程序的访问，以避免潜在的死锁或数据损坏。*"

Aspose组件具有高度的可扩展性和极快的速度。Office应用程序并非设计用于同时由数百到数千用户使用; 但是，Aspose组件正是为此而设计的。我们的组件是真正的.NET解决方案，在为单个应用程序提供动力的单个服务器或在为整个企业应用程序提供动力的负载平衡的Web服务器上都能完美运行。

## **价格**

当应用程序使用 Microsoft Office 自动化时，必须为运行该应用程序的每台机器购买一份 Microsoft Office。有许多情况下，应用程序可能需要创建或操作 Office 文件，但不要求用户拥有 Office。Aspose提供非常具有成本效益的，免版税的，无需担心许可问题的重新分发许可，将允许部署到无限数量的用户。

在创建基于Web的应用程序时，重要的是要知道Microsoft Office自动化组件不是针对服务器端解决方案进行定价或许可；因此，对于部署利用Microsoft Office组件的Web应用程序，没有好的许可解决方案。Aspose为服务器端应用程序提供了一个非常经济实惠的解决方案。

## **功能**

Aspose组件提供了管理Office文件所需的一切，以及更多。它们设计的理念是允许开发人员用最少的工作量获得最大的结果。与Office自动化不同，Aspose组件提供了许多强大、节省时间的功能。例如，[Aspose.Cells](https://products.aspose.com/cells/java/)提供了开发人员直接将**DataTable**或**DataView**导出到Excel文件的能力。[Aspose家族中的每个组件](https://products.aspose.com/total/)都提供其自己独特而强大的功能。

购买 Aspose 组件或组件套件的最大优点是可以获得我们的开发团队支持。我们的开发团队意识到，如果您的公司需要某个功能，很可能其他公司也需要该功能。虽然不能添加每个功能请求，但我们的团队在提供帮助时会尽量开放和灵活。这种思维方式帮助 Aspose 组件成为它们目前所具备的强大功能。如果您对 Office 自动化对象需要其他功能，那么这些功能被添加的可能性非常低。

## **结论**

{{% alert color="primary" %}}

本文介绍了Aspose组件为何比Office自动化更好的关键点。所有不同的Aspose组件都提供了一个无风险、无义务的[评估版本](https://products.aspose.com/total/)。我们鼓励您利用该评估，以更好地了解Aspose可以为您的应用程序做些什么。

更多信息，请参阅以下网络文章：

- [Office服务器端自动化注意事项](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
