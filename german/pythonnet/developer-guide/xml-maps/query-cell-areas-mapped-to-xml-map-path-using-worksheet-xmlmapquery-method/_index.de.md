---
title: Abfrage von Zellbereichen, die mit dem XML Map Pfad verbunden sind, mithilfe der Worksheet.XmlMapQuery Methode
type: docs
weight: 60
url: /de/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Mögliche Verwendungsszenarien**

Sie können Zellbereiche, die dem XML-Map-Pfad zugeordnet sind, mit Aspose.Cells für Python via .NET anhand der Methode [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) abfragen. Falls der Pfad existiert, gibt sie die Liste der Zellbereiche zurück, die mit diesem Pfad innerhalb des XML-Maps verbunden sind. Der erste Parameter der Methode [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) gibt den XML-Element-Pfad an, und der zweite Parameter gibt den XML-Map an, den Sie abfragen möchten.

## **Abfrage von Zellbereichen, die mit dem XML-Map-Pfad verbunden sind, mithilfe der Worksheet.XmlMapQuery-Methode**

Der folgende Screenshot zeigt Microsoft Excel, das die XML-Map in der [Beispiel-Excel-Datei](55541790.xlsx) anzeigt, die im Code verwendet wird. Der Code fragt die XML-Map zweimal ab und gibt die Liste der von der Methode [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) zurückgegebenen Zellbereiche in der Konsole aus, wie unten gezeigt.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

XML-Daten können in Arbeitsblätter importiert werden. Manchmal ist der XML-Pfad von den ListObjects im Arbeitsblatt erforderlich. Diese Funktion ist in Excel durch einen Ausdruck wie Sheet1.ListObjects(1).XmlMap.DataBinding verfügbar. Diese Funktion ist in Aspose.Cells für Python via .NET durch Aufruf von [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url) verfügbar. Das folgende Beispiel demonstriert diese Funktion. Vorlage-Dateien und andere Quelldateien können von den folgenden Links heruntergeladen werden:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

