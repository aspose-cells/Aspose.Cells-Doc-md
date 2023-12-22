---
title: Visualizzazioni del foglio di lavoro
type: docs
weight: 40
url: /it/cpp/worksheet-views/
---
##  **Anteprima interruzione pagina**
Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Visualizzazione normale.
- Anteprima dell'interruzione di pagina.

La visualizzazione Normale è la visualizzazione predefinita di un foglio di lavoro. L'anteprima dell'interruzione di pagina è una visualizzazione di modifica che mostra un foglio di lavoro così come verrà stampato. L'anteprima delle interruzioni di pagina mostra quali dati verranno inseriti in ciascuna pagina in modo da poter regolare l'area di stampa e le interruzioni di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare la modalità di visualizzazione normale o di anteprima dell'interruzione di pagina.
###  **Controllo delle modalità di visualizzazione**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La classe fornisce un'ampia gamma di metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di anteprima normale o di interruzione di pagina, utilizzare il file[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) restituisce un valore bool, il che significa che può memorizzare solo a**VERO** O**falso** valore.
####  **Abilitazione della visualizzazione normale**
Imposta un foglio di lavoro sulla visualizzazione normale impostando il file[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe in *falso**.
####  **Abilitazione dell'anteprima delle interruzioni di pagina**
Imposta qualsiasi foglio di lavoro sull'anteprima dell'interruzione di pagina impostando il file[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe su *true**. In questo modo il foglio di lavoro passa dalla visualizzazione normale all'anteprima dell'interruzione di pagina.

Di seguito è riportato un esempio completo che dimostra come utilizzare il file[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)metodo per abilitare la modalità di anteprima dell'interruzione di pagina per il primo foglio di lavoro di un file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Fattore di zoom**
###  **Utilizzando Microsoft Excel**
Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare il fattore di zoom o ridimensionamento di un foglio di lavoro. Questa funzionalità aiuta gli utenti a visualizzare i contenuti del foglio di lavoro in visualizzazioni più piccole o più grandi. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.
###  **Aspose.Cells & Fattore di zoom**
 Aspose.Cells consente inoltre agli sviluppatori di impostare il fattore di zoom del foglio di lavoro. Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fornisce un'ampia gamma di metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il comando[ImpostaZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Il fattore di zoom viene impostato assegnando un valore numerico (intero) a[ImpostaZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)metodo.

Di seguito è riportato un esempio completo che dimostra come utilizzare il file[ImpostaZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)metodo per impostare il fattore di zoom del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Blocca riquadri**
###  **Utilizzando Microsoft Excel**
Blocca riquadri è una funzionalità fornita da Microsoft Excel. Il blocco dei riquadri consente di selezionare i dati in modo che rimangano visibili durante lo scorrimento in un foglio di lavoro.
###  **Aspose.Cells & Blocca riquadri**
 Aspose.Cells consente inoltre agli sviluppatori di applicare i riquadri di blocco ai fogli di lavoro in fase di esecuzione. Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fornisce un'ampia gamma di metodi per la gestione dei fogli di lavoro. Per configurare i riquadri bloccati, chiamare il[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)Il metodo accetta i seguenti parametri:

- *Riga**, l'indice della riga della cella da cui inizierà il freeze.
- *Colonna**, l'indice della colonna della cella da cui inizierà il blocco.
- *Righe bloccate**, il numero di righe visibili nel riquadro superiore.
- *Colonne bloccate**, il numero di colonne visibili nel riquadro sinistro

 Di seguito è riportato un esempio completo che mostra come utilizzare il file[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)metodo per congelare righe e colonne (a partire da C4, rappresentato dalla 4a riga e dalla 3a colonna, dove le righe e le colonne iniziano dall'indice 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Riquadri divisi**
Se è necessario dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, dividere i riquadri. Microsoft Excel offre una funzionalità molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di poter scorrere ciascun riquadro del tuo foglio di lavoro in modo indipendente: i riquadri divisi.

I riquadri funzionano contemporaneamente. Se apporti una modifica in uno, la modifica apparirà contemporaneamente anche nell'altro. Aspose.Cells fornisce la funzionalità dei riquadri divisi per gli utenti.
###  **Applicazione e rimozione dei riquadri divisi**
####  **Divisione dei riquadri**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)La classe fornisce un'ampia gamma di metodi per la gestione di un file Excel. Per implementare le visualizzazioni divise, utilizzare il file[Diviso](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Per rimuovere i riquadri divisi, utilizzare il file[RimuoviSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)metodo.

Nell'esempio, utilizziamo un semplice file modello che viene caricato, quindi la funzionalità di impostazione dei riquadri divisi viene applicata su una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Rimozione dei riquadri**
 Rimuovere i riquadri divisi utilizzando il file[RimuoviSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)metodo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
