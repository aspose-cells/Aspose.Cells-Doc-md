---
title: Copiar Rangos de Excel
linktitle: Copiar Rangos
type: docs
weight: 105
url: /es/python-net/copy-ranges-of-excel/
description: Este artículo describe cómo copiar rangos de Excel con la biblioteca Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Cómo copiar rangos de Excel en Python, Cómo copiar solo datos de un rango con la biblioteca de Excel en Python, cómo pegar un rango con opciones en Python, cómo copiar solo datos del rango.
---

## **Introducción**

En Excel, puede seleccionar un rango, copiarlo y luego pegarlo con opciones específicas en la misma hoja de cálculo, en otras hojas de cálculo o en otros archivos.

## **Copiar rangos utilizando la biblioteca Aspose.Cells para Python Excel**

Aspose.Cells para Python via .NET proporciona algunas sobrecargas de métodos [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) para copiar el rango.
Y [**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) solo el estilo de copia del rango; [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) solo el valor de copia del rango

## **Copiar Rango**

Creación de dos rangos: el rango de origen, el rango de destino, luego copiar el rango de origen al rango de destino con el método [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range).

Vea el siguiente código:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **Pegar Rango Con Opciones**

Aspose.Cells para Python via .NET admite pegar el rango con un tipo específico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **Solo copiar datos del rango**
También puedes copiar los datos con el método [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) como en el siguiente código:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **Temas avanzados**
- [Copiar alturas de fila del rango de origen al rango de destino](/cells/es/python-net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="python-net" >}}
