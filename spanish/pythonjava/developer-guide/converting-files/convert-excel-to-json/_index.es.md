---
title: Convertir Excel a JSON
type: docs
weight: 300
url: /es/python-java/convert-excel-to-json/
description: Aprenda a convertir archivos de Excel a JSON con Aspose.Cells for Python via Java.
keywords: Exportar Libro a JSON sin office 2013, office 2016, office 2019 y office 365
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java admite la conversión de un libro a un archivo Json (JavaScript Object Notation).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

No es necesario preguntarse cómo convertir un libro de Excel a JSON, porque la biblioteca Aspose.Cells for Python via Java tiene la mejor opción. La API de Aspose.Cells for Python via Java proporciona soporte para la conversión de hojas de cálculo al formato JSON. Para exportar el libro a JSON, pase [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) como el segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). También puede usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra la exportación de un libro de Excel a Json. Consulte el código para convertir [archivo de origen](sample.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

El siguiente ejemplo de código, que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales, demuestra la exportación de una hoja de cálculo de Excel a JSON. Consulte el código para convertir el [archivo fuente](muestra.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
