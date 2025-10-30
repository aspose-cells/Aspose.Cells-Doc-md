---
title: Eliminar rangos nombrados con Golang vía C++
linktitle: Eliminar rangos con nombres
type: docs
weight: 90
url: /es/go-cpp/delete-named-ranges/
description: Aprenda cómo eliminar nombres definidos o rangos con nombre de archivos de Excel o OpenOffice usando Aspose.Cells for C++.
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

## **Elimina Rango con Nombre usando Aspose.Cells for C++**
Con Aspose.Cells for C++, puedes eliminar rangos nombrados o nombres definidos por [texto](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/) o [índice](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) en la lista.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
Nota: si el nombre definido es referido por fórmulas, no se puede eliminar. Solo se puede eliminar la fórmula del nombre definido.

## **Eliminar algunos rangos con nombre**
Cuando eliminamos un nombre definido, debemos verificar si está referido por todas las fórmulas en el archivo.
Para mejorar el rendimiento de la eliminación de rangos con nombre, podemos eliminar algunos juntos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **Eliminar nombres definidos duplicados**
Algunos archivos de Excel se corrompen porque algunos nombres definidos están duplicados. Por lo tanto, podemos eliminar estos nombres duplicados para reparar el archivo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
