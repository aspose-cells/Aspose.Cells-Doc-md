---
title: Impostare i formati condizionali dei file Excel e ODS.
linktitle: Formati condizionali
type: docs
weight: 60
url: /it/net/conditional-formatting/
description: Come applicare i formati condizionali ai file Excel e ODS in CSharp.
keywords: apply conditional formats 
---
## **introduzione**

 La formattazione condizionale è una funzionalità avanzata di Excel Microsoft che consente di applicare formati a una cella o a un intervallo di celle e di modificare la formattazione in base al valore della cella o al valore di una formula. Ad esempio, è possibile visualizzare una cella in grassetto solo quando il valore della cella è maggiore di 500. Quando il valore della cella soddisfa la condizione, alla cella viene applicato il formato specificato. Se il valore della cella non soddisfa la condizione del formato, viene utilizzata la formattazione predefinita della cella. In Microsoft Excel, selezionare**Formato** , poi**Formattazione condizionale** per aprire la finestra di dialogo Formattazione condizionale.

Aspose.Cells supporta l'applicazione della formattazione condizionale alle celle in fase di esecuzione. Questo articolo spiega come. Spiega inoltre come calcolare il colore utilizzato da Excel per la formattazione condizionale della scala di colori.

## **Applicazione della formattazione condizionale**

Aspose.Cells supporta la formattazione condizionale in diversi modi:

- Utilizzo del foglio di calcolo del designer
- Utilizzando il metodo della copia.
- Creazione di formattazione condizionale in fase di esecuzione.

### **Utilizzo del foglio di calcolo del progettista**

Gli sviluppatori possono creare un foglio di lavoro di progettazione che contiene la formattazione condizionale in Microsoft Excel e quindi aprire tale foglio di lavoro con Aspose.Cells. Aspose.Cells carica e salva il foglio di lavoro di progettazione, mantenendo qualsiasi impostazione di formattazione condizionale.

### **Utilizzando il metodo della copia**

 Aspose.Cells consente agli sviluppatori di copiare le impostazioni del formato condizionale da una cella all'altra nel foglio di lavoro chiamando il[**Intervallo.Copia()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Applicazione della formattazione condizionale in fase di esecuzione**

Aspose.Cells consente sia di aggiungere che di rimuovere la formattazione condizionale in fase di esecuzione. Gli esempi di codice seguenti mostrano come impostare la formattazione condizionale:

1. Crea un'istanza di una cartella di lavoro.
1. Aggiungi un formato condizionale vuoto.
1. Imposta l'intervallo a cui deve essere applicata la formattazione.
1. Definire le condizioni di formattazione.
1. Salva il file.

Dopo questo esempio arriva una serie di altri esempi più piccoli che mostrano come applicare le impostazioni dei caratteri, le impostazioni dei bordi e i motivi.

Microsoft Excel 2007 ha aggiunto una formattazione condizionale più avanzata supportata anche da Aspose.Cells. Gli esempi qui illustrano come utilizzare una formattazione semplice, gli esempi Microsoft Excel 2007 mostrano come applicare una formattazione condizionale più avanzata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Imposta carattere**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Puoi modificare solo lo stile del carattere, il colore del testo, lo stile della sottolineatura e lo stile del barrato.

{{% /alert %}}

### **Imposta bordo**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Puoi utilizzare solo stili di linea sottili per il bordo del contorno. Le linee diagonali non sono consentite.

{{% /alert %}}

### **Impostare il modello**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Argomenti avanzati**
- [Aggiunta di formattazioni condizionali scala a 2 colori e scala a 3 colori](/cells/it/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Applicare la formattazione condizionale avanzata](/cells/it/net/apply-advanced-conditional-formatting/)
- [Applicare la formattazione condizionale nei fogli di lavoro](/cells/it/net/apply-conditional-formatting-in-worksheets/)
- [Applicare l'ombreggiatura a righe e colonne alternative con la formattazione condizionale](/cells/it/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Genera immagini DataBars con formattazione condizionale](/cells/it/net/generate-conditional-formatting-databars-images/)
- [Ottieni set di icone, barre dati o scale di colori Oggetti utilizzati nella formattazione condizionale](/cells/it/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

