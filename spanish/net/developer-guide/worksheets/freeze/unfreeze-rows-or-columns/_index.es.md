---
title: Descongelar Filas o Columnas
linktitle: Descongelar paneles
type: docs
weight: 190
url: /es/net/unfreeze-rows-or-columns-of-excel-worksheet
description: En este artículo, aprenderás cómo descongelar filas, columnas o paneles de hojas de cálculo de Excel programáticamente utilizando la biblioteca C# con API .NET.
keywords: Descongelar paneles, Descongelar filas, Descongelar columnas, descongelar ventana.
---

## **Introducción**

En este artículo, aprenderemos cómo deshacer la congelación de filas, columnas y paneles. Si las hojas de cálculo de los archivos de Excel están congeladas, a veces queremos descongelar la hoja de cálculo o ajustar las filas, columnas o paneles congelados.


## **En Excel**

1. Haz clic en la pestaña Vista > Congelar paneles > Descongelar paneles.

**![descongelar paneles en Excel](Unfreeze-Panes.png)**




## **Descongela Filas, Columnas o Paneles con Aspose.Cells para .Net**
Es fácil descongelar paneles con Aspose.Cells para .Net. Por favor, utiliza el método [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes) para descongelar paneles.

1. Construye el libro para abrir el archivo congelado.
2. Descongela los paneles con el método Worksheet.UnFreezePanes().
3. Guarda el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Adjunto [archivo de Excel de origen de ejemplo](Frozen.xlsx).
{{< app/cells/assistant language="csharp" >}}
