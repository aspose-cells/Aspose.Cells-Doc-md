---
title: Uso de la clase GlobalizationSettings para etiquetas de subtotales personalizadas y otras etiquetas de gráficos circulares
type: docs
weight: 50
url: /es/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Posibles escenarios de uso**
 Aspose.Cells Las API han expuesto el[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) class para manejar los escenarios en los que el usuario desea utilizar etiquetas personalizadas para subtotales en una hoja de cálculo. Además, el[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) La clase también se puede utilizar para modificar la**Otro** etiqueta para el gráfico circular al renderizar la hoja de trabajo o el gráfico.
## **Introducción a la clase GlobalizationSettings**
 Él[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Actualmente, la clase ofrece los siguientes 3 métodos que se pueden anular en una clase personalizada para obtener las etiquetas deseadas para los Subtotales o para representar texto personalizado para el**Otro** etiqueta de un gráfico circular.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Obtiene el nombre total de la función.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Obtiene el nombre total general de la función.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): obtiene el nombre de las etiquetas "Otros" para los gráficos circulares.
### **Etiquetas personalizadas para subtotales**
 Él[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)La clase se puede utilizar para personalizar las etiquetas de subtotal anulando el[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) métodos como se demuestra más adelante.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Para poder inyectar etiquetas personalizadas, se requiere asignar el[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) propiedad a una instancia de la*Ajustes personalizados*definida anteriormente antes de agregar los subtotales a la hoja de trabajo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 Él[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)La clase solo funciona para agregar nuevos subtotales. Si una hoja de cálculo ya contiene Subtotales, sus etiquetas no se pueden modificar.

{{% /alert %}} 
### **Texto personalizado para otra etiqueta de gráfico circular**
 Él[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) clase ofrece la[obtenerOtroNombre](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) que es útil para dar a la etiqueta "Otro" de los gráficos circulares un valor personalizado. El siguiente fragmento define una clase personalizada y anula la[obtenerOtroNombre](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) para obtener una etiqueta personalizada basada en el conjunto de idiomas predeterminado para JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular y representa el gráfico en una imagen mientras utiliza el*Ajustes personalizados*clase creada anteriormente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


 continuación se muestra la imagen resultante cuando la configuración regional de la máquina se establece en Francia. Como puede ver, la etiqueta "Otro" se ha traducido a "Autre" como se define en*Ajustes personalizados*clase.

![todo:imagen_alternativa_texto](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
