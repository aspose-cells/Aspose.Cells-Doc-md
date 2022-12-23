---
title: Viste del foglio di lavoro
type: docs
weight: 40
url: /it/net/worksheet-views/
description:  Questo articolo descriverà come utilizzare C# e .NET API per interagire con l'anteprima dell'interruzione di pagina di una cartella di lavoro e fogli di lavoro di Excel. Lavora anche con riquadri divisi, riquadri congelati e fattore di zoom.
---
## **Anteprima interruzione di pagina**

Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Vista normale.
- Anteprima dell'interruzione di pagina.

La visualizzazione normale è la visualizzazione predefinita di un foglio di lavoro. L'anteprima dell'interruzione di pagina è una visualizzazione di modifica che mostra un foglio di lavoro così come verrà stampato. L'anteprima dell'interruzione di pagina mostra quali dati andranno su ogni pagina in modo da poter regolare l'area di stampa e le interruzioni di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare la visualizzazione normale o le modalità di anteprima dell'interruzione di pagina.

### **Controllo delle modalità di visualizzazione**

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di anteprima normale o interruzione di pagina, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) proprietà.[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) è una proprietà booleana, il che significa che può memorizzare solo a**VERO** o un**falso** valore.

#### **Abilitazione della visualizzazione normale**

 Impostare un foglio di lavoro sulla visualizzazione normale impostando il file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) proprietà a**falso**.

#### **Abilitazione dell'anteprima dell'interruzione di pagina**

 Imposta qualsiasi foglio di lavoro sull'anteprima dell'interruzione di pagina impostando il file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) proprietà a**VERO**In questo modo il foglio di lavoro passa dalla visualizzazione normale all'anteprima dell'interruzione di pagina.

 Di seguito viene fornito un esempio completo che dimostra come utilizzare il file[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)proprietà per abilitare la modalità di anteprima dell'interruzione di pagina per il primo foglio di lavoro di un file Excel.

Il file book1.xls viene aperto creando un'istanza del file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe. La visualizzazione passa all'anteprima dell'interruzione di pagina per il primo foglio di lavoro impostando il file[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)proprietà a**VERO**. Il file modificato viene salvato come output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Fattore di ingrandimento**

### **Utilizzando Microsoft Excel**

Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare lo zoom o il fattore di ridimensionamento di un foglio di lavoro. Questa funzione aiuta gli utenti a vedere i contenuti del foglio di lavoro in viste più piccole o più grandi. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.

### **Aspose.Cells e fattore di ingrandimento**

Aspose.Cells consente agli sviluppatori di impostare il fattore di zoom del foglio di lavoro.
Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Ingrandisci**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)proprietà. Il fattore di zoom viene impostato assegnando un valore numerico (intero) a[**Ingrandisci**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) proprietà.

Di seguito viene fornito un esempio completo che dimostra come utilizzare il file[**Ingrandisci**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) proprietà per impostare il fattore di zoom del primo foglio di lavoro del file Excel.

Il file book1.xls viene aperto creando un'istanza del file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe. Il fattore di zoom del primo foglio di lavoro è impostato su 75 e il file modificato viene salvato come output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Blocca i riquadri**

### **Utilizzando Microsoft Excel**

Blocca riquadri è una funzionalità fornita da Microsoft Excel. Il blocco dei riquadri consente di selezionare i dati in modo che rimangano visibili durante lo scorrimento in un foglio di lavoro.

### **Aspose.Cells & Blocca riquadri**

Aspose.Cells consente agli sviluppatori di applicare blocchi di riquadri ai fogli di lavoro in fase di esecuzione.

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per configurare i riquadri bloccati, chiama la classe Foglio di lavoro'[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)metodo. Il[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)metodo accetta i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe congelate**, il numero di righe visibili nel riquadro superiore.
- **Colonne congelate**, il numero di colonne visibili nel riquadro sinistro

 Il file book1.xls viene aperto chiamando il file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class' durante la creazione di un'istanza e alcune righe e colonne vengono bloccate nel primo foglio di lavoro. Il file modificato viene salvato come output.xls.

 Di seguito viene fornito un esempio completo che mostra come utilizzare il file[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)metodo per bloccare righe e colonne (a partire da C4, rappresentato dalla 4a riga e dalla 3a colonna, dove le righe e le colonne iniziano dall'indice 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Riquadri divisi**

Se devi dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, dividi i riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di poter scorrere ogni riquadro del tuo foglio di lavoro in modo indipendente: i riquadri divisi.

I riquadri funzionano contemporaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzione di riquadri divisi per gli utenti.

### **Applicazione e rimozione di riquadri divisi**

#### **Divisione dei riquadri**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class fornisce un'ampia gamma di proprietà e metodi per la gestione di un file Excel. Per implementare le visualizzazioni divise, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Diviso**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . Per rimuovere i riquadri divisi, utilizzare il[**RimuoviSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)metodo.

Nell'esempio, viene utilizzato un semplice file modello che viene caricato, quindi la funzione Imposta riquadri divisi viene applicata a una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Dopo aver eseguito il codice precedente, il file generato avrà una visualizzazione divisa.

#### **Rimozione dei riquadri**

 Rimuovere i riquadri divisi utilizzando il[**RimuoviSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Argomenti avanzati**
- [Nascondere la visualizzazione dei valori zero nel foglio di lavoro](/cells/it/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Imposta il colore della scheda del foglio di lavoro](/cells/it/net/set-worksheet-tab-color/)
- [Mostra e nascondi le linee della griglia e le intestazioni delle colonne delle righe](/cells/it/net/show-and-hide-gridlines-and-row-column-headers/)
- [Mostra e nascondi righe, colonne e barre di scorrimento](/cells/it/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostra e nascondi fogli di lavoro e schede](/cells/it/net/show-and-hide-worksheets-and-tabs/)
- [Mostra formule invece di valori in un foglio di lavoro](/cells/it/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Usa le opzioni di controllo degli errori](/cells/it/net/use-error-checking-options/)

