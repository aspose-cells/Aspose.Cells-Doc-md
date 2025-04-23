---
title: Cambiar los valores de ajuste de la forma
type: docs
weight: 3200
url: /es/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona la propiedad [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) para realizar cambios en los puntos de ajuste de las formas. En la interfaz de usuario de Microsoft Excel, los ajustes se muestran como nodos de diamante amarillos. Por ejemplo:

- El rectángulo redondeado tiene un ajuste para cambiar el arco
- El triángulo tiene un ajuste para cambiar la ubicación del punto
- Un trapezoide tiene un ajuste para cambiar el ancho de la parte superior
- Las flechas tienen dos ajustes para cambiar la forma de la cabeza y la cola

Este artículo explicará el uso de la propiedad [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) para cambiar el valor de ajuste de las distintas formas.

{{% /alert %}} 
## **Cambiar los valores de ajuste de la forma**
El siguiente código de muestra accede a los primeros tres formas de la primera hoja de cálculo en el archivo de Excel fuente y luego cambia los valores de ajuste de las formas. A continuación, capturas de pantalla muestran cómo lucen las formas antes y después de cambiar los valores de ajuste.
### **Dibujo de Formas Antes de Cambiar Valores de Ajuste**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Dibujo de Formas Después de Cambiar Valores de Ajuste**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
