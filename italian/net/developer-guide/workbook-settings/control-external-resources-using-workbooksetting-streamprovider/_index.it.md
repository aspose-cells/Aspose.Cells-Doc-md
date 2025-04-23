---
title: Controllare le risorse esterne utilizzando WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /it/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Possibili Scenari di Utilizzo**

A volte il tuo file Excel contiene risorse esterne come immagini collegate, ecc. Aspose.Cells ti consente di controllare queste risorse esterne utilizzando [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) che prende l'implementazione dell'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider). Ogni qualvolta proverai a visualizzare il foglio di lavoro contenente risorse esterne come immagini collegate, verranno invocati i metodi dell'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) che ti consentiranno di prendere azioni appropriate per le tue risorse esterne.

## **Controllare le risorse esterne utilizzando WorkbookSetting.StreamProvider**

Il codice di esempio seguente spiega l'uso del [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). Carica il [file Excel di esempio](61767863.xlsx) contenente un'immagine collegata. Il codice sostituisce l'immagine collegata con il [Logo Aspose](61767862.png) e renderizza l'intero foglio in un'unica immagine utilizzando la classe [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender). Lo screenshot seguente mostra il file Excel di esempio e la sua [immagine di output renderizzata](61767865.png) per riferimento. Come puoi vedere, l'immagine collegata danneggiata è stata sostituita con il Logo Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
