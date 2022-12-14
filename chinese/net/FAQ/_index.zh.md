---
title: 常问问题
type: docs
weight: 100
url: /zh/net/faq/
---
## **如何修复 Workbook.CalculateFormula 上的 System.StackOverFlowException？**
有时，用户会在 Workbook.CalculateFormula 方法上遇到 System.StackOverFlowException。出现这种异常通常是因为 IIS 默认的堆栈大小太小（只有 265k）。您可以通过创建另一个增加堆栈大小的线程，然后将您的 Workbook.CalculateFormula 相关代码移入其中来修复此错误。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **将 Excel 渲染为 PDF 时出现线条粗细问题**
有时，当 Excel 文件转换为 PDF 时，输出 PDF 中的线条粗细不同。此问题不是由 Aspose.Cells 引起的。它是由**Adobe 阅读器**当它的设置**“流畅的线条艺术”**和**“增强细线”**被检查。取消选中这些选项将正常显示 PDF。

如果检查**“流畅的线条艺术”**和**“增强细线”**，线条粗细不同。请参阅以下步骤如何完成：

- 去**编辑**
- 选择**喜好**
- 在里面**页面显示**分类勾选**“流畅的线条艺术”**和**“增强细线”**

如果取消勾选**“流畅的线条艺术”**和**“增强细线”**线的粗细是一样的。要实现这一点，只需按照以下步骤操作：

- 去**编辑**
- 选择**喜好**
- 在里面**页面显示**类别取消选中**“流畅的线条艺术”**和**“增强细线”**
## **如何在加载大型电子表格时修复 System.OutOfMemoryException？**
加载大型电子表格时，Workbook 构造函数很有可能会抛出 System.OutOfMemoryException。此异常表明可用内存不足以将电子表格完全加载到内存中，因此必须在启用时加载电子表格[内存首选项](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells API 提供内存首选项以优化加载和处理电子表格时的内存消耗。这些选项也有助于有效地加载包含工作簿对象中大量数据集的大型电子表格，如下所示。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **确定特定工作簿需要的堆栈大小**
虽然，我们已经增强了 Aspose.Cells 公式计算引擎，并且在大多数情况下，您应该能够为给定的模板文件成功计算所有公式，而无需指定较小的堆栈大小。但是，有时 Workbook.CalculateFormula 方法上的 StackOverFlowException 可能是不可避免的。我们为用户提供了新的 API 来跟踪公式计算。我们添加了一个名为“AbstractCalculationMonitor”的类并提供了一个属性，即*计算选项.计算监视器*处理/追踪问题。

用户可以使用 API 自行跟踪堆栈大小。请注意，检查每个单元格的堆栈肯定会更大程度地降低性能。请参阅示例代码段供您参考：

`     `公共类 MyCalculationMonitor：AbstractCalculationMonitor
`     `{``public override void BeforeCalculate(int sheetIndex, int rowIndex, int colIndex) ``{``if(new StackTrace(false).FrameCount > 2000)``{``抛出新异常（"停止公式计算，因为有 StackOverflowException 的风险");  ` }  ` }  ` `} 



{{% alert color="primary" %}} 

没有更好的方法来获取运行时使用的堆栈大小。我们提供的上述代码仅作为示例。性能肯定会显着下降。所以，我们认为代码可以由用户（真正想要使用它的人）根据他们不同的场景和需求进行优化。例如，当递归单元计数达到一定数量时，检查堆栈，收集一个递归单元的堆栈平均增长率，并确定检查堆栈的频率等。

{{% /alert %}}

