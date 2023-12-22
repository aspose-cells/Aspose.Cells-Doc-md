---
title: Eliminar rangos con nombre
type: docs
weight: 90
url: /es/net/Delete-named-ranges/
description: Puede aprender cómo eliminar nombres definidos o rangos de nombres de archivos de Excel u OpenOffice con Aspose.Cells para .Net.
---
##  **Introducción**
Si hay demasiados nombres definidos o rangos con nombres en los archivos de Excel, debemos borrar algunos para que no se vuelvan a hacer referencia a ellos.

##  **Eliminar rango con nombre en MS Excel**

Para eliminar un rango con nombre de Excel, puede seguir estos pasos:
1. Abra Microsoft Excel y abra el libro que contiene el rango nombrado.
2. Vaya a la pestaña "Fórmulas" en la cinta de Excel.
3. Haga clic en el botón "Administrador de nombres" en el grupo "Nombres definidos". Esto abrirá el cuadro de diálogo Administrador de nombres.
4. En el cuadro de diálogo Administrador de nombres, seleccione el rango con nombre que desea eliminar.
5. Haga clic en el botón "Eliminar". Confirme la eliminación cuando se le solicite.
6. Haga clic en el botón "Cerrar" para cerrar el cuadro de diálogo Administrador de nombres.
7. Guarde el libro de trabajo para conservar los cambios.


##  ** Elimina el rango con nombre usando Aspose.Cells para .Net**
 Con Aspose.Cells para .Net, puede eliminar rangos con nombres o nombres definidos mediante[texto](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) o[índice](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) en la lista.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Nota: si el nombre definido está referenciado por fórmulas, no se podrá eliminar. Solo podemos eliminar la fórmula del nombre definido.

##  **Elimina algunos rangos con nombre**
Cuando eliminamos un nombre definido, tenemos que comprobar si todas las fórmulas del archivo hacen referencia a él.
Para mejorar el rendimiento de la eliminación de rangos con nombre, podemos eliminar algunos juntos.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **Eliminar nombres definidos duplicados**
Algunos campos de Excel están dañados porque algunos nombres definidos están duplicados. Entonces podemos eliminar estos nombres duplicados para reparar el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



