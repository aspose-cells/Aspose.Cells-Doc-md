---
title: Обнаружение циклической ссылки
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для обнаружения циклических ссылок в Microsoft Excel. Загрузив существующий файл Excel или создав новый, мы можем использовать метод, предоставленный Aspose.Cells, для обнаружения циклических ссылок и получения результатов. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /ru/net/detecting-circular-reference/
---
##  **Введение**

В книгах могут быть циклические ссылки, и иногда необходимо определить, есть ли циклические ссылки или нет.

##  **Концепция обнаружения циклической ссылки**

Циклические ссылки можно обнаружить только при вычислении формулы, поскольку ссылки одной формулы обычно зависят от вычисленного результата других частей или других формул. Поэтому мы предоставляем новые API для этого требования (для сбора ячеек с циклическими ссылками) в процессе вычисления формулы:

[**РасчетЯчейка**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): представляет расчет соответствующих данных об одной вычисляемой ячейке.

[**AbstractCalculationMonitor.OnCircular (IEnumeratorcircularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): будет вызываться механизмом вычисления формул при обнаружении циклических ссылок, элемент в перечислителе[**РасчетЯчейка**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) объекты, которые представляют все ячейки в одном круге. Возвращаемое значение указывает, нужно ли обработчику формул вычислять эти ячейки по кругу после этого вызова.

 Пользователь может собирать эти циклические ссылки при реализации[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) метод.

Исходный файл примера можно скачать по следующей ссылке:

[Круговые формулы.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Значение*КруговойМонитор* класс, который является производным от[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) класс следующий:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
