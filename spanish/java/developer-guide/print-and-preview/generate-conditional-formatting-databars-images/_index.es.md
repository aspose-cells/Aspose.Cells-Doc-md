---
title: Generar imágenes de barras de datos de formato condicional
type: docs
weight: 170
url: /es/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A veces, necesita generar imágenes de barras de datos de formato condicional. Puede utilizar el método [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) de Aspose.Cells para generar estas imágenes. Este artículo muestra cómo generar una imagen de barra de datos usando Aspose.Cells.

{{% /alert %}}

## **Ejemplo**

El siguiente código de muestra genera la imagen de DataBar de la celda C1. Primero, accede al objeto de condición de formato de la celda, y luego desde ese objeto, accede al objeto DataBar y utiliza su método [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) para generar la imagen de la celda. Finalmente, guarda la imagen en el disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
