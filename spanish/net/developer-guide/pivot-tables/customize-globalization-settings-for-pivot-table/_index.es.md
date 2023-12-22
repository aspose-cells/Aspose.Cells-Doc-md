---
title: Personalizar la configuración de globalización para la tabla dinámica
type: docs
weight: 50
url: /es/net/customize-globalization-settings-for-pivot-table/
---
##  **Posibles escenarios de uso**

 A veces quieres personalizar el*Total dinámico, subtotal, total general, todos los elementos, varios elementos, etiquetas de columna, etiquetas de fila, valores en blanco*texto según sus requisitos. Aspose.Cells le permite personalizar la configuración de globalización de la tabla dinámica para hacer frente a tales escenarios. También puede utilizar esta función para cambiar las etiquetas a otros idiomas como árabe, hindi, polaco, etc.

##  **Personalizar la configuración de globalización para la tabla dinámica**

El siguiente código de muestra explica cómo personalizar la configuración de globalización para la tabla dinámica. Crea una clase*Configuración de globalización de tabla dinámica personalizada* derivado de una clase base[**Configuración de globalización de Pivot**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)y anula todos sus métodos necesarios. Estos métodos devuelven el texto personalizado para *Pivote Total, Subtotal, Gran Total, Todos los elementos, Varios elementos, Etiquetas de columna, Etiquetas de fila, Valores en blanco*. Luego asigna el objeto de esta clase a[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) propiedad. El código carga el[archivo excel fuente](40468488.xlsx) que contiene la tabla dinámica, actualiza y calcula sus datos y los guarda como[salida PDF](40468487.pdf) archivo. La siguiente captura de pantalla muestra el efecto del código de muestra en la salida PDF. Como puede ver en la captura de pantalla, diferentes partes de la tabla dinámica ahora tienen un texto personalizado devuelto por los métodos anulados de[**Configuración de globalización de Pivot**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)clase.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
