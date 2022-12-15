---
title: Aggiungi parti XML personalizzate e selezionale per ID
type: docs
weight: 70
url: /it/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Possibili scenari di utilizzo**

Le parti XML personalizzate sono i dati XML che vengono memorizzati all'interno dei documenti Microsoft Excel e vengono utilizzati dalle applicazioni che li gestiscono. Al momento non esiste un modo diretto per aggiungerli utilizzando l'interfaccia utente di Microsoft Excel. Tuttavia, puoi aggiungerli a livello di codice in vari modi, ad esempio utilizzando VSTO, utilizzando Aspose.Cells ecc. Utilizzare[**Cartella di lavoro.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) metodo se si desidera aggiungere una parte XML personalizzata utilizzando l'API Aspose.Cells. Puoi anche impostare il suo ID, usando il file[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)proprietà. Allo stesso modo, se si desidera selezionare Custom XML Part by ID, è possibile utilizzare[**Cartella di lavoro.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)metodo.

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il codice di esempio seguente aggiunge innanzitutto quattro parti XML personalizzate utilizzando[**Cartella di lavoro.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)metodo. Quindi imposta i loro ID utilizzando[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) proprietà. Infine, trova o seleziona una delle parti XML personalizzate aggiunte utilizzando[**Cartella di lavoro.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)metodo. Si prega di consultare anche l'output della console del codice fornito di seguito per riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
