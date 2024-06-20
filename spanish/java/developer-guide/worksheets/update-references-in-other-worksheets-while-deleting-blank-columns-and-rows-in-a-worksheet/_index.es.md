---
title: Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo
type: docs
weight: 700
url: /es/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

Cuando elimina columnas y filas en blanco en una hoja de cálculo, entonces sus referencias en otras hojas de cálculo se vuelven inválidas. Si desea evitar este comportamiento y desea que esas referencias también se actualicen, entonces utilice [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) y configúrelo como **true**.

{{% /alert %}} 
## **Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo**
Por favor, consulte el siguiente código de ejemplo y su salida por consola. La celda E3 en la segunda hoja de cálculo tiene una fórmula =Sheet1!C3 que se refiere a la celda C3 en la primera hoja de cálculo. Si configura la propiedad [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) como **true**, esta fórmula se actualizará y se convertirá en =Sheet1!A1 al eliminar columnas y filas en blanco en la primera hoja de cálculo. Sin embargo, si configura la propiedad [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) como **false**, la fórmula en la celda E3 de la segunda hoja de cálculo seguirá siendo =Sheet1!C3 y será inválida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Salida de la consola**
Esta es la salida por consola del código de ejemplo anterior cuando la propiedad [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) se ha configurado como **true**.

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

Esta es la salida por consola del código de ejemplo anterior cuando la propiedad [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) se ha configurado como **false**. Como puede ver, la fórmula en la celda E3 de la segunda hoja de cálculo no se actualiza y su valor de celda ahora es 0 en lugar de 4, lo cual es inválido.

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
