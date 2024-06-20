---
title: Copiar una hoja de cálculo
type: docs
weight: 50
url: /es/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb, copiar, GridWorksheet
description: Este artículo presenta cómo copiar una hoja de cálculo (GridWorksheet) en GridWeb.
---

{{% alert color="primary" %}} 

[Agregar hojas de cálculo](/cells/es/net/aspose-cells-gridweb/add-worksheets/) describe cómo agregar nuevas hojas de cálculo a Aspose.Cells.GridWeb. También es posible agregar una copia (o réplica) de otra hoja de cálculo al control Aspose.Cells.GridWeb. Esta función puede ser útil cuando datos idénticos o similares de una hoja de cálculo también se requieren en otra hoja de cálculo. En ese caso, es más fácil copiar una hoja de cálculo existente y agregarla a Aspose.Cells.GridWeb como una nueva hoja de cálculo en lugar de crearla desde cero.

{{% /alert %}} 
## **Copiando una hoja de cálculo**
### **Usando el índice de hoja**
El siguiente código de ejemplo muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el índice de la hoja de cálculo en el método AddCopy de GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Usando el nombre de la hoja**
El siguiente código de ejemplo muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el nombre de la hoja de cálculo en el método AddCopy de GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

El método AddCopy devuelve el índice de la hoja de cálculo recién agregada que se puede usar para acceder a la instancia de la hoja de cálculo. Para obtener más detalles sobre cómo acceder a las hojas de cálculo, lea [Acceder a hojas de cálculo](/cells/es/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}}
