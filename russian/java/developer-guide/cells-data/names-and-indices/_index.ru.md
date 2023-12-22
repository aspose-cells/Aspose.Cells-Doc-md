---
title: Преобразование между именем ячейки и индексом строки/столбца
linktitle: Cell Преобразование имени и индекса
type: docs
weight: 5
url: /ru/java/names-and-indices/
description: Узнайте, как получить результат преобразования между именем ячейки и индексом строки/столбца с помощью API Aspose.Cells for Java.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **Как получить имя Cell из индексов строк и столбцов**
Можно найти имя ячейки по индексу строки и столбца. В этой статье объясняется, как это сделать.

 Aspose.Cells обеспечивает[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) метод, который позволяет разработчикам получить имя ячейки, если они предоставили индекс строки и столбца.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает отсчет индексов строк и столбцов с 0.

{{% /alert %}} 

 Следующий пример кода иллюстрирует, как использовать[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) для доступа к имени ячейки, заданному по известному индексу строки и столбца. Код генерирует следующий вывод.



Cell Имя в [0, 0]: A1

Cell Имя в [4, 0]: A5

Cell Имя в [0, 4]: E1

Cell Имя в [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **Как получить индексы строк и столбцов из имени Cell**
По ее названию можно найти индекс строки и столбца ячейки. В этой статье объясняется, как это сделать.

 Aspose.Cells обеспечивает[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) метод, который позволяет разработчикам получить индекс строки и столбца из имени ячейки.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает отсчет индексов строк и столбцов с 0.

{{% /alert %}} 

 Следующий пример кода иллюстрирует, как использовать[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)), чтобы получить индекс строки и столбца из имени ячейки. Код генерирует следующий вывод.



Индекс строки Cell C6:5

Индекс колонки Cell C6:2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **Как создать имена безопасных листов**
 Иногда возникает необходимость назначить имя листа во время выполнения. В этом сценарии могут быть имена листов, которые могут содержать дополнительные символы, например<>+(?». Любой такой символ, который не допускается в качестве имени листа, необходимо заменить каким-либо предустановленным символом, предоставленным пользователем. Аналогично, длина может увеличиться до более чем 31 символа, который необходимо усечь. Apache POI предоставляет определенные функции создания безопасных имен, поэтому для решения всех этих проблем аналогичная функция предусмотрена в Aspose.Cells. Следующий пример кода демонстрирует эту функцию:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Консольный вывод**

это имя, которое является Cre

` `<> + (прил.Частный _ «Частный»
