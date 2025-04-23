---
title: Usar la Clase GlobalizationSettings para Etiquetas de Subtotal Personalizadas y Otra Etiqueta de Gráfico de Sectores
type: docs
weight: 50
url: /es/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Escenarios de uso posibles**
Las APIs de Aspose.Cells han expuesto la clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) para tratar los escenarios en los que el usuario desea usar etiquetas personalizadas para los subtotales en una hoja de cálculo. Además, la clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) también se puede usar para modificar la etiqueta **Otros** de un gráfico circular mientras se representa la hoja de cálculo o el gráfico.
## **Introducción a la Clase Configuración Global**
La clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) actualmente ofrece los siguientes 3 métodos que se pueden anular en una clase personalizada para obtener las etiquetas deseadas para los subtotales o para representar un texto personalizado para la etiqueta **Otros** de un gráfico circular.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): Obtiene el nombre total de la función.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): Obtiene el nombre del total general de la función.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): Obtiene el nombre de las etiquetas "Otros" para gráficos de pastel.
### **Etiquetas Personalizadas para Subtotales**
La clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) puede ser utilizada para personalizar las etiquetas de Subtotal modificando los métodos [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) y [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-) como se demuestra a continuación.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Para inyectar etiquetas personalizadas, es necesario asignar la propiedad [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) a una instancia de la clase *CustomSettings* definida anteriormente antes de agregar los subtotales a la hoja de cálculo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

La clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) solo funciona para agregar nuevos Subtotales. Si una hoja de cálculo ya contiene Subtotales, sus etiquetas no pueden ser modificadas.

{{% /alert %}} 
### **Texto Personalizado para Otra Etiqueta del Gráfico Circular**
La clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) ofrece el método [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) que es útil para asignar un valor personalizado a la etiqueta "Otros" en gráficos de pastel. El siguiente fragmento define una clase personalizada y sobrescribe el método [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) para obtener una etiqueta personalizada basada en el idioma predeterminado configurado para la JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular y renderiza el gráfico a una imagen utilizando la clase *CustomSettings* creada anteriormente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


A continuación se muestra la imagen resultante cuando la configuración regional de la máquina está establecida en Francia. Como puedes ver, la etiqueta "Otro" se ha traducido a "Autre" como se define en la clase *CustomSettings*.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
