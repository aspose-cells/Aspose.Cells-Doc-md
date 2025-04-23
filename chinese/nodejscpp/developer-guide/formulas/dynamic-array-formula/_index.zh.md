---  
title: 设置动态数组公式（Node.js via C++）  
linktitle: 设置动态数组公式  
description: 如何使用Aspose.Cells库在Node.js via C++中计算Excel中的动态数组公式。轻松加载、计算和保存Excel文件。  
keywords: 动态数组公式、Excel中的动态数组公式、Node.js via C++设置动态数组公式、动态数组公式计算Node.js via C++、操作Excel的动态数组公式。  
type: docs  
weight: 70  
url: /zh/nodejs-cpp/calculation-of-dynamic-array-formulas/  
---  
## **什么是Excel数组公式**  
在Excel中，数组公式是一种特殊类型的公式，允许您对数据数组进行计算，而不是单个单元格。数组公式可用于执行复杂计算，操作数据和有效解决特定问题。它们的输入方式与常规公式不同，并且通常需要使用Ctrl + Shift + Enter。

以下是关于Excel数组公式的一些要点：  
1. 语法：  
<br>  
数组公式的编写方式类似于常规公式，但涉及对值数组的操作。它们用花括号 { } 括起来，以指示它们是数组公式。但是，您不需要自己键入这些花括号；当您正确输入公式时，Excel会自动添加它们。  
2. 输入数组公式：  
<br>  
要输入数组公式，在公式栏中输入公式。完成后，不按 Enter，而是按 Ctrl + Shift + Enter。这告诉 Excel 它是一个数组公式。正确输入后，Excel 会在公式栏中显示带有大括号的公式，以表示这是一个数组公式。  
3. 用例：  
<br>  
数组公式对于同时在多个单元格或范围中执行计算非常有用。它们可用于高级数学计算，条件操作，数据过滤等。  
4. 好处：  
<br>  
数组公式允许您在单个公式中执行复杂计算，可以提高效率并简化您的工作表。它们可以处理大型数据集并执行通常需要多个中间步骤的计算。  
5. 限制：  
<br>  
数组公式可能比常规公式更难理解和解决故障。它们可能会减慢工作表的性能，特别是在广泛使用或与大型数据集一起使用时。  
6. 示例：  
<br>  
对范围中的值求和：**{=SUM(A1:A5*B1:B5)}**  
<br>  
查找范围中的最大值：**{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

请记住，应谨慎使用数组公式，并在将其应用于工作表之前了解它们的工作原理是很重要的。它们可以成为 Excel 中用于数据分析和操纵的强大工具。

## **什么是 Excel 动态数组公式**  
动态数组公式是 Excel 365 和 Excel 2021 中引入的新功能。与传统数组公式相比，它们允许您更无缝、更高效地处理数据数组。动态数组公式会自动将结果溢出到相邻单元格，无需使用 Ctrl + Shift + Enter，从而更轻松地操纵数据。

关于 Excel 中动态数组公式的关键点：  
1. 自动溢出：  
<br>  
动态数组公式会根据输出数据的大小自动将结果溢出到相邻单元格。这意味着您在输入公式之前不需要选择一系列单元格或使用 Ctrl + Shift + Enter 来确认公式。  
2. 单个单元格输入：  
<br>  
动态数组公式输入到单个单元格中，Excel 会自动填充相邻单元格的结果。这样更容易管理和理解公式，因为您只需要一次输入公式。  
3. 新功能：  
<br>  
动态数组公式引入了可以原生处理数组的新函数，如 **FILTER**、**SORT**、**UNIQUE**、**SEQUENCE**、**SORTBY** 和 **RANDARRAY**。这些函数可以返回多个值或直接操作数组，简化了复杂的计算。  
4. 灵活的范围处理：  
<br>  
动态数组公式会根据输入数据的大小或执行的计算动态调整溢出范围的大小。这种灵活性可以更高效地利用工作表空间，并简化公式的创建。  
5. 提升的性能：  
<br>  
与传统数组公式相比，动态数组公式可以提高性能，特别是在处理大型数据集或复杂计算时。  
6. 兼容性：  
<br>  
动态数组公式适用于 Excel 365 和 Excel 2021，可能不受旧版本 Excel 的支持。  
7. 动态数组公式示例：  
<br>  
**FILTER**：返回满足指定条件的数值数组。  
<br>  
**SORT**：对范围或数组中的数值进行排序。  
<br>  
**UNIQUE**：从列表或范围中返回唯一数值。  
<br>  
**SEQUENCE**：生成数字或日期序列。  
<br>  
**RANDARRAY**：生成随机数数组。  
<br>  
<image src="2.png" width="70%" />  
<br>  

动态数组公式在Excel中提供了强大的数据操作和分析功能，使得处理数据数组和进行复杂计算变得更加高效。

## **Excel中数组公式和动态数组公式的区别**  
在Excel中，数组公式和动态数组公式都用于同时对多个数值进行计算，但它们在功能和实现方式上有一些区别。

### **数组公式特点**  
1. 数组公式是Excel中可以对数据数组进行计算的传统公式。  
2. 它们在输入公式后通过按 Ctrl + Shift + Enter 来告诉Excel这是数组公式。  
3. 数组公式在向相邻单元格溢出结果方面存在限制。它们通常返回单个结果，尽管该结果可能是一个单元格数组。  
4. 它们存在已久并且在所有版本的Excel中都支持。

### **动态数组公式特点**  
1. 动态数组公式是Excel 365（Office 365订阅）和Excel 2021中引入的新功能。  
2. 它们会根据输入数据的大小或公式的计算自动溢出到相邻的单元格。  
3. 动态数组公式不需要按Ctrl + Shift + Enter；只需在一个单元格中输入公式，Excel会自动用结果填充相邻单元格。  
4. 这些公式能够直接返回多个结果（一个区域），无需使用数组公式或按Ctrl + Shift + Enter。  
5. 它们具有新的函数，例如**FILTER**、**SORT**、**UNIQUE**等，可以本地处理数组并以动态数组格式返回结果。  
总之，与传统数组公式相比，动态数组公式是在Excel中处理数组的更现代便捷的方式，提供了结果的自动填充并简化了处理数组的过程。但是它们仅在支持动态数组的较新版本的Excel中可用。

## **如何在Excel中设置和计算动态数组公式**  
在Excel中设置动态数组公式涉及使用专门设计用于处理数据数组并允许结果自动溢出到相邻单元格的特定函数。 

以下是设置动态数组公式的逐步指南:  
1. 选择单元格:  
<br>  
选择要将动态数组公式结果显示的单元格。动态数组公式会将结果溢出到相邻单元格，因此确保有足够的空间用于溢出输出。  
2. 输入公式：  
<br>  
将动态数组公式键入所选单元格的公式栏中。使用Excel 365和Excel 2021中提供的其中一个动态数组函数，例如**FILTER**、**SORT**、**UNIQUE**、**SEQUENCE**、**SORTBY**或**RANDARRAY**。  
<br>  
例如，您可能会使用FILTER函数根据特定条件对数据列表进行过滤: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**。  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. 按回车：  
<br>  
键入公式后，只需在键盘上按Enter键。与传统的数组公式不同，您无需按Ctrl + Shift + Enter键。  
4. 观察溢出范围：  
<br>  
Excel会自动将公式结果溢出到相邻单元格。溢出范围会根据输出数据的大小或公式执行的计算动态调整。Excel会用边框和对角箭头图标突出显示溢出范围，以指示它包含了溢出数据。  
5. 与溢出范围进行交互：  
<br>  
您可以像在Excel的任何其他单元格范围一样与溢出范围交互。在其他公式中使用溢出范围，对其执行计算，进行格式设置，或在图表或表格中引用它。  
6. 更新公式：  
<br>  
如果需要修改动态数组公式，只需编辑原始单元格中的公式。编辑完成后再次按回车确认修改，Excel会自动更新溢出范围（如果需要）。  
7. 清除溢出范围：  
<br>  
如果要清除溢出数据，可以从原始单元格中删除公式。Excel也会清除溢出范围。或者，您也可以直接选择溢出范围，然后按Delete键删除它。  
<br>  

通过按照这些步骤进行操作，您可以在Excel中设置动态数组公式，以便有效分析和操作数据数组，从而使数据分析和报告任务更加轻松。

## **如何使用Aspose.Cells设置和刷新动态数组公式**  
请参阅以下示例代码，该代码加载包含一些虚拟数据的[样本Excel文件](dynamicArrayFormula.xlsx)。加载文件后，调用[Cell.setDynamicArrayFormula(字符串，公式解析选项，布尔值)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setDynamicArrayFormula-string-formulaparseoptions-boolean-)函数设置动态数组公式，并调用[Workbook.refreshDynamicArrayFormulas(布尔值)](https://reference.aspose.com/cells/nodejs-cpp/workbook/#refreshDynamicArrayFormulas-boolean-)函数刷新动态数组公式，然后调用公式计算，最后将工作簿保存为[输出Excel文件](out.xlsx)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "dynamicArrayFormula.xlsx");

// Instantiate an Workbook object
const wb = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = wb.getWorksheets().get(0);

// Getting the F16 
const f16 = ws.getCells().get("F16");

// Set dynamic array formula
f16.setDynamicArrayFormula("=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new AsposeCells.FormulaParseOptions(), false);

// Refresh the dynamic array formulas
wb.refreshDynamicArrayFormulas(true);

wb.calculateFormula();
wb.save("out.xlsx");
```

输出快照：  
<br>  
<image src="4.png" width="70%" />  

