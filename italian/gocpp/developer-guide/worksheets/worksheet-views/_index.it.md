---
title: Viste del foglio di lavoro
type: docs
weight: 40
url: /it/go-cpp/worksheet-views/
---

## **Anteprima interruzioni di pagina**

Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Visualizzazione normale.
- Anteprima interruzioni di pagina.

La visualizzazione Normale è la visualizzazione predefinita di un foglio di lavoro. Anteprima dei salti di pagina è una visualizzazione di modifica che mostra un foglio di lavoro come verrà stampato. L'anteprima dei salti di pagina mostra quali dati andranno su ciascuna pagina in modo da poter regolare l'area di stampa e i salti di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare le modalità di visualizzazione normale o anteprima dei salti di pagina.

### **Controllo delle modalità di visualizzazione**

Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che consente l’accesso a ogni foglio di lavoro nel file Excel.

Una scheda di lavoro è rappresentata dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre un'ampia gamma di metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di anteprima senza interruzioni di pagina o con interruzioni di pagina, utilizza il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) restituisce un valore booleano, il che significa che può contenere solo un valore **true** o **false**.

#### **Abilitazione visualizzazione normale**

Imposta una scheda di lavoro in visualizzazione normale impostando il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) a **false**.

#### **Abilitazione anteprima interruzioni di pagina**

Imposta qualsiasi scheda di lavoro in modalità anteprima interruzioni di pagina impostando il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) a **true**. Così facendo, il foglio di lavoro passa dalla visualizzazione normale alla modalità anteprima interruzioni di pagina.

Un esempio completo è dato di seguito, dimostrando come utilizzare il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) per attivare la modalità anteprima interruzioni di pagina per il primo foglio di lavoro di un file Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Fattore di zoom**

### **Utilizzando Microsoft Excel**

Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare un fattore di zoom o di ridimensionamento di un foglio di lavoro. Questa funzionalità aiuta gli utenti a vedere i contenuti del foglio di lavoro in visualizzazioni più piccole o più ampie. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.

### **Aspose.Cells e Fattore di Zoom**

Aspose.Cells permette inoltre agli sviluppatori di impostare il fattore di zoom del foglio di lavoro. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che permette l’accesso a ogni foglio di lavoro nel file Excel.

Una scheda di lavoro è rappresentata dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre una vasta gamma di metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom del foglio di lavoro, usa il metodo [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Il fattore di zoom si imposta assegnando un valore numerico (intero) al metodo [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/).

Un esempio completo è dato di seguito, dimostrando come usare il metodo [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) per impostare il fattore di zoom del primo foglio di Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Blocco delle celle**

### **Utilizzando Microsoft Excel**

Blocco celle è una funzione fornita da Microsoft Excel. Bloccare le celle consente di selezionare i dati che rimarranno visibili durante lo scorrimento in un foglio di lavoro.

### **Aspose.Cells e Blocco Riquadri**

Aspose.Cells permette inoltre agli sviluppatori di applicare la funzione di blocco dei riquadri ai fogli di lavoro in fase di esecuzione. Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che permette l’accesso a ogni foglio di lavoro nel file Excel.

Una scheda di lavoro è rappresentata dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre una vasta gamma di metodi per la gestione dei fogli di lavoro. Per configurare i riquadri di blocco, chiama il metodo [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Il metodo [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) prende i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe bloccate**, il numero di righe visibili nel riquadro superiore.
- **Colonne bloccate**, il numero di colonne visibili nel riquadro sinistro.

Un esempio completo seguente illustra come usare il metodo [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) per bloccare righe e colonne (a partire da C4, rappresentato dalla quarta riga e dalla terza colonna, dove righe e colonne partono dall’indice 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **Divisione dei riquadri**

Se hai bisogno di dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, utilizza la divisione dei riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di scorrere indipendentemente attraverso ciascun riquadro del foglio di lavoro: divisione dei riquadri.

I riquadri funzionano simultaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzionalità di divisione dei riquadri agli utenti.

### **Applicare e rimuovere divisioni dei riquadri**

#### **Divisione dei riquadri**

Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) offre un'ampia gamma di metodi per la gestione di un file Excel. Per implementare le viste divise, utilizza il metodo [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) della classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Per rimuovere i riquadri divisi, utilizza il metodo [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

Nell'esempio, viene utilizzato un semplice file di modello che viene caricato, poi viene applicata la funzione di divisione dei riquadri su una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Rimozione dei riquadri**

Rimuovere i riquadri divisi usando il metodo [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
