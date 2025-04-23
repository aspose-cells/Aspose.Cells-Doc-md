---
title: 先例和从属
type: docs
weight: 230
url: /zh/python-net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

复杂的财务工作表，尤其是合作开发的工作表，可能隐藏最令人尴尬的错误。当公式使用先例单元格和从属单元格时，检查公式的准确性并找到错误的来源可能很困难。

{{% /alert %}} 
## **介绍**
- **前代单元格** 是由另一个单元格的公式引用的单元格。例如，如果单元格D10包含公式=B5，则单元格B5是单元格D10的前代。
- **依赖单元格**包含引用其他单元格的公式。例如，如果单元格 D10 包含公式 =B5，则单元格 D10 依赖于单元格 B5。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格中用于公式的单元格。同样，您可能需要提取其他单元格的依赖单元格。

 Aspose.Cells for Python via .NET 允许您追踪单元格并查找链接的单元格。
## **跟踪先例和依赖单元格：Microsoft Excel**
公式可能会根据客户做出的修改而改变。例如，如果单元格 C1 依赖于包含公式的 C3 和 C4，并且更改了 C1（使公式被覆盖），则根据业务规则需要更改 C3 和 C4，或其他单元格，以使电子表格保持平衡。

类似地，假设 C1 包含公式"=(B1*22)/(M2*N32)"。我想找到 C1 依赖的单元格，即先例单元格 B1、M2 和 N32。

您可能需要跟踪特定单元格到其他单元格的依赖关系。如果业务规则嵌入在公式中，我们希望找出依赖关系，并根据此执行一些规则。同样，如果特定单元格的值被修改，那么工作表中哪些单元格受到此变化的影响？

Microsoft Excel 允许用户跟踪先例和依赖。

1. 在**查看工具栏**上选择**公式审计**。将显示公式审计对话框。
1. 跟踪先例：
   1. 选择包含您想要查找先例单元格的公式的单元格。
   1. 要向每个直接提供数据给活动单元格的单元格显示跟踪箭头，请单击**公式审计**工具栏上的**跟踪先例**。
1. 跟踪引用特定单元格的公式（依赖项）
   1. 选择要识别其依赖单元格的单元格。
   1. 要向每个依赖于活动单元格的单元格显示跟踪箭头，请单击**公式审计**工具栏上的**跟踪依赖**。
## ** 追踪前置和后续单元格：Aspose.Cells for Python via .NET**
### **跟踪先例**
 Aspose.Cells for Python via .NET 方便获取前置单元格。它不仅能检索提供数据的简单公式前置单元格，也能找到提供数据的复杂公式前置单元格（含命名区域）。

在下面的示例中，使用了模板Excel文件《Book1.xls》。电子表格在第一个工作表上包含数据和公式。

 Aspose.Cells for Python via .NET 提供 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的 [**get_precedents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents/#) 方法，用于追踪单元格的前置单元格。它返回一个 [**ReferredAreaCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/referredareacollection)。如上图例，在Book1.xls中，单元格B7包含公式 "=SUM(A1:A3)"，因此A1:A3是B7的前置单元格。以下示例演示如何使用模板文件Book1.xls实现追踪前置单元格。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingPrecedents-1.py" >}}
### **跟踪依赖项**
 Aspose.Cells for Python via .NET 允许您获取电子表格中的后续单元格。它不仅可以检索提供数据的简单公式的后续单元格，也能找到提供数据的复杂公式（含命名区域）的后续单元格。

 Aspose.Cells for Python via .NET 提供 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的 [**get_dependents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents/#bool) 方法，用于追踪单元格的后续单元格。例如，在Book1.xlsx中的公式："=A1+20" 和 "=A1+30" 分别位于 B2 和 C2 单元格。以下示例演示如何追踪A1单元格的后续单元格，使用模板文件Book1.xlsx。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependents-1.py" >}}

### **根据计算链跟踪先行单元格和依赖单元格**
 上述追踪前置和后续的API都是根据公式表达式本身设计的。它们仅提供一个方便的方式让用户追踪少量公式的相互依赖关系。如果工作簿中有大量公式，并且用户需要追踪每个单元格的前置和后续，则性能会变差。在这种情况下，建议使用 [**get_precedents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents_in_calculation/#) 和 [**get_dependents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents_in_calculation/#bool) 方法。这两个方法按计算链追踪依赖关系。因此，要使用它们，首先需要启用计算链 [**Workbook.settings.formula_settings.enable_calculation_chain**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/enable_calculation_chain/)。然后对工作簿执行完整计算 [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。之后，即可追踪所有相关单元格的前置或后续单元格。

对于一些公式，GetPrecedents和GetPrecedentsInCalculation得到的结果可能不同，GetDependents和GetDependentsInCalculation得到的结果也可能不同。例如，如果单元格A1的公式是"=IF(TRUE,B2,C3)"，GetPrecedents将提供B2和C3作为A1的先行单元格。据此，当通过GetDependents检查时，B2和C3都有依赖项A1。然而，对于这个公式的计算，很明显只有B2可以影响计算结果。因此，GetPrecedentsInCalculation将不为A1提供C3，GetDependentsInCalculation也不会为C3提供A1。有时，用户可能只需要跟踪那些实际上根据工作簿当前数据影响公式计算结果的相互依存关系，那么他们也需要使用GetDependentsInCalculation/GetPrecedentsInCalculation而不是GetDependents/GetPrecedents。

以下示例演示了如何根据计算链追踪单元格的先行和依赖项：


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependenciesInCalculation.py" >}}

