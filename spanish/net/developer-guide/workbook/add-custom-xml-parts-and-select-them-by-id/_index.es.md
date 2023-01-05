---
title: Agregue partes XML personalizadas y selecciónelas por ID
type: docs
weight: 70
url: /es/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Posibles escenarios de uso**

Las partes XML personalizadas son los datos XML que se almacenan dentro de los documentos de Excel Microsoft y son utilizados por las aplicaciones que se ocupan de ellos. No hay una forma directa de agregarlos usando la interfaz de usuario de Excel Microsoft en este momento. Sin embargo, puede agregarlos programáticamente de varias maneras, por ejemplo, usando VSTO, usando Aspose.Cells, etc. Utilice[**Libro de trabajo.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)si desea agregar una parte XML personalizada usando Aspose.Cells API. También puede configurar su ID, usando el[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)propiedad. Del mismo modo, si desea seleccionar Elemento XML personalizado por ID, puede utilizar[**Libro de trabajo.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)método.

## **Agregue partes XML personalizadas y selecciónelas por ID**

El siguiente código de muestra primero agrega cuatro partes XML personalizadas usando[**Libro de trabajo.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)método. Luego establece sus ID usando[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) propiedad. Finalmente, encuentra o selecciona una de las partes XML personalizadas agregadas usando[**Libro de trabajo.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)método. Consulte también la salida de la consola del código que se proporciona a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
