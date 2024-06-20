---
title: Interroga le aree delle celle mappate al percorso della mappa XML utilizzando il metodo Worksheet.XmlMapQuery
type: docs
weight: 60
url: /it/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Possibili Scenari di Utilizzo**

È possibile interrogare le aree delle celle mappate al percorso della mappa XML con Aspose.Cells utilizzando il metodo [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery). Se il percorso esiste, restituirà l'elenco delle aree delle celle correlate a quel percorso all'interno della mappa XML. Il primo parametro del metodo [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) specifica il percorso dell'elemento XML mentre il secondo parametro specifica una mappa XML che si desidera interrogare.

## **Interroga le aree delle celle mappate al percorso della mappa XML utilizzando il metodo Worksheet.XmlMapQuery**

Nella seguente schermata viene mostrato Microsoft Excel visualizzante la mappa XML all'interno del file Excel di esempio utilizzato nel codice. Il codice interroga la mappa XML due volte e stampa l'elenco delle aree delle celle restituite dal metodo [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) sulla console come mostrato di seguito.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Output della console**

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

I dati XML possono essere importati nei fogli di lavoro. A volte è necessario il percorso XML dalle ListObjects del foglio di lavoro. Questa funzione è disponibile in Excel utilizzando un'espressione come Sheet1.ListObjects(1).XmlMap.DataBinding. La stessa funzione è disponibile in Aspose.Cells chiamando [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). L'esempio seguente illustra questa funzione. Il file modello e altri file di origine possono essere scaricati dai seguenti collegamenti:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
