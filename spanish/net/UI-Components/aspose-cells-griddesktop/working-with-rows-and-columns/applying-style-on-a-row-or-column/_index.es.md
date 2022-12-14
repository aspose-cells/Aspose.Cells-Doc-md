---
title: Aplicar estilo en una fila o columna
type: docs
weight: 50
url: /es/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

En este tema, hablaremos sobre cómo cambiar la fuente y el color de la fuente de las filas y columnas de una hoja de trabajo. Este es un nivel básico de función de formato que ofrece Aspose.Cells.GridDesktop que permite a los desarrolladores personalizar la vista de sus hojas de trabajo para hacerlas más presentables.

{{% /alert %}} 
## **Aplicar estilo en una columna**
Para aplicar un estilo personalizado en una columna usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Accede a cualquier deseado**Hoja de cálculo**
-  Accede a un**Columna** sobre el que queremos aplicar un**Estilo**
-  Obtener**Estilo** del**Columna**
-  Establecer**Estilo** propiedades de acuerdo a sus necesidades personalizadas
-  Finalmente, establezca**Estilo** del**Columna** con el actualizado

 Hay muchas propiedades y métodos útiles ofrecidos por**Estilo** objeto que pueden usar los desarrolladores para personalizar el estilo de acuerdo con sus requisitos.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Aplicar estilo en una fila**
Para aplicar un estilo personalizado en una fila usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Accede a cualquier deseado**Hoja de cálculo**
-  Accede a un**Fila** sobre el que queremos aplicar un**Estilo**
-  Obtener**Estilo** del**Fila**
-  Establecer**Estilo** propiedades de acuerdo a sus necesidades personalizadas
-  Finalmente, establezca**Estilo** del**Fila** con el actualizado

 Hay muchas propiedades y métodos útiles ofrecidos por**Estilo** objeto que pueden usar los desarrolladores para personalizar el estilo de acuerdo con sus requisitos.



{{< highlight "csharp" >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
