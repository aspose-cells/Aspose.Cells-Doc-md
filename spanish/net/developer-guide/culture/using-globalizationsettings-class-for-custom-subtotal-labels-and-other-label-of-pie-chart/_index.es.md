---
title: Uso de la clase GlobalizationSettings para etiquetas de subtotales personalizadas y otras etiquetas de gráficos circulares
type: docs
weight: 70
url: /es/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Posibles escenarios de uso**

 Aspose.Cells Las API han expuesto el[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)class para manejar los escenarios en los que el usuario desea utilizar etiquetas personalizadas para subtotales en una hoja de cálculo. Además, el[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)La clase también se puede utilizar para modificar la**Otro** etiqueta para el gráfico circular al renderizar la hoja de trabajo o el gráfico.

## **Introducción a la clase GlobalizationSettings**

 los[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) Actualmente, la clase ofrece los siguientes 3 métodos que se pueden anular en una clase personalizada para obtener las etiquetas deseadas para los Subtotales o para representar texto personalizado para el**Otro** etiqueta de un gráfico circular.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Obtiene el nombre total de la función.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Obtiene el nombre total general de la función.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Obtiene el nombre de las etiquetas "Otros" para los gráficos circulares.

### **Etiquetas personalizadas para subtotales**

 los[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) La clase se puede utilizar para personalizar las etiquetas de subtotal anulando el[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)métodos como se demuestra más adelante.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 Para poder inyectar etiquetas personalizadas, se requiere asignar el[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) propiedad a una instancia de la**Ajustes personalizados**definida anteriormente antes de agregar los subtotales a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 los[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)La clase solo funciona para agregar nuevos subtotales. Si una hoja de cálculo ya contiene Subtotales, sus etiquetas no se pueden modificar.

{{% /alert %}}

### **Texto personalizado para otra etiqueta de gráfico circular**

 los[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) ofertas de clases[**ObtenerOtroNombre**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)método que es útil para dar a la etiqueta "Otro" de los gráficos circulares un valor personalizado. El siguiente fragmento define una clase personalizada y anula la[**ObtenerOtroNombre**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)método para obtener una etiqueta personalizada basada en el identificador cultural del sistema.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular y representa el gráfico en una imagen mientras utiliza el**Ajustes personalizados**clase creada anteriormente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
