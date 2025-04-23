---
title: Conversión entre el nombre de la celda y el índice de fila/columna
linktitle: Conversión entre Nombre de Celda e Índice
type: docs
weight: 10
url: /es/net/names-and-indices/
description: Aprenda cómo obtener la conversión entre el nombre de la celda y el índice de fila/columna a través de la API Aspose.Cells for .NET.
keywords: Obtener el nombre de la celda a partir de los índices de fila y columna, obtener los índices de fila y columna a partir del nombre de la celda, crear nombres seguros de hojas de cálculo, agregar nombres seguros de hojas de cálculo
---

## **Obtener el nombre de celda a partir de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells proporciona el método CellsHelper.CellIndexToName que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

Microsoft Excel comienza a contar los índices de filas y columnas desde 1. A diferencia de Microsoft Excel, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar CellsHelper.CellIndexToName para acceder al nombre de la celda dado un índice de fila y columna conocido. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Obtener Índices de Fila y Columna a partir del Nombre de la Celda**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells proporciona el método CellsHelper.CellNameToIndex que permite a los desarrolladores obtener los índices de fila y columna a partir del nombre de la celda.

{{% alert color="primary" %}} 

Microsoft Excel comienza a contar los índices de filas y columnas desde 1. A diferencia de Microsoft Excel, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar CellsHelper.CellNameToIndex para obtener los índices de fila y columna a partir del nombre de la celda. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Crear nombres seguros de hoja**
A veces es necesario asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hojas que contengan algunos caracteres adicionales como <>+(?”. Es necesario reemplazar cualquier carácter de este tipo, que no esté permitido como nombre de hoja, con algún carácter predefinido proporcionado por el usuario. Del mismo modo, la longitud puede aumentar a más de 31 caracteres, que necesita ser truncada. Apache POI proporciona ciertas características para crear nombres seguros, por lo tanto, se proporciona una característica similar por Aspose.Cells para manejar todos estos problemas. El siguiente código de ejemplo demuestra esta característica:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Salida:

este es el primer nombre que se creó

` <>(adj. Privado _ " Privado"
{{< app/cells/assistant language="csharp" >}}
