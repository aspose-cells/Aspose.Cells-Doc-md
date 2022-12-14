---
title: Conversión entre nombre de celda e índice de fila/columna
linktitle: Cell Conversión de nombres e índices
type: docs
weight: 10
url: /es/net/names-and-indices/
---
## **Obtenga el nombre Cell de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells proporciona el método CellsHelper.CellIndexToName que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar CellsHelper.CellIndexToName para acceder al nombre de la celda dado un índice de fila y columna conocido. El código genera el siguiente resultado.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Obtener índices de fila y columna de Cell Nombre**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells proporciona el método CellsHelper.CellNameToIndex que permite a los desarrolladores obtener un índice de fila y columna del nombre de la celda.

{{% alert color="primary" %}} 

diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar CellsHelper.CellNameToIndex para obtener el índice de fila y columna del nombre de la celda. El código genera el siguiente resultado.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Crear nombres de hojas seguras**
 A veces es necesario asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hojas que pueden contener algunos caracteres adicionales como<>+(?”. Es necesario reemplazar cualquier carácter de este tipo, que no está permitido como nombre de hoja con algún carácter preestablecido proporcionado por el usuario. De manera similar, la longitud puede aumentar a más de 31 caracteres que deben truncarse. Apache POI proporciona ciertas funciones de creación de nombres seguros, por lo tanto, Aspose.Cells proporciona una función similar para manejar todos estos problemas. El siguiente código de muestra demuestra esta función:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Producción:

este es el primer nombre que es cre

` `<> + (adj.Privado _ "Privado"
