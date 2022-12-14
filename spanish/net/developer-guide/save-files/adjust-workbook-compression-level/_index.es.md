---
title: Ajustar el nivel de compresión del libro
type: docs
weight: 180
url: /es/net/adjust-workbook-compression-level/
---
## **Ajustar el nivel de compresión del libro de trabajo**

Los desarrolladores pueden ajustar el nivel de compresión del libro de trabajo cuando trabajan con libros de trabajo más grandes. Los desarrolladores pueden priorizar tamaños de archivo más pequeños sobre el tiempo de procesamiento o viceversa. Aspose.Cells proporciona**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** enumeración que puede usar para establecer el nivel de compresión del libro de trabajo. los**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** enumeración proporciona los siguientes miembros.

- Level1: La compresión más rápida pero menos efectiva.
- Nivel 2: Un poco más lento, pero mejor que el nivel 1.
- Nivel 3: Un poco más lento, pero mejor que el nivel 2.
- Nivel 4: Un poco más lento, pero mejor que el nivel 3.
- Nivel 5: Un poco más lento que el nivel 4, pero con mejor compresión.
- Level6: Un buen equilibrio entre velocidad y eficiencia de compresión.
- Level7: ¡Bastante buena compresión!
- Level8: ¡Mejor compresión que Level7!
- Level9: La "mejor" compresión, donde mejor significa la mayor reducción en el tamaño del flujo de datos de entrada. Esta es también la compresión más lenta.

 El siguiente fragmento de código demuestra el uso de**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**enumeración y compara el tiempo de conversión para Level1, Level6 y Level9. También puede comparar los tamaños de los archivos generados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
