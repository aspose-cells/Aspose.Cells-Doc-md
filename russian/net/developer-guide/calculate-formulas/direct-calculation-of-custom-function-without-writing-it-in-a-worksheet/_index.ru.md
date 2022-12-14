---
title: Прямой расчет пользовательской функции без записи ее на листе
type: docs
weight: 90
url: /ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Прямой расчет пользовательской функции без записи ее на листе**

 В этом разделе объясняется, как можно напрямую рассчитать свои пользовательские функции, не записывая их сначала на листе. Пожалуйста, используйте[**Worksheet.CalculateFormula (строковая формула, параметры CalculationOptions)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)метод для этой цели.

См. следующий пример кода, иллюстрирующий использование этого метода. Мы использовали пользовательскую функцию с именем MyCompany.CustomFunction() и вычислили ее значение как «Aspose.Cells». мы сами, а затем это значение автоматически объединяется со значением ячейки A1, которое является «Добро пожаловать», механизмом расчета, и окончательное вычисленное значение возвращается как «Добро пожаловать в Aspose.Cells». Как вы можете видеть в коде, который у нас есть наша пользовательская функция не написана нигде на листе, и она вычисляется непосредственно с помощью нашей собственной пользовательской логики.

### **Образец программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Консольный вывод**

Ниже приведен консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Реализовать пользовательский механизм расчета, чтобы расширить механизм расчета по умолчанию Aspose.Cells.](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
