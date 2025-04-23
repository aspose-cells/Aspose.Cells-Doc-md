---  
title: Cómo usar la paleta de colores
linktitle: Cómo usar la paleta de colores  
type: docs  
weight: 80  
url: /es/nodejs-cpp/excel-color-palette/  
description: Código de Node.js para añadir colores personalizados a la paleta y usar la paleta de colores de Excel con Aspose.Cells for Node.js via C++.  
keywords: node.js añade colores personalizados a la paleta, programa node.js para la paleta de colores de Excel, cómo usar programáticamente la paleta de colores en un libro de trabajo, node.js cómo usar la paleta de colores en Excel  
---  

## **Colores y paleta**  

Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.  

Con Aspose.Cells for Node.js via C++, es posible no solo usar los colores existentes en la paleta, sino también colores personalizados. Antes de usar un color personalizado, añádelo primero a la paleta.  

Este tema trata sobre cómo agregar colores personalizados a la paleta.  

## **Agregar colores personalizados a la paleta**  

Aspose.Cells soporta la paleta de colores de Microsoft Excel con 56 colores. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) proporciona un método [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) que recibe los siguientes parámetros para agregar un color personalizado y modificar la paleta:  

- Color personalizado, el color personalizado que se agregará.  
- Índice, el índice del color en la paleta que el color personalizado reemplazará. Debe estar entre 0-55.  

El siguiente ejemplo agrega un color personalizado (Orchid) a la paleta antes de aplicarlo a una fuente.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Por lo tanto, tenga mucho cuidado al cambiar la paleta. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no hay tal limitación para formatos de archivo XLSX o más avanzados de MS Excel (2007/2010 o 2013).  

{{% /alert %}}  

