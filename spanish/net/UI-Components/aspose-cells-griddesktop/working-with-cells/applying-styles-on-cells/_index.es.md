---
title: Aplicar estilo en la celda
type: docs
weight: 50
url: /es/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop, formato, estilo, formatos de número, formato numérico, NumberFormat
description: Este artículo presenta cómo obtener o establecer formato de estilo en la celda en la hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Este tema trata sobre aplicar formato de estilo en una celda, cubriremos casi todas las propiedades relacionadas que se pueden utilizar para aplicar estilo en una celda. Además de algunas configuraciones básicas de formato, también discutiremos sobre dibujar bordes y establecer el formato numérico en la celda en detalle.

{{% /alert %}} 
## **Aplicar un estilo personalizado en una celda - Un ejemplo**
Para cambiar la fuente y el color de una celda utilizando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceda a un **Celda** en la que queremos aplicar un **Estilo**
- Obtenga el **Estilo** de la **Celda**
- Establecer las propiedades del **Estilo** según sus necesidades personalizadas
- Finalmente, establezca el **Estilo** de la **Celda** con el actualizado

Hay muchas propiedades y métodos útiles ofrecidos por el objeto **Estilo** que pueden ser utilizados por los desarrolladores para personalizar el estilo según sus requisitos. En el siguiente código se demuestra cómo aplicar un estilo personalizado en una celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Dibujar bordes de las celdas**
Usando el objeto **Estilo**, podemos dibujar bordes de una celda muy fácilmente. Los bordes se pueden dibujar en cualquier color. Además, los desarrolladores también tienen la flexibilidad de elegir un tipo específico de línea que se utilizará para dibujar los bordes alrededor de la celda. Los desarrolladores pueden utilizar los métodos **SetBorderLine** y **SetBorderColor** del objeto **Estilo** para dibujar bordes de cualquier tipo y color. Del mismo modo, para obtener información sobre los bordes de cualquier celda, los desarrolladores también pueden hacer uso de los métodos **GetBorderLine** y **GetBorderColor** del objeto **Estilo**.
### **Tipos de bordes**
Hay seis tipos de bordes soportados por Aspose.Cells.GridDesktop de la siguiente manera:

- **Izquierda**, representa el borde izquierdo
- **Derecha**, representa el borde derecho
- **Superior**, representa el borde superior
- **Inferior**, representa el borde inferior
- **Diagonal hacía abajo**, representa el borde diagonal hacia abajo
- **Diagonal hacia arriba**, representa el borde diagonal hacia arriba
### **Tipos de líneas de borde**
Un borde está compuesto por una línea. Cambiar el tipo de línea cambia la apariencia de un borde. Aspose.Cells.GridDesktop admite muchos tipos de líneas de borde, que también se enumeran a continuación:

- **Ninguno**, representa ningún borde
- **Delgado**, representa un borde de línea sólida
- **Medio**, representa un borde de línea sólida con un ancho de línea igual a 2f
- **Guionado**, representa un borde de línea discontinua
- **Punteado**, representa un borde de línea de puntos
- **Grueso**, representa un borde de línea sólida con un ancho de línea igual a 3f
- **MedioGuionado**, representa un borde de línea discontinua con un ancho de línea igual a 2f
- **DelgadoGuionPunteado**, representa un borde de línea guion-punteado
- **MedioGuionPunteado**, representa un borde de línea guion-punteado con un ancho de línea igual a 2f
- **DelgadoGuionPuntoPunteado**, representa un borde de línea guion-punto-punteado
- **MedioGuionPuntoPunteado**, representa un borde de línea guion-punto-punteado con un ancho de línea igual a 2f
## **Resumiendo todo junto - Ejemplo**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Establecer formatos de números**
Aspose.Cells.GridDesktop también proporciona tipos de configuración de formatos de números. Hay 58 formatos de número integrados ofrecidos por Aspose.Cells.GridDesktop. Para ver una lista completa de todos los formatos de número admitidos, consulte [Formatos de Número Admitidos.](/cells/es/net/list-of-supported-number-formats/)

Todos los formatos de número integrados se asignan un número de **Índice**. **Por ejemplo**, el número de **Índice** del formato de número **0.00E+00** es **11**. Para utilizar un formato de número integrado en cualquier celda, los desarrolladores pueden establecer la propiedad NumberFormat del objeto **Estilo** en el número de **Índice** de ese formato de número específico. Sin embargo, si los desarrolladores necesitan tener su propio formato de número personalizado, también pueden usar la propiedad Personalizada del objeto **Estilo**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
