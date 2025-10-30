---
title: Agregar partes XML personalizadas y seleccionarlas por ID con Golang mediante C++
linktitle: Agregar partes XML personalizadas y seleccionarlas por ID
type: docs
weight: 70
url: /es/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Aprenda cómo agregar y seleccionar partes XML personalizadas en archivos de Excel usando Aspose.Cells con Golang mediante C++
---

## **Escenarios de uso posibles**

Las partes XML personalizadas son datos XML almacenados dentro de documentos de Microsoft Excel y son utilizadas por aplicaciones que interactúan con ellos. Actualmente, no hay una forma directa de agregarlas usando la interfaz de usuario de Microsoft Excel. Sin embargo, puede agregarlas programáticamente de varias maneras, como usando VSTO o Aspose.Cells. Use el método [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) para agregar una Parte XML Personalizada usando la API de Aspose.Cells. También puede establecer su ID usando la propiedad [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). De manera similar, si desea seleccionar una Parte XML Personalizada por ID, puede usar el método [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Agregar partes XML personalizadas y seleccionarlas por ID**

El siguiente código de ejemplo primero agrega cuatro Partes XML Personalizadas usando el método [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/). Luego establece sus IDs usando la propiedad [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Finalmente, encuentra o selecciona una de las Partes XML Personalizadas agregadas usando el método [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Por favor, consulte también la salida de la consola del código dado a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Salida de la consola**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
