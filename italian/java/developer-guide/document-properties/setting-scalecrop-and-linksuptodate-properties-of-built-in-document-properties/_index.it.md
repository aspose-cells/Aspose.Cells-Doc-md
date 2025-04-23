---
title: Imposta le proprietà ScaleCrop e LinksUpToDate delle proprietà del documento built in
type: docs
weight: 1050
url: /it/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Possibili Scenari di Utilizzo**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) e [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) sono due proprietà di documento incorporate estese definite all'interno del formato OpenXml. Lo scopo di queste proprietà è il seguente
## **1) ScaleCrop**
Questo elemento indica la modalità di visualizzazione della miniatura del documento. Imposta questo elemento su **true** per abilitare il ridimensionamento della miniatura del documento per la visualizzazione. Imposta questo elemento su **false** per abilitare il ritaglio della miniatura del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.
## **2) LinksUpToDate**
Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su **true** per indicare che i collegamenti ipertestuali sono aggiornati. Imposta questo elemento su **false** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.
## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato**
Il seguente codice di esempio imposta le proprietà di documento incorporate estese [ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) e [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) del workbook. Si prega di controllare il [file Excel di output](5472494.xlsx) generato con questo codice, cambiare la sua estensione in .zip ed estrarre i contenuti e visualizzare il file aap.xml come mostrato nello screenshot sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
{{< app/cells/assistant language="java" >}}
