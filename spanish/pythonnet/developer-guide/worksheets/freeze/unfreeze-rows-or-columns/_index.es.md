---
title: Descongelar Filas o Columnas
linktitle: Descongelar paneles
type: docs
weight: 190
url: /es/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: En este artículo, aprenderás cómo desbloquear filas, columnas o paneles de hojas de Excel mediante programación usando las APIs de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, Desbloquear paneles en Python, Cómo desbloquear filas en Python, Cómo desbloquear columnas en Python, Cómo desbloquear ventana en Python.
---

## **Introducción**

En este artículo, aprenderemos cómo deshacer la congelación de filas, columnas y paneles. Si las hojas de cálculo de los archivos de Excel están congeladas, a veces queremos descongelar la hoja de cálculo o ajustar las filas, columnas o paneles congelados.


## **Cómo desbloquear filas o columnas en Excel**

1. Haz clic en la pestaña Vista > Congelar paneles > Descongelar paneles.

**![descongelar paneles en Excel](Unfreeze-Panes.png)**




## **Cómo desbloquear filas, columnas o paneles con Aspose.Cells para Python Biblioteca de Excel**
Es sencillo desbloquear paneles con Aspose.Cells para Python via .NET. Utiliza el método [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) para desbloquear paneles.

1. Construye el libro para abrir el archivo congelado.
2. Descongela los paneles con el método Worksheet.UnFreezePanes().
3. Guarda el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Adjunto [archivo de Excel de origen de ejemplo](Frozen.xlsx).
{{< app/cells/assistant language="python-net" >}}
