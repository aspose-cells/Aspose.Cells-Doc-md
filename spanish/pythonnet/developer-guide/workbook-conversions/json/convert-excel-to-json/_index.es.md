---
title: Convertir Excel a JSON
type: docs
weight: 300
url: /es/python-net/convert-excel-to-json/
description: Aprende cómo convertir un archivo de excel a json con la API Aspose.Cells para Python via .NET.
keywords: Python Convertir excel a json, Convertir excel a json Pyton via NET, Exportar Libro de Trabajo a json, Convertir archivo excel a json
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET admite la conversión de un Libro de Trabajo a archivo Json(Object Notation de JavaScript).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

No es necesario preguntarse cómo convertir un Libro de Trabajo de Excel a JSON, porque la biblioteca Aspose.Cells para Python via .NET tiene la mejor solución. La API de Aspose.Cells brinda soporte para convertir hojas de cálculo al formato JSON. Para exportar el libro de trabajo a JSON, pase [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) como segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions) para especificar ajustes adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo de Excel a JSON. Consulte el código para convertir el [archivo fuente](muestra.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New.py" >}}

El siguiente ejemplo de código, que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales, demuestra la exportación de una hoja de cálculo de Excel a JSON. Consulte el código para convertir el [archivo fuente](muestra.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New2.py" >}}

