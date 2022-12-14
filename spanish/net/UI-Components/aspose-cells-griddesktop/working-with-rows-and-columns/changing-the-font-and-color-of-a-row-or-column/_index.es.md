---
title: Cambiar la fuente y el color de una fila o columna
type: docs
weight: 110
url: /es/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

En este tema, hablaremos sobre cómo cambiar la fuente y el color de la fuente de las filas y columnas de una hoja de trabajo. Este es un nivel básico de función de formato que ofrece Aspose.Cells.GridDesktop que permite a los desarrolladores personalizar la vista de sus hojas de trabajo para hacerlas más presentables.

{{% /alert %}} 
## **Cambiar la fuente y el color de una columna**
Para cambiar la fuente y el color de una columna usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Accede a cualquier deseado**Hoja de cálculo**
-  Accede a un**Columna** cuya fuente y color se van a cambiar
-  Crea una personalizada**Fuente**
-  Selecciona el**Fuente** del**Columna** al personalizado
-  Finalmente, establezca**Color de fuente** del**Columna** a cualquier deseado**Color**



{{< highlight "csharp" >}}

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
## **Cambiar la fuente y el color de una fila**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Accede a un**Fila** cuya fuente y color se van a cambiar
-  Crea una personalizada**Fuente**
-  Selecciona el**Fuente** del**Fila** al personalizado
-  Finalmente, establezca**Color de fuente** del**Fila** a cualquier deseado**Color**



{{< highlight "csharp" >}}

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
