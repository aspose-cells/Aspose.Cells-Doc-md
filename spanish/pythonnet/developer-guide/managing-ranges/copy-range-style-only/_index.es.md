---
title: Copiar solo estilo de rango
type: docs
weight: 620
url: /es/python-net/copy-range-style-only/
description: Este artículo describe cómo copiar solo el estilo del rango con Aspose.Cells para la biblioteca Python via .NET.
keywords: Biblioteca de Excel de Python, Cómo copiar solo el estilo del rango en Python, Cómo copiar solo el estilo del rango en la biblioteca de Excel de Python.
---

{{% alert color="primary" %}}

[Copiar solo datos de rango](/cells/es/python-net/copy-range-data-only/) y [Copiar datos de rango con estilo](/cells/es/python-net/copy-range-data-with-style/) explican cómo copiar datos de un rango a otro por sí mismo o completo con formato. También es posible copiar solo el formato. Este artículo muestra cómo.

{{% /alert %}} 

Este ejemplo crea un libro de trabajo, lo llena con datos y copia solo el estilo de un rango.

1. Crear un rango.
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) con atributos de formato especificados.
1. Aplica el formato de estilo al rango.
1. Crear un segundo rango de celdas.
1. Copiar el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeStyleOnly-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
