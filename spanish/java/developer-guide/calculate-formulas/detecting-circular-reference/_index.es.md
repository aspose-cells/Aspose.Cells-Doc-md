---
title: Detectar Referencia Circular
type: docs
weight: 70
url: /es/java/detecting-circular-reference/
---

## **Introducción**

Los libros pueden tener referencias circulares y a veces es necesario detectar si las referencias circulares existen o no.

## **Concepto detrás de la detección de la referencia circular**

Las referencias circulares solo se pueden detectar cuando se calcula la fórmula porque las referencias de una fórmula comúnmente dependen del resultado calculado de otras partes u otras fórmulas. Por lo tanto, proporcionamos nuevas API para este requisito (para recopilar celdas con referencias circulares) en el proceso de cálculo de fórmulas:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Representa el cálculo de datos relevantes sobre una celda que se está calculando

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): será invocado por el motor de cálculo de fórmulas cuando se encuentren referencias circulares, el elemento en el enumerador es objetos [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) que representan todas las celdas en un círculo. El valor devuelto denota si el motor de fórmulas necesita calcular esas celdas de forma circular después de esta llamada.

El usuario puede recopilar esas referencias circulares en la implementación del método [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-).

El archivo de muestra fuente se puede descargar desde el siguiente enlace:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Definición de la clase *CircularMonitor* que se deriva de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) es la siguiente:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
