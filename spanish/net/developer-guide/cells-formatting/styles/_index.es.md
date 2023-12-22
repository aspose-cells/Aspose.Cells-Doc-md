---
title: Obtener y establecer estilo para celdas
description: Descubra cómo formatear y diseñar datos en Aspose.Cells for .NET, incluido el formato de texto, el formato de números, el formato de fecha y otras opciones de estilo. Nuestra guía le ayudará a crear hojas de cálculo de aspecto profesional con un formato atractivo.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Estilos
type: docs
weight: 50
url: /es/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 introdujo dos nuevos métodos para formatear celdas: Cell.GetStyle y Cell.SetStyle. Este artículo examina el enfoque Cell.GetStyle/SetStyle para ayudarle a juzgar qué técnica se adapta mejor a sus necesidades.

{{% /alert %}} 
##  **Formato Cells**
Hay dos formas de formatear una celda, que se ilustran a continuación.
###  **Usando GetStyle()**
Con el siguiente fragmento de código, se inicia un objeto Estilo para cada celda al formatearla. Si se dan formato a muchas celdas, se consume una gran cantidad de memoria porque el objeto Estilo es un objeto grande. Estos objetos Style no se liberarán hasta que se llame al método Workbook.Save.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **Usando SetStyle()**
El primer enfoque es fácil y directo, entonces ¿por qué agregamos el segundo enfoque?

Agregamos el segundo enfoque para optimizar el uso de la memoria. Después de usar el método Cell.GetStyle para recuperar un objeto Style, modifíquelo y use el método Cell.SetStyle para volver a configurarlo en esta celda. Este objeto de estilo no se conservará y .NET GC lo recopilará cuando no se haga referencia a él.

Al llamar al método Cell.SetStyle, el objeto Style no se guarda para cada celda. En su lugar, comparamos este objeto de estilo con un grupo de objetos de estilo interno para ver si se puede reutilizar. Sólo se conservan para cada objeto de Libro de trabajo los objetos de Estilo que difieren de los existentes. Esto significa que sólo hay varios cientos de objetos de estilo para cada archivo de Excel en lugar de miles. Para cada celda, solo se conserva un índice del grupo de objetos de estilo.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **Temas avanzados**
- [Crear objeto de estilo usando la clase CellsFactory](/cells/es/net/create-style-object-using-cellsfactory-class/)
- [Modificar un estilo existente](/cells/es/net/modify-an-existing-style/)
- [Reutilizar objetos de estilo](/cells/es/net/reusing-style-objects/)
- [Usar estilos integrados](/cells/es/net/using-built-in-styles/)


