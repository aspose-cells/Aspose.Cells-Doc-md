---
title: Obtener rango con enlaces externos
type: docs
weight: 120
url: /es/net/get-range-with-external-links/
---
## **Obtener rango con enlaces externos**

Muchas veces, los archivos de Excel acceden a datos de otros archivos de Excel mediante enlaces externos. Aspose.Cells ofrece la opción de recuperar estos enlaces externos mediante el[**Nombre.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)método. Él[**Nombre.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)método devuelve una matriz de tipo[**Área referida**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). Él[**Área referida**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) la clase proporciona una[**Nombre de archivo externo**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)propiedad que devuelve el nombre del archivo externo. Él[**Área referida**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)La clase expone los siguientes miembros.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): La columna final del área
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): La última fila del área
- [**Nombre de archivo externo**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): obtenga el nombre del archivo externo si se trata de una referencia externa
- [**esÁrea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indica si se trata de un área
- [**Es un enlace externo**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indica si se trata de un enlace externo
- [**NombreHoja**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indica en qué hoja se encuentra esta referencia
- [**Columna de inicio**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): La columna de inicio del área
- [**fila de inicio**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): La fila de inicio del área

 El código de ejemplo que se proporciona a continuación demuestra el uso de[**Nombre.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)método para obtener rangos con enlaces externos.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
