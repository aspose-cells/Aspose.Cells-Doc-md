---
title: 将VSTO与Aspose.Cells for .NET进行比较
type: docs
weight: 20
url: /zh/net/comparing-vsto-with-aspose-cells-for-net/
---

{{% alert color="primary" %}}

本文将使用VSTO（Visual Studio Tools for Office）与其他开发Microsoft Office解决方案的方法进行比较。特别是，它研究了Aspose.Cells，并对这两种解决方案的工作方式进行了比较。本文提供了开发人员可以用来分析、比较和评估不同选项的信息，在采用解决方案之前。

{{% /alert %}}

## **概览**

Microsoft Excel被企业和个人广泛使用在各种行业。这款电子表格应用程序几乎无处不在，不仅可以存储和组织数据，还可以使用公式构建复杂模型，并通过高级格式和图表清晰地呈现数据。

VSTO允许Microsoft Office文档执行包装在.NET程序集中的代码。它用于开发与Microsoft Office文件和功能一起工作的应用程序。开发人员多年来一直在应用程序中使用ASP、Office Web组件和COM互操作性。微软已经增强了VSTO，以便更易于开发和部署应用程序，并改进内存管理。但问题依然存在：VSTO是否设计得比今天其他可用的方法更易于使用和更可靠？开发人员希望使用不会在性能改进、安全性、可扩展性、稳定性、可靠性或功能方面让他们失望的解决方案。

[Aspose]（http://www.aspose.com/）提供了一系列优秀的.NET、Java、云和Android API。Aspose APIs 包括Aspose.Cells、Aspose.Words、Aspose.Pdf和Aspose.Slides等产品，可以帮助开发人员打开、修改、生成、保存、合并和转换各种格式的文档，包括XLS、XLSX、DOC、DOCX、HTML、PDF、PPT。

本文中，我们比较VSTO与Aspose.Cells for .NET。

[Aspose.Cells]（https://products.aspose.com/cells/net/）是一个独立的Microsoft Excel电子表格操作API，可以在客户端或服务器端不安装Microsoft Excel的情况下读取和编写Microsoft Excel电子表格。Aspose.Cells是功能丰富的组件，不仅提供基本数据导出，还可以导出数据、格式化电子表格、导入图像、创建和操作图表、流式传输Excel数据，并保存为各种格式。要了解更多关于产品及其特性的信息：

