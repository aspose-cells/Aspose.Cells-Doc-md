---
title: Convertir fechas a fechas japonesas con Python.NET
linktitle: Convertir Fechas a Fechas Japonesas
type: docs
weight: 350
url: /es/python-net/convert-dates-to-japanese-dates/
description: Aprende cómo convertir fechas gregorianas a fechas japonesas en archivos Excel usando Aspose.Cells para Python via .NET.
---

{{% alert color="primary" %}} 

En el calendario japonés, una nueva era comienza con el reinado de un nuevo emperador. El 1 de mayo de 2019, un nuevo emperador asumió el poder, finalizando la era Heisei y comenzando la era Reiwa.

{{% /alert %}} 

Aspose.Cells ofrece una forma de convertir fechas gregorianas en fechas japonesas considerando los cambios de era. El siguiente fragmento de código demuestra cómo convertir un archivo Excel fuente que contiene fechas gregorianas en un PDF con fechas japonesas:

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```python
import os
from aspose.cells import Workbook, LoadOptions, LoadFormat, SaveFormat, CountryCode

# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Create output directory if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize load options with XLSX format
options = LoadOptions(LoadFormat.XLSX)
options.region = CountryCode.JAPAN

# Load workbook with Japanese regional settings
workbook = Workbook(os.path.join(source_dir, "JapaneseDates.xlsx"), options)

# Save as PDF
workbook.save(os.path.join(output_dir, "JapaneseDates.pdf"), SaveFormat.PDF)
```

**Conversión con Python.NET:**


Nota: asegúrate de que el soporte para el idioma japonés esté habilitado en tu entorno para conversiones precisas de eras. La clase [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) y las [Opciones de Guardado en PDF](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) proporcionan la funcionalidad necesaria para esta conversión.
