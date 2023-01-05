---
title: Abfrage Cell Dem XML-Zuordnungspfad zugeordnete Bereiche mithilfe der Worksheet.XmlMapQuery-Methode
type: docs
weight: 60
url: /de/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Mögliche Nutzungsszenarien**

Mit Aspose.Cells können Sie Zellbereiche abfragen, die dem XML-Zuordnungspfad zugeordnet sind[**Arbeitsblatt.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)Methode. Wenn der Pfad vorhanden ist, wird die Liste der Zellbereiche zurückgegeben, die sich auf diesen Pfad innerhalb der XML-Zuordnung beziehen. Der erste Parameter der[**Arbeitsblatt.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)-Methode gibt den XML-Elementpfad an, und der zweite Parameter gibt eine XML-Zuordnung an, die Sie abfragen möchten.

## **Abfrage Cell Dem XML-Zuordnungspfad zugeordnete Bereiche mithilfe der Worksheet.XmlMapQuery-Methode**

 Der folgende Screenshot zeigt die Excel-Datei Microsoft, die eine XML-Karte im Inneren anzeigt[Beispiel-Excel-Datei](55541790.xlsx) im Code verwendet. Der Code fragt die XML-Zuordnung zweimal ab und druckt die Liste der von zurückgegebenen Zellbereiche[**Arbeitsblatt.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)Methode auf der Konsole wie unten gezeigt.

![todo: Bild_alt_Text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Konsolenausgabe**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Holen Sie sich den XML-Pfad aus List Object/Table**

XML-Daten können in Arbeitsblätter importiert werden. Manchmal ist ein XML-Pfad aus den ListObjects des Arbeitsblatts erforderlich. Dieses Feature ist in Excel verfügbar, indem ein Ausdruck wie Sheet1.ListObjects(1).XmlMap.DataBinding verwendet wird. Die gleiche Funktion ist telefonisch unter Aspose.Cells verfügbar[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). Das folgende Beispiel demonstriert diese Funktion. Vorlagendatei und andere Quelldateien können unter den folgenden Links heruntergeladen werden:

1. [XML-Daten.xlsx](72417285.xlsx)
1. [Länderliste.xml](72417287.xml)
1. [Lebensmittelliste.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
