---
title: Controlla le risorse esterne utilizzando WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /it/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **Possibili scenari di utilizzo**
A volte, il tuo file Excel contiene risorse esterne, ad esempio immagini collegate, ecc. Aspose.Cells ti consente di controllare queste risorse esterne utilizzando[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)che prende l'attuazione di[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interfaccia. Ogni volta che proverai a rendere il tuo foglio di lavoro contenente risorse esterne, ad esempio immagini collegate, i metodi di[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)verrà richiamata l'interfaccia che ti consentirà di intraprendere azioni appropriate per le tue risorse esterne.
## **Controlla le risorse esterne utilizzando WorkbookSetting.StreamProvider**
Il seguente codice di esempio spiega l'utilizzo di[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Carica il[esempio di file Excel](61767877.xlsx)contenente un'immagine collegata. Il codice sostituisce l'immagine collegata con[Aspose Logo](61767874.png)e rende l'intero foglio in una singola immagine utilizzando[FoglioRendering](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)classe. Lo screenshot seguente mostra il file Excel di esempio e il relativo file[immagine di output renderizzata](61767874.png)per un riferimento. Come puoi vedere, l'immagine collegata interrotta viene sostituita con il logo Aspose.

![cose da fare:immagine_alt_testo](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
