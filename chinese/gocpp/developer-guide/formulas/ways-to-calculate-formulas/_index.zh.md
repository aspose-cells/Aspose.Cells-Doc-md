---
title: 计算公式的方式
type: docs
weight: 30
url: /zh/go-cpp/ways-to-calculate-formulas/
---

## **介绍**

Aspose.Cells内置有公式计算引擎。 它不仅可以重新计算从设计模板导入的公式，还支持计算运行时添加的公式的结果。

## **添加公式及计算结果**

Aspose.Cells支持大部分Microsoft Excel中的公式或函数。它们可以通过API或设计者电子表格使用。Aspose.Cells支持大量的数学、字符串、布尔、日期/时间、统计、查找和引用公式。

使用Cell.SetFormula方法向单元格添加公式。当将公式应用于单元格时，始终以等号(=)开头，就像在Microsoft Excel中创建公式时一样。使用逗号(,)来分隔函数参数。

要计算公式的结果，请调用Workbook.CalculateFormula()方法，该方法可以处理Excel文件中嵌入的所有公式。请参阅下面的示例代码，添加公式并计算其结果。请检查使用此代码生成的[输出excel文件](38109185.xlsx)。

**示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **仅计算一次公式**

当调用Workbook.CalculateFormula()来计算工作簿模板中公式的值时，Aspose.Cells会创建一个计算链。当第二或第三次计算公式时，会提高性能。

但是，如果模板包含大量公式，第一次计算公式可能会消耗大量CPU处理时间和内存。

Aspose.Cells允许您关闭创建计算链，这在您只想计算公式一次时很有用。

请调用Workbook.GetISettings().SetCreateCalcChain()，参数为false。您可以使用[提供的excel文件](38109186.xlsx)测试此代码。

**示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}
