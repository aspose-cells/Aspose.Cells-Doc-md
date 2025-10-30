---
title: Interroga le aree delle celle mappate al percorso della mappa XML utilizzando il metodo Worksheet.XmlMapQuery
type: docs
weight: 60
url: /it/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Possibili Scenari di Utilizzo**

Puoi interrogare le aree di celle mappate al percorso della mappa XML con Aspose.Cells for Python via .NET usando il metodo [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query). Se il percorso esiste, restituirà la lista delle aree di celle correlate a quel percorso all’interno della mappa XML. Il primo parametro del metodo [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) specifica il percorso dell’elemento XML e il secondo parametro specifica una mappa XML da interrogare.

## **Interroga le aree delle celle mappate al percorso della mappa XML utilizzando il metodo Worksheet.XmlMapQuery**

Nella seguente schermata viene mostrato Microsoft Excel visualizzante la mappa XML all'interno del file Excel di esempio utilizzato nel codice. Il codice interroga la mappa XML due volte e stampa l'elenco delle aree delle celle restituite dal metodo [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) sulla console come mostrato di seguito.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

I dati XML possono essere importati nei fogli di lavoro. A volte è necessario il percorso XML dai ListObjects del foglio di lavoro. Questa funzionalità è disponibile in Excel usando un’espressione come Sheet1.ListObjects(1).XmlMap.DataBinding. La stessa funzionalità è disponibile in Aspose.Cells for Python via .NET chiamando [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url). Il seguente esempio dimostra questa funzionalità. I file modello e gli altri file sorgente possono essere scaricati dai link seguenti:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

{{< app/cells/assistant language="python-net" >}}
