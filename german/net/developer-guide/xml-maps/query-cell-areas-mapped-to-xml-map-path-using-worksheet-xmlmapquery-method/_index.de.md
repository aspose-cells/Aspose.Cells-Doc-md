---
title: Abfrage von Zellbereichen, die mit dem XML Map Pfad verbunden sind, mithilfe der Worksheet.XmlMapQuery Methode
type: docs
weight: 60
url: /de/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Mögliche Verwendungsszenarien**

Sie können mit Aspose.Cells mithilfe der Methode [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) Zellbereiche abfragen, die mit dem XML-Map-Pfad verknüpft sind. Wenn der Pfad vorhanden ist, gibt die Methode eine Liste der mit diesem Pfad verknüpften Zellbereiche in der XML-Map zurück. Der erste Parameter der Methode [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) gibt den XML-Elementpfad an und der zweite Parameter gibt an, welche XML-Map abgefragt werden soll.

## **Abfrage von Zellbereichen, die mit dem XML-Map-Pfad verbunden sind, mithilfe der Worksheet.XmlMapQuery-Methode**

Der folgende Screenshot zeigt Microsoft Excel, das die XML-Map in der [Beispiel-Excel-Datei](55541790.xlsx) anzeigt, die im Code verwendet wird. Der Code fragt die XML-Map zweimal ab und gibt die Liste der von der Methode [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) zurückgegebenen Zellbereiche in der Konsole aus, wie unten gezeigt.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **XML-Pfad aus Objektliste/Tabelle erhalten**

XML-Daten können in Arbeitsblätter importiert werden. Manchmal wird der XML-Pfad aus den ListObjects des Arbeitsblatts benötigt. Diese Funktion steht in Excel zur Verfügung, indem ein Ausdruck wie Sheet1.ListObjects(1).XmlMap.DataBinding verwendet wird. Die gleiche Funktion ist in Aspose.Cells verfügbar, indem [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url) aufgerufen wird. Das folgende Beispiel demonstriert diese Funktion. Die Vorlagendatei und andere Quelldateien können von den folgenden Links heruntergeladen werden:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
{{< app/cells/assistant language="csharp" >}}
