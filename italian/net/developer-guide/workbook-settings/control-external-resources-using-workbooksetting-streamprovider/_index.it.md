---
title: Controlla le risorse esterne utilizzando WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /it/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **Possibili scenari di utilizzo**

A volte, il tuo file Excel contiene risorse esterne, ad esempio immagini collegate, ecc. Aspose.Cells ti consente di controllare queste risorse esterne utilizzando[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)che prende l'attuazione del[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interfaccia. Ogni volta che proverai a rendere il tuo foglio di lavoro contenente risorse esterne, ad esempio immagini collegate, i metodi del file[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)verrà richiamata l'interfaccia che ti consentirà di intraprendere azioni appropriate per le tue risorse esterne.

## **Controlla le risorse esterne utilizzando WorkbookSetting.StreamProvider**

Il codice di esempio seguente illustra l'utilizzo di[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . Carica il[esempio di file Excel](61767863.xlsx) contenente un'immagine collegata. Il codice sostituisce l'immagine collegata con[Aspose Logo](61767862.png) e rende l'intero foglio in una singola immagine utilizzando[**FoglioRendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) classe. Lo screenshot seguente mostra il file Excel di esempio e il relativo file[immagine di output renderizzata](61767865.png) per un riferimento. Come puoi vedere, l'immagine collegata interrotta viene sostituita con il logo Aspose.

![cose da fare:immagine_alt_testo](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
