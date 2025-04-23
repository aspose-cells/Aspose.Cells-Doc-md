---
title: Прямой расчет пользовательской функции без записи ее в рабочий лист
type: docs
weight: 650
url: /ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Эта статья объясняет, как вы можете прямо вычислять ваши пользовательские функции без предварительного их написания в листе. Пожалуйста, используйте метод [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) для этой цели.

{{% /alert %}} 
## **Прямой расчет пользовательской функции без записи ее на лист**
Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, иллюстрирующим использование этого метода. Мы использовали пользовательскую функцию *MyCompany.CustomFunction()* и вычисляем ее значение как *"Aspose.Cells."* сами, затем это значение автоматически конкатенируется с значением ячейки A1, которое равно *"Welcome to "*, двигатель вычисления и возвращает итоговое вычисленное значение как *"Welcome to Aspose.Cells."*. Как видно из кода, мы нигде не записали нашу пользовательскую функцию на листе, и она вычисляется непосредственно нашей собственной пользовательской логикой.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Вывод в консоль**
Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Связанная статья**
{{% alert color="primary" %}} 

- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
