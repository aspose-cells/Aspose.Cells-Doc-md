---
title: Implementar etiquetas de Subtotal o Gran Total en otros idiomas
type: docs
weight: 50
url: /es/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **Posibles escenarios de uso**

 A veces, desea mostrar etiquetas de subtotales y totales generales en idiomas que no sean inglés, como chino, japonés, árabe, hindi, etc. Aspose.Cells le permite hacer esto usando el[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)clase y[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) propiedad. Consulte este artículo sobre cómo utilizar[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)clase

- [Uso de la clase GlobalizationSettings para etiquetas de subtotales personalizadas y otras etiquetas de gráficos circulares](/cells/es/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementar etiquetas de Subtotal o Gran Total en otros idiomas**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](5115151.xlsx) e implementa nombres de subtotal y gran total en el idioma chino. Por favor, checa el[archivo de salida de Excel](5115152.xlsx) generado por este código para su referencia. Primero creamos una clase de[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)y luego usarlo en nuestro código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Ahora use la clase creada anteriormente en el código como se muestra a continuación:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
