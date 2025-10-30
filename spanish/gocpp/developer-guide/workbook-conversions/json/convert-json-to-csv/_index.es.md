---
title: Convertir JSON a CSV con Golang mediante C++
linktitle: Convertir JSON a CSV
type: docs
weight: 210
url: /es/go-cpp/convert-json-to-csv/
description: Aprende cómo convertir JSON a CSV usando Aspose.Cells for C++ con ejemplos de JSON simples y anidados.
---

## **Convertir JSON a CSV**

Aspose.Cells soporta la conversión de JSON simple y anidado a CSV. Para esto, la API ofrece las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) y [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) proporciona opciones para el diseño del JSON como [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (ignora el título si el array es una propiedad de un objeto) o [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (procesa el array como una tabla). La clase [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) procesa el JSON usando las opciones de diseño configuradas con la clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/).

El siguiente ejemplo de código demuestra el uso de las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) y [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) para cargar el archivo [JSON fuente](104398869.json) y genera el [archivo CSV de salida](104398870.csv).

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
