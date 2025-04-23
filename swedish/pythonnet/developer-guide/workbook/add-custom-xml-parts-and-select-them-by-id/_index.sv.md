---
title: Lägg till anpassade XML delar och välj dem efter ID
type: docs
weight: 70
url: /sv/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Möjliga användningsscenario**

Anpassade XML-delar är XML-data som lagras inuti Microsoft Excel-dokument och används av applikationer som hanterar dem. Det finns för närvarande ingen direkt metod för att lägga till dem via Microsoft Excels GUI. Du kan dock lägga till dem programatiskt på olika sätt, t.ex. med VSTO, Aspose.Cells etc. Använd [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)-metoden om du vill lägga till anpassade XML-delar med Aspose.Cells för Python via .NET API. Du kan också ange dess ID med hjälp av egenskapen [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Om du vill välja anpassad XML-del efter ID kan du använda [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)-metoden.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Följande exempelkod lägger först till fyra anpassade XML-delar med [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) metoden. Den ställer sedan in deras ID:er med [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id) egenskapen. Slutligen hittar eller väljer den ena av de tillagda anpassade XML-delarna med [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str) metoden. Se även konsoloutputen för koden nedan som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Konsoloutput**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

