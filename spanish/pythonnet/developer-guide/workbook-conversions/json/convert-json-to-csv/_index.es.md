---
title: Convertir JSON a CSV
type: docs
weight: 210
url: /es/python-net/convert-json-to-csv/
description: Aprenda a convertir archivos json a csv con Aspose.Cells for Python via .NET API.
keywords: Python Convert json to csv, Convert json to csv Pyton via NET, Export json to csv, Convert json to csv
---
##  **Convertir JSON a CSV**

Aspose.Cells for Python via .NET admite la conversión de JSON simple y anidado a CSV. Para ello, API proporciona**[Opciones de JsonLayout](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)** y**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** clases. El**[Opciones de JsonLayout](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**La clase proporciona opciones para el diseño JSON como**[ignore_array_title](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)**(ignora el título si la matriz es una propiedad de un objeto) o ** [array_as_table](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)**(procesa la matriz como una tabla). El **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**La clase procesa el JSON usando las opciones de diseño configuradas con el**[Opciones de JsonLayout](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**clase.

El siguiente ejemplo de código demuestra el uso de**[Opciones de JsonLayout](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**y**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** clases para cargar el[fuente JSON archivo](104398869.json) y genera el[salida del archivo CSV](104398870.csv).

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
