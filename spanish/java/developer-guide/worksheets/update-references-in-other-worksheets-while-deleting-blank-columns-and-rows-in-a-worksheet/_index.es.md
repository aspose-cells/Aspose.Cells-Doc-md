---
title: Actualice referencias en otras hojas de trabajo mientras elimina columnas y filas en blanco en una hoja de trabajo
type: docs
weight: 700
url: /es/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Cuando elimina columnas y filas en blanco en una hoja de trabajo, sus referencias en otras hojas de trabajo dejan de ser válidas. Si desea evitar este comportamiento y desea que esas referencias también se actualicen, utilice el[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) y configurarlo**verdadero**.

{{% /alert %}} 
## **Actualice referencias en otras hojas de trabajo mientras elimina columnas y filas en blanco en una hoja de trabajo**
 Consulte el siguiente código de ejemplo y su salida de consola. La celda E3 de la segunda hoja de trabajo tiene una fórmula =Hoja1!C3 que hace referencia a la celda C3 de la primera hoja de trabajo. si vas a establecer[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) propiedad como**verdadero** , esta fórmula se actualizará y se convertirá en =Sheet1!A1 al eliminar columnas y filas en blanco en la primera hoja de trabajo. Sin embargo, si establece[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) propiedad como**falso**, la fórmula en la celda E3 de la segunda hoja de cálculo seguirá siendo =Hoja1!C3 y dejará de ser válida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Salida de consola**
Esta es la salida de la consola del código de muestra anterior cuando[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) la propiedad se ha establecido como**verdadero**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Esta es la salida de la consola del código de muestra anterior cuando[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) la propiedad se ha establecido como**falso**. Como puede ver, la fórmula en la celda E3 de la segunda hoja de trabajo no se actualiza y su valor de celda ahora es 0 en lugar de 4, lo cual no es válido.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
