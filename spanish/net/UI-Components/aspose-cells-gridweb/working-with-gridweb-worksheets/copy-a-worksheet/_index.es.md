---
title: Copiar una hoja de trabajo
type: docs
weight: 50
url: /es/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[Agregar hojas de trabajo](/cells/es/net/add-worksheets/) describe cómo agregar nuevas hojas de trabajo a Aspose.Cells.GridWeb. También es posible agregar una copia (o réplica) de otra hoja de cálculo al control Aspose.Cells.GridWeb. Esta característica puede ser útil cuando también se requieren datos idénticos o similares en una hoja de trabajo en otra hoja de trabajo. Cuando ese es el caso, es más fácil copiar una hoja de trabajo existente y agregarla a Aspose.Cells.GridWeb como una nueva hoja de trabajo en lugar de crearla desde cero.

{{% /alert %}} 
## **Copiar una hoja de trabajo**
### **Uso del índice de hoja**
El siguiente código de ejemplo muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el índice de la hoja de cálculo en el método AddCopy de GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Usando el nombre de la hoja**
El siguiente código de ejemplo muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el nombre de la hoja de cálculo en el método AddCopy de GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 El método AddCopy devuelve el índice de la hoja de trabajo recién agregada que se puede usar para acceder a la instancia de la hoja de trabajo. Para obtener más detalles sobre cómo acceder a las hojas de trabajo, lea[Acceder a hojas de trabajo](/cells/es/net/access-worksheets/).

{{% /alert %}}
