---
title: Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo
type: docs
weight: 5000
url: /es/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

Cuando eliminas columnas y filas en blanco en una hoja de cálculo, sus referencias en otras hojas de cálculo se vuelven inválidas. Si deseas evitar este comportamiento y que esas referencias de la hoja de cálculo actual en otras hojas de cálculo también se actualicen, entonces por favor utiliza la propiedad [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) y configúrala como **true**.

{{% /alert %}}

## **Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo**

Por favor, consulta el siguiente código de muestra y su salida en consola. La celda E3 en la segunda hoja de cálculo tiene una fórmula =Sheet1!C3 que se refiere a la celda C3 en la primera hoja de cálculo. Si configuras la propiedad [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) como **true**, esta fórmula se actualizará y se convertirá en =Sheet1!A1 al eliminar columnas y filas en blanco en la primera hoja de cálculo. Sin embargo, si configurar [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) como **false**, la fórmula en la celda E3 de la segunda hoja de cálculo seguirá siendo =Sheet1!C3 y se volverá inválida.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Salida de la consola**

Esta es la salida en consola del código de muestra anterior cuando la propiedad [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) se ha configurado como **true**.

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

Esta es la salida de la consola del código de ejemplo anterior cuando la propiedad [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) se establece como **false**. Como se puede ver, la fórmula en la celda E3 de la segunda hoja de cálculo no se actualiza y su valor de celda ahora es 0 en lugar de 4, lo cual es inválido.

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
