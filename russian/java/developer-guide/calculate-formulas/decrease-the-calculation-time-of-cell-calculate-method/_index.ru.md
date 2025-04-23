---
title: Уменьшить время вычисления метода Cell.Calculate
type: docs
weight: 860
url: /ru/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Возможные сценарии использования

Обычно мы рекомендуем пользователям вызывать метод [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) один раз, а затем получать рассчитанные значения отдельных ячеек. Но иногда пользователи не хотят вычислять всю книгу. Они просто хотят вычислить одну ячейку. Aspose.Cells предоставляет свойство [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive), которое можно установить в **false**, и это значительно уменьшит время вычислений для отдельной ячейки. Потому что, когда рекурсивное свойство установлено в **true**, все зависимые ячейки пересчитываются при каждом вызове. Но при установке свойства в **false** зависимые ячейки вычисляются только один раз и не пересчитываются при последующих вызовах.
## **Уменьшение времени вычисления метода Cell.Calculate()**
Приведенный ниже образец кода иллюстрирует использование свойства [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). Пожалуйста, выполните этот код с данным [образцом файла Excel](5472288.xlsx) и проверьте его вывод в консоли. Вы увидите, что установка свойства рекурсии в **false** значительно сократила время вычислений. Пожалуйста, также ознакомьтесь с комментариями для лучшего понимания этого свойства.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Вывод в консоль**
Это вывод консоли вышеуказанного образца кода при выполнении с данным [образцом файла Excel](5472288.xlsx) на нашем устройстве. Обратите внимание, что ваш вывод может отличаться, но затраченное время после установки свойства рекурсии в **false** всегда будет меньше, чем при установке его в **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
