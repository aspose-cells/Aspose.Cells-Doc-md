---
title: Obtener rango con enlaces externos
type: docs
weight: 120
url: /es/python-net/get-range-with-external-links/
description: Este artículo muestra cómo obtener un rango con enlaces externos utilizando la API de Aspose.Cells para Python via .NET.
keywords: Librería de Excel de Python, obtener rango con enlaces externos en Python.
---

## **Obtener Rango con Vínculos Externos**

Muchas veces, los archivos de Excel acceden a datos de otros archivos de Excel utilizando enlaces externos. Aspose.Cells for Python via .NET proporciona la opción de recuperar estos enlaces externos utilizando el método [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool). El método [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) devuelve una matriz de tipo [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). La clase [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) proporciona una propiedad [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) que devuelve el nombre del archivo externo. La clase [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) expone los siguientes miembros.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): La columna final del área
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): La fila final del área
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Obtener el nombre del archivo externo si esta es una referencia externa
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Indica si esto es un área
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Indica si esto es un enlace externo
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Indica en qué hoja está esta referencia
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): La columna de inicio del área
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): La fila de inicio del área

El código de muestra que se muestra a continuación demuestra el uso del método [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) para obtener rangos con enlaces externos.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
