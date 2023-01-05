---
title: 比较VSTO与Aspose.Cells for .NET
type: docs
weight: 20
url: /zh/net/comparing-vsto-with-aspose-cells-for-net/
---
{{% alert color="primary" %}}

本文比较了使用 VSTO（Office 的 Visual Studio 工具）和其他方法来开发基于 Microsoft Office 的解决方案。特别是，它查看了 Aspose.Cells 并提供了两种解决方案工作方式的比较。这些文章为开发人员提供了在采用解决方案之前可以用来分析、比较和评估不同选项的信息。

{{% /alert %}}

## **概述**

Microsoft Excel被各行各业的企业和个人广泛使用。电子表格应用程序几乎无处不在，它不仅允许用户存储和组织数据，还可以使用公式构建复杂的模型，并使用高级格式和图表清晰地呈现数据。

VSTO 允许 Microsoft Office 文档执行包装在 .NET 程序集中的代码。它用于开发使用 Microsoft Office 文件和功能的应用程序。开发人员多年来一直在应用程序中使用 ASP、Office Web 组件和 COM 互操作。 Microsoft 增强了 VSTO 以开发和部署应用程序并改进内存管理。但是，问题仍然存在：VSTO 是否设计为比当今可用的其他方法更易于使用和更可靠？开发人员希望使用在改进的性能、安全性、可扩展性、稳定性、可靠性或功能方面不会让他们失望的解决方案。