- 查看[Aspose.Cells文档](https://docs.aspose.com/cells/net/)。
- 在[在线演示中查看它的运作方式](https://github.com/aspose-cells/Aspose.Cells-for-.NET)。
- 试用一下：[下载](https://downloads.aspose.com/cells/net)免费试用版本。

本文比较了VSTO和Aspose.Cells在与Microsoft Excel相关的不同方面。列表并不完整，但它代表了决策者在采用方法之前必须了解的一些问题。

### **.NET框架要求**

VSTO需要在客户端上执行最终应用程序的.NET框架（包括Visual Studio Tools for Office SE Runtime）。在大多数企业环境中，特别是在Web场景中，最终用户无法安装应用程序软件和相关的运行时框架。这一要求独自就使基于VSTO的应用程序变得棘手。它实际上淘汰了基于VSTO的现成应用程序。

与之相反，Aspose.Cells for .NET不一定要求客户端上有.NET框架用于底层场景。使用该组件构建的Office应用程序是轻量级的，并保证在Microsoft Windows系统下承受重载条件下工作。

### **功能**

VSTO提供的功能取决于您安装了哪些组合的VSTO和Visual Studio产品。VSTO为Microsoft Office Excel 2003执行的常见任务包括向单元格添加数据、创建、打开和保存工作簿、添加、移动和隐藏工作表、保护工作表、命名范围、列表对象、样式格式化、在单元格中搜索文本、对数据进行排序、打印和Excel公式计算。

Aspose.Cells提供了管理Microsoft Office Excel文件所需的一切，还包括更多功能。该API可以让开发人员以最少的努力获得出色的结果。Aspose.Cells提供许多强大、节省时间的功能。API为各种类型的电子表格管理活动提供了易于使用的API，几乎涵盖了Microsoft Excel提供的所有功能。VSTO列出的所有任务都可以轻松地由Aspose.Cells执行。

Aspose.Cells还支持几个高级功能，包括支持智能标记、将数据导入导出到多个数据来源、对象和Excel文件，与组件的COM客户端（ASP客户端）互操作性、将Excel文件转换为PDF格式、将Excel图表和工作表保存为图像文件。

### **安全性**

默认情况下，VSTO应用程序需要完全信任权限才能执行，因为它不允许部分信任的调用方。为了锁定一个Web应用程序并在托管环境中提供额外的应用程序隔离级别，您可以使用代码访问安全性来限制应用程序可以访问的资源和可以执行的特权操作。但需要投入一些时间和精力来了解.NET安全性。

托管多个来自许多不同公司的应用程序的互联网服务提供商（ISP）通常使用中等信任级别来确保应用程序无法阅读彼此的数据或干扰彼此。出于安全原因，ISP可能会将共享服务器上的单个Web应用程序限制为部分信任。

Aspose.Cells for .NET可以在中等信任安全级别下运行。在托管环境中不需要特殊权限来运行该程序集。中等信任对应用程序可以访问的共享系统资源施加了限制。许多Web应用程序正在Web托管服务器上运行。在Web托管模式下，大多数应用程序只能在中等信任安全级别下运行。Aspose.Cells for .NET在这方面可以很好地满足它们的需求。

### **性能**

性能是选择任何方法或方法来构建解决方案时的最关键因素。

据一些用户报告，VSTO应用程序的性能依赖VBA和COM方法。有几个因素会影响VSTO的性能，重要的是要正确看待这些因素。

- .NET启动成本固有地昂贵。使用.NET编写的应用程序必须承担即时（JIT）编译的开销，因此无法避免即时编译。
- 影响基于VSTO的应用程序的另一个性能因素与调用厚重的自动化外观层有关，这些外观层包装了Microsoft Office COM对象。与.NET相比，为与Microsoft Office交互而构建和优化的VBA要经过较短的距离。
- 最后，在Visual Studio IDE中承载Excel对象在资源方面是昂贵的。VSTO应用程序比VBA应用程序占用更多的内存。VSTO Excel应用程序使用大量内存，并且直到所有Microsoft Excel实例都关闭之前，才能将其释放回操作系统。

如果您正在考虑将VSTO作为Microsoft Office技术开发平台，花一些时间研究资源，以熟悉这些属性。

此外，总是检查更新的性能影响可能不适合解决方案（部署服务器速度较慢，网络连接速度较慢或无法频繁访问服务器可能对加载时间产生负面影响）。

相比之下，Aspose.Cells for .NET 高度可扩展、灵活且快速。一般来说，办公应用程序并不是为数百或数千用户同时使用而设计的；然而，Aspose.Cells 可以胜任。该 API 稳定可靠，在单个服务器上运行、供单个应用程序使用或在负载平衡的 Web 农场上运行时都能完美执行电子表格任务。

### **系统要求**

分析这两种方法的系统要求，我们发现 VSTO 更昂贵，需要更多的基本要素。

VSTO有一长串的先决条件：

- **受支持的操作系统**：Windows 2000；Windows Server 2003；Windows Vista；Windows XP
- **.NET Framework 版本支持**：仅支持 .NET Framework 2.0 或更高版本
- 下列 Visual Studio 工具版本之一：
  - Microsoft Visual Studio 2005 用于 Microsoft Office 系统的工具
  - 适用于 2007 Microsoft Office 系统的 Microsoft Visual Studio 2005 工具
  - Visual Studio 2008 专业版
  - Visual Studio 2008 团队套件版
  - 一个版本的 Microsoft Office：
  - Microsoft Office Professional 2003 SP1
  - 2007 Microsoft Office 系统

Aspose.Cells 无需在客户端或服务器上安装 Microsoft Excel，因为它是一款电子表格创建引擎。但是，要查看 Microsoft Excel 文档，您至少需要在系统上安装 Microsoft Excel Viewer。

- **受支持的操作系统**：Windows 2000；Windows Server 2003；Windows Vista；Windows XP
- **.NET Framework 版本支持**：支持所有 .NET Framework 版本，1.0、1.1、2.0、3.x 等

### **安装和部署**

安装 VSTO 可能是一项庞大且烦琐的任务。有时，安装要求您手动重新安装工具的某些部分，并手动注册它们。这可能会变得复杂。

另一方面，Aspose.Cells for .NET 打包成一个单独的 DLL，因此无需安装额外的应用程序。该组件仅由 .NET 应用程序使用，组件代码中的任何部分都不是设计等待人类响应的。只需访问 Aspose.Cells [下载页面](https://downloads.aspose.com/cells/net)，下载最新的 Aspose.Cells 安装程序。运行下载的文件并按照安装程序的说明进行操作。然后，在项目中引用该组件即可使用。

## **示例任务**

为了展示这两种方法之间的差异，下面的代码演示了如何使用 VSTO 和 Aspose.Cells API 填充一个模板文件的数据。

1. 使用一个 Microsoft Excel 文件（TempBook.xls）作为模板。
   工作簿中包含几个工作表，并在其中填写了一些数据。
1. 示例代码在模板 Excel 文件的第一个工作表中放置 1000*20 条记录。
   工作表填充了常量（虚拟）数据到单元格中。

此任务在装有 Intel(R) Celeron(R) CPU 2.40 GHz、760 MB RAM 的 Microsoft Windows XP 专业版操作系统上执行。

下面的代码片段示例了如何使用每个 API 执行这些任务。

### **VSTO 代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-VSTOCode-1.cs" >}}

### **Aspose.Cells 代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-UsingAsposeCells-1.cs" >}}

### **结果**

结果显示，使用VSTO API完成任务大约需要2.5分钟（约超过150秒），而Aspose.Cells在普通硬件和正常系统配置下只需不到1秒。

如果循环扩展到填充10,000*20个单元格，则Aspose.Cells需要约5.5秒来完成任务。

## **结论**

如果考虑在业务解决方案中使用Microsoft Office技术，请首先熟悉可用的替代方案。基于不同产品执行一些测试，并暴露它们于各种真实世界条件，如负载和压力下的表现。

Aspose.Cells是一个稳定且成熟的产品，在全球拥有广泛的客户群，并能够在重负载下表现良好。

VSTO的性能尚未完善。这些性能问题很可能与.NET JIT编译过程有关，而不是与VSTO本身有关。但是，仍然存在某些疑虑，即VSTO应用程序是否在负载增加时会自动扩展。最新的VSTO模型不需要Excel驻留在Web服务器上进行文档处理，但我认为VSTO还有很长的路要走才能产生真正的影响。
