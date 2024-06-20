---
title: Implementar Etiquetas de Subtotal o Gran Total en otros idiomas
type: docs
weight: 50
url: /es/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Escenarios de uso posibles**

A veces, deseas mostrar etiquetas de subtotal y gran total en idiomas no-ingleses como chino, japonés, árabe, hindi, etc. Aspose.Cells te permite hacer esto usando la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) y la propiedad [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Por favor consulta este artículo sobre cómo utilizar la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)

- [Usando la Clase GlobalizationSettings para Etiquetas de Subtotal Personalizadas y Otra Etiqueta de Gráfico de Sectores](/cells/es/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementar Etiquetas de Subtotal o Gran Total en otros idiomas**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115151.xlsx) e implementa los nombres de subtotal y gran total en el idioma chino. Por favor verifica el [archivo de Excel de salida](5115152.xlsx) generado por este código para tu referencia. Primero creamos una clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) y luego la usamos en nuestro código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Ahora usa la clase creada anteriormente en el código como se muestra a continuación:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
