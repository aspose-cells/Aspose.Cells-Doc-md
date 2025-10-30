---
title: Imposta le proprietà ScaleCrop e LinksUpToDate delle proprietà del documento built in
type: docs
weight: 320
url: /it/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Possibili Scenari di Utilizzo**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) e [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) sono due proprietà estese integrate definite nel formato OpenXml. Lo scopo di queste proprietà è il seguente
## **1) ScaleCrop**
Questo elemento indica la modalità di visualizzazione dell'anteprima del documento. Imposta questo elemento su **TRUE** per abilitare il ridimensionamento dell'anteprima del documento per la visualizzazione. Imposta questo elemento su **FALSE** per abilitare il ritaglio dell'anteprima del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.
## **2) LinksUpToDate**
Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su **TRUE** per indicare che i collegamenti ipertestuali sono aggiornati. Imposta questo elemento su **FALSE** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.
## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato**
Il seguente esempio di codice imposta le proprietà estese integrate [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) e [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) del workbook. Si prega di controllare il [file Excel di output](5115500.xlsx) generato con questo codice, cambiare la sua estensione in .zip ed estrarne i contenuti visualizzando app.xml come mostrato nello screenshot sopra.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}
