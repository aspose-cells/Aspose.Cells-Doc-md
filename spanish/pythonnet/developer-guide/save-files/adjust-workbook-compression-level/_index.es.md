---
title: Ajustar el nivel de compresión del libro de trabajo
type: docs
weight: 180
url: /es/python-net/adjust-workbook-compression-level/
---

## **Ajustar el Nivel de Compresión del Libro de Trabajo**

Los desarrolladores pueden ajustar el nivel de compresión del libro al trabajar con libros más grandes. Los desarrolladores pueden priorizar tamaños de archivo más pequeños sobre tiempo de procesamiento o viceversa. Aspose.Cells para Python via .NET proporciona la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) que se puede usar para establecer el nivel de compresión del libro. La enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) ofrece los siguientes miembros.

- Nivel1: La compresión más rápida pero menos efectiva.
- Nivel2: Un poco más lento, pero mejor, que el nivel 1.
- Nivel3: Un poco más lento, pero mejor, que el nivel 2.
- Nivel4: Un poco más lento, pero mejor, que el nivel 3.
- Nivel5: Un poco más lento que el nivel 4, pero con una mejor compresión.
- Nivel6: Un buen equilibrio entre velocidad y eficiencia de compresión.
- Nivel7: ¡Buena compresión!
- Nivel8: ¡Mejor compresión que Nivel7!
- Nivel9: La compresión "mejor", donde mejor significa la mayor reducción en el tamaño del flujo de datos de entrada. También es la compresión más lenta.

El siguiente fragmento de código demuestra el uso de la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) y compara el tiempo de conversión para Nivel1, Nivel6 y Nivel9. También puedes comparar los tamaños de los archivos generados.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
