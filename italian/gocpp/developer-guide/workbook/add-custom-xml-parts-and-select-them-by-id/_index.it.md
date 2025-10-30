---
title: Aggiungi parti XML personalizzate e selezionale per ID con Golang tramite C++
linktitle: Aggiungi Parti XML personalizzate e selezionale per ID
type: docs
weight: 70
url: /it/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Impara come aggiungere e selezionare parti XML personalizzate nei file Excel usando Aspose.Cells con Golang tramite C++.
---

## **Possibili Scenari di Utilizzo**

Le parti XML personalizzate sono dati XML memorizzati all’interno dei documenti Microsoft Excel e sono utilizzate dalle applicazioni che interagiscono con essi. Attualmente non esiste un modo diretto per aggiungerle tramite l’interfaccia utente di Microsoft Excel. Tuttavia, puoi aggiungerle programmaticamente in vari modi, ad esempio utilizzando VSTO o Aspose.Cells. Usa il metodo [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) per aggiungere una parte XML personalizzata tramite l’API Aspose.Cells. Puoi anche impostare il suo ID utilizzando la proprietà [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Allo stesso modo, se desideri selezionare una parte XML personalizzata per ID, puoi usare il metodo [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il seguente esempio di codice aggiunge prima quattro parti XML personalizzate utilizzando il metodo [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/). Successivamente, imposta i loro ID usando la proprietà [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Infine, trova o seleziona una delle parti XML personalizzate aggiunte usando il metodo [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Consulta anche l’output di console del codice di seguito come riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Output della console**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
