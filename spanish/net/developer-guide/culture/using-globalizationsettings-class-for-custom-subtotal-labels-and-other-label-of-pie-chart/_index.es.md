---
title: Usar la Clase GlobalizationSettings para Etiquetas de Subtotal Personalizadas y Otra Etiqueta de Gráfico de Sectores
type: docs
weight: 70
url: /es/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Escenarios de uso posibles**

Las API de Aspose.Cells han expuesto la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) para manejar los escenarios en los que el usuario desea usar etiquetas personalizadas para los Subtotales en una hoja de cálculo. Además, la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) también se puede usar para modificar la etiqueta **Otros** para el gráfico circular al renderizar la hoja de cálculo o el gráfico.

## **Introducción a la Clase Configuración Global**

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) actualmente ofrece los siguientes 3 métodos que se pueden anular en una clase personalizada para obtener etiquetas deseadas para los Subtotales o para renderizar texto personalizado para la etiqueta **Otros** de un gráfico circular.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Obtiene el nombre total de la función.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Obtiene el nombre del total general de la función.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Obtiene el nombre de las etiquetas "Otros" para gráficos circulares.

### **Etiquetas Personalizadas para Subtotales**

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) se puede usar para personalizar las etiquetas de los Subtotales anulando los métodos [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) y [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) como se demuestra a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

Para inyectar etiquetas personalizadas, es necesario asignar la propiedad [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) a una instancia de la clase **Configuración Personalizada** definida anteriormente antes de agregar los Subtotales a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) solo funciona para agregar nuevos Subtotales. Si una hoja de cálculo ya contiene Subtotales, no se pueden modificar sus etiquetas.

{{% /alert %}}

### **Texto Personalizado para Otra Etiqueta del Gráfico Circular**

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) ofrece el método [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) que es útil para darle un valor personalizado a la etiqueta "Otros" de los gráficos circulares. El siguiente fragmento de código define una clase personalizada y anula el método [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) para obtener una etiqueta personalizada basada en el identificador de la cultura del sistema.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

El siguiente fragmento de código carga una hoja de cálculo existente que contiene un gráfico circular y renderiza el gráfico a una imagen utilizando la clase **Configuración Personalizada** creada anteriormente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
