---
title: Imposta Formati Condizionali di file Excel e ODS.
linktitle: Formati Condizionali
type: docs
weight: 60
url: /it/python-net/conditional-formatting/
description: Come applicare formati condizionali ai file Excel e ODS in Python.
keywords: applicare formati condizionali 
---

## **Introduzione**

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a una cella o a un intervallo di celle e far sì che tale formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, è possibile rendere una cella in grassetto solo quando il suo valore supera i 500. Quando il valore della cella soddisfa la condizione, il formato specificato viene applicato alla cella. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella. In Microsoft Excel, seleziona **Formato**, quindi **Formattazione condizionale** per aprire il dialogo della Formattazione condizionale.

Aspose.Cells per Python via .NET supporta l'applicazione di formattazione condizionale alle celle a runtime. Questo articolo spiega come. Spiega anche come calcolare il colore utilizzato da Excel per la formattazione condizionale con scala di colori.

## **Applicare la formattazione condizionale**

Aspose.Cells per Python via .NET supporta la formattazione condizionale in diversi modi:

- Utilizzando il foglio di calcolo del designer
- Utilizzando il metodo di copia.
- Creare la formattazione condizionale in fase di esecuzione.

### **Utilizzo del foglio di calcolo del designer**

Gli sviluppatori possono creare un foglio di calcolo designer con formattazione condizionale in Microsoft Excel e poi aprire quel foglio con Aspose.Cells per Python via .NET. Aspose.Cells per Python via .NET carica e salva il foglio di calcolo designer, mantenendo tutte le impostazioni di formattazione condizionale.

### **Utilizzando il metodo di copia**

Aspose.Cells per Python via .NET permette agli sviluppatori di copiare le impostazioni di formattazione condizionale da una cella all'altra nel foglio di lavoro chiamando il metodo [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **Applicare la formattazione condizionale in fase di esecuzione**

Aspose.Cells per Python via .NET permette sia di aggiungere che di rimuovere la formattazione condizionale a runtime. I campioni di codice mostrano come impostare la formattazione condizionale:

1. Istanziare un foglio di lavoro.
1. Aggiungere un formato condizionale vuoto.
1. Impostare l'intervallo a cui dovrebbe essere applicata la formattazione.
1. Definire le condizioni di formattazione.
1. Salvare il file.

Dopo questo esempio ci sono diversi altri esempi più piccoli che mostrano come applicare impostazioni del carattere, impostazioni dei bordi e schemi.

Microsoft Excel 2007 ha aggiunto una formattazione condizionale più avanzata che Aspose.Cells per Python via .NET supporta anche. Gli esempi qui illustrano come usare una formattazione semplice, gli esempi di Microsoft Excel 2007 mostrano come applicare formattazioni più avanzate.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **Imposta Carattere**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

Puoi solo cambiare lo stile del carattere, il colore del testo, lo stile sottolineato e lo stile barrato.

{{% /alert %}}

### **Imposta Bordo**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

Puoi solo usare stili di linea sottili per il bordo di contorno. Le linee diagonali non sono consentite.

{{% /alert %}}

### **Imposta Schema**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **Argomenti avanzati**
- [Aggiunta di Formattazioni Condizionali a Scala a 2 Colori e Scala a 3 Colori](/cells/it/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Applica la formattazione condizionale nei fogli di lavoro](/cells/it/python-net/apply-conditional-formatting-in-worksheets/)
- [Applica sfumature a righe e colonne alternative con la formattazione condizionale](/cells/it/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Genera Immagini Barre Dati delle Formattazioni Condizionali](/cells/it/python-net/generate-conditional-formatting-databars-images/)
- [Ottieni Insiemi di Icone, Barre Dati o Oggetti Scala a Colori usati nella Formattazione Condizionale](/cells/it/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
