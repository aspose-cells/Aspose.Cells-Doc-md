---
title: Agregue partes XML personalizadas y selecciónelas por ID
type: docs
weight: 10
url: /es/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Posibles escenarios de uso**

Las partes XML personalizadas son los datos XML que se almacenan dentro de los documentos de Excel Microsoft y son utilizados por las aplicaciones que se ocupan de ellos. No hay una forma directa de agregarlos usando la interfaz de usuario de Excel Microsoft en este momento. Sin embargo, puede agregarlos programáticamente de varias maneras, por ejemplo, usando*VSTO*, usando*Aspose.Cells*etc Por favor use[**Libro de trabajo.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) si desea agregar una parte XML personalizada usando Aspose.Cells API. También puede establecer su ID, usando el[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)propiedad. Del mismo modo, si desea seleccionar Elemento XML personalizado por ID, puede utilizar[**Libro de trabajo.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) método.

## **Agregue partes XML personalizadas y selecciónelas por ID**

El siguiente código de muestra primero agrega cuatro partes XML personalizadas usando[**Libro de trabajo.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) método. Luego establece sus ID usando[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)propiedad. Finalmente, encuentra o selecciona una de las partes XML personalizadas agregadas usando[**Libro de trabajo.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) método. Consulte también la salida de la consola del código que se proporciona a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
