---
title: Прямой расчет пользовательской функции без записи ее на листе
type: docs
weight: 650
url: /ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 В этой статье объясняется, как можно напрямую рассчитать свои пользовательские функции без предварительного написания их на листе. Пожалуйста, используйте[Worksheet.calculateFormula (строковая формула, параметры CalculationOptions)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) метод для этой цели.

{{% /alert %}} 
## **Прямой расчет пользовательской функции без записи ее на листе**
См. следующий пример кода, иллюстрирующий использование этого метода. Мы использовали пользовательскую функцию с именем*МояКомпания.ПользовательскаяФункция()*и мы вычисляем его значение как «Aspose.Cells». самостоятельно, а затем это значение автоматически объединяется со значением ячейки A1, которое является «Добро пожаловать в», с помощью механизма расчета, и окончательное вычисленное значение возвращается как «Добро пожаловать в Aspose.Cells». Как вы можете видеть в коде, мы не написали нашу пользовательскую функцию нигде на листе, и она вычисляется непосредственно с помощью нашей собственной пользовательской логики.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Консольный вывод**
Ниже приведен консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Связанная статья**
{{% alert color="primary" %}} 

- [Реализовать пользовательский механизм расчета, чтобы расширить механизм расчета по умолчанию Aspose.Cells.](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
