---
title: Agregar partes XML personalizadas y seleccionarlas por ID
type: docs
weight: 70
url: /es/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Escenarios de uso posibles**

Las partes de XML personalizadas son los datos XML que se almacenan dentro de los documentos de Microsoft Excel y son utilizados por las aplicaciones que trabajan con ellos. Actualmente no hay una forma directa de agregarlos mediante la interfaz de usuario de Microsoft Excel. Sin embargo, puede agregarlos programáticamente de varias maneras, por ejemplo, usando VSTO, usando Aspose.Cells, etc. Use el método [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) si desea agregar una parte de XML personalizada usando la API de Aspose.Cells. También puede establecer su ID utilizando la propiedad [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). De manera similar, si desea seleccionar una parte de XML personalizada por ID, puede usar el método [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid).

## **Agregar partes XML personalizadas y seleccionarlas por ID**

El siguiente código de muestra primero agrega cuatro partes de XML personalizadas utilizando el método [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add). Luego establece sus ID utilizando la propiedad [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Finalmente, encuentra o selecciona una de las partes de XML personalizadas agregadas usando el método [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid). Consulte también la salida por consola del código a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
