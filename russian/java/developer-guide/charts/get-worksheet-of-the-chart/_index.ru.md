---
title: Получить рабочий лист диаграммы
type: docs
weight: 80
url: /ru/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Иногда вам нужно получить доступ к листу рабочей книги из ссылки на диаграмму. Aspose.Cells предоставляет свойство [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet), которое возвращает ссылку на лист рабочей книги, содержащий диаграмму.

{{% /alert %}}

## Пример

В следующем примере показано, как использовать свойство [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet). Сначала код выводит имя листа, затем получает доступ к первой диаграмме на листе. Затем он снова выводит имя листа, используя свойство [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet).

### Пример Java-кода для доступа к листу диаграммы

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Вывод консоли, сгенерированный примерным кодом

Ниже приведен вывод консоли, к которому приводит результат примерного кода. Как видите, он печатает то же имя листа в обоих случаях.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
