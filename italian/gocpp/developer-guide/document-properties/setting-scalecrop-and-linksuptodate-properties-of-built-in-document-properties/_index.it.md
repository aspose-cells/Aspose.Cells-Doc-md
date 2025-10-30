---
title: Impostare le Proprietà Built In ScaleCrop e LinksUpToDate delle Proprietà Documento con Golang via C++
linktitle: Impostazione delle proprietà ScaleCrop e LinksUpToDate
type: docs
weight: 320
url: /it/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Impara come impostare le proprietà ScaleCrop e LinksUpToDate delle proprietà di documento integrate usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) e [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) sono due proprietà estese delle proprietà documento integrato definite all’interno del formato OpenXml. Lo scopo di queste proprietà è il seguente:

## **1) ScaleCrop**
Questo elemento indica la modalità di visualizzazione dell'anteprima del documento. Imposta questo elemento su **TRUE** per abilitare il ridimensionamento dell'anteprima del documento per la visualizzazione. Imposta questo elemento su **FALSE** per abilitare il ritaglio dell'anteprima del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.

## **2) LinksUpToDate**
Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su **TRUE** per indicare che i collegamenti ipertestuali sono aggiornati. Imposta questo elemento su **FALSE** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.

## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà di documento integrate**
Il seguente esempio di codice imposta le proprietà del documento estese [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) e [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) del workbook. Si prega di verificare il file Excel di output ([5115500.xlsx](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop)), generato con questo codice, cambiare estensione in .zip e estrarre i contenuti per visualizzare app.xml come mostrato nello screenshot sopra.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
