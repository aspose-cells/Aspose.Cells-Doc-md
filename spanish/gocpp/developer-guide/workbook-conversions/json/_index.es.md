---
title: Convertir Libro de trabajo a JSON con Golang a través de C++
linktitle: Convertir Libro a JSON
type: docs
weight: 300
url: /es/go-cpp/convert-workbook-to-json/
description: Aprende a convertir libros de Excel a formato JSON usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells soporta convertir un libro en un archivo JSON (JavaScript Object Notation).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato JSON. Para exportar el libro a JSON, pasa [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a JSON usando el miembro de enumeración [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). Consulte el código para convertir el [archivo fuente](book1.xlsx) en el [archivo JSON de salida](book1.json) generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **Temas avanzados**
- [Convertir CSV a JSON](/cells/es/cpp/convert-csv-to-json/)
- [Convertir Excel a JSON](/cells/es/cpp/convert-excel-to-json/)
- [Convertir JSON a CSV](/cells/es/cpp/convert-json-to-csv/)
- [Convertir JSON a Excel](/cells/es/cpp/convert-json-to-excel/)
