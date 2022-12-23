---
title: Agregar o insertar una fila en la hoja de trabajo
type: docs
weight: 30
url: /es/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

Similar a uno de nuestros temas anteriores, este tema describe la característica de agregar e insertar filas en las hojas de trabajo en tiempo de ejecución usando API de Aspose.Cells.GridDesktop. La diferencia básica entre la adición y la inserción es que, además, se agrega una fila al final de la colección de filas de la hoja de trabajo donde, como en la inserción, se puede agregar una fila a cualquier posición especificada en la hoja de trabajo.

{{% /alert %}} 
## **Agregar una fila a la hoja de trabajo**
Para agregar una nueva fila a la hoja de trabajo, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregar**Fila** al**Hoja de cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Insertar una fila en la hoja de trabajo**
Para insertar una nueva fila en la hoja de trabajo en una posición específica, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Insertar**Fila** en**Hoja de cálculo**(en una posición específica especificando el índice de la fila donde insertarlo)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
