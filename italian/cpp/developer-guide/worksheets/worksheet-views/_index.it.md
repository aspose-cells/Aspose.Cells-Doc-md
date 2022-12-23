---
title: Viste del foglio di lavoro
type: docs
weight: 40
url: /it/cpp/worksheet-views/
---
## **Anteprima interruzione di pagina**
Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Vista normale.
- Anteprima dell'interruzione di pagina.

La visualizzazione Normale è la visualizzazione predefinita di un foglio di lavoro. L'anteprima dell'interruzione di pagina è una visualizzazione di modifica che mostra un foglio di lavoro così come verrà stampato. L'anteprima dell'interruzione di pagina mostra quali dati andranno su ogni pagina in modo da poter regolare l'area di stampa e le interruzioni di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare la visualizzazione normale o le modalità di anteprima dell'interruzione di pagina.
### **Controllo delle modalità di visualizzazione**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di anteprima normale o interruzione di pagina, utilizzare il[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) restituisce un valore bool, il che significa che può memorizzare solo a**VERO** o**falso** valore.
#### **Abilitazione della visualizzazione normale**
Impostare un foglio di lavoro sulla visualizzazione normale impostando il file[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe a**falso**.
#### **Abilitazione dell'anteprima dell'interruzione di pagina**
Imposta qualsiasi foglio di lavoro sull'anteprima dell'interruzione di pagina impostando il file[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe a**VERO**In questo modo il foglio di lavoro passa dalla visualizzazione normale all'anteprima dell'interruzione di pagina.

 Di seguito viene fornito un esempio completo che dimostra come utilizzare il file[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metodo per abilitare la modalità di anteprima dell'interruzione di pagina per il primo foglio di lavoro di un file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Fattore di ingrandimento**
### **Utilizzando Microsoft Excel**
Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare lo zoom o il fattore di ridimensionamento di un foglio di lavoro. Questa funzione aiuta gli utenti a vedere i contenuti del foglio di lavoro in viste più piccole o più grandi. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.
### **Aspose.Cells e fattore di ingrandimento**
 Aspose.Cells consente inoltre agli sviluppatori di impostare il fattore di zoom del foglio di lavoro. Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il[Ingrandisci](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class Il fattore di zoom viene impostato assegnando un valore numerico (intero) a[Ingrandisci](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)metodo.

 Di seguito viene fornito un esempio completo che dimostra come utilizzare il file[Ingrandisci](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)metodo per impostare il fattore di zoom del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Blocca i riquadri**
### **Utilizzando Microsoft Excel**
Blocca riquadri è una funzionalità fornita da Microsoft Excel. Il blocco dei riquadri consente di selezionare i dati in modo che rimangano visibili durante lo scorrimento in un foglio di lavoro.
### **Aspose.Cells & Blocca riquadri**
 Aspose.Cells consente inoltre agli sviluppatori di applicare blocchi di riquadri ai fogli di lavoro in fase di esecuzione. Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per configurare i riquadri bloccati, chiamare il[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metodo accetta i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe congelate**, il numero di righe visibili nel riquadro superiore.
- **Colonne congelate**, il numero di colonne visibili nel riquadro sinistro

 Di seguito viene fornito un esempio completo che mostra come utilizzare il file[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metodo per bloccare righe e colonne (a partire da C4, rappresentato dalla 4a riga e dalla 3a colonna, dove le righe e le colonne iniziano dall'indice 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Riquadri divisi**
Se devi dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, dividi i riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di poter scorrere ogni riquadro del tuo foglio di lavoro in modo indipendente: i riquadri divisi.

I riquadri funzionano contemporaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzione di riquadri divisi per gli utenti.
### **Applicazione e rimozione di riquadri divisi**
#### **Divisione dei riquadri**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)fornisce una vasta gamma di metodi per la gestione di un file Excel. Per implementare le visualizzazioni divise, utilizzare il[Diviso](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Per rimuovere i riquadri divisi, utilizzare il[RimuoviSplit](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)metodo.

Nell'esempio, viene utilizzato un semplice file modello che viene caricato, quindi la funzione Imposta riquadri divisi viene applicata a una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Rimozione dei riquadri**
 Rimuovere i riquadri divisi utilizzando il[RimuoviSplit](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)metodo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
