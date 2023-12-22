---
title: Cómo utilizar la paleta de colores
type: docs
weight: 80
url: /es/net/excel-color-palette/
description: Código C# para agregar colores personalizados a la paleta y usar la paleta de colores de Excel con Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **Colores y paleta**

Una paleta es la cantidad de colores disponibles para usar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear una apariencia consistente. Cada archivo Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas de un gráfico.

Con Aspose.Cells es posible no sólo utilizar los colores existentes de la paleta sino también colores personalizados. Antes de usar un color personalizado, agréguelo primero a la paleta.

En este tema se analiza cómo agregar colores personalizados a la paleta.

##  **Agregar colores personalizados a la paleta**

Aspose.Cells admite la paleta de 56 colores de Microsoft Excel. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase proporciona un[**Cambiar paleta**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Método que toma los siguientes parámetros para agregar un color personalizado para modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que reemplazará el color personalizado. Debe estar entre 0 y 55.

El siguiente ejemplo agrega un color personalizado (Orquídea) a la paleta antes de aplicarlo a una fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La paleta sólo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento del archivo formateado con el color anterior cambia. Entonces, cuando cambies la paleta, ten mucho cuidado. Además, esta es la limitación solo en el formato de archivo XLS (Excel 97 - 2003), ya que no existe tal limitación para XLSX u otros formatos de archivo avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}