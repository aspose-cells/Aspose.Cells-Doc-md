---
title: 比较VSTO与Aspose.Cells for .NET
type: docs
weight: 20
url: /zh/net/comparing-vsto-with-aspose-cells-for-net/
---

{{% alert color="primary" %}}

本文比较使用VSTO（Visual Studio Tools for Office）与其他方法来开发基于Microsoft Office的解决方案。特别是，它研究了Aspose.Cells，并提供了这两种解决方案如何运作的比较。本文提供了开发人员可以用来分析、比较和评估不同选项的信息，然后再选择解决方案。

{{% /alert %}}

## **概述**

Microsoft Excel被各种行业的企业和个人广泛使用。这款电子表格应用几乎无处不在，它不仅允许用户存储和组织数据，还可以使用公式构建复杂的模型，并通过高级格式和图表清晰地呈现数据。

VSTO允许Microsoft Office文档执行.NET程序集中的代码。它用于开发与Microsoft Office文件和功能一起工作的应用程序。开发人员多年来在应用程序中使用ASP、Office Web组件和COM互操作。Microsoft已经增强了VSTO，以便开发和部署应用程序，并改进内存管理。但是问题仍然存在：VSTO是否被设计为比当今其他可用方法更易于使用和更可靠？开发人员希望使用不会让他们失望的解决方案，改进性能、安全性、可扩展性、稳定性、可靠性或功能。

