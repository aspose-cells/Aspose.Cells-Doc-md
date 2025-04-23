---
title: Detectar Referencia Circular
description: Este artículo presenta cómo usar la biblioteca Aspose.Cells para detectar referencias circulares en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar el método proporcionado por Aspose.Cells para detectar referencias circulares y obtener los resultados. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, referencias circulares, detección
type: docs
weight: 70
url: /es/net/detecting-circular-reference/
---

## **Introducción**

Los libros pueden tener referencias circulares y a veces es necesario detectar si las referencias circulares existen o no.

## **Concepto detrás de la detección de la referencia circular**

Las referencias circulares solo se pueden detectar cuando se calcula la fórmula porque las referencias de una fórmula comúnmente dependen del resultado calculado de otras partes u otras fórmulas. Por lo tanto, proporcionamos nuevas API para este requisito (para recopilar celdas con referencias circulares) en el proceso de cálculo de fórmulas:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Representa el cálculo de datos relevantes sobre una celda que se está calculando

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): será invocado por el motor de cálculo de fórmulas cuando se encuentren referencias circulares, el elemento en el enumerador es objetos [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) que representan todas las celdas en un círculo. El valor devuelto denota si el motor de fórmulas necesita calcular esas celdas de forma circular después de esta llamada.

El usuario puede recopilar esas referencias circulares en la implementación del método [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular).

El archivo de muestra fuente se puede descargar desde el siguiente enlace:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definición de la clase *CircularMonitor* que se deriva de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) es la siguiente:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
