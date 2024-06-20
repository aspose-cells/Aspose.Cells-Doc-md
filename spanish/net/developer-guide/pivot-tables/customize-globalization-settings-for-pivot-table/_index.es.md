---
title: Personalizar la configuración de globalización para la tabla dinámica
type: docs
weight: 50
url: /es/net/customize-globalization-settings-for-pivot-table/
---

## **Escenarios de uso posibles**

A veces quieres personalizar el texto de *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* según tus requisitos. Aspose.Cells te permite personalizar la configuración de globalización de la tabla dinámica para tratar con tales escenarios. También puedes usar esta función para cambiar las etiquetas a otros idiomas como árabe, hindi, polaco, etc.

## **Personalizar la configuración de globalización para la tabla dinámica**

El siguiente código de muestra explica cómo personalizar la configuración de globalización para la tabla dinámica. Crea una clase *CustomPivotTableGlobalizationSettings* derivada de una clase base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) y anula todos sus métodos necesarios. Estos métodos devuelven el texto personalizado para los *Total de tabla dinámica, Subtotal, Gran total, Todos los elementos, Elementos múltiples, Etiquetas de columna, Etiquetas de fila, Valores en blanco*. Luego asigna el objeto de esta clase a la propiedad [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/). El código carga el [archivo de Excel fuente](40468488.xlsx) que contiene la tabla dinámica, actualiza y calcula sus datos y lo guarda como [archivo de PDF de salida](40468487.pdf). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo de PDF de salida. Como se puede ver en la captura de pantalla, diferentes partes de la tabla dinámica tienen ahora un texto personalizado devuelto por los métodos anulados de la clase [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
