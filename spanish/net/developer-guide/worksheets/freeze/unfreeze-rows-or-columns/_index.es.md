---
title: Descongelar filas o columnas
linktitle: Descongelar paneles
type: docs
weight: 190
url: /es/net/unfreeze-rows-or-columns-of-excel-worksheet
description: En este artículo, aprenderá cómo descongelar filas, columnas o paneles de hojas de cálculo de Excel mediante programación utilizando la biblioteca C# con .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

En este artículo, aprenderemos cómo descongelar filas, columnas y paneles.
Si las hojas de cálculo de los archivos de Excel están congeladas, a veces queremos descongelarlas o ajustar las filas, columnas o paneles congelados.

{{% /alert %}}

##  **en excel**

1. Haga clic en la pestaña Ver > Congelar paneles > Descongelar paneles.

**![descongelar paneles en Excel](Unfreeze-Panes.png)**




##  **Descongelar filas, columnas o paneles con Aspose.Cells para .Net**
 Es sencillo descongelar paneles con Aspose.Cells para .Net. Por favor use el[**Hoja de trabajo.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)Método para desacoplar los cristales.

1. Construya el libro de trabajo para abrir el archivo congelado.
2. Descongelar paneles con el método Worksheet.UnFreezePanes().
3. Guarde el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Adjunto[archivo Excel fuente de muestra](Frozen.xlsx).
