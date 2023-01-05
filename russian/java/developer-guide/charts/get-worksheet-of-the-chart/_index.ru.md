---
title: Получить рабочий лист диаграммы
type: docs
weight: 80
url: /ru/java/get-worksheet-of-the-chart/
---
{{% alert color="primary" %}}

Иногда вы хотите получить доступ к рабочему листу из ссылки на диаграмму. Aspose.Cells обеспечивает[**Диаграмма.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) свойство, которое возвращает ссылку на рабочий лист, содержащий диаграмму.

{{% /alert %}}

## Пример

 В следующем примере показано, как использовать[**Диаграмма.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) имущество. Код сначала печатает имя рабочего листа, а затем обращается к первой диаграмме на рабочем листе. Затем он снова печатает имя рабочего листа, используя[**Диаграмма.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)имущество.

### Java код для доступа к рабочему листу диаграммы

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Консольный вывод, сгенерированный примером кода

Ниже приведен вывод консоли, к которому приводит пример кода. Как вы можете видеть, он печатает одно и то же имя рабочего листа оба раза.

{{< highlight "java" >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
