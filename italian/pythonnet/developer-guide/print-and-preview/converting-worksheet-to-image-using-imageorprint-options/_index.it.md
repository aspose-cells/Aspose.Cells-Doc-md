---
title: Conversone del Foglio di Lavoro in Immagine utilizzando le Opzioni Immagine o Stampa
type: docs
weight: 90
url: /it/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire una comprensione dettagliata su come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, come risoluzione, compressione TIFF, formato immagine e qualità della pagina.

{{% /alert %}}

## **Salvataggio Fogli di lavoro in Immagini - Diverse Approcci**

A volte, potresti aver bisogno di presentare i tuoi fogli di lavoro come rappresentazioni pittoriche. È necessario inserire le immagini dei fogli di lavoro nelle tue applicazioni o pagine web. Potresti dover inserire le immagini in un documento Word, in un file PDF, in una presentazione PowerPoint o usarle in altri scenari. In modo semplice, vuoi un foglio di lavoro reso come immagine, così da poterlo usare altrove. Aspose.Cells per Python via .NET supporta la conversione di fogli di calcolo Excel in immagini. Inoltre, supporta la configurazione di opzioni come formato immagine, risoluzione (orizzontale e verticale), qualità dell'immagine e altre opzioni di immagine e stampa.

Potresti provare l'Automazione di Office, ma l'automazione di Office ha i suoi svantaggi. Sono coinvolti diversi motivi e problemi: ad esempio, sicurezza, stabilità, scalabilità e velocità, prezzo e funzionalità. In breve, ci sono molti motivi, con il principale che Microsoft stessa sconsiglia vivamente l'automazione di Office dalle soluzioni software.

Questo articolo mostra come creare un'applicazione console in Visual Studio .NET, eseguire la conversione di un foglio di lavoro in immagine usando diverse opzioni di immagine e stampa con poche e semplici righe di codice usando l'API Aspose.Cells per Python via .NET.

È necessario importare il namespace [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) nel tuo programma/progetto. Ha diverse classi preziose, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) etc.

La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) rappresenta un foglio di lavoro per rendere immagini per il foglio di lavoro, ha un metodo sovraccaricato [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) che può convertire direttamente un foglio di lavoro in file di immagine specificati con le tue opzioni desiderate. Può restituire un oggetto System.Drawing.Bitmap e puoi salvare un file di immagine sul disco/flusso. Sono supportati diversi formati di immagini, ad esempio BMP, PNG, GIFF, JPEG, TIFF, EMF e così via.

## **Utilizzo di Aspose.Cells per convertire un foglio di lavoro in immagine usando le opzioni ImageOrPrint.**

### **Creazione di un libro di lavoro modello in Microsoft Excel**

Ho creato un nuovo libro di lavoro in MS Excel e aggiunto alcuni dati nel primo foglio di lavoro. Ora, convertirò il foglio di lavoro del file modello "Foglio1" in un file immagine "FoglioImmagine.tiff" e applicherò diverse opzioni di immagine come risoluzioni orizzontali e verticali, compressione Tiff, ecc.

### **Convertire un foglio di lavoro in un file immagine**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **Conversione dell'immagine utilizzando WorkbookRender**

Un'immagine TIFF può contenere più di una cornice. È possibile salvare l'intero libro di lavoro in un'unica immagine TIFF con più cornici o pagine:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
