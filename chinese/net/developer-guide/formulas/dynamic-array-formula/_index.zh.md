---
title: 设置动态数组公式
description: 如何使用Aspose.Cells库在Microsoft Excel中计算动态数组公式。通过加载现有的Excel文件或者新建一个Excel文件，我们可以使用Aspose.Cells提供的方法来计算动态数组公式并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /zh/net/calculation-of-dynamic-array-formulas/
---
##  **Excel数组公式是什么**
在 Excel 中，数组公式是一种特殊类型的公式，它允许您对数据数组而不是单个单元格执行计算。数组公式可用于执行复杂的计算、操作数据并有效地解决特定问题。它们的输入方式与常规公式不同，通常需要使用 Ctrl + Shift + Enter。

以下是有关 Excel 中数组公式的一些要点：
1. 句法：
<br>
数组公式的编写方式与常规公式类似，但涉及对值数组的运算。它们用大括号 { } 括起来，表明它们是数组公式。但是，您不需要自己键入这些花括号；而是需要您自己输入这些花括号。当您正确输入公式时，Excel 会自动添加它们。
1. 输入数组公式：
<br>
要输入数组公式，请在公式栏中键入公式。不要按 Enter 来完成，而是按 Ctrl + Shift + Enter。这告诉 Excel 这是一个数组公式。输入正确后，Excel 会在公式栏中将公式显示在大括号内，以表明它是数组公式。
1. 用例：
<br>
数组公式对于同时跨多个单元格或范围执行计算非常有用。它们可用于高级数学计算、条件运算、过滤数据等。
1. 好处：
<br>
数组公式允许您在单个公式中执行复杂的计算，这可以提高效率并简化工作表。它们可以处理大型数据集并执行需要多个中间步骤的计算。
1. 限制：
<br>
数组公式比常规公式更难理解和排除故障。它们可能会降低工作表性能，特别是在广泛使用或处理大型数据集时。
1. 例子：
<br>
对某个范围内的值求和：**{=SUM(A1:A5*B1:B5)}**
<br>
求一个范围内的最大值：**{=最大值(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

请记住，应谨慎使用数组公式，在工作表中实现它们之前了解它们的工作原理非常重要。它们可以成为 Excel 中数据分析和操作的强大工具。

##  **Excel动态数组公式是什么**
动态数组公式是 Excel 365 和 Excel 2021 中引入的一项新功能。与传统数组公式相比，动态数组公式允许您更无缝、更高效地处理数据数组。动态数组公式会自动将结果溢出到相邻单元格中，无需使用 Ctrl + Shift + Enter，并且可以更轻松地操作数据。

Excel中动态数组公式的要点：
1. 自动溢出：
<br>
动态数组公式根据输出数据的大小自动将结果溢出到相邻单元格中。这意味着您无需在输入公式之前选择单元格范围或使用 Ctrl + Shift + Enter 确认公式。
1. 单-Cell条目：
<br>
将动态数组公式输入到单个单元格中，Excel 会自动将结果填充到相邻单元格中。这使得管理和理解公式变得更加容易，因为您只需输入公式一次。
1. 新功能：
<br>
动态数组公式引入了可以本地处理数组的新函数，例如 *FILTER**、*SORT**、*UNIQUE**、*SEQUENCE**、*SORTBY** 和 *RANDARRAY**。这些函数可以返回多个值或直接操作数组，从而简化复杂的计算。
1. 灵活的范围处理：
<br>
动态数组公式根据输入数据的大小或执行的计算动态调整溢出范围的大小。这种灵活性可以更有效地利用工作表空间并简化公式创建。
1. 改进的性能：
<br>
与传统数组公式相比，动态数组公式可以提高性能，尤其是在处理大型数据集或复杂计算时。
1. 兼容性：
<br>
动态数组公式在 Excel 365 和 Excel 2021 中可用。旧版本的 Excel 可能不支持它们。
1. 动态数组公式示例：
<br>
*FILTER**：返回满足指定条件的值数组。
<br>
*SORT**：对范围或数组中的值进行排序。
<br>
*UNIQUE**：返回列表或范围中的唯一值。
<br>
*SEQUENCE**：生成数字或日期序列。
<br>
*RANDARRAY**：生成随机数数组。
<br>
<image src="2.png" width="70%" />
<br>

动态数组公式为 Excel 中的数据操作和分析提供了强大的功能，使您可以更轻松地处理数据数组并高效执行复杂的计算。

##  **Excel中数组公式和动态数组公式有什么区别**
在Excel中，数组公式和动态数组公式都用于同时对多个值进行计算，但它们在功能和实现方式方面存在一些差异。

###  **数组公式特点**
1. 数组公式是 Excel 中的传统公式，可以对数据数组执行计算。
1. 输入公式后按 Ctrl + Shift + Enter 即可输入它们，这告诉 Excel 这是一个数组公式。
1. 数组公式在将结果溢出到相邻单元格的能力方面存在局限性。 1. 它们通常返回单个结果，尽管该结果可能是元胞数组。
1. 它们已经存在很长时间了，并且在所有版本的 Excel 中都受支持。

###  **动态数组公式功能**
1. 动态数组公式是 Excel 365（Office 365 订阅）和 Excel 2021 中引入的新功能。
1. 它们根据输入数据的大小或公式的计算自动将结果溢出到相邻的单元格中。
1. 动态数组公式不需要按 Ctrl + Shift + Enter；您只需在一个单元格中键入公式，Excel 就会自动将结果填充到相邻的单元格中。
1. 这些公式能够直接返回多个结果（一系列单元格），而不需要数组公式或 Ctrl + Shift + Enter。
1. 它们具有 *FILTER**、*SORT**、*UNIQUE** 等新函数，可以本地处理数组并以动态数组格式返回结果。
总之，动态数组公式是一种在 Excel 中处理数组的更现代、更方便的方法，与传统数组公式相比，它提供结果自动溢出并简化了处理数组的过程。但是，它们仅在支持动态数组的较新版本的 Excel 中可用。

##  **如何在 Excel 中设置和计算动态数组公式**
在 Excel 中设置动态数组公式涉及使用特定函数，这些函数旨在处理数据数组并允许结果自动溢出到相邻单元格中。

以下是设置动态数组公式的分步指南：
1. 选择Cell：
<br>
选择要显示动态数组公式结果的单元格。动态数组公式将结果溢出到相邻单元格中，因此请确保有足够的空间用于溢出的输出。
1. 输入公式：
<br>
在所选单元格的编辑栏中键入动态数组公式。使用 Excel 365 和 Excel 2021 中提供的动态数组函数之一，例如 *FILTER**、*SORT**、*UNIQUE**、*SEQUENCE**、*SORTBY** 或 *RANDARRAY**。
<br>
例如，您可以使用 FILTER 函数根据特定条件筛选数据列表：*=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**。
<br>
<image src="3.png" width="70%" />
<br>
1. 按输入键：
<br>
输入公式后，只需按键盘上的 Enter 键即可。与传统的数组公式不同，您不需要按 Ctrl + Shift + Enter。
1. 观察溢出范围：
<br>
Excel 会自动将公式的结果溢出到相邻的单元格中。溢出范围根据输出数据的大小或公式执行的计算动态调整。 Excel 用边框和对角箭头图标突出显示溢出范围，以指示它包含溢出数据。
1. 与溢出范围交互：
<br>
您可以像 Excel 中的任何其他单元格区域一样与溢出区域进行交互。在其他公式中使用溢出范围、对其执行计算、设置其格式或在图表或表格中引用它。
1. 更新公式：
<br>
如果需要修改动态数组公式，只需在输入公式的原始单元格中编辑公式即可。
编辑完成后，再次按 Enter 键确认更改。如有必要，Excel 将自动更新溢出范围。
1. 清除溢出范围：
<br>
如果要清除溢出的数据，可以从原始单元格中删除公式。 Excel 也会清除溢出的范围。或者，您可以通过选择溢出范围并按删除键来直接删除溢出范围。
<br>

通过执行以下步骤，您可以在 Excel 中设置动态数组公式，以有效地分析和操作数据数组，从而更轻松地完成数据分析和报告任务。

##  **如何使用 Aspose.Cells 设置和刷新动态数组公式**
请参阅以下加载示例代码[Excel 文件示例](dynamicArrayFormula.xlsx)其中包含一些虚拟数据。加载文件后，调用[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula)设置动态数组公式的函数和[Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas)函数在调用公式计算之前刷新动态数组公式，最后将工作簿另存为[输出Excel文件](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

输出快照：
<br>
<image src="4.png" width="70%" />