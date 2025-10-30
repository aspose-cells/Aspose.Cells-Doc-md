---
title: Extraer Texto de la Forma SmartArt de Tipo Engranaje con Golang a través de C++
linktitle: Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje
type: docs
weight: 500
url: /es/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aprenda cómo extraer texto de formas de SmartArt de tipo engranaje en Excel usando Aspose.Cells for C++ con orientación paso a paso y ejemplos de código.
---

## **Escenarios de uso posibles**

Aspose.Cells for C++ puede extraer texto de la forma de SmartArt de tipo engranaje. Para lograrlo, siga estos pasos:
1. Convertir la forma de SmartArt en forma de grupo usando el método [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/).
2. Recuperar todas las formas individuales que forman la forma de grupo usando el método [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/).
3. Iterar a través de cada forma individual y extraer el texto usando el método [**GetText()**](https://reference.aspose.com/cells/go-cpp/).

## **Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje**

El siguiente código de ejemplo carga un [archivo de Excel de muestra](67338483.xlsx) que contiene una forma de SmartArt de tipo engranaje y extrae texto de sus formas individuales. Consulte la salida en consola a continuación para obtener los resultados.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Salida de la consola**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
