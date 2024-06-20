---
title: Obtener rango con enlaces externos
type: docs
weight: 120
url: /es/net/get-range-with-external-links/
---

## **Obtener Rango con Vínculos Externos**

Muchas veces los archivos de Excel acceden a datos de otros archivos de Excel mediante enlaces externos. Aspose.Cells proporciona la opción de recuperar estos enlaces externos usando el método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas). El método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) devuelve una matriz de tipo [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). La clase [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) proporciona una propiedad [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) que devuelve el nombre del archivo externo. La clase [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) expone los siguientes miembros.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): La columna final del área
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): La fila final del área
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Obtener el nombre del archivo externo si esta es una referencia externa
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indica si esto es un área
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indica si esto es un enlace externo
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indica en qué hoja está esta referencia
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): La columna de inicio del área
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): La fila de inicio del área

El código de muestra que se muestra a continuación demuestra el uso del método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) para obtener rangos con enlaces externos.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
