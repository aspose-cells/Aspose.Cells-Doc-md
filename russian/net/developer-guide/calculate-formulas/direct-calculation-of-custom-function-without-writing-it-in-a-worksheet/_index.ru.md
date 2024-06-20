---
title: Прямой расчет пользовательской функции без записи ее в рабочий лист
description: Эта статья представляет, как использовать библиотеку Aspose.Cells для прямого расчета пользовательских функций в Microsoft Excel без записи функции в рабочем листе. Загружая существующий файл Excel или создавая новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для расчета пользовательской функции и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, пользовательские функции, прямые расчеты, нет необходимости в написании, рабочие листы
type: docs
weight: 90
url: /ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Прямой расчет пользовательской функции без записи ее на лист**

В данной теме объясняется, как можно прямо рассчитать пользовательские функции без предварительной записи их в рабочем листе. Пожалуйста, используйте метод [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) для этой цели.

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, иллюстрирующим использование этого метода. Мы использовали пользовательскую функцию MyCompany.CustomFunction() и рассчитываем ее значение как "Aspose.Cells." сами, после чего это значение автоматически конкатенируется со значением ячейки A1, которая равна "Добро пожаловать в " движком расчета, и окончательное рассчитанное значение возвращается как "Добро пожаловать в Aspose.Cells.". Как видно из кода, мы не писали нашу пользовательскую функцию где-либо на рабочем листе, и она рассчитывается напрямую нашей собственной пользовательской логикой.

### **Пример программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Вывод в консоль**

Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Реализация собственного расчетного механизма для расширения стандартного расчетного механизма Aspose.Cells](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
