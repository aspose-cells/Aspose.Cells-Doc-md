##Conversion between cell name and row/column index
Learn how to get Conversion result between cell name and row/column index with Aspose.Cells for Java APIs.
## **How to Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.
Aspose.Cells provides the [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) method which allows developers to get a cell's name if they provide the row and column index.
Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.
The following sample code illustrates how to use [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) to access the cell's name given at a known row and column index. The code generates the following output.
Cell Name at [0, 0]: A1
Cell Name at [4, 0]: A5
Cell Name at [0, 4]: E1
Cell Name at [2, 2]: C3
## **How to Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.
Aspose.Cells provides the [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) method which allows developers to get a row and column index from the cell's name.
Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.
The following sample code illustrates how to use [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) to get the row and column index from the cell's name. The code generates the following output.
Row Index of Cell C6: 5
Column Index of Cell C6: 2
## **How to Create safe sheet names**
Sometimes there is a need for assigning the sheet name at runtime. In this scenario, there may be sheet names which may contain some additional characters like <>+(?”. There is a need to replace any such character, which is not allowed as a sheet name with some preset character provided by the user. Similarly, the length may increase to more than 31 characters which needs to be truncated. Apache POI provides certain features of creating safe names, hence similar feature is provided by Aspose.Cells to handle all these issues. Following sample code demonstrates this feature:
**Console Output**
this is first name which is cre
` `<> + (adj.Private _ " Private"
