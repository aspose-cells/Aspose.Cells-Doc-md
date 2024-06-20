---
title: Interroga le aree delle celle mappate al percorso della mappa XML utilizzando il metodo Worksheet.XmlMapQuery
type: docs
weight: 60
url: /it/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Possibili Scenari di Utilizzo**

Puoi interrogare le aree delle celle mappate al percorso della mappa XML con Aspose.Cells utilizzando il metodo [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)). Se il percorso esiste, restituirà l'elenco delle aree delle celle relative a quel percorso all'interno della mappa XML. Il primo parametro del metodo [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) specifica il percorso dell'elemento XML e il secondo parametro specifica la mappa XML che si desidera interrogare.

## **Interroga le aree delle celle mappate al percorso della mappa XML utilizzando il metodo Worksheet.XmlMapQuery**

La seguente schermata mostra Microsoft Excel visualizzando la mappa XML all'interno del [file Excel di esempio](55541818.xlsx) utilizzato nel codice. Il codice interroga la mappa XML due volte e stampa l'elenco delle aree delle celle restituite dal metodo [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) sulla console come mostrato di seguito.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Output della console**

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

## **Ottieni il percorso XML dall'elenco degli oggetti/tabelle**

I dati XML possono essere importati nei fogli di lavoro. A volte è richiesto un percorso XML dalla ListObjects del foglio di lavoro. Questa funzionalità è disponibile in Excel utilizzando un'espressione come Sheet1.ListObjects(1).XmlMap.DataBinding. La stessa funzionalità è disponibile in Aspose.Cells chiamando [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url).  L'esempio seguente illustra questa funzionalità. Il file del modello e altri file di origine possono essere scaricati dai seguenti link:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
