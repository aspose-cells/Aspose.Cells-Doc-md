---
title: Conversone del Foglio di Lavoro in Immagine utilizzando le Opzioni Immagine o Stampa
type: docs
weight: 90
url: /it/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire una comprensione dettagliata su come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, come risoluzione, compressione TIFF, formato immagine e qualità della pagina.

{{% /alert %}}

## **Salvataggio Fogli di lavoro in Immagini - Diverse Approcci**

A volte potresti aver bisogno di presentare i tuoi fogli di lavoro come rappresentazione pittorica. Devi presentare le immagini del foglio di lavoro nelle tue applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint, o utilizzarle in qualche altro scenario. Semplicemente desideri un foglio di lavoro rappresentato come un'immagine in modo da poterlo utilizzare altrove. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel in immagini. Inoltre, Aspose.Cells supporta impostare diverse opzioni come formato immagine, risoluzione (sia verticale che orizzontale), qualità dell'immagine e altre opzioni di immagine e stampa.

Potresti provare l'Automazione di Office, ma l'automazione di Office ha i suoi svantaggi. Sono coinvolti diversi motivi e problemi: ad esempio, sicurezza, stabilità, scalabilità e velocità, prezzo e funzionalità. In breve, ci sono molti motivi, con il principale che Microsoft stessa sconsiglia vivamente l'automazione di Office dalle soluzioni software.

Questo articolo mostra come creare un'applicazione console in Visual Studio .NET, eseguire la conversione di un foglio di lavoro in un'immagine utilizzando diverse opzioni di immagine e stampa con poche e semplici righe di codice utilizzando l'API Aspose.Cells.

È necessario importare il namespace [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) nel tuo programma/progetto. Ha diverse classi preziose, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) etc.

La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) rappresenta un foglio di lavoro per rendere immagini per il foglio di lavoro, ha un metodo sovraccaricato [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) che può convertire direttamente un foglio di lavoro in file di immagine specificati con le tue opzioni desiderate. Può restituire un oggetto System.Drawing.Bitmap e puoi salvare un file di immagine sul disco/flusso. Sono supportati diversi formati di immagini, ad esempio BMP, PNG, GIFF, JPEG, TIFF, EMF e così via.

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in immagine utilizzando le opzioni ImageOrPrint.**

### **Creazione di un libro di lavoro modello in Microsoft Excel**

Ho creato un nuovo libro di lavoro in MS Excel e aggiunto alcuni dati nel primo foglio di lavoro. Ora, convertirò il foglio di lavoro del file modello "Foglio1" in un file immagine "FoglioImmagine.tiff" e applicherò diverse opzioni di immagine come risoluzioni orizzontali e verticali, compressione Tiff, ecc.

### **Scarica e installa Aspose.Cells**

Innanzitutto, è necessario [scaricare](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net. Installalo sul tuo computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), quando installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inietta solo filigrane nei documenti prodotti.

### **Crea un Progetto**

Avviare Visual Studio. Net e creare una nuova applicazione console. Questo esempio mostrerà un'applicazione console C#, ma è possibile utilizzare anche VB.NET.

### **Aggiungi Riferimenti**

Questo progetto utilizzerà Aspose.Cells. Quindi, devi aggiungere il riferimento al componente Aspose.Cells nel tuo progetto. Ad esempio, aggiungi un riferimento a ....\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

### **Convertire un foglio di lavoro in un file immagine**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Opzioni di conversione**

È possibile salvare pagine specifiche in immagine. Il codice seguente converte il primo e il secondo foglio di lavoro in un libro di lavoro in immagini JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Conversione dell'immagine utilizzando WorkbookRender**

Un'immagine TIFF può contenere più di una cornice. È possibile salvare l'intero libro di lavoro in un'unica immagine TIFF con più cornici o pagine:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
