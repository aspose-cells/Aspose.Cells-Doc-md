---
title: Преобразование между именем ячейки и индексом строки/столбца
linktitle: Cell Преобразование имени и индекса
type: docs
weight: 5
url: /ru/java/names-and-indices/
---
## **Получить имя Cell из индексов строк и столбцов**
Можно найти имя ячейки по индексу строки и столбца. В этой статье объясняется, как.

 Aspose.Cells обеспечивает[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)), который позволяет разработчикам получить имя ячейки, если они предоставляют индекс строки и столбца.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает подсчет индексов строк и столбцов с 0.

{{% /alert %}} 

 В следующем примере кода показано, как использовать[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) для доступа к имени ячейки, указанному в известном индексе строки и столбца. Код генерирует следующий вывод.



Cell Имя в [0, 0]: A1

Cell Имя в [4, 0]: A5

Cell Имя в [0, 4]: E1

Cell Имя в [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Получить индексы строк и столбцов из имени Cell**
Можно найти индекс строки и столбца ячейки по ее имени. В этой статье объясняется, как.

 Aspose.Cells обеспечивает[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)), который позволяет разработчикам получить индекс строки и столбца из имени ячейки.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает подсчет индексов строк и столбцов с 0.

{{% /alert %}} 

 В следующем примере кода показано, как использовать[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)), чтобы получить индекс строки и столбца из имени ячейки. Код генерирует следующий вывод.



Индекс строки Cell C6: 5

Индекс столбца Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Создать безопасные имена листов**
Иногда возникает необходимость присвоить имя листу во время выполнения. В этом случае могут быть имена листов, которые могут содержать некоторые дополнительные символы, такие как<>+(?”. Необходимо заменить любой такой символ, который не разрешен в качестве имени листа, на какой-либо предустановленный символ, предоставленный пользователем. Точно так же длина может увеличиться до более чем 31 символа, который необходимо усечь. Apache POI предоставляет определенные функции для создания безопасных имен, поэтому для решения всех этих проблем предусмотрена аналогичная функция Aspose.Cells. Следующий пример кода демонстрирует эту функцию:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Консольный вывод**

это имя, которое является cre

` `<> + (прил.Частный _ "Частный"
