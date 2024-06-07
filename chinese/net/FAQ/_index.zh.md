---
title: FAQ
type: docs
weight: 100
url: /zh/net/faq/
---

## **如何解决Workbook.CalculateFormula上的System.StackOverFlowException？**
有时，用户在使用Workbook.CalculateFormula方法时会遇到System.StackOverFlowException异常。这种异常通常是由于IIS的默认堆栈大小太小（仅265k）而导致的。您可以通过创建另一个具有增加的堆栈大小的线程，然后将与Workbook.CalculateFormula相关的代码移动到其中来解决此错误。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **在将Excel转换为PDF时线条粗细不一致的问题**
有时，将Excel文件转换为PDF后，输出PDF中线条的粗细不同。这个问题不是由Aspose.Cells引起的。是由Adobe Reader在其设置"平滑线条"和"增强细线"被勾选时引起的。取消勾选这些选项将正常显示PDF。

如果勾选"平滑线条"和"增强细线"，线条的粗细会有所不同。请参考以下步骤执行：

- 进入**编辑**
- 选择**首选项**
- 在**页面显示**类别中勾选**"平滑线条"**和**"增强细线"**

如果取消勾选"平滑线条"和"增强细线"，线条的粗细会相同。要实现此目的，请按照以下步骤执行：

- 进入**编辑**
- 选择**首选项**
- 在**页面显示**类别中，取消选择**“平滑线条”**和**“增强细线”**
## **如何解决在加载大型电子表格时出现System.OutOfMemoryException的问题？**
Workbook构造函数有可能在加载大型电子表格时抛出System.OutOfMemoryException异常。此异常表明可用内存不足以完全加载电子表格到内存中，因此必须在加载电子表格时启用[内存首选项](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)。

Aspose.Cells API提供内存首选项，以优化加载和处理电子表格时的内存消耗。这些选项还有助于有效地加载包含大量数据集的大型电子表格到Workbook对象中，如下所示。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **确定加载某个工作簿所需的堆栈大小**
尽管我们已经增强了Aspose.Cells公式计算引擎，在大多数情况下，您应该能够成功计算给定模板文件中的所有公式，而无需指定较小的堆栈大小。但有时在Workbook.CalculateFormula方法中可能不可避免地会出现StackOverFlowException。我们为用户提供了新的API来跟踪公式计算。我们添加了一个名为"AbstractCalculationMonitor"的类，并提供了一个属性，即*CalculationOptions.CalculationMonitor*，以应对/跟踪此问题。

用户可以使用API自行跟踪堆栈大小。请注意，为每个单元格检查堆栈肯定会严重降低性能。请参阅以下示例代码段供参考：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

在运行时获取使用的堆栈大小没有更好的方式。我们提供的上述代码仅供参考。这肯定会严重降低性能。因此，我们认为用户（确实想要使用的用户）可以根据其不同的场景和需求对代码进行优化。例如，当递归单元格计数达到一定数量时检查堆栈，收集一个递归单元格的平均堆栈增长率，并确定检查堆栈的频率等。

{{% /alert %}}

