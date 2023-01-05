---
title: Agregar o insertar una columna en la hoja de trabajo
type: docs
weight: 10
url: /es/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

En este tema, describiremos la característica básica de agregar e insertar columnas a las hojas de trabajo en tiempo de ejecución usando API de Aspose.Cells.GridDesktop. La diferencia básica entre la adición y la inserción es que, además, la columna se agrega al final de la colección de columnas de la hoja de trabajo, mientras que en la inserción, la columna se puede agregar a cualquier posición especificada en la hoja de trabajo.

{{% /alert %}} 
## **Agregar una columna a la hoja de trabajo**
Para agregar una nueva columna a la hoja de trabajo, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregar**Columna** al**Hoja de cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Insertar una columna en la hoja de trabajo**
Para insertar una nueva columna en la hoja de trabajo en una posición específica, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Insertar**Columna** en**Hoja de cálculo** (en una posición específica especificando el índice de la columna donde insertarlo)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