[Aspose](http://www.aspose.com/)提供了一系列优秀的.NET、Java、云和Android API。Aspose的API包括Aspose.Cells、Aspose.Words、Aspose.Pdf和Aspose.Slides等产品，这些API帮助开发人员打开、修改、生成、保存、合并和转换各种格式的文档，包括XLS、XLSX、DOC、DOCX、HTML、PDF、PPT。

在本文中，我们将VSTO与Aspose.Cells for .NET进行了比较。

[Aspose.Cells](https://products.aspose.com/cells/net/)是一个独立的Microsoft Excel电子表格处理API，可在客户端或服务器中安装Microsoft Excel的情况下读取和写入Microsoft Excel电子表格。Aspose.Cells是功能丰富的组件，不仅提供基本的数据导出，还能够导出数据、格式化电子表格、导入图片、创建和操纵图表、流式传输Excel数据，以及保存到各种格式。要了解产品及其功能的更多信息：

-查看[Aspose.Cells文档](https://docs.aspose.com/cells/net/)。
-在[在线演示](https://github.com/aspose-cells/Aspose.Cells-for-.NET)中查看其工作原理。
-尝试：[免费下载](https://downloads.aspose.com/cells/net)评估版本。

本文比较了VSTO和Aspose.Cells在与Microsoft Excel相关的不同方面。这个列表并不完整，但它代表了决策者在采用方法之前必须了解的一些问题。

### **.NET Framework要求**

VSTO在客户端侧要求.NET Framework（包括Visual Studio Tools for Office SE运行时）来执行最终应用程序。在大多数企业环境中，特别是在Web场景中，最终用户无法安装应用软件和相关的运行时框架。这一要求单独就使基于VSTO的应用程序变得棘手。它实际上排除了基于VSTO的现成应用程序。

相反，对于底层场景，Aspose.Cells for .NET并不一定需要在客户端使用.NET Framework。使用该组件构建的Office应用程序是轻量级的，并且保证能够在Microsoft Windows系统上以重大负载稳定运行。

### **功能**

VSTO提供的功能取决于您安装了哪种组合的VSTO和Visual Studio产品。VSTO执行Microsoft Office Excel 2003的常见任务包括向单元格添加数据、创建、打开和保存工作簿、添加、移动和隐藏工作表、保护工作表、命名范围、列表对象、样式格式设置、在单元格中搜索文本、排序数据、打印和Excel公式计算。

Aspose.Cells提供了管理Microsoft Office Excel文件所需的一切，而且更多。该API为开发人员提供了最少的努力获得最佳成果。Aspose.Cells提供了许多强大且节省时间的功能。API为几乎所有类型的电子表格管理活动提供了易于使用的API，几乎包括Microsoft Excel提供的所有功能。VSTO列出的所有任务都可以轻松地由Aspose.Cells执行。

Aspose.Cells还支持几个高级功能，包括支持智能标记、将数据导入导出到多个数据源、对象和Excel文件、与组件的COM客户端（ASP客户端）互操作性、将Excel文件转换为PDF格式、将Excel图表和工作表保存为图像文件。

### **安全性**

默认情况下，VSTO应用程序需要完全信任权限才能执行，因为它不允许部分信任的调用者。为了锁定Web应用程序并在托管环境中提供额外的应用程序隔离级别，您可以使用代码访问安全性来限制应用程序能够访问的资源和其可以执行的特权操作。但是，您需要投入一些时间和精力来了解.NET安全性。

主机多家公司的多个应用程序的网络服务提供商（ISPs）通常使用中等信任级别，以确保应用程序不能读取彼此的数据或干扰彼此。出于安全原因，ISP 可能会限制共享服务器上的单个 Web 应用程序的部分信任。

Aspose.Cells for .NET可以在中等信任安全级别下运行。在托管环境中运行程序时无需特殊权限。中等信任会限制应用程序访问共享系统资源的类型。许多Web应用程序正在Web托管服务器上运行。在Web托管模式下，大多数应用程序只能在中等信任安全级别下运行。Aspose.Cells for .NET适应了他们在这方面的需求。

### **性能**

性能是选择任何方法或构建解决方案时最关键的因素。

根据某些用户的报告，VSTO 应用程序的性能倒退到了 VBA 和 COM 方法。有一些因素影响了 VSTO 的性能，重要的是要正确看待这些因素。

- .NET 启动成本固有地昂贵。使用 .NET 编写的应用程序必须承担即时（JIT）编译的开销，因此无法避免 JIT 编译。
- 影响基于 VSTO 的应用程序的另一个性能因素与调用包装 Microsoft Office COM 对象的厚层自动化皮肤的开销有关。与 .NET 相比，专为与 Microsoft Office 交互而构建和优化的 VBA 路程较短。
- 最后，在 Visual Studio IDE 中托管 Excel 对象在资源方面成本很高。VSTO 应用程序的内存占用比 VBA 应用程序更大。VSTO Excel 应用程序占用大量内存，并且在关闭所有 Microsoft Excel 实例之前不会将其释放回操作系统。

如果您考虑采用 VSTO 作为 Microsoft Office 技术的开发平台，请花些时间研究资源，以了解这些属性。

此外，始终检查更新的性能影响可能不适合该解决方案（较慢的部署服务器、较慢的网络连接或干脆无法频繁连接到服务器可能会对加载时间产生负面影响）。

相比之下，Aspose.Cells for .NET具有高度的可伸缩性、灵活性和快速性。一般来说，Office应用程序并不是为100多或1000多用户同时使用而设计的；然而，Aspose.Cells是。该API很稳定，并且能够在单个服务器上运行并为单个应用程序提供支持，也能在负载平衡的Web服务器集群上提供支持，为企业级的应用程序提供支持。

### **系统要求**

分析这两种方法的系统要求，我们发现 VSTO 更昂贵并且需要更多的基本条件。

VSTO 需要满足一长串的先决条件：

- **支持的操作系统**: Windows 2000; Windows Server 2003; Windows Vista; Windows XP
- **支持的 .NET Framework 版本**：仅 .NET Framework 2.0 或更高版本。
- 下列一项或多项 Visual Studio Tools for Office 版本：
  - Microsoft Visual Studio 2005 Tools for the Microsoft Office System
  - Microsoft Visual Studio 2005 Tools for the 2007 Microsoft Office System
  - Visual Studio 2008 专业版
  - Visual Studio 2008 团队套件版
  - Microsoft Office的一个版本:
  - Microsoft Office专业版2003 SP1
  - 2007 Microsoft Office系统

Aspose.Cells不需要客户端或服务器上安装Microsoft Excel，因为它是一个电子表格创建引擎。但是，要查看Microsoft Excel文档，您需要至少在系统上安装Microsoft Excel查看器。

- **支持的操作系统**: Windows 2000; Windows Server 2003; Windows Vista; Windows XP
- **支持的.NET Framework版本**: 支持所有.NET Framework版本，1.0, 1.1, 2.0, 3.x等。

### **安装和部署**

安装VSTO可能是一个繁琐而麻烦的任务。有时，安装需要手动重新安装工具的某些部分，并且也需要手动注册它们。这可能会变得复杂。

另一方面，Aspose.Cells for .NET被打包到单个DLL中，因此无需安装其他应用程序。该组件仅被.NET应用程序使用，组件代码的任何部分都不是设计等待人类响应的。只需访问Aspose.Cells的[下载页面](https://downloads.aspose.com/cells/net)，然后下载最新的Aspose.Cells安装程序。运行下载的文件，按照安装程序的说明进行操作。然后，在项目中引用该组件即可。

## **示例任务**

为了展示这两种方法的不同之处，以下代码展示了如何使用VSTO和Aspose.Cells API来填充模板文件的数据。

1. 一个Microsoft Excel文件（TempBook.xls）被用作模板。
   工作簿包含一些填充有数据的工作表。
1. 例子中的代码将1000*20条记录放在模板Excel文件的第一个工作表中。
   工作表中的单元格被填充有常量（虚拟）数据。

该任务在一个使用Intel(R) Celeron(R) CPU 2.40 GHz、760 MB RAM的Microsoft Windows XP专业版操作系统的系统上执行。

以下代码段说明如何使用每个API执行这些任务。

### **VSTO代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-VSTOCode-1.cs" >}}

### **Aspose.Cells代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-UsingAsposeCells-1.cs" >}}

### **结果**

结果显示，使用 VSTO API 大约需要 2.5 分钟（约 150 秒以上）才能完成任务，而 Aspose.Cells 在常规硬件和正常系统配置下不到 1 秒就能完成任务。

如果循环扩展，例如填充 10,000*20 个单元格，Aspose.Cells 需要大约 5.5 秒来完成任务。

## **结论**

如果你考虑在业务解决方案中使用 Microsoft Office 技术，首先要熟悉可用的替代方案。基于不同产品执行一些测试，将其暴露在各种实际条件下，如负载和压力，以查看它们的性能如何。

Aspose.Cells 是一个稳定且成熟的产品，拥有全球客户群，并具有足够的可扩展性，可以在重负载下表现良好。

VSTO 的性能还不够精致。很可能一些性能问题并非与 VSTO 本身有关，而是与 .NET JIT 编译过程有关。但是，仍然存在一定的怀疑，即随着负载的增加，VSTO 应用程序是否能够自行扩展。VSTO 的新模型不需要 Excel 驻留在 web 服务器上进行文档处理，但我认为 VSTO 在产生真正影响方面还有很长的道路要走。
{{< app/cells/assistant language="csharp" >}}
