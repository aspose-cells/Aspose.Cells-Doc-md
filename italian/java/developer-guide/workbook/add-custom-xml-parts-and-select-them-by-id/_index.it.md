---
title: Aggiungi parti XML personalizzate e selezionale per ID
type: docs
weight: 10
url: /it/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Possibili scenari di utilizzo**

Le parti XML personalizzate sono i dati XML che vengono memorizzati all'interno dei documenti Microsoft Excel e vengono utilizzati dalle applicazioni che li gestiscono. Al momento non esiste un modo diretto per aggiungerli utilizzando l'interfaccia utente di Microsoft Excel. Tuttavia, puoi aggiungerli a livello di codice in vari modi, ad esempio utilizzando*VSTO*, utilizzando*Aspose.Cells*ecc. Si prega di utilizzare[**Cartella di lavoro.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) se si desidera aggiungere una parte XML personalizzata utilizzando l'API Aspose.Cells. Puoi anche impostare il suo ID, usando il file[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)proprietà. Allo stesso modo, se si desidera selezionare Custom XML Part by ID, è possibile utilizzare[**Cartella di lavoro.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) metodo.

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il codice di esempio seguente aggiunge innanzitutto quattro parti XML personalizzate utilizzando[**Cartella di lavoro.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) metodo. Quindi imposta i loro ID utilizzando[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)proprietà. Infine, trova o seleziona una delle parti XML personalizzate aggiunte utilizzando[**Cartella di lavoro.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) metodo. Si prega di consultare anche l'output della console del codice fornito di seguito per un riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Uscita console**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
