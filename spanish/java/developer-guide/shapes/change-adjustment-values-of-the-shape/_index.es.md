---
title: Cambiar los valores de ajuste de la forma
type: docs
weight: 3200
url: /es/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

 Aspose.Cells proporciona[Forma.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) propiedad para realizar cambios en los puntos de ajuste con formas. En la interfaz de usuario de Excel Microsoft, los ajustes se muestran como nodos de diamantes amarillos. Por ejemplo:

- Rectángulo redondeado tiene un ajuste para cambiar el arco
- Triángulo tiene un ajuste para cambiar la ubicación del punto
- Un trapezoide tiene un ajuste para cambiar el ancho de la parte superior
- Las flechas tienen dos ajustes para cambiar la forma de la cabeza y la cola.

 Este artículo explicará el uso de[Forma.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) propiedad para cambiar el valor de ajuste de las diferentes formas.

{{% /alert %}} 
## **Cambiar los valores de ajuste de la forma**
El siguiente código de muestra accede a las tres primeras formas de la primera hoja de trabajo en el archivo de origen de Excel y luego cambia los valores de ajuste de las formas. Las siguientes capturas de pantalla muestran cómo se ven las formas antes de cambiar los valores de ajuste y luego después de cambiar los valores de ajuste.
### **Dibujar formas antes de cambiar los valores de ajuste**
![todo:imagen_alternativa_texto](change-adjustment-values-of-the-shape_1.png)
### **Dibujar formas después de cambiar los valores de ajuste**
![todo:imagen_alternativa_texto](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
