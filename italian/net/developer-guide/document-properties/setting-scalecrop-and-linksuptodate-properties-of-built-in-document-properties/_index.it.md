---
title: Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento incorporate
type: docs
weight: 320
url: /it/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Possibili scenari di utilizzo**
[ScalaRitaglia](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) e[LinkUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)sono due proprietà integrate del documento estese definite all'interno del formato OpenXml. Lo scopo di queste proprietà sta seguendo
## **1) Ritaglia scala**
 Questo elemento indica la modalità di visualizzazione della miniatura del documento. Imposta questo elemento su**VERO**per abilitare il ridimensionamento della miniatura del documento sul display. Imposta questo elemento su**FALSO** per abilitare il ritaglio della miniatura del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dati booleano W3C XML Schema.
## **2) LinkUpToDate**
 Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su**VERO** per indicare che i collegamenti ipertestuali vengono aggiornati. Imposta questo elemento su**FALSO** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dati booleano W3C XML Schema.
## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![cose da fare:immagine_alt_testo](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento incorporate**
 Il codice di esempio seguente imposta il[ScalaRitaglia](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) e[LinkUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) proprietà del documento integrate estese della cartella di lavoro. Si prega di controllare[file excel di output](5115500.xlsx)generato con questo codice, cambia la sua estensione in .zip ed estrai il suo contenuto e visualizza l'app.xml come mostrato nello screenshot qui sopra.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