[Aspose](http://www.aspose.com/)提供了一系列 .NET、Java、Cloud 和 Android API。 Aspose API包括Aspose.Cells、Aspose.Words、Aspose.Pdf、Aspose.Slides等产品，API帮助[开发人员打开、修改、生成、保存、合并和转换各种格式的文档，包括XLS、XLSX、DOC、DOCX、HTML、PDF、PPT。

在本文中，我们将 VSTO 与 Aspose.Cells for .NET 进行比较。

[Aspose.Cells]](https://products.aspose.com/cells/net/)是一个独立的 Microsoft Excel 电子表格操作 API 读写 Microsoft Excel 电子表格，无需在客户端或服务器端安装 Microsoft Excel。 Aspose.Cells 是功能丰富的组件，提供的不仅仅是基本数据导出。借助 Aspose.Cells，开发人员可以导出数据、格式化电子表格、导入图像、导入创建和操作图表、流式传输 Excel 数据以及保存为各种格式。要了解有关产品及其功能的更多信息：

- 查看[Aspose.Cells 文档](https://docs.aspose.com/cells/net/).
- 看看它是如何工作的[在线演示](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
- 试试看：[下载](https://downloads.aspose.com/cells/net)免费的评估版。

本文在与 Microsoft Excel 相关的不同方面对 VSTO 和 Aspose.Cells 进行了比较。该列表并不完整，但它代表了决策者在采用某种方法之前做出最终决定之前必须了解的一些问题。

### **.NET 框架要求**

VSTO 需要客户端的 .NET Framework（包括 Visual Studio Tools for Office SE Runtime）来执行最终的应用程序。在大多数企业环境中，尤其是在 Web 场景中，最终用户无法安装应用软件和相关的运行时框架。仅这一要求就会使基于 VSTO 的应用程序出现问题。它实际上排除了基于 VSTO 的现成应用程序。

相反，Aspose.Cells for .NET 底层场景不一定需要客户端的.NET Framework。使用该组件构建的 Office 应用程序是轻量级的，并且保证在 Microsoft Windows 系统上运行在高负载下。

### **特征**

VSTO 提供的功能取决于你安装的 VSTO 和 Visual Studio 产品的组合。 VSTO 为 Microsoft Office Excel 2003 执行的常见任务包括向 Cells 添加数据、创建、打开和保存工作簿、添加、移动和隐藏工作表、保护工作表、命名范围、列表对象、样式格式化、在单元格中搜索文本、排序数据、打印和Excel公式计算。

Aspose.Cells 提供了管理 Microsoft Office Excel 文件所需的一切，还有很多很多。 API 以最少的工作量为开发人员提供了出色的结果。 Aspose.Cells 提供了许多强大、省时的功能。 API 为所有类型的电子表格管理活动提供易于使用的 API，几乎涵盖了 Microsoft Excel 提供的所有功能。为 VSTO 列出的所有任务都可以通过 Aspose.Cells 轻松执行。

Aspose.Cells 还支持几个高级功能，包括支持智能标记，从多个数据源、对象和 Excel 文件导入和导出数据，支持 COM 客户端（ASP 客户端）与组件的互操作性，将 Excel 文件转换为 PDF 格式，将 Excel 图表和工作表保存为图像文件。

### **安全**

默认情况下，VSTO 应用程序需要完全信任权限才能执行，因为它不允许部分信任的调用方。要锁定 Web 应用程序并在托管环境中提供额外级别的应用程序隔离，您可以使用代码访问安全性来限制应用程序可以访问的资源和它可以执行的特权操作。但是您需要投入一些时间和精力来了解 .NET 安全性。

托管来自许多不同公司的多个应用程序的 Internet 服务提供商 (ISP) 经常使用中等信任级别来帮助确保应用程序无法读取彼此的数据或相互干扰。出于安全原因，ISP 可能会将共享服务器上的单个 Web 应用程序限制为部分信任。

Aspose.Cells for .NET 可以在中信任安全级别下运行。在托管环境中运行程序集不需要特殊权限。中等信任对应用程序可以访问的共享系统资源的类型进行限制。许多 Web 应用程序都在 Web 托管服务器中运行。在虚拟主机模式下，它们中的大多数只能在中等信任安全级别下运行。 Aspose.Cells for .NET 在这方面可以很好地满足他们的需求。

### **表现**

在选择任何方法来构建解决方案时，性能是最关键的因素。

根据一些用户的报告，VSTO 应用程序的性能依赖于 VBA 和 COM 方法。影响 VSTO 性能的因素有很多，正确看待这些因素很重要。

- .NET 的启动成本本来就很昂贵。用 .NET 编写的应用程序必须承担 Just-In-Time (JIT) 编译的开销，因此无法避免 JIT 编译。
- 影响基于 VSTO 的应用程序的另一个性能因素与通过包装 Microsoft Office COM 对象的厚厚的自动化皮肤层进行调用的费用有关。为与 Microsoft Office 交互而构建和优化的 VBA，比 .NET 的移动距离更短。
- 最后，在 Visual Studio IDE 中托管 Excel 对象在资源方面非常昂贵。 VSTO 应用程序比 VBA 应用程序占用更大的内存。 VSTO Excel 应用程序使用大量内存，在关闭 Microsoft Excel 的所有实例之前，永远不会将其释放回操作系统。

如果您正在考虑采用 VSTO 作为 Microsoft Office 技术的开发平台，请花一些时间查看资源以熟悉这些属性。

此外，始终检查更新对性能的影响可能不适合该解决方案（较慢的部署服务器、较慢的网络连接或无法频繁访问服务器会对加载时间产生负面影响）。

相比之下，Aspose.Cells for .NET 可扩展性强，灵活且快速。通常，Office 应用程序的设计目的不是让 100 和 1000 名用户同时使用；但是，Aspose.Cells 是。 API 稳定并且可以完美地执行电子表格任务，无论是在为单个应用程序提供支持的单个服务器上，还是在为企业范围的应用程序提供支持的负载平衡网络场上。

### **系统要求**

分析这两种方法的系统要求，我们发现 VSTO 更昂贵并且需要更多的要素。

VSTO 有一长串先决条件：

- **支持的操作系统**: Windows 2000; Windows 服务器 2003； Windows 远景； Windows 经验值
- **.NET 支持的框架版本**只有 .NET 框架 2.0 或更高版本。
- 以下一个或多个版本的 Visual Studio Tools for Office：
 - Microsoft 用于 Microsoft 办公系统的 Visual Studio 2005 工具
 Microsoft Visual Studio 2005 Tools for the 2007 Microsoft Office System
 - Visual Studio 2008 专业版
 Visual Studio 2008 团队套件版
 Microsoft Office 一个版本：
 - Microsoft Office 专业版 2003 SP1
 - 2007 Microsoft 办公系统

Aspose.Cells 不需要在客户端或服务器上安装 Microsoft Excel，因为它是一个电子表格创建引擎。但是，要查看 Microsoft Excel 文档，您至少需要在系统上安装 Microsoft Excel Viewer。

- **支持的操作系统**: Windows 2000; Windows 服务器 2003； Windows 远景； Windows 经验值
- **.NET 支持的框架版本**: 支持所有 .NET 框架，1.0、1.1、2.0、3.x 等。

### **安装部署**

安装 VSTO 可能是一项艰巨而麻烦的任务。有时，安装要求您手动重新安装工具的某些方面，并手动注册它们。它会变得复杂。

另一方面，Aspose.Cells for .NET 被打包到单个 DLL 中，因此无需安装额外的应用程序。该组件仅由 .NET 应用程序使用，组件代码的任何部分均未设计为等待人工响应。只需访问 Aspose.Cells[下载页面](https://downloads.aspose.com/cells/net)并下载最新的 Aspose.Cells 安装程序。运行下载的文件并按照安装程序说明进行操作。然后，要使用该组件，请在您的项目中引用它。

## **示例任务**

为了显示这两种方法之间的区别，下面的代码显示了如何使用 VSTO 和 Aspose.Cells API 来用数据填充模板文件。

1. Microsoft Excel 文件 (TempBook.xls) 用作模板。
该工作簿包含一些工作表，其中一些单元格填充了数据。
1. 示例代码将 1000*20 条记录放在模板 Excel 文件的第一个工作表上。
工作表的单元格中填充了常量（虚拟）数据。

该任务在具有 Intel(R) Celeron(R) CPU 2.40 GHz、760 MB RAM、Microsoft Windows XP Professional 操作系统的系统上执行。

下面的代码段说明了如何对每个 API 执行这些任务。

### **VSTO代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-VSTOCode-1.cs" >}}

### **Aspose.Cells 代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-UsingAsposeCells-1.cs" >}}

### **结果**

结果显示，使用 VSTO API 完成任务大约需要 2.5 分钟（大约超过 150 秒），而 Aspose.Cells 在具有正常系统配置的普通硬件上使用不到 1 秒。

如果延长循环，比如填充 10,000*20 个单元格，Aspose.Cells 大约需要 5.5 秒来完成这项工作。

## **结论**

如果您正在考虑在业务解决方案中使用 Microsoft Office 技术，请首先熟悉可用的替代方案。基于不同的产品执行一些测试，并将它们暴露在各种真实世界条件下，例如负载和压力，以查看它们的性能。

Aspose.Cells 是一款稳定成熟的产品，拥有全球客户群，可扩展性足以在重负载下表现良好。

VSTO 的性能还没有完善。很可能其中一些性能问题与 VSTO 本身无关，而是与 .NET JIT 编译过程有关。但是，仍然存在一些疑问，即 VSTO 应用程序是否会随着负载的增加而自行扩展。较新的 VSTO 模型不需要将 Excel 驻留在 Web 服务器上进行文档处理，但我认为 VSTO 要产生真正的影响还有很长的路要走。
