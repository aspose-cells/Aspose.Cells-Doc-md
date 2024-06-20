---
title: Aplicar estilo a una fila o columna
type: docs
weight: 50
url: /es/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, estilo, fila, columna
description: Este artículo presenta cómo aplicar estilo en una fila o columna en GridDesktop.
---

{{% alert color="primary" %}} 

En este tema, discutiremos sobre cómo cambiar la fuente y el color de la fuente de filas y columnas de una hoja de cálculo. Esta es una función básica de formato ofrecida por Aspose.Cells.GridDesktop que permite a los desarrolladores personalizar la vista de sus hojas de cálculo para hacerlas más presentables.

{{% /alert %}} 
## **Aplicar estilo en una columna**
Para aplicar un estilo personalizado en una columna usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceda a una **Columna** en la que queremos aplicar un **Estilo**
- Obtenga el **Estilo** de la **Columna**
- Establecer las propiedades del **Estilo** según sus necesidades personalizadas
- Finalmente, establezca el **Estilo** de la **Columna** con el actualizado

Existen muchas propiedades y métodos útiles ofrecidos por el objeto **Estilo** que pueden ser utilizados por los desarrolladores para personalizar el estilo según sus requisitos.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Aplicar estilo en una fila**
Para aplicar un estilo personalizado en una fila usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceda a una **Fila** en la que queremos aplicar un **Estilo**
- Obtenga el **Estilo** de la **Fila**
- Establecer las propiedades del **Estilo** según sus necesidades personalizadas
- Finalmente, establezca el **Estilo** de la **Fila** con el actualizado

Existen muchas propiedades y métodos útiles ofrecidos por el objeto **Estilo** que pueden ser utilizados por los desarrolladores para personalizar el estilo según sus requisitos.



{{< highlight csharp >}}

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
