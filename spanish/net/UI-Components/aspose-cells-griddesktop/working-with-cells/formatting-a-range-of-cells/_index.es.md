---
title: Formato de un Rango de Celdas
type: docs
weight: 60
url: /es/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop, formato, estilo, celdas
description: Este artículo presenta cómo aplicar formato de estilo en celdas en GridDesktop.
---

{{% alert color="primary" %}} 

Este tema también pertenece a la serie de temas relacionados con la aplicación de configuraciones de fuente y otros estilos de formato en celdas. Nuestros últimos temas han cubierto bien estas características. Por ejemplo, puedes consultar los temas [Cambiar la Fuente y el Color de una Celda](/cells/es/net/changing-the-font-and-color-of-a-cell/) y [Aplicar Estilos en Celdas](/cells/es/net/applying-styles-on-cells/) para aprender sobre las mismas características. Entonces, ¿qué hay de nuevo en este tema si ya hemos cubierto estos conceptos? Bueno, la única diferencia de este tema con los anteriores es que aplicaremos ajustes de formato (relacionados con fuentes y otros estilos) en un rango de celdas en lugar de solo una celda. Esperamos que aún encuentres útil este tema para ti.

{{% /alert %}} 
## **Estableciendo Fuente y Estilo de un Rango de Celdas**
Antes de hablar sobre los ajustes de formato (de los que ya hemos hablado mucho en nuestros temas anteriores), debemos saber cómo crear un rango de celdas. Bueno, podemos crear un rango de celdas usando la clase **CellRange** cuyo constructor toma algunos parámetros para especificar el rango de celdas. Podemos especificar el rango de celdas usando los **Nombres** o los **Índices de Fila y Columna** de las celdas de inicio y fin.

Una vez que hemos creado un objeto **CellRange**, podemos utilizar las versiones sobrecargadas de los métodos **SetStyle**, **SetFont** y **SetFontColor** de Worksheet que pueden tomar un objeto **CellRange** para aplicar ajustes de formato en el rango especificado de celdas.

Veamos un ejemplo para entender este concepto básico.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
