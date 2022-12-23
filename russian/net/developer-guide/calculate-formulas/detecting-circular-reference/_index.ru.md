---
title: Обнаружение циклической ссылки
type: docs
weight: 70
url: /ru/net/detecting-circular-reference/
---
## **Вступление**

Рабочие книги могут иметь циклические ссылки, и иногда необходимо определить, есть ли циклические ссылки или нет.

## **Концепция обнаружения циклической ссылки**

Циклические ссылки могут быть обнаружены только при вычислении формулы, поскольку ссылки одной формулы обычно зависят от результата вычисления других частей или других формул. Поэтому мы предоставляем новые API для этого требования (для сбора ячеек с циклическими ссылками) в процессе вычисления формулы:

[**Расчетная ячейка**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Представляет вычисление релевантных данных об одной вычисляемой ячейке.

[**AbstractCalculationMonitor.OnCircular (IEnumerator circleCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): будет вызываться механизмом расчета формулы при встрече с циклическими ссылками, элемент в перечислителе[**Расчетная ячейка**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) объекты, которые представляют все клетки в одном круге. Возвращаемое значение указывает, нужно ли обработчику формул вычислять эти ячейки по кругу после этого вызова.

 Пользователь может собирать эти циклические ссылки при реализации[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) метод.

Исходный образец файла можно скачать по следующей ссылке:

[Круговые формулы.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Значение*ЦиркулярМонитор* класс, производный от[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) класс выглядит следующим образом:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
