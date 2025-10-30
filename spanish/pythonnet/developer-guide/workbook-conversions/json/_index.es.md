---
title: Json
type: docs
weight: 300
url: /es/python-net/convert-workbook-to-json/
description: Aprende cómo convertir el libro de Excel a json con la API de Aspose.Cells para Python via .NET.
keywords: Convertir libro de trabajo de Excel a json, Convertir libro de trabajo de Excel a json Pyton via NET, Exportar libro a json, Convertir libro de Excel a json
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET admite la conversión de un libro de trabajo a un archivo Json (Notación de Objetos de JavaScript).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

La API de Aspose.Cells para Python via .NET brinda soporte para convertir hojas de cálculo al formato JSON. Para exportar el libro de trabajo a JSON, pasa [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) como segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo activa a Json utilizando el miembro de enumeración [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat). Consulta el código para convertir el archivo de origen [book1.xlsx] al archivo Json de salida [book1.Json] generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **Temas avanzados**
- [Convertir CSV a JSON](/cells/es/python-net/convert-csv-to-json/)
- [Convertir-Excel-a-JSON](/cells/es/python-net/convert-excel-to-json/)
- [Convertir JSON a CSV](/cells/es/python-net/convert-json-to-csv/)
- [Convertir-JSON-a-Excel](/cells/es/python-net/convert-json-to-excel/)
{{< app/cells/assistant language="python-net" >}}
