---
title: Conversión entre el nombre de la celda y el índice de fila/columna
linktitle: Conversión entre Nombre de Celda e Índice
type: docs
weight: 10
url: /es/python-net/names-and-indices/
description: Aprenda a obtener la conversión entre el nombre de la celda y el índice de fila/columna a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Obtener el nombre de la celda a partir de índices de fila y columna con Python, Obtener los índices de fila y columna a partir del nombre de la celda con Python, Crear nombres seguros de hojas de trabajo con Python, Agregar nombres seguros de hojas de trabajo con Python
---

## **Obtener el nombre de celda a partir de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells for Python via .NET proporciona el método [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int), que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de fila y columna empiezan en 1, Aspose.Cells para Python via .NET comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de muestra ilustra cómo usar [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) para acceder al nombre de la celda dado un índice de fila y columna conocido. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Obtener Índices de Fila y Columna a partir del Nombre de la Celda**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells para Python via .NET proporciona el método [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) que permite a los desarrolladores obtener un índice de fila y columna a partir del nombre de la celda.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de fila y columna empiezan en 1, Aspose.Cells para Python via .NET comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de muestra ilustra cómo usar [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) para obtener el índice de fila y columna a partir del nombre de la celda. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Crear nombres seguros de hoja**
A veces es necesario asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hoja que contengan algunos caracteres adicionales como <>+(?”. Es necesario reemplazar cualquier característica que no esté permitida como nombre de hoja con algún carácter preestablecido proporcionado por el usuario. De manera similar, la longitud puede aumentar a más de 31 caracteres que necesitan ser truncados. Apache POI proporciona ciertas características de creación de nombres seguros, por lo tanto, se proporciona una función similar por Aspose.Cells para Python via .NET para manejar todos estos problemas. El siguiente código de muestra demuestra esta característica:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Salida:

este es el primer nombre que se creó

` <>(adj. Privado _ " Privado"
{{< app/cells/assistant language="python-net" >}}
