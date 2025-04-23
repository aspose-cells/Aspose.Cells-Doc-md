---
title: Obtener rango con enlaces externos
type: docs
weight: 140
url: /es/java/get-range-with-external-links/
---

## **Obtener Rango con Vínculos Externos**

Muchas veces los archivos de Excel acceden a datos de otros archivos de Excel mediante enlaces externos. Aspose.Cells proporciona la opción de recuperar estos enlaces externos utilizando el método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-). El método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) devuelve un array de tipo [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). La clase [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) proporciona una propiedad [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName) que devuelve el nombre del archivo externo. La clase [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) expone los siguientes miembros.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): La columna final del área
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): La fila final del área
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Obtener el nombre del archivo externo si esta es una referencia externa
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indica si esto es un área
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indica si esto es un enlace externo
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indica en qué hoja está esta referencia
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): La columna de inicio del área
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): La fila de inicio del área

El código de muestra dado a continuación demuestra el uso del método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) para obtener rangos con enlaces externos.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
{{< app/cells/assistant language="java" >}}
