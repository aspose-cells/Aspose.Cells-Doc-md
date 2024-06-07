---
title: 前置和后置
type: docs
weight: 230
url: /zh/net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

特别是在协作开发的复杂财务工作表中，可能会隐藏最尴尬的错误。当公式使用前置单元格和后置单元格时，检查公式的准确性并找到错误来源可能会变得困难。

{{% /alert %}} 
## **介绍**
- **前置单元格** 是由另一个单元格中的公式引用的单元格。例如，如果单元格 D10 包含公式 =B5，则单元格 B5 是单元格 D10 的前置。
- **后置单元格** 包含引用其他单元格的公式。例如，如果单元格 D10 包含公式 =B5，则单元格 D10 是单元格 B5 的后置。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格上使用的公式单元格。同样，您可能希望提取其他单元格的后置单元格。

Aspose.Cells允许您跟踪单元格并找出哪些单元格是链接的。
## **跟踪先行和从属单元格：Microsoft Excel**
根据客户所做的修改，公式可能会改变。例如，如果单元格 C1 依赖于包含公式的 C3 和 C4，并且更改了 C1（使公式被覆盖），则需要根据业务规则调整 C3 和 C4 或其他单元格以平衡电子表格。

同样地，假设 C1 包含公式"=(B1*22)/(M2*N32)"。我想找出 C1 依赖的单元格，即先行单元格 B1、M2 和 N32。

您可能需要追踪特定单元格对其他单元格的依赖关系。如果业务规则嵌入在公式中，我们希望找出依赖关系并根据此执行一些规则。同样地，如果特定单元格的值被修改，工作表中哪些单元格会受到该更改的影响？

Microsoft Excel 允许用户跟踪先行和从属。

1. 在**查看工具栏**上，选择**公式审计**。将显示“公式审计”对话框。
1. 追踪先行：
   1. 选择包含您要查找先行单元格公式的单元格。
   1. 要为直接提供数据给活动单元格的每个单元格显示跟踪箭头，请在**公式审计**工具栏上单击**跟踪先行**。
1. 追踪引用特定单元格的公式（从属）
   1. 选择要识别从属单元格的单元格。
   1. 要为依赖于活动单元格的每个单元格显示跟踪箭头，请在公式审计工具栏上单击“跟踪从属”。
## **跟踪先行和从属单元格：Aspose.Cells**
### **跟踪先行**
Aspose.Cells 使获取先行单元格变得很容易。它不仅可以检索提供数据给简单公式先行的单元格，还可以找到提供数据给带有命名范围的复杂公式先行的单元格。

在下面的示例中，使用一个模板excel文件 Book1.xls。电子表格在第一个工作表上有数据和公式。

Aspose.Cells提供了 [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) 方法，用于跟踪单元格的先行。它返回一个 [ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection)。正如您在 Book1.xls 中看到的，单元格 B7 包含公式"=SUM(A1:A3)"。因此单元格 A1:A3 是单元格 B7 的先行单元格。以下示例演示了如何使用模板文件 Book1.xls 跟踪先行的功能。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **跟踪从属**
Aspose.Cells允许您获取电子表格中的依赖单元格。Aspose.Cells 不仅可以检索提供简单公式数据的单元格，还可以找到提供带有命名范围的复杂公式从属的单元格。

Aspose.Cells提供了 [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents) 方法，用于跟踪单元格的从属。例如，在 Book1.xlsx 中有公式:"=A1+20" 和"=A1+30" 分别在 B2 和 C2 单元格中。以下示例演示了如何使用模板文件 Book1.xlsx 跟踪 A1 单元格的从属。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **根据计算链跟踪先行和从属单元格**
跟踪先行和从属的上述 API 都基于公式表达式本身。它们为用户提供了一种方便的方式来跟踪少量公式的相互依赖关系。如果工作簿中有大量公式且用户需要为每个单元格跟踪先行和从属，性能会很差。对于这种情况，用户应该考虑使用 [GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) 和 [GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) 方法。这两种方法会根据计算链跟踪依赖关系。因此，要使用它们，首先需要通过 [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) 启用计算链。然后您需要通过 [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) 对工作簿执行完全计算。之后，您可以为所有需要的单元格跟踪先行或从属。

对于某些公式，GetPrecedents 和 GetPrecedentsInCalculation 可能产生不同的先行结果，GetDependents 和 GetDependentsInCalculation 可能产生不同的从属结果。例如，如果单元格 A1 的公式是"=IF(TRUE,B2,C3)"，GetPrecedents 将提供 B2 和 C3 作为 A1 的先行。相应地，通过 GetDependents 检查时，B2 和 C3 都有依赖于 A1。然而，对于该公式的计算，很明显只有 B2 可以影响计算结果。因此，GetPrecedentsInCalculation 将不会为 A1 提供 C3，GetDependentsInCalculation 将不会为 C3 提供 A1。有时用户可能只需追踪那些实际上会根据工作簿当前数据影响公式计算结果的相互依赖关系，那么他们也需要使用 GetDependentsInCalculation/GetPrecedentsInCalculation，而不是 GetDependents/GetPrecedents。

以下示例演示了如何根据计算链跟踪单元格的先行和从属：


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
