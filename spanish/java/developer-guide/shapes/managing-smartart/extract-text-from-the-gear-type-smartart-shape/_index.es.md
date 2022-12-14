---
title: Extraiga texto de la forma SmartArt de tipo de engranaje
type: docs
weight: 130
url: /es/java/extract-text-from-the-gear-type-smartart-shape/
---
## **Posibles escenarios de uso**

Aspose.Cells puede extraer texto de Gear Type Smart Art Shape. Para hacerlo, primero debe convertir Smart Art Shape a Group Shape usando el[**Forma.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) método. Luego, debe obtener la matriz de todas las Formas individuales que forman la Forma de grupo usando el[**FormaGrupo.getFormasAgrupadas()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) método. Finalmente, puede iterar todas las formas individuales una por una en un bucle y extraer su texto usando el[**Forma.Texto**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)propiedad.

## **Extraiga texto de la forma SmartArt de tipo de engranaje**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](67338510.xlsx)que contiene Gear Type Smart Art Shape. Luego extrae el texto de sus formas individuales como se discutió anteriormente. Consulte la salida de la consola del código que se proporciona a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
