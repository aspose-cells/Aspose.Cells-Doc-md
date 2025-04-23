---
title: Преобразование между именем ячейки и индексом строки/столбца
linktitle: Преобразование имени ячейки и индекса
type: docs
weight: 5
url: /ru/java/names-and-indices/
description: Узнайте, как получить результат преобразования между именем ячейки и индексом строки/столбца с помощью Aspose.Cells for Java API.
keywords: Java. Преобразование индекса ячейки в имя, преобразование имени ячейки в индекс строки/столбца с использованием Java API, как получить имя ячейки из индексов строки и столбца с помощью Java, Java. Как получить индексы строки и столбца из имени ячейки.
---

## **Как получить имя ячейки из индексов строки и столбца**
Возможно определить имя ячейки по индексам строки и столбца. В этой статье объясняется как это сделать.

Aspose.Cells предоставляет метод [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-), который позволяет разработчикам получить имя ячейки, предоставляя индекс строки и столбца.

{{% alert color="primary" %}} 

Microsoft Excel начинает нумерацию индексов строк и столбцов с 1. В отличие от Microsoft Excel, Aspose.Cells начинает нумерацию индексов строк и столбцов с 0.

{{% /alert %}} 

Следующий пример кода показывает, как использовать [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) для получения имени ячейки при заданных известных индексах строки и столбца. Код выводит следующий результат.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Как получить индексы строки и столбца из имени ячейки**
Возможно определить индекс строки и столбца ячейки по ее имени. В этой статье объясняется как это сделать.

Aspose.Cells предоставляет метод [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-), который позволяет разработчикам получить индекс строки и столбца из имени ячейки.

{{% alert color="primary" %}} 

Microsoft Excel начинает нумерацию индексов строк и столбцов с 1. В отличие от Microsoft Excel, Aspose.Cells начинает нумерацию индексов строк и столбцов с 0.

{{% /alert %}} 

Следующий пример кода показывает, как использовать [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) для получения индексов строки и столбца по имени ячейки. Код выводит следующий результат.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Как создать безопасные имена листов**
Иногда есть необходимость назначать имя листа во время выполнения программы. В этом сценарии может потребоваться использовать имена листов, которые могут содержать дополнительные символы, такие как <>+(?”. Необходимо заменить любой такой символ, который не допускается в качестве имени листа, на некоторый предварительно установленный пользователем символ. Аналогично, длина имени может превысить 31 символ, и ее следует сократить. Apache POI предоставляет определенные функции для создания безопасных имен, аналогичная функция предоставляется Aspose.Cells для обработки всех этих проблем. Приведенный ниже образец кода демонстрирует эту функцию:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Вывод в консоль**

это первое имя, которое создано

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
