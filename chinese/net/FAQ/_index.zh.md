---
title: 常见问题解答
type: docs
weight: 100
url: /zh/net/faq/
---

## **如何修复Workbook.CalculateFormula上的System.StackOverFlowException?**
有时用户在使用Workbook.CalculateFormula方法时会遇到System.StackOverFlowException。这个异常通常是因为IIS的默认堆栈大小太小（仅为265k）所导致的。您可以通过创建另一个具有增加堆栈大小的线程，然后将与Workbook.CalculateFormula相关的代码移至其中来修复此错误。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **将Excel渲染为PDF时线条粗细的问题**
有时将Excel文件转换为PDF后，输出的PDF中线条的粗细会有所不同。这个问题不是由Aspose.Cells引起的，而是由于在Adobe Reader的设置中勾选了"平滑线条图"和"增强细线"选项导致的。取消这些选项将能正常显示PDF。

如果勾选了"平滑线条图"和"增强细线"，线条的粗细将有所不同。请参照以下步骤进行操作:

- 进入"编辑"
- 选择"首选项"
- 在"页面显示"类别中勾选"平滑线条图"和"增强细线"

如果取消勾选"平滑线条图"和"增强细线"，线条的粗细将保持一致。请参照以下步骤进行操作:

- 进入"编辑"
- 选择"首选项"
- 在"页面显示"类别中取消勾选"平滑线条图"和"增强细线"
## **如何修复加载大型电子表格时的System.OutOfMemoryException?**
在加载大型电子表格时，Workbook构造函数可能会引发System.OutOfMemoryException。这个异常表明可用内存不足以将整个电子表格完全加载到内存中，因此必须在启用[内存优化偏好设置](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)的情况下加载电子表格。

Aspose.Cells APIs提供了内存优化偏好设置，可以优化加载和处理电子表格时的内存消耗。这些选项还可以有效地在Workbook对象中加载包含大量数据集的大型电子表格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **确定某个工作簿所需的堆栈大小**
尽管我们增强了Aspose.Cells的公式计算引擎，大多数情况下，您应该能够成功计算给定模板文件的所有公式而无需指定较小的堆栈大小。但有时，在Workbook.CalculateFormula方法上发生StackOverFlowException是不可避免的。我们为用户提供了用于跟踪公式计算的新API。我们添加了一个名为"AbstractCalculationMonitor"的类，并提供了一个属性，即*CalculationOptions.CalculationMonitor*，以处理/跟踪这个问题。

用户可以使用API自行跟踪堆栈大小。请注意，为每个单元格检查堆栈肯定会大大降低性能。请参考以下示例代码片段：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

在运行时，没有更好的方式来获取堆栈大小。我们提供的以上代码仅供参考。性能肯定会显著降低。因此，我们认为用户（确实想要使用它的人）可以根据其不同的场景和要求优化代码。例如，当递归单元格计数达到一定数量时检查堆栈，收集一个递归单元格的平均增长率并确定检查堆栈的频率等。

{{% /alert %}}

