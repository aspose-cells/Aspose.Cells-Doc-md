---
title: Convertir Excel a JSON
type: docs
weight: 300
url: /es/net/convert-excel-to-json/
description: Aprenda cómo convertir un archivo de Excel a JSON con Aspose.Cells.
keywords: Exportar Libro a JSON sin office 2013, office 2016, office 2019 y office 365
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de una hoja de cálculo a un archivo JSON (JavaScript Object Notation).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

No es necesario preguntarse cómo convertir una hoja de cálculo de Excel a JSON, porque la biblioteca Aspose.Cells para .NET tiene la mejor solución. La API Aspose.Cells proporciona soporte para convertir hojas de cálculo al formato JSON. Para exportar la hoja de cálculo a JSON, pase [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). También puede usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo de Excel a JSON. Consulte el código para convertir el [archivo fuente](muestra.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

El siguiente ejemplo de código, que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales, demuestra la exportación de una hoja de cálculo de Excel a JSON. Consulte el código para convertir el [archivo fuente](muestra.xlsx) al archivo Json generado por el código como referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}

