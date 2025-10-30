---
title: Convertir Excel a JSON con Golang mediante C++
linktitle: Convertir Excel a JSON
type: docs
weight: 300
url: /es/go-cpp/convert-excel-to-json/
description: Aprende a convertir archivos Excel a JSON con Aspose.Cells usando C++.
keywords: Exportar Libro a JSON sin office 2013, office 2016, office 2019 y office 365
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de una hoja de cálculo a un archivo JSON (JavaScript Object Notation).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

No hay necesidad de preguntarse cómo convertir un Libro de Excel a JSON, porque la biblioteca Aspose.Cells for C++ tiene la mejor solución. La API de Aspose.Cells soporta la conversión de hojas de cálculo a formato JSON. Para exportar el libro a JSON, pasa [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) para especificar configuraciones adicionales al exportar la hoja de trabajo a JSON.

El siguiente ejemplo de código demuestra cómo exportar un Libro de Excel a JSON. Consulta el código para convertir [archivo fuente](sample.xlsx) al archivo JSON generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
El siguiente ejemplo de código, que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales, demuestra cómo exportar un Libro de Excel a JSON. Consulta el código para convertir [archivo fuente](sample.xlsx) al archivo JSON generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
