---
title: Adición de la protección Cell en la hoja de trabajo
type: docs
weight: 130
url: /es/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells para GridDesktop le permite proteger sus celdas en una hoja de trabajo. Primero debe proteger su hoja de trabajo, luego puede proteger las celdas deseadas en una hoja de trabajo. Para proteger la hoja de trabajo, configure**Hoja de trabajo.Protegido** propiedad a verdadero, luego use**Hoja de trabajo.SetProtected()** método para proteger el rango de células.

{{% /alert %}} 
## **Proteja Cell usando Aspose.Cells.GridDesktop**
 El siguiente código de muestra protege todas las celdas en el rango**A1:B1** de la hoja de cálculo activa de GridDesktop. Cuando haga doble clic en cualquier celda en este rango, no podrá editar. Hará que estas celdas sean de solo lectura.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
