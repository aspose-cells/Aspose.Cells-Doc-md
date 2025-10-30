---
title: Convertir JSON a CSV
type: docs
weight: 210
url: /es/python-net/convert-json-to-csv/
description: Aprende cómo convertir un archivo json a csv con la API Aspose.Cells para Python via .NET.
keywords: Python Convertir json a csv, Convertir json a csv Pyton via NET, Exportar json a csv, Convertir json a csv
---

## **Convertir JSON a CSV**

Aspose.Cells for Python via .NET admite la conversión de JSON simple y anidado a CSV. Para esto, la API proporciona las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) y [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) ofrece opciones para el diseño JSON como [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/) (ignora el título si el array es una propiedad de un objeto) o [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/) (procesa el array como una tabla). La clase [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) procesa el JSON utilizando las opciones de diseño establecidas con la clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions).

El siguiente ejemplo de código demuestra el uso de las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) y [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) para cargar el [archivo JSON fuente](104398869.json) y generar el [archivo CSV de salida](104398870.csv).

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
