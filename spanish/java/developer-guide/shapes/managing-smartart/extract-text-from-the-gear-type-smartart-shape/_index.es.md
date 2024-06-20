---
title: Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje
type: docs
weight: 130
url: /es/java/extract-text-from-the-gear-type-smartart-shape/
---

## **Escenarios de uso posibles**

Aspose.Cells puede extraer texto de la Forma de Arte Inteligente de Tipo de Engranaje. Para hacerlo, primero debe convertir la Forma de Arte Inteligente a Forma de Grupo usando el método [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--). Luego debe obtener la matriz de todas las Formas Individuales que forman la Forma de Grupo usando el método [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--). Finalmente, puede iterar todas las Formas Individuales uno por uno en un bucle y extraer su texto usando la propiedad [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text).

## **Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](67338510.xlsx) que contiene una Forma de Arte Inteligente de Tipo de Engranaje. Luego extrae el texto de sus formas individuales como se discutió anteriormente. Consulte la salida de la consola del código a continuación para obtener más información.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
