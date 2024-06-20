---
title: Agregar partes XML personalizadas y seleccionarlas por ID
type: docs
weight: 10
url: /es/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Escenarios de uso posibles**

Las partes XML personalizadas son los datos XML que se almacenan dentro de los documentos de Microsoft Excel y son utilizados por las aplicaciones que tratan con ellos. No hay una manera directa de agregarlos usando la interfaz de usuario de Microsoft Excel en este momento. Sin embargo, puede agregarlos programáticamente de varias maneras, por ejemplo, usando *VSTO*, usando *Aspose.Cells*, etc. Utilice el método [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) si desea agregar una Parte XML personalizada utilizando la API de Aspose.Cells. También puede establecer su ID, utilizando la propiedad [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Del mismo modo, si desea seleccionar una Parte XML personalizada por ID, puede usar el método [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)).

## **Agregar partes XML personalizadas y seleccionarlas por ID**

El siguiente código de ejemplo primero agrega cuatro partes de XML personalizadas usando el método [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)). Luego establece sus identificadores usando la propiedad [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Finalmente, encuentra o selecciona una de las partes de XML personalizadas añadidas utilizando el método [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)). Consulte también la salida de la consola del código que se muestra a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
