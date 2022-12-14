---
title: Formateo de un rango de Cells
type: docs
weight: 60
url: /es/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

Este tema también pertenece a la serie de temas relacionados con la aplicación de configuraciones de fuente y otros estilos de formato en las celdas. Nuestros últimos temas han cubierto bien el manejo de tales características. Por ejemplo, puede referirse a[Cambiar la fuente y el color de un Cell](/cells/es/net/changing-the-font-and-color-of-a-cell/) y[Aplicación de estilos en Cells](/cells/es/net/applying-styles-on-cells/) temas para aprender sobre las mismas características. Entonces que hay de nuevo en este tema si ya hemos cubierto estos conceptos. Bueno, la única diferencia de este tema con los anteriores es que aplicaremos configuraciones de formato (relacionadas con fuentes y otros estilos) en un rango de celdas en lugar de solo una celda. Esperamos que todavía encuentre este tema útil para usted.

{{% /alert %}} 
## **Configuración de fuente y estilo de un rango de Cells**
 Antes de hablar sobre la configuración de formato (que ya hemos hablado mucho en nuestros temas anteriores), debemos saber cómo crear un rango de celdas. Bueno, podemos crear un rango de celdas usando**rango de celdas** clase cuyo constructor toma algunos parámetros para especificar el rango de celdas. Podemos especificar el rango de celdas usando el**nombres** o**Índices de fila y columna** de celdas iniciales y finales.

 Una vez que hemos creado un**rango de celdas** objeto entonces podemos usar las versiones sobrecargadas de**EstablecerEstilo**, **Establecer fuente** & **Establecer color de fuente** métodos de hoja de trabajo que pueden tomar un**rango de celdas** objeto para aplicar la configuración de formato en el rango de celdas especificado.

Veamos un ejemplo para entender este concepto básico.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
