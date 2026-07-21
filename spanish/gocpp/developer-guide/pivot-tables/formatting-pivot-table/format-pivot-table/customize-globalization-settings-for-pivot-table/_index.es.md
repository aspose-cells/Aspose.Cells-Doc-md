---
title: Personalizar la configuración de globalización para la tabla dinámica con Golang vía C++
linktitle: Personalizar la configuración de globalización para la tabla dinámica
type: docs
weight: 50
url: /es/go-cpp/customize-globalization-settings-for-pivot-table/
description: Aprende cómo personalizar las configuraciones de globalización de la tabla dinámica usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces quieres personalizar el texto de *Total de Pivote, Subtotal, Total General, Todos los Elementos, Elementos Múltiples, Etiquetas de Columna, Etiquetas de Fila, Valores en Blanco* según tus requisitos. Aspose.Cells for C++ te permite personalizar las configuraciones de globalización de la tabla dinámica para manejar tales escenarios. También puedes usar esta característica para cambiar las etiquetas a otros idiomas como árabe, hindi, polaco, etc.

## **Personalizar la configuración de globalización para la tabla dinámica**

El siguiente código de ejemplo explica cómo personalizar las configuraciones de globalización para la tabla dinámica en C++. Crea una clase *CustomPivotTableGlobalizationSettings* derivada de la clase base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) y sobrescribe todos los métodos necesarios. Estos métodos devuelven texto personalizado para varios elementos de la tabla dinámica. Luego, el código asigna esta implementación a la propiedad [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). El ejemplo carga un archivo [Excel fuente](40468488.xlsx), actualiza los datos de la tabla dinámica y lo guarda como [PDF de salida](40468487.pdf). La captura de pantalla a continuación muestra etiquetas personalizadas en la salida.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
