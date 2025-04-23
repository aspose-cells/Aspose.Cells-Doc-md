---  
title: Imposta i Formati Condizionali dei file Excel e ODS
linktitle: Formati Condizionali  
type: docs  
weight: 60  
url: /it/nodejs-cpp/conditional-formatting/  
description: Come applicare formati condizionali ai file Excel e ODS in Node.js tramite C++.  
keywords: applica formati condizionali in Node.js tramite C++  
---  

## **Introduzione**

La formattazione condizionale è una funzione avanzata che permette di applicare formati a una cella o un intervallo di celle e fare in modo che tale formattazione cambi in base al valore della cella o al valore di una formula. Ad esempio, puoi far apparire una cella in grassetto solo quando il valore della cella è superiore a 500. Quando il valore della cella soddisfa la condizione, il formato specificato viene applicato alla cella. Se il valore della cella non soddisfa la condizione, viene utilizzata la formattazione predefinita della cella. In Microsoft Excel, seleziona **Formato**, poi **Formattazione Condizionale** per aprire la finestra di dialogo della formattazione condizionale.

Aspose.Cells supporta l'applicazione della formattazione condizionale alle celle in fase di esecuzione. Questo articolo spiega come farlo. Spiega anche come calcolare il colore utilizzato da Excel per la formattazione condizionale basata sulla scala cromatica.

## **Applicare la formattazione condizionale**

Aspose.Cells supporta la formattazione condizionale in diversi modi:

- Utilizzando il foglio di calcolo del designer
- Utilizzando il metodo di copia.
- Creare la formattazione condizionale in fase di esecuzione.

### **Utilizzo del foglio di calcolo del designer**

I programmatori possono creare un foglio di calcolo del designer che contiene la formattazione condizionale in Microsoft Excel e quindi aprire quel foglio di calcolo con Aspose.Cells. Aspose.Cells carica e salva il foglio di calcolo del designer, mantenendo qualsiasi impostazione della formattazione condizionale.

### **Utilizzando il metodo di copia**

Aspose.Cells consente ai programmatori di copiare le impostazioni della formattazione condizionale da una cella a un'altra nel foglio di lavoro chiamando il metodo [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **Applicare la formattazione condizionale in fase di esecuzione**

Aspose.Cells consente di aggiungere e rimuovere la formattazione condizionale in fase di esecuzione. Di seguito sono riportati degli esempi di codice su come impostare la formattazione condizionale:

1. Istanziare un foglio di lavoro.
1. Aggiungere un formato condizionale vuoto.
1. Impostare l'intervallo a cui dovrebbe essere applicata la formattazione.
1. Definire le condizioni di formattazione.
1. Salvare il file.

Dopo questo esempio ci sono diversi altri esempi più piccoli che mostrano come applicare impostazioni del carattere, impostazioni dei bordi e schemi.

Microsoft Excel 2007 ha aggiunto una formattazione condizionale più avanzata, che anche Aspose.Cells supporta. Gli esempi qui mostrano come usare formattazioni semplici, mentre gli esempi di Microsoft Excel 2007 mostrano come applicare formattazioni condizionali più avanzate.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **Imposta Carattere**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

Puoi solo cambiare lo stile del carattere, il colore del testo, lo stile sottolineato e lo stile barrato.

{{% /alert %}}

### **Imposta Bordo**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

Puoi usare solo stili di linea sottili per il bordo esterno. Le linee diagonali non sono consentite.

{{% /alert %}}

### **Imposta Schema**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **Argomenti avanzati**  
- [Aggiunta di Formattazioni Condizionali a Scala a 2 Colori e Scala a 3 Colori](/cells/it/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Applica la formattazione condizionale nei fogli di lavoro](/cells/it/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Applica sfumature a righe e colonne alternative con la formattazione condizionale](/cells/it/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Genera Immagini Barre Dati delle Formattazioni Condizionali](/cells/it/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Ottieni Insiemi di Icone, Barre Dati o Oggetti Scala a Colori usati nella Formattazione Condizionale](/cells/it/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


