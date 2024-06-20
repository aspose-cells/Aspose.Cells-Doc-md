---
title: Cambio de la fuente y el color de una fila o columna
type: docs
weight: 110
url: /es/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop,fuente,color
description: Este artículo presenta cómo cambiar la fuente y el color en una fila o columna en GridDesktop.
---

{{% alert color="primary" %}} 

En este tema, discutiremos sobre cómo cambiar la fuente y el color de la fuente de filas y columnas de una hoja de cálculo. Esta es una función básica de formato ofrecida por Aspose.Cells.GridDesktop que permite a los desarrolladores personalizar la vista de sus hojas de cálculo para hacerlas más presentables.

{{% /alert %}} 
## **Cambiar la Fuente y Color de una Columna**
Para cambiar la fuente y color de una columna utilizando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceda a una **Columna** cuya fuente y color se van a cambiar
- Cree una **Fuente** personalizada
- Establezca la **Fuente** de la **Columna** a la personalizada
- Finalmente, establezca el **Color de Fuente** de la **Columna** al **Color** deseado



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **Cambiar la Fuente y Color de una Fila**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceda a una **Fila** cuya fuente y color se van a cambiar
- Cree una **Fuente** personalizada
- Establezca la **Fuente** de la **Fila** a la personalizada
- Finalmente, establezca el **Color de Fuente** de la **Fila** al **Color** deseado



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
