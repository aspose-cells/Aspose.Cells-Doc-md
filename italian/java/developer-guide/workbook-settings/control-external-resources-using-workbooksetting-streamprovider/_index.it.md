---
title: Controllare le risorse esterne utilizzando WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /it/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Possibili Scenari di Utilizzo**
A volte, il tuo file Excel contiene risorse esterne come ad esempio immagini collegate, ecc. Aspose.Cells ti consente di controllare queste risorse esterne utilizzando [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider) che accetta l'implementazione dell'interfaccia [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider). Ogni volta che tenterai di rendere il tuo foglio di lavoro contenente risorse esterne come ad esempio immagini collegate, verranno invocati i metodi dell'interfaccia [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) che ti consentiranno di intraprendere azioni appropriate per le tue risorse esterne.
## **Controllare le risorse esterne utilizzando WorkbookSetting.StreamProvider**
Il seguente codice di esempio spiega l'utilizzo di [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Carica il [file di Excel di esempio](61767877.xlsx) contenente un'immagine collegata. Il codice sostituisce l'immagine collegata con il [logo di Aspose](61767874.png) e rende l'intero foglio in un'unica immagine utilizzando la classe [SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender). La seguente schermata mostra il file di Excel di esempio e la sua [immagine di output renderizzata](61767874.png) a titolo di riferimento. Come puoi vedere, l'immagine collegata danneggiata è stata sostituita dal logo di Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
{{< app/cells/assistant language="java" >}}
