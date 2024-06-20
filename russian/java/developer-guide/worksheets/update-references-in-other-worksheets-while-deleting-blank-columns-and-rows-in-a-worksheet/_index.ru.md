---
title: Обновление ссылок в других листах при удалении пустых столбцов и строк на листе
type: docs
weight: 700
url: /ru/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

При удалении пустых столбцов и строк на листе его ссылки в других листах становятся недопустимыми. Если вы хотите избежать этого поведения и хотите, чтобы эти ссылки также обновлялись, пожалуйста, используйте [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) и установите ее значение **true**.

{{% /alert %}} 
## **Обновление ссылок в других листах при удалении пустых столбцов и строк на листе**
Пожалуйста, ознакомьтесь с приведенным ниже образцом кода и его выводом в консоли. Ячейка E3 на втором листе имеет формулу =Sheet1!C3, которая ссылается на ячейку C3 на первом листе. Если вы установите свойство [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) как **true**, эта формула будет обновлена и станет равной =Sheet1!A1 после удаления пустых столбцов и строк на первом листе. Однако, если вы установите свойство [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) как **false**, формула в ячейке E3 на втором листе останется =Sheet1!C3 и станет недопустимой.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Вывод в консоль**
Это вывод в консоль приведенного выше образца кода, когда свойство [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) установлено в **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Это вывод в консоль приведенного выше образца кода, когда свойство [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) установлено в **false**. Как видно, формула в ячейке E3 на втором листе не обновляется, и ее значение ячейки теперь равно 0 вместо 4, что недопустимо.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
