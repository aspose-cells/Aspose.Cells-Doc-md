---
title: Congelar paneles de la hoja de cálculo de Excel
linktitle: Congelar paneles
type: docs
weight: 190
url: /es/python-net/how-to-freeze-panes-of-excel-worksheet
description: En este artículo, aprenderá cómo congelar paneles de hojas de Excel de forma programática utilizando las APIs de Aspose.Cells for Python via .NET.
keywords: Biblioteca de Python Excel, congelar paneles de Python, congelar ventana en Python.
---

## **Introducción**

En este artículo, aprenderemos cómo congelar paneles. Cuando tiene una gran cantidad de datos bajo un encabezado común y no puede ver el encabezado al desplazarse por la hoja de cálculo. Y cada registro contiene muchos datos. Puede congelar paneles para que pueda ver esa parte congelada incluso cuando el resto de los datos se están desplazando. Puede ver fácilmente los encabezados en las primeras filas o columnas. Congelar y descongelar los paneles solo cambia la vista de los datos sin cambiar los datos mismos.

## ***Cómo congelar paneles en Excel**

**![Congelar paneles en Excel](Congelar-paneles.png)**


1. Si desea congelar paneles, congelar filas y columnas, primero seleccione una celda (como B2)
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haga clic en Congelar paneles.
4. Si se desplaza hacia abajo o hacia la derecha, la primera fila y columna quedarán congeladas.

**![Paneles congelados](Frozen-Panes.png)**

Como puedes ver, la primera fila y la columna A están congeladas, la segunda fila es 32 y la segunda columna visible es D. 

Los paneles congelados te permiten ver tus datos extensos sin necesidad de estar pendiente de la etiqueta de fila o columna.




## **Cómo congelar paneles con la Biblioteca de Python Excel de Aspose.Cells**
Es sencillo congelar paneles con Aspose.Cells for Python via .NET. Por favor, utilice el método [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) para congelar los paneles en la celda seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congela paneles con el método Worksheet.FreezePanes().
3. Guarda el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
