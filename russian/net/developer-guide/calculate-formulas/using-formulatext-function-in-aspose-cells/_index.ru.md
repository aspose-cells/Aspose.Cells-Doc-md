---
title: Использование функции FormulaText в Aspose.Cells
description: В этой статье рассматривается, как использовать функцию FormulaText в библиотеке Aspose.Cells для обработки формул в Microsoft Excel. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать метод, предоставленный Aspose.Cells, для получения и установки текста формулы ячейки и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, функции FormulaText
type: docs
weight: 60
url: /ru/net/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

Функция FormulaText является функцией Excel 2013 и новее. Она не поддерживается в предыдущих версиях, таких как Excel 2010 или 2007 и т. д. Как следует из названия, она печатает текст формулы, которая присутствует в заданной ячейке. В этой статье мы покажем вам, как использовать эту функцию с помощью Aspose.Cells.

{{% /alert %}} 

В следующем примере показано использование функции FormulaText с Aspose.Cells. В этом коде сначала записывается формула в ячейку A1, а затем печатается текст формулы с помощью FormulaText в ячейке A2.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
