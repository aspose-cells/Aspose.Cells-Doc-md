---
title: 先例和家属
type: docs
weight: 230
url: /zh/net/precedents-and-dependents/
---
{{% alert color="primary" %}} 

复杂的财务工作表，尤其是合作开发的财务工作表，可能会隐藏最令人尴尬的错误。当公式使用引用单元格和依赖单元格时，检查公式的准确性和查找错误来源可能很困难。

{{% /alert %}} 
## **介绍**
- **判例单元格**是由另一个 Cell 中的公式引用的单元格。例如，如果单元格 D10 包含公式 =B5，则单元格 B5 是单元格 D10 的先例。
- **依赖细胞**包含引用其他单元格的公式。例如，如果单元格 D10 包含公式 =B5，则单元格 D10 依赖于单元格 B5。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格中的哪些单元格用于公式。同样，您可能想要提取其他单元格的依赖单元格。

Aspose.Cells 允许您跟踪单元格并找出链接的单元格。
## **追踪先例和从属 Cells: Microsoft Excel**
配方可能会根据客户所做的修改而改变。例如，如果单元格 C1 依赖于包含公式的 C3 和 C4，并且更改了 C1（因此公式被覆盖），则需要更改 C3 和 C4 或其他单元格以根据业务规则平衡电子表格。

同样，假设 C1 包含公式“=(B1*22)/(平方米*N32)”。我想找到 C1 所依赖的单元格，即前面的单元格 B1、M2 和 N32。

您可能需要跟踪特定单元格对其他单元格的依赖性。如果业务规则嵌入到公式中，我们想找出依赖关系并根据它执行一些规则。同样，如果修改了特定单元格的值，工作表中的哪些单元格会受到该更改的影响？

Microsoft Excel 允许用户追踪先例和相关信息。

1. 在**查看工具栏**， 选择**配方审核**.将显示公式审核对话框。
1. 追溯先例：
1. 选择包含要为其查找引用单元格的公式的单元格。
 1. 要向直接向活动单元格提供数据的每个单元格显示示踪箭头，请单击**追溯先例**在**配方审核**工具栏。
1. 引用特定单元格（依赖项）的跟踪公式
1. 选择要为其标识依赖单元格的单元格。
 1. 要向依赖于活动单元格的每个单元格显示示踪箭头，请单击公式审核工具栏上的跟踪依赖项。
## **追溯先例和从属 Cells: Aspose.Cells**
### **追溯先例**
Aspose.Cells 可以轻松获得先例单元格。它不仅可以检索为简单公式引用提供数据的单元格，还可以找到为具有命名范围的复杂公式引用提供数据的单元格。

在下面的示例中，使用了模板 excel 文件 Book1.xls。电子表格在第一个工作表上有数据和公式。

 Aspose.Cells 提供了[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[获取先例](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents)用于追踪细胞先例的方法。它返回一个[参考区域集合](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection).正如您在上面看到的，在 Book1.xls 中，单元格 B7 包含一个公式“=SUM(A1:A3)”。因此，单元格 A1:A3 是单元格 B7 的先行单元格。以下示例使用模板文件 Book1.xls 演示了跟踪先例功能。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **追踪家属**
Aspose.Cells 可让您获取电子表格中的相关单元格。 Aspose.Cells 不仅可以检索提供有关简单公式数据的单元格，还可以找到为具有命名范围的复杂公式依赖项提供数据的单元格。

Aspose.Cells 提供了[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[获取依赖项](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents)用于跟踪单元格的依赖项的方法。例如，Book1.xlsx中B2和C2单元格分别有公式：“=A1+20”和“=A1+30”。以下示例演示如何使用模板文件 Book1.xlsx 跟踪 A1 单元格的依赖项。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **根据计算链追踪先例和从属单元格**
以上追根溯源的api都是根据公式自己表达的。它们只是为用户提供方便的方式来跟踪一些公式的相互依赖性。如果工作簿中有大量公式并且用户需要跟踪每个单元格的先例和依赖项，则它们的性能会很差。对于这种情况，用户应考虑使用[获取先例计算](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/)和[GetDependentsInCalculation 函数](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/)方法。这两种方法根据计算链跟踪依赖关系。所以，要使用它们，首先你需要启用计算链[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) .然后您应该通过以下方式对工作簿执行完整计算[工作簿.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1).之后，您可以追踪所有需要的单元格的先例或相关项。

对于某些公式，GetPrecedents 和 GetPrecedentsInCalculation 的结果先例可能不同，而 GetDependents 和 GetDependentsInCalculation 的结果依赖项可能不同。例如，如果单元格 A1 的公式为“=IF(TRUE,B2,C3)”，GetPrecedents 将提供 B2 和 C3 作为 A1 的先例。相应地，B2和C3在GetDependents检查时都有依赖A1。但是对于这个公式的计算，显然只有B2能影响计算结果。所以GetPrecedentsInCalculation不会为A1提供C3，GetDependentsInCalculation也不会为C3提供A1。有时用户可能只是需要根据工作簿的当前数据跟踪那些实际影响公式计算结果的相互依赖关系，那么他们还需要使用 GetDependentsInCalculation/GetPrecedentsInCalculation 而不是 GetDependents/GetPrecedents。

以下示例演示如何根据单元格的计算链跟踪先例和依赖项：


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
