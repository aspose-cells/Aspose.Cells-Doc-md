---
title: Viste del foglio di lavoro
type: docs
weight: 40
url: /it/python-net/worksheet-views/
description: Questo articolo descriverà come utilizzare l API Aspose.Cells for Python via .NET per interagire con l anteprima della visualizzazione di pagina di un workbook Excel e dei fogli di lavoro. Lavora con riquadri divisi, riquadri bloccati e fattore di zoom. 
keywords: Libreria Excel di Python, Come impostare l anteprima della visualizzazione di pagina, Come abilitare la visualizzazione normale, Come impostare il fattore di zoom, Come bloccare i riquadri, Come dividere i riquadri, Come rimuovere i riquadri.
---

## **Anteprima interruzioni di pagina**

Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Visualizzazione normale.
- Anteprima interruzioni di pagina.

La vista normale è la visualizzazione predefinita di un foglio di lavoro. Anteprima interruzioni di pagina è una visualizzazione di modifica che visualizza un foglio di lavoro come verrà stampato. L'anteprima interruzioni di pagina mostra quali dati andranno su ciascuna pagina in modo da poter regolare l'area di stampa e le interruzioni di pagina. Utilizzando Aspose.Cells per Python via .NET gli sviluppatori possono abilitare le modalità di visualizzazione normale o anteprima interruzioni di pagina.

### **Controllo delle modalità di visualizzazione**

Aspose.Cells per Python via .NET fornisce una classe che rappresenta un file Microsoft Excel. La classe contiene una raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di visualizzazione normale o anteprima del salto di pagina, usare la proprietà [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) della classe [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview). [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) è una proprietà booleana, il che significa che può solo memorizzare un valore **true** o **false**.

#### **Abilitazione visualizzazione normale**

Imposta un foglio di lavoro nella visualizzazione normale impostando la proprietà [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) su **false**.

#### **Abilitazione anteprima interruzioni di pagina**

Imposta qualsiasi foglio di lavoro in anteprima del salto di pagina impostando la proprietà [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) su **true**. In questo modo si passa dal visualizzazione normale all'anteprima del salto di pagina.

Di seguito è riportato un esempio completo che dimostra come utilizzare la proprietà [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) per abilitare la modalità anteprima del salto di pagina per il primo foglio di lavoro di un file Excel.

Il file book1.xls viene aperto creando un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). La visualizzazione viene passata all'anteprima del salto di pagina per il primo foglio di lavoro impostando la proprietà [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) su **true**. Il file modificato viene salvato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Fattore di zoom**

### **Utilizzando Microsoft Excel**

Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare un fattore di zoom o di ridimensionamento di un foglio di lavoro. Questa funzionalità aiuta gli utenti a vedere i contenuti del foglio di lavoro in visualizzazioni più piccole o più ampie. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.

### **Aspose.Cells e Fattore di Zoom**

Aspose.Cells consente ai programmatori di impostare il fattore di zoom del foglio di lavoro.
Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente di accedere a ciascun foglio di lavoro in un file di Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare la proprietà [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Il fattore di zoom viene impostato assegnando un valore numerico (intero) alla proprietà [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom).

Di seguito è riportato un esempio completo che dimostra come utilizzare la proprietà [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) per impostare il fattore di zoom del primo foglio di lavoro del file di Excel.

Il file book1.xls viene aperto creando un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Il fattore di zoom del primo foglio di lavoro viene impostato su 75 e il file modificato viene salvato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Blocco delle celle**

### **Utilizzando Microsoft Excel**

Blocco celle è una funzione fornita da Microsoft Excel. Bloccare le celle consente di selezionare i dati che rimarranno visibili durante lo scorrimento in un foglio di lavoro.

### **Aspose.Cells e Blocco Riquadri**

Aspose.Cells consente ai programmatori di applicare i blocchi riquadri ai fogli di lavoro durante l'esecuzione.

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente di accedere a ciascun foglio di lavoro in un file di Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per configurare i blocchi riquadri, chiamare il metodo [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) della classe Foglio di lavoro. Il metodo [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) accetta i seguenti parametri:

- **riga**, l'indice di riga della cella da cui inizierà il blocco.
- **colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **righe_fisse**, il numero di righe visibili nel riquadro superiore.
- **colonne_fisse**, il numero di colonne visibili nel riquadro sinistro

Il file book1.xls viene aperto chiamando il costruttore della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) durante listanziazione e alcune righe e colonne vengono bloccate nel primo foglio di lavoro. Il file modificato viene salvato come output.xls.

Di seguito è riportato un esempio completo che mostra come utilizzare il metodo [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) per bloccare righe e colonne (a partire da C4, rappresentato dalla 4ª riga e la 3ª colonna, dove le righe e le colonne iniziano dall'indice 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **Divisione dei riquadri**

Se hai bisogno di dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, utilizza la divisione dei riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di scorrere indipendentemente attraverso ciascun riquadro del foglio di lavoro: divisione dei riquadri.

I riquadri funzionano simultaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzionalità di divisione dei riquadri agli utenti.

### **Applicare e rimuovere divisioni dei riquadri**

#### **Divisione dei riquadri**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per implementare viste divise, usa il [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) della classe [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split). Per rimuovere i pannelli divisi, usa il metodo [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

Nell'esempio, viene utilizzato un semplice file di modello che viene caricato, poi viene applicata la funzione di divisione dei riquadri su una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

Dopo aver eseguito il codice sopra, il file generato avrà una vista divisa.

#### **Rimozione dei riquadri**

Rimuovere i pannelli divisi utilizzando il metodo [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Argomenti avanzati**
- [Nascondere la visualizzazione dei valori zero nel foglio di lavoro](/cells/it/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Imposta il colore della scheda del foglio di lavoro](/cells/it/python-net/set-worksheet-tab-color/)
- [Mostra e nascondi griglie, intestazioni di riga e colonna](/cells/it/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Mostra e nascondi righe, colonne e barre di scorrimento](/cells/it/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostra e nascondi fogli di lavoro e schede](/cells/it/python-net/show-and-hide-worksheets-and-tabs/)
- [Mostra formule invece di valori in un foglio di lavoro](/cells/it/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Usa le opzioni di controllo degli errori](/cells/it/python-net/use-error-checking-options/)

