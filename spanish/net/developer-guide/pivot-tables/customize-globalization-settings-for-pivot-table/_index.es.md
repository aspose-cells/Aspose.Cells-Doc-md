---
title: Personalizar la configuración de globalización para la tabla dinámica
type: docs
weight: 50
url: /es/net/customize-globalization-settings-for-pivot-table/
---
## **Posibles escenarios de uso**

 A veces desea personalizar el*Total de pivote, subtotal, total general, todos los elementos, elementos múltiples, etiquetas de columna, etiquetas de fila, valores en blanco*texto según sus requisitos. Aspose.Cells le permite personalizar la configuración de globalización de la tabla dinámica para hacer frente a tales escenarios. También puede usar esta función para cambiar las etiquetas a otros idiomas como árabe, hindi, polaco, etc.

## **Personalizar la configuración de globalización para la tabla dinámica**

 El siguiente código de ejemplo explica cómo personalizar la configuración de globalización para la tabla dinámica. Crea una clase*Configuración de globalización de tabla dinámica personalizada* derivado de una clase base[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) y anula todos sus métodos necesarios. Estos métodos devuelven el texto personalizado para el*Total de pivote, subtotal, total general, todos los elementos, elementos múltiples, etiquetas de columna, etiquetas de fila, valores en blanco*. Luego asigna el objeto de esta clase a[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) propiedad. El código carga el[archivo fuente excel](40468488.xlsx) que contiene la tabla dinámica, actualiza y calcula sus datos y los guarda como[PDF de salida](40468487.pdf)expediente. La siguiente captura de pantalla muestra el efecto del código de muestra en el PDF de salida. Como puede ver en la captura de pantalla, diferentes partes de la tabla dinámica ahora tienen un texto personalizado devuelto por los métodos anulados de[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)clase.

![todo:imagen_alternativa_texto](customize-globalization-settings-for-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
