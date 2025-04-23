---
title: Redimensionar la forma de la etiqueta de datos del gráfico para ajustar el texto
type: docs
weight: 190
url: /es/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

La aplicación Excel proporciona la opción **Redimensionar la forma para ajustar el texto** para las etiquetas de datos del gráfico con el fin de aumentar el tamaño de la forma para que el texto encaje dentro de ella. Esta opción se puede acceder en la interfaz de Excel seleccionando cualquiera de las etiquetas de datos en el gráfico. Haga clic con el botón derecho y seleccione el menú **Formato de etiquetas de datos**. En la pestaña **Tamaño y propiedades**, expanda **Alineación** para revelar las propiedades relacionadas, incluida la opción **Redimensionar la forma para ajustar el texto**.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto**

Para imitar la característica de Excel de redimensionar las formas de las etiquetas de datos para que se ajusten al texto, las APIs de Aspose.Cells han expuesto la propiedad de tipo Booleano [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText). El siguiente fragmento de código muestra el escenario de uso simple de la propiedad [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText).

El gráfico se ve como sigue antes de ejecutar el código.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

El gráfico se ve como sigue después de ejecutar el código.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
{{< app/cells/assistant language="java" >}}
