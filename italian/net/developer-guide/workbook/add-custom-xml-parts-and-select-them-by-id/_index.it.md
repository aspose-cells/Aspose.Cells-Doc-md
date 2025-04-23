---
title: Aggiungi Parti XML personalizzate e selezionale per ID
type: docs
weight: 70
url: /it/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Possibili Scenari di Utilizzo**

Le parti XML personalizzate sono i dati XML memorizzati all'interno dei documenti di Microsoft Excel e vengono utilizzati dalle applicazioni che trattano tali dati. Al momento non esiste un modo diretto di aggiungerle utilizzando l'interfaccia utente di Microsoft Excel. Tuttavia, è possibile aggiungerle programmatticamente in vari modi ad esempio utilizzando VSTO, utilizzando Aspose.Cells, ecc. Si prega di utilizzare il metodo [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) se si desidera aggiungere una parte XML personalizzata utilizzando l'API Aspose.Cells. È inoltre possibile impostare il suo ID utilizzando la proprietà [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Allo stesso modo, se si desidera selezionare una parte XML personalizzata tramite ID, è possibile utilizzare il metodo [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid).

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il seguente codice di esempio aggiunge prima quattro parti XML personalizzate utilizzando il metodo [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add). Imposta quindi i loro ID utilizzando la proprietà [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Infine, trova o seleziona una delle parti XML personalizzate aggiunte utilizzando il metodo [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid). Si prega di consultare anche l'output della console del codice fornito di seguito per avere un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Output della console**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
