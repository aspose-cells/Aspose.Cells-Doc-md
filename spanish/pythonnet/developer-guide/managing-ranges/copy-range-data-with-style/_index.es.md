---
title: Copiar Datos de Rango con Estilo
type: docs
weight: 610
url: /es/python-net/copy-range-data-with-style/
description: Este artículo describe cómo copiar datos de rango con estilo con la biblioteca Aspose.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, cómo copiar datos de rango con estilo en Python, cómo copiar datos de rango con estilo en la biblioteca de excel de Python.
---

{{% alert color="primary" %}}

[Copiar solo datos de rango](/cells/es/python-net/copy-range-data-only/) explica cómo copiar los datos de un rango de celdas a otro rango. Específicamente, procesa y aplica un nuevo conjunto de estilos a las celdas copiadas. Aspose.Cells for Python via .NET también puede copiar un rango completo con formato. Este artículo lo explica.

{{% /alert %}}

Aspose.Cells for Python via .NET proporciona una variedad de clases y métodos para trabajar con rangos, por ejemplo, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) y [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

Este ejemplo:

1. Crea un libro de trabajo.
1. Rellena un número de celdas en la primera hoja de cálculo con datos.
1. Crea un [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) con atributos de formato especificados.
1. Aplica el estilo al rango de datos.
1. Crea un segundo rango de celdas.
1. Copia datos con el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
