---
title: Personalizar la configuración de globalización para la tabla dinámica
type: docs
weight: 20
url: /es/java/customize-globalization-settings-for-pivot-table/
---

## **Escenarios de uso posibles**

A veces quieres personalizar el texto de *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* según tus requisitos. Aspose.Cells te permite personalizar la configuración de globalización de la tabla dinámica para tratar con tales escenarios. También puedes usar esta función para cambiar las etiquetas a otros idiomas como árabe, hindi, polaco, etc.

## **Personalizar la configuración de globalización para la tabla dinámica**

El siguiente código de ejemplo explica cómo personalizar la configuración de globalización para la tabla dinámica. Crea una clase *CustomPivotTableGlobalizationSettings* derivada de una clase base [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) y anula todos sus métodos necesarios. Estos métodos devuelven el texto personalizado para *Total de Tabla Dinámica, Subtotal, Gran Total, Todos los Elementos, Múltiples Elementos, Etiquetas de Columna, Etiquetas de Fila, Valores en Blanco*. Luego asigna el objeto de esta clase a la propiedad [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings). El código carga el [archivo de excel fuente](40468491.xlsx) que contiene la tabla dinámica, actualiza y calcula sus datos y lo guarda como [archivo PDF de salida](40468490.pdf). La siguiente captura de pantalla muestra el efecto del código de ejemplo en el archivo PDF de salida. Como se puede ver en la captura de pantalla, diferentes partes de la tabla dinámica ahora tienen un texto personalizado devuelto por los métodos anulados de la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
