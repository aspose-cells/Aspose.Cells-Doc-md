---
title: Agregar o insertar una fila en la hoja de cálculo
type: docs
weight: 30
url: /es/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: Este artículo presenta cómo agregar o insertar una fila en GridDesktop.
---

{{% alert color="primary" %}} 

Similar a uno de nuestros temas anteriores, este tema describe la característica de agregar e insertar filas en las hojas de cálculo en tiempo de ejecución utilizando la API de Aspose.Cells.GridDesktop. La diferencia básica entre la adición y la inserción es que en la adición, se agrega una fila al final de la colección de filas de la hoja de cálculo mientras que en la inserción, una fila puede agregarse a cualquier posición especificada en la hoja de cálculo.

{{% /alert %}} 
## **Agregando una fila a la hoja de cálculo**
Para agregar una nueva fila a la hoja de cálculo, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregue una **Fila** a la **Hoja de cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Insertar una fila en la hoja de cálculo**
Para insertar una nueva fila en la hoja de cálculo en una posición especificada, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Inserte una **Fila** en la **Hoja de cálculo** (en una posición específica especificando el índice de la fila donde desea insertarla)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
