---
title: Obtener rango con enlaces externos
type: docs
weight: 140
url: /es/java/get-range-with-external-links/
---
## **Obtener rango con enlaces externos**

Muchas veces, los archivos de Excel acceden a datos de otros archivos de Excel mediante enlaces externos. Aspose.Cells ofrece la opción de recuperar estos enlaces externos mediante el[**Nombre.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) método. los[**Nombre.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) método devuelve una matriz de tipo[**Área referida**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). los[**Área referida**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)la clase proporciona un[**Nombre de archivo externo**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)propiedad que devuelve el nombre del archivo externo. los[**Área referida**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)La clase expone los siguientes miembros.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): La columna final del área
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): La última fila del área
- [**Nombre de archivo externo**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): obtenga el nombre del archivo externo si se trata de una referencia externa
- [**esÁrea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indica si se trata de un área
- [**Es un enlace externo**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indica si se trata de un enlace externo
- [**NombreHoja**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indica en qué hoja se encuentra esta referencia
- [**Columna de inicio**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): La columna de inicio del área
- [**fila de inicio**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): La fila de inicio del área

El código de ejemplo que se proporciona a continuación demuestra el uso de[**Nombre.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) método para obtener rangos con enlaces externos.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
