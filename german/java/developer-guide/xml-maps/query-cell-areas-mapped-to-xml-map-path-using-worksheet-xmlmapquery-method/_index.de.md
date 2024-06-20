---
title: Abfrage von Zellbereichen, die mit dem XML Map Pfad verbunden sind, mithilfe der Worksheet.XmlMapQuery Methode
type: docs
weight: 60
url: /de/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Mögliche Verwendungsszenarien**

Sie können mit Aspose.Cells Zellbereiche abfragen, die dem XML-Pfadbereich zugeordnet sind, und die Methode [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) verwenden. Wenn der Pfad vorhanden ist, gibt sie die Liste der mit diesem Pfad verbundenen Zellbereiche innerhalb der XML-Map zurück. Der erste Parameter der Methode [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) gibt den XML-Elementpfad an und der zweite Parameter gibt an, welche XML-Map Sie abfragen möchten.

## **Abfrage von Zellbereichen, die mit dem XML-Map-Pfad verbunden sind, mithilfe der Worksheet.XmlMapQuery-Methode**

Der folgende Screenshot zeigt Microsoft Excel, das die XML-Map innerhalb der [Beispiel-Excel-Datei](55541818.xlsx) anzeigt, die im Code verwendet wird. Der Code ruft die XML-Map zweimal ab und druckt die Liste der durch die Methode [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) zurückgegebenen Zellbereiche in der Konsole ab, wie unten gezeigt.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Konsolenausgabe**

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

XML-Daten können in Arbeitsblätter importiert werden. Manchmal ist der XML-Pfad aus den ListObjects des Arbeitsblatts erforderlich. Diese Funktion ist in Excel verfügbar, indem ein Ausdruck wie Sheet1.ListObjects(1).XmlMap.DataBinding verwendet wird. Die gleiche Funktion ist in Aspose.Cells verfügbar, indem [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url) aufgerufen wird. Das folgende Beispiel demonstriert diese Funktion. Die Vorlagendatei und andere Quelldateien können von den folgenden Links heruntergeladen werden:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
