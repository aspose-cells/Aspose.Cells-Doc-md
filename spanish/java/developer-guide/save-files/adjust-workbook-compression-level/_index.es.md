---
title: Ajustar el nivel de compresión del libro de trabajo
type: docs
weight: 130
url: /es/java/adjust-workbook-compression-level/
---

## **Ajustar el nivel de compresión del libro de trabajo**

Los desarrolladores pueden ajustar el nivel de compresión del libro de trabajo al trabajar con libros de trabajo más grandes. Los desarrolladores pueden priorizar tamaños de archivo más pequeños sobre el tiempo de procesamiento o viceversa. Aspose.Cells proporciona la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) que se puede utilizar para establecer el nivel de compresión del libro de trabajo. La enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) proporciona los siguientes elementos.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1): La compresión más rápida pero menos efectiva.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2): Un poco más lento, pero mejor, que el nivel 1.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3): Un poco más lento, pero mejor, que el nivel 2.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4): Un poco más lento, pero mejor, que el nivel 3.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5): Un poco más lento que el nivel 4, pero con mejor compresión.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6): Un buen equilibrio entre velocidad y eficiencia de compresión.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7): ¡Buena compresión!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8): ¡Mejor compresión que Level7!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9): La compresión "óptima", donde óptima significa la mayor reducción en el tamaño del flujo de datos de entrada. Esta también es la compresión más lenta.

El siguiente fragmento de código demuestra el uso de la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) y compara el tiempo de conversión para [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6), y [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9). También puedes comparar los tamaños de los archivos generados.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
