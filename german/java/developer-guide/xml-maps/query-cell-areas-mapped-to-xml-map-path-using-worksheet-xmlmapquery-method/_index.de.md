---
title: Abfrage Cell Dem XML-Zuordnungspfad zugeordnete Bereiche mithilfe der Worksheet.XmlMapQuery-Methode
type: docs
weight: 60
url: /de/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Mögliche Nutzungsszenarien**

Sie können Zellbereiche abfragen, die dem XML-Zuordnungspfad mit Aspose.Cells zugeordnet sind, indem Sie die verwenden[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) Methode. Wenn der Pfad vorhanden ist, wird die Liste der Zellbereiche zurückgegeben, die sich auf diesen Pfad innerhalb der XML-Zuordnung beziehen. Der erste Parameter von[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))-Methode gibt den XML-Elementpfad an, und der zweite Parameter gibt eine XML-Zuordnung an, die Sie abfragen möchten.

## **Abfrage Cell Dem XML-Zuordnungspfad zugeordnete Bereiche mithilfe der Worksheet.XmlMapQuery-Methode**

Der folgende Screenshot zeigt die Excel-Datei Microsoft, die eine XML-Karte im Inneren anzeigt[Beispiel-Excel-Datei](55541818.xlsx)im Code verwendet. Der Code fragt die XML-Zuordnung zweimal ab und druckt die Liste der von zurückgegebenen Zellbereiche[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))-Methode auf der Konsole wie unten gezeigt.

![todo: Bild_alt_Text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Holen Sie sich den XML-Pfad aus List Object/Table**

XML-Daten können in Arbeitsblätter importiert werden. Manchmal ist ein XML-Pfad aus den ListObjects des Arbeitsblatts erforderlich. Dieses Feature ist in Excel verfügbar, indem ein Ausdruck wie Sheet1.ListObjects(1).XmlMap.DataBinding verwendet wird. Die gleiche Funktion ist telefonisch unter Aspose.Cells verfügbar[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). Das folgende Beispiel demonstriert diese Funktion. Vorlagendatei und andere Quelldateien können unter den folgenden Links heruntergeladen werden:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
