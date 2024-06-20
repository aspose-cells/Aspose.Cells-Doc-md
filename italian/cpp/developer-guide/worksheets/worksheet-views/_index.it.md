---
title: Viste del foglio di lavoro
type: docs
weight: 40
url: /it/cpp/worksheet-views/
---

## **Anteprima interruzioni di pagina**
Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Visualizzazione normale.
- Anteprima interruzioni di pagina.

La visualizzazione Normale è la visualizzazione predefinita di un foglio di lavoro. Anteprima dei salti di pagina è una visualizzazione di modifica che mostra un foglio di lavoro come verrà stampato. L'anteprima dei salti di pagina mostra quali dati andranno su ciascuna pagina in modo da poter regolare l'area di stampa e i salti di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare le modalità di visualizzazione normale o anteprima dei salti di pagina.
### **Controllo delle modalità di visualizzazione**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di visualizzazione normale o anteprima dei salti di pagina, utilizzare il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) restituisce un valore bool, il che significa che può solo memorizzare un valore **true** o **false**.
#### **Abilitazione visualizzazione normale**
Impostare un foglio di lavoro alla visualizzazione normale impostando il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) su **false**.
#### **Abilitazione anteprima interruzioni di pagina**
Impostare qualsiasi foglio di lavoro sulla visualizzazione anteprima dei salti di pagina impostando il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) su **true**. In questo modo si passa dal visualizzazione normale alla visualizzazione anteprima dei salti di pagina.

Di seguito è riportato un esempio completo che dimostra come utilizzare il metodo [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) per abilitare la modalità anteprima dei salti di pagina per il primo foglio di lavoro di un file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Fattore di zoom**
### **Utilizzando Microsoft Excel**
Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare un fattore di zoom o di ridimensionamento di un foglio di lavoro. Questa funzionalità aiuta gli utenti a vedere i contenuti del foglio di lavoro in visualizzazioni più piccole o più ampie. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.
### **Aspose.Cells e Fattore di Zoom**
Aspose.Cells consente anche agli sviluppatori di impostare il fattore di zoom del foglio di lavoro. Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il metodo [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Il fattore di zoom viene impostato assegnando un valore numerico (intero) al metodo [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/).

Di seguito è riportato un esempio completo che dimostra come utilizzare il metodo [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) per impostare il fattore di zoom del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Blocco delle celle**
### **Utilizzando Microsoft Excel**
Blocco celle è una funzione fornita da Microsoft Excel. Bloccare le celle consente di selezionare i dati che rimarranno visibili durante lo scorrimento in un foglio di lavoro.
### **Aspose.Cells e Blocco Riquadri**
Aspose.Cells consente anche agli sviluppatori di applicare riquadri di blocco ai fogli di lavoro in fase di esecuzione. Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per configurare i riquadri di blocco, chiamare il metodo [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Il metodo [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) prende i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe bloccate**, il numero di righe visibili nel riquadro superiore.
- **Colonne bloccate**, il numero di colonne visibili nel riquadro sinistro.

Di seguito è riportato un esempio completo che mostra come utilizzare il metodo [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) per bloccare righe e colonne (a partire da C4, rappresentato dalla 4a riga e la 3a colonna, dove le righe e le colonne partono dall'indice 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **Divisione dei riquadri**
Se hai bisogno di dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, utilizza la divisione dei riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di scorrere indipendentemente attraverso ciascun riquadro del foglio di lavoro: divisione dei riquadri.

I riquadri funzionano simultaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzionalità di divisione dei riquadri agli utenti.
### **Applicare e rimuovere divisioni dei riquadri**
#### **Divisione dei riquadri**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fornisce una vasta gamma di metodi per gestire un file Excel. Per implementare visualizzazioni suddivise, utilizzare il metodo [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Per rimuovere i riquadri suddivisi, utilizzare il metodo [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

Nell'esempio, viene utilizzato un semplice file di modello che viene caricato, poi viene applicata la funzione di divisione dei riquadri su una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Rimozione dei riquadri**
Rimuovere i riquadri suddivisi utilizzando il metodo [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
