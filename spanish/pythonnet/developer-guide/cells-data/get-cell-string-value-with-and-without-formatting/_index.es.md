---
title: Obtener el valor de cadena de la celda con estrategia de formato
type: docs
weight: 240
url: /es/python-net/get-cell-string-value-with-format-strategy/
description: Aprende a obtener el valor de cadena de la celda con y sin formato a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Obtener valor de cadena de celda con y sin formato en Python, Recuperar valor de cadena de celda con y sin formato en Python, Obtener valor de cadena de celda con y sin formato en Python
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET proporciona un método [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) que se puede utilizar para obtener el valor de cadena de la celda con o sin formato. Supongamos que tienes una celda con el valor 0.012345 y lo has formateado para mostrar solo dos decimales. Entonces se mostrará como 0.01 en Excel. Puedes recuperar los valores de cadena tanto como 0.01 como 0.012345 utilizando el método [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/). Toma como parámetro un [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) enum que tiene los siguientes valores

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

El siguiente código de ejemplo explica el uso del método [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
