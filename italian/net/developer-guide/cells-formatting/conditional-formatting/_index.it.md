---
title: Imposta Formati Condizionali di file Excel e ODS.
linktitle: Formati Condizionali
type: docs
weight: 60
url: /it/net/conditional-formatting/
description: Come applicare formati condizionali ai file Excel e ODS in CSharp.
keywords: applicare formati condizionali 
---

## **Introduzione**

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a una cella o a un intervallo di celle e far sì che tale formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, è possibile rendere una cella in grassetto solo quando il suo valore supera i 500. Quando il valore della cella soddisfa la condizione, il formato specificato viene applicato alla cella. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella. In Microsoft Excel, seleziona **Formato**, quindi **Formattazione condizionale** per aprire il dialogo della Formattazione condizionale.

Aspose.Cells supporta l'applicazione della formattazione condizionale alle celle in fase di esecuzione. Questo articolo spiega come farlo. Spiega anche come calcolare il colore utilizzato da Excel per la formattazione condizionale basata sulla scala cromatica.

## **Applicare la formattazione condizionale**

Aspose.Cells supporta la formattazione condizionale in diversi modi:

- Utilizzando il foglio di calcolo del designer
- Utilizzando il metodo di copia.
- Creare la formattazione condizionale in fase di esecuzione.

### **Utilizzo del foglio di calcolo del designer**

I programmatori possono creare un foglio di calcolo del designer che contiene la formattazione condizionale in Microsoft Excel e quindi aprire quel foglio di calcolo con Aspose.Cells. Aspose.Cells carica e salva il foglio di calcolo del designer, mantenendo qualsiasi impostazione della formattazione condizionale.

### **Utilizzando il metodo di copia**

Aspose.Cells consente ai programmatori di copiare le impostazioni della formattazione condizionale da una cella a un'altra nel foglio di lavoro chiamando il metodo [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Applicare la formattazione condizionale in fase di esecuzione**

Aspose.Cells consente di aggiungere e rimuovere la formattazione condizionale in fase di esecuzione. Di seguito sono riportati degli esempi di codice su come impostare la formattazione condizionale:

1. Istanziare un foglio di lavoro.
1. Aggiungere un formato condizionale vuoto.
1. Impostare l'intervallo a cui dovrebbe essere applicata la formattazione.
1. Definire le condizioni di formattazione.
1. Salvare il file.

Dopo questo esempio ci sono diversi altri esempi più piccoli che mostrano come applicare impostazioni del carattere, impostazioni dei bordi e schemi.

Microsoft Excel 2007 ha aggiunto formattazioni condizionali più avanzate che Aspose.Cells supporta anche. Gli esempi qui illustrano come utilizzare formattazioni semplici, gli esempi di Microsoft Excel 2007 mostrano come applicare formattazioni condizionali più avanzate.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Imposta Carattere**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Puoi solo cambiare lo stile del carattere, il colore del testo, lo stile sottolineato e lo stile barrato.

{{% /alert %}}

### **Imposta Bordo**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Puoi solo usare stili di linea sottili per il bordo di contorno. Le linee diagonali non sono consentite.

{{% /alert %}}

### **Imposta Schema**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Argomenti avanzati**
- [Aggiunta di Formattazioni Condizionali a Scala a 2 Colori e Scala a 3 Colori](/cells/it/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Applicare la formattazione condizionale avanzata](/cells/it/net/apply-advanced-conditional-formatting/)
- [Applica la formattazione condizionale nei fogli di lavoro](/cells/it/net/apply-conditional-formatting-in-worksheets/)
- [Applica sfumature a righe e colonne alternative con la formattazione condizionale](/cells/it/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Genera Immagini Barre Dati delle Formattazioni Condizionali](/cells/it/net/generate-conditional-formatting-databars-images/)
- [Ottieni Insiemi di Icone, Barre Dati o Oggetti Scala a Colori usati nella Formattazione Condizionale](/cells/it/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
