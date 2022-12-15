---
title: Aplicación de estilos en Cells
type: docs
weight: 50
url: /es/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

Este tema trata sobre la aplicación de estilos en las celdas, por lo que intentaremos cubrir casi todo lo que se puede usar para aplicar estilos en una celda. Además de algunas configuraciones básicas de formato, también discutiremos sobre dibujar bordes y configurar el formato numérico de las celdas en detalle.

{{% /alert %}} 
## **Aplicar un estilo personalizado en un Cell: un ejemplo**
Para cambiar la fuente y el color de una celda usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Accede a cualquier deseado**Hoja de cálculo**
-  Accede a un**Cell** sobre el que queremos aplicar un**Estilo**
-  Obtener**Estilo** del**Cell**
-  Establecer**Estilo** propiedades de acuerdo a sus necesidades personalizadas
-  Finalmente, establezca**Estilo** del**Cell** con el actualizado

 Hay muchas propiedades y métodos útiles ofrecidos por**Estilo** objeto que pueden usar los desarrolladores para personalizar el estilo de acuerdo con sus requisitos. En el siguiente código, se demuestra cómo aplicar un estilo personalizado en la celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Bordes de dibujo de Cells**
 Usando**Estilo**objeto, podemos dibujar los bordes de una celda muy fácilmente. Los bordes se pueden dibujar en cualquier color. Además, los desarrolladores también tienen la flexibilidad de elegir un tipo específico de línea que se usará para dibujar los bordes alrededor de la celda. Los desarrolladores pueden usar**EstablecerBorderLine** y**EstablecerBorderColor** métodos de**Estilo** objeto para dibujar bordes de cualquier tipo y colores. Del mismo modo, para obtener información de los bordes de cualquier celda, los desarrolladores también pueden hacer uso de**ObtenerLíneaBorde** y**ObtenerBorderColor** métodos de**Estilo** objeto.
### **Tipos de bordes**
Hay seis tipos de bordes admitidos por Aspose.Cells.GridDesktop de la siguiente manera:

- **Izquierda** , representa el borde izquierdo
- **Derecha** , representa el borde derecho
- **Parte superior** , representa el borde superior
- **Abajo** , representa el borde inferior
- **DiagonalAbajo** , representa el borde diagonal hacia abajo
- **DiagonalArriba** , representa el borde diagonal hacia arriba
### **Tipos de líneas de borde**
Un borde se compone de una línea. Al cambiar el tipo de línea, cambia la apariencia de un borde. Hay muchos tipos de líneas de borde compatibles con Aspose.Cells.GridDesktop, que también se enumeran a continuación:

- **Ninguna** , no representa ninguna frontera
- **Delgada** , representa un borde de línea continua
- **Medio** , representa un borde de línea sólida con un ancho de línea igual a 2f
- **punteado** , representa el borde de la línea discontinua
- **Punteado** , representa el borde de la línea de puntos
- **Grueso** , representa un borde de línea sólida con un ancho de línea igual a 3f
- **medio punteado** , representa un borde de línea discontinua con un ancho de línea igual a 2f
- **DelgadaGuiónPunteado** , representa el borde de la línea de puntos del guión
- **Medio Guión Punteado** , representa el borde de la línea de puntos con un ancho de línea igual a 2f
- **DelgadaGuiónPuntoPunteado** , representa el borde de línea punteada de punto de guion
- **Medio Guión Punto Punteado** , representa el borde de línea punteada de punto de guión con un ancho de línea igual a 2f
## **Resumen de todos juntos - Ejemplo**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Configuración de formatos de número**
Aspose.Cells.GridDesktop también proporciona una función sólida de configuración de formatos de números para los valores ingresados en las celdas. Hay 58 formatos de números integrados ofrecidos por Aspose.Cells.GridDesktop. Para ver una lista completa de todos los formatos de número admitidos, consulte[Formatos de número admitidos.](/cells/es/net/list-of-supported-number-formats/)

 A todos los formatos numéricos integrados se les asigna un**Índice** número.**Por ejemplo** la**Índice** número de**0.00E+00** el formato de número es**11** . Para usar un formato de número incorporado en cualquier celda, los desarrolladores pueden establecer la propiedad NumberFormat de**Estilo** objetar a la**Índice** número de ese formato de número específico. Sin embargo, si los desarrolladores necesitan tener su propio formato de número personalizado, también pueden usar la propiedad personalizada de**Estilo** objeto.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
