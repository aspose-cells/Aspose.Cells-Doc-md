---
title: Imposta le proprietà ScaleCrop e LinksUpToDate delle proprietà del documento built in
type: docs
weight: 320
url: /it/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Possibili Scenari di Utilizzo**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) e [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) sono due proprietà del documento integrate estese definite nel formato OpenXml. Lo scopo di queste proprietà è il seguente
## **1) ScaleCrop**
Questo elemento indica la modalità di visualizzazione dell'anteprima del documento. Imposta questo elemento su **TRUE** per abilitare il ridimensionamento dell'anteprima del documento per la visualizzazione. Imposta questo elemento su **FALSE** per abilitare il ritaglio dell'anteprima del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.
## **2) LinksUpToDate**
Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su **TRUE** per indicare che i collegamenti ipertestuali sono aggiornati. Imposta questo elemento su **FALSE** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.
## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato**
Il codice di esempio seguente imposta le proprietà [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) e [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) delle proprietà del documento integrato del workbook. Si prega di controllare il [file Excel di output](5115500.xlsx) generato con questo codice, cambiare la sua estensione in .zip ed estrarre i suoi contenuti e visualizzare il file app.xml come mostrato nello screenshot sopra.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
{{< app/cells/assistant language="csharp" >}}
