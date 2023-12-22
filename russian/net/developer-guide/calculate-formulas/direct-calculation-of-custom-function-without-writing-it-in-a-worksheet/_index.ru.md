---
title: Прямой расчет пользовательской функции без записи ее на листе
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для прямого вычисления пользовательских функций в Excel Microsoft без записи функции на лист. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для вычисления пользовательской функции и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **Прямой расчет пользовательской функции без записи ее на листе**

 В этом разделе объясняется, как можно напрямую вычислить пользовательские функции, не записывая их предварительно на лист. Пожалуйста, используйте[**Worksheet.CalculateFormula(строковая формула, параметры CalculationOptions)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)метод для этой цели.

См. следующий пример кода, иллюстрирующий использование этого метода. Мы использовали пользовательскую функцию с именем MyCompany.CustomFunction() и вычисляем ее значение как «Aspose.Cells». нами, а затем это значение автоматически объединяется со значением ячейки A1, которое является «Добро пожаловать в» механизмом вычислений, и окончательное рассчитанное значение возвращается как «Добро пожаловать в Aspose.Cells». Как вы можете видеть в коде, который у нас есть наша пользовательская функция нигде на листе не записана, и она вычисляется непосредственно нашей собственной пользовательской логикой.

###  **Пример программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **Консольный вывод**

Ниже приведен консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **Связанная статья**

{{% alert color="primary" %}}

[Внедрите пользовательский механизм вычислений, чтобы расширить механизм вычислений по умолчанию Aspose.Cells.](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
