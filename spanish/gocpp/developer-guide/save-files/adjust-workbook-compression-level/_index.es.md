---
title: Ajustar nivel de compresión del libro de trabajo con Golang a través de C++
linktitle: Ajustar nivel de compresión del libro de trabajo
type: docs
weight: 180
url: /es/go-cpp/adjust-workbook-compression-level/
description: Aprenda cómo ajustar el nivel de compresión de un libro de trabajo usando Aspose.Cells for C++ para optimizar tamaño de archivo y tiempo de procesamiento.
---

## **Ajustar el Nivel de Compresión del Libro de Trabajo**

Los desarrolladores pueden ajustar el nivel de compresión del libro de trabajo al trabajar con libros de trabajo más grandes. Los desarrolladores pueden priorizar tamaños de archivo más pequeños sobre el tiempo de procesamiento o viceversa. Aspose.Cells proporciona la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) que se puede utilizar para establecer el nivel de compresión del libro de trabajo. La enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) proporciona los siguientes miembros.

- Nivel1: La compresión más rápida pero menos efectiva.
- Nivel2: Un poco más lento, pero mejor, que el nivel 1.
- Nivel3: Un poco más lento, pero mejor, que el nivel 2.
- Nivel4: Un poco más lento, pero mejor, que el nivel 3.
- Nivel5: Un poco más lento que el nivel 4, pero con una mejor compresión.
- Nivel6: Un buen equilibrio entre velocidad y eficiencia de compresión.
- Nivel7: ¡Buena compresión!
- Nivel8: ¡Mejor compresión que Nivel7!
- Nivel9: La compresión "mejor", donde mejor significa la mayor reducción en el tamaño del flujo de datos de entrada. También es la compresión más lenta.

El siguiente fragmento de código demuestra el uso de la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) y compara el tiempo de conversión para Nivel1, Nivel6 y Nivel9. También puedes comparar los tamaños de los archivos generados.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}
