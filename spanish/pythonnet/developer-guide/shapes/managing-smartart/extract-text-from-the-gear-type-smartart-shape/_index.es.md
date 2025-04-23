---
title: Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje
type: docs
weight: 500
url: /es/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **Escenarios de uso posibles**

Aspose.Cells puede extraer texto de la Forma de Arte SmartArt de Tipo de Engranaje. Para hacerlo, primero debes convertir la Forma de Arte SmartArt en Forma de Grupo usando el método [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art). Luego debes obtener el arreglo de todas las formas individuales que forman la Forma de Grupo usando el método [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes). Finalmente, puedes iterar todas las formas individuales una por una en un bucle y extraer su texto usando la propiedad [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text).

## **Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje**

El siguiente código de muestra carga el [archivo Excel de muestra](67338483.xlsx) que contiene una Forma de Arte SmartArt de Tipo de Engranaje. Luego extrae el texto de sus formas individuales como se discutió anteriormente. Consulte la salida de la consola del código a continuación para una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Salida de la consola**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
