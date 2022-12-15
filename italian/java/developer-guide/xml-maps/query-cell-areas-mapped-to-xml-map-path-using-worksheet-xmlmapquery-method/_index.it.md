---
title: Query Cell Aree mappate su XML Map Path utilizzando il metodo Worksheet.XmlMapQuery
type: docs
weight: 60
url: /it/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Possibili scenari di utilizzo**

È possibile interrogare le aree delle celle mappate al percorso della mappa XML con Aspose.Cells utilizzando il file[**Foglio di lavoro.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) metodo. Se il percorso esiste, restituirà l'elenco delle aree di celle relative a quel percorso all'interno della mappa XML. Il primo parametro di[**Foglio di lavoro.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) specifica il percorso dell'elemento XML e il secondo parametro specifica una mappa XML che si desidera interrogare.

## **Query Cell Aree mappate su XML Map Path utilizzando il metodo Worksheet.XmlMapQuery**

Lo screenshot seguente mostra Microsoft Excel che visualizza la mappa XML all'interno del file[esempio di file Excel](55541818.xlsx)utilizzato nel codice. Il codice interroga due volte la mappa XML e stampa l'elenco delle aree delle celle restituite da[**Foglio di lavoro.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) sulla console come mostrato di seguito.

![cose da fare:immagine_alt_testo](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Uscita console**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Ottieni il percorso XML da List Object/Table**

I dati XML possono essere importati nei fogli di lavoro. A volte è richiesto il percorso XML da ListObjects del foglio di lavoro. Questa funzionalità è disponibile in Excel utilizzando un'espressione come Sheet1.ListObjects(1).XmlMap.DataBinding. La stessa funzione è disponibile allo Aspose.Cells chiamando[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). L'esempio seguente mostra questa funzione. Il file modello e altri file di origine possono essere scaricati dai seguenti collegamenti:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
