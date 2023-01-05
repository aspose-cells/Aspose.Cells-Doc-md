---
title: Extraiga texto de la forma SmartArt de tipo de engranaje
type: docs
weight: 500
url: /es/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Posibles escenarios de uso**

 Aspose.Cells puede extraer texto de Gear Type Smart Art Shape. Para hacerlo, primero debe convertir Smart Art Shape a Group Shape usando el[**Forma.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) método. Luego, debe obtener la matriz de todas las Formas individuales que forman la Forma de grupo usando el[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) método. Finalmente, puede iterar todas las formas individuales una por una en un bucle y extraer su texto usando el[**Forma.Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)propiedad.

## **Extraiga texto de la forma SmartArt de tipo de engranaje**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](67338483.xlsx) que contiene Gear Type Smart Art Shape. Luego extrae el texto de sus formas individuales como se discutió anteriormente. Consulte la salida de la consola del código que se proporciona a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
