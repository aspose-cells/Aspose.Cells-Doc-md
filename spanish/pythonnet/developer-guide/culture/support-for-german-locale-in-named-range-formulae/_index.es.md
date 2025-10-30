---
title: Soporte para formato alemán en fórmulas de rango nombrado con Python.NET
linktitle: Soporte para Configuración Regional Alemana en Fórmulas de Rango Nombrado
type: docs
weight: 60
url: /es/python-net/support-for-german-locale-in-named-range-formulae/
description: Aprende cómo manejar configuraciones regionales alemanas para fórmulas de rango nombrado en Excel usando Aspose.Cells para Python via .NET.
---

Las fórmulas en inglés están escritas en regiones con nombre. Este archivo de Excel puede abrirse en un entorno donde el sistema esté configurado para la localidad alemana, y la fórmula en inglés se traducirá al alemán. Este ejemplo requiere tener Excel instalado con configuraciones de idioma alemán y que la configuración regional del sistema sea alemana.

El archivo de ejemplo para probar esta función se puede descargar desde:  
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
{{< app/cells/assistant language="python-net" >}}
