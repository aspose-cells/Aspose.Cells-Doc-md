---
title: Eliminar rangos con nombres
type: docs
weight: 90
url: /es/net/Delete-named-ranges/
description: Puede aprender cómo eliminar nombres definidos o rangos con nombre de archivos de Excel u OpenOffice con Aspose.Cells para .Net.
---

## **Introducción**
Si hay demasiados nombres definidos o rangos con nombre en los archivos de Excel, debemos eliminar algunos para que no se vuelvan a hacer referencia.

## **Eliminar rango con nombre en MS Excel**

Para eliminar un rango con nombre en Excel, siga estos pasos:
1. Abra Microsoft Excel y abra el libro que contiene el rango con nombre.
2. Vaya a la pestaña "Fórmulas" en la cinta de Excel.
3. Haga clic en el botón "Administrador de nombres" en el grupo "Nombres definidos". Esto abrirá la ventana de diálogo del Administrador de nombres.
4. En la ventana de diálogo del Administrador de nombres, seleccione el rango con nombre que desea eliminar.
5. Haga clic en el botón "Eliminar". Confirme la eliminación cuando se lo soliciten.
6. Haz clic en el botón "Cerrar" para cerrar el cuadro de diálogo del Administrador de nombres.
7. Guarda el libro para guardar los cambios.


## **Elimina el rango con nombre usando Aspose.Cells for .Net**
Con Aspose.Cells for .Net, puedes quitar rangos con nombre o nombres definidos por [text](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove)  o [index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) en la lista.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Nota: si el nombre definido es referido por fórmulas, no se puede eliminar. Solo podemos quitar la fórmula del nombre definido.

## **Eliminar algunos rangos con nombre**
Cuando eliminamos un nombre definido, debemos verificar si está referido por todas las fórmulas en el archivo.
Para mejorar el rendimiento al eliminar rangos con nombre, podemos eliminar algunos juntos.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **Eliminar nombres definidos duplicados**
Algunos archivos de Excel se corrompen porque algunos nombres definidos son duplicados. Entonces podemos eliminar estos nombres duplicados para reparar el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



