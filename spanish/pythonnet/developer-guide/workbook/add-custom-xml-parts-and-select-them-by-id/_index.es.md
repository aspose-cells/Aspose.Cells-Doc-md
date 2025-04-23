---
title: Agregar partes XML personalizadas y seleccionarlas por ID
type: docs
weight: 70
url: /es/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Escenarios de uso posibles**

Las Partes XML personalizadas son los datos XML almacenados dentro de los documentos Microsoft Excel y son utilizados por las aplicaciones que las manejan. Actualmente no hay una forma directa de agregarlas usando la interfaz de usuario de Microsoft Excel. Sin embargo, puedes agregarlas programáticamente de varias formas, por ejemplo, usando VSTO, Aspose.Cells, etc. Por favor, usa el método [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) si deseas agregar una Parte XML personalizando usando la API Aspose.Cells para Python via .NET. También puedes establecer su ID usando la propiedad [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). De manera similar, si deseas seleccionar una Parte XML personalizada por ID, puedes usar el método [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str).

## **Agregar partes XML personalizadas y seleccionarlas por ID**

El siguiente código de muestra primero agrega cuatro partes de XML personalizadas utilizando el método [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes). Luego establece sus ID utilizando la propiedad [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Finalmente, encuentra o selecciona una de las partes de XML personalizadas agregadas usando el método [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str). Consulte también la salida por consola del código a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Salida de la consola**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

