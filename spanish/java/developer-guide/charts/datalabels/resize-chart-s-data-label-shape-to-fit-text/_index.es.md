---
title: Cambiar el tamaño de la forma de la etiqueta de datos del gráfico para que se ajuste al texto
type: docs
weight: 190
url: /es/java/resize-chart-s-data-label-shape-to-fit-text/
---
{{% alert color="primary" %}}

 La aplicación Excel proporciona la**Cambiar el tamaño de la forma para que se ajuste al texto** opción para DataLabels de Chart para aumentar el tamaño de la forma para que el texto quepa dentro de ella. Se puede acceder a esta opción en la interfaz de Excel seleccionando cualquiera de las etiquetas de datos en el gráfico. Haga clic derecho y seleccione**Formatear etiquetas de datos** menú. Sobre**Tamaño y propiedades** pestaña, expandir**Alineación** para revelar las propiedades relacionadas, incluida la**Cambiar el tamaño de la forma para corregir el texto** opción.

![todo:imagen_alternativa_texto](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Cambiar el tamaño de la forma de la etiqueta de datos del gráfico para que se ajuste al texto**

 Para imitar la función de Excel de cambiar el tamaño de las formas de las etiquetas de datos para que se ajusten al texto, las API Aspose.Cells han expuesto el tipo booleano[**Etiquetas de datos.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText)propiedad. El siguiente fragmento de código muestra el escenario de uso simple de[**Etiquetas de datos.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText)propiedad.

El gráfico tiene el siguiente aspecto antes de ejecutar el código.

![todo:imagen_alternativa_texto](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

El gráfico se ve de la siguiente manera después de ejecutar el código.

![todo:imagen_alternativa_texto](resize-chart-s-data-label-shape-to-fit-text_3.png)
