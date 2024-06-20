---
title: Aggiungi Parti XML personalizzate e selezionale per ID
type: docs
weight: 10
url: /it/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Possibili Scenari di Utilizzo**

Le parti XML personalizzate sono i dati XML memorizzati all'interno dei documenti di Microsoft Excel e vengono utilizzati dalle applicazioni che li gestiscono. Al momento non esiste un modo diretto di aggiungerli utilizzando l'interfaccia utente di Microsoft Excel. Tuttavia, è possibile aggiungerli in modo programmato in vari modi, ad esempio utilizzando *VSTO*, utilizzando *Aspose.Cells* ecc. Utilizza il metodo [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) se desideri aggiungere una parte XML personalizzata tramite l'API Aspose.Cells. È inoltre possibile impostare il suo ID utilizzando la proprietà [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Allo stesso modo, se desideri selezionare una parte XML personalizzata per ID, puoi utilizzare il metodo [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)).

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il seguente codice di esempio aggiunge prima quattro parti XML personalizzate utilizzando il metodo [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)). Imposta quindi i loro ID utilizzando la proprietà [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Infine, trova o seleziona una delle parti XML personalizzate aggiunte utilizzando il metodo [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)). Si prega di vedere anche l'output della console del codice riportato di seguito per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Output della console**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
