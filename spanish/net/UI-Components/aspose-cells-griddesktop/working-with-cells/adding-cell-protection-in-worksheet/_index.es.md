---
title: Agregar protección en la hoja de cálculo
type: docs
weight: 130
url: /es/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop, proteger
description: Este artículo presenta cómo proteger celdas en la hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells for GridDesktop le permite proteger celdas en una hoja de cálculo. Primero debe proteger su hoja de cálculo, luego puede proteger las celdas deseadas en la hoja de cálculo. Para proteger la hoja de cálculo, configure la propiedad **Worksheet.Protected** en true, luego utilice el método **Worksheet.SetProtected()** para proteger el rango de celdas.

{{% /alert %}} 
## **Proteger celda usando Aspose.Cells.GridDesktop**
El siguiente código de ejemplo protege todas las celdas en el rango **A1:B1** de la hoja de cálculo activa de GridDesktop. Cuando haga doble clic en cualquier celda en este rango, no podrá editarla. Estas celdas serán de solo lectura.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
