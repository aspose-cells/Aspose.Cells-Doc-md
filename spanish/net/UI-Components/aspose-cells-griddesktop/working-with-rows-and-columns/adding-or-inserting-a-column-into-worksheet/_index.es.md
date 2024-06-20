---
title: Agregar o Insertar una Columna en la Hoja de trabajo
type: docs
weight: 10
url: /es/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,insertar,añadir,columna,insertar columna,insertar fila
description: Este artículo presenta cómo insertar o agregar una columna en GridDesktop.
---

{{% alert color="primary" %}} 

En este tema, describiremos la característica básica de agregar e insertar columnas en las hojas de trabajo en tiempo de ejecución usando la API de Aspose.Cells.GridDesktop. La diferencia básica entre agregar e insertar es que en la adición, la columna se agrega al final de la colección de columnas de la hoja de trabajo, mientras que en la inserción, la columna se puede agregar a cualquier posición especificada en la hoja de trabajo.

{{% /alert %}} 
## **Agregar una Columna a la Hoja de trabajo**
Para agregar una nueva columna a la hoja de trabajo, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregar **Columna** a la **Hoja de trabajo



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Insertar una columna en la hoja de cálculo**
Para insertar una nueva columna en la hoja de cálculo en una posición especificada, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Inserte una **Columna** en la **Hoja de cálculo** (en una posición específica especificando el índice de la columna donde desea insertarla)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
