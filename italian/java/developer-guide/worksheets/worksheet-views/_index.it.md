---
title: Viste del foglio di lavoro
type: docs
weight: 10
url: /it/java/worksheet-views/
---
## **Anteprima interruzione di pagina**
Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Vista normale.
- Anteprima dell'interruzione di pagina.

Una visualizzazione normale è la visualizzazione predefinita di un foglio di lavoro. L'anteprima dell'interruzione di pagina è una visualizzazione di modifica che mostra un foglio di lavoro così come verrà stampato. L'anteprima dell'interruzione di pagina mostra quali dati andranno su ogni pagina in modo da poter regolare l'area di stampa e le interruzioni di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare la visualizzazione normale o le modalità di anteprima dell'interruzione di pagina.
### **Controllo delle modalità di visualizzazione**
 Aspose.Cells fornisce a[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di anteprima normale o interruzione di pagina, utilizzare il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metodo.
#### **Abilitazione della visualizzazione normale**
Imposta qualsiasi foglio di lavoro sulla visualizzazione normale utilizzando il file[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) metodo del[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe e passaggio**falso** come parametro.
#### **Abilitazione dell'anteprima dell'interruzione di pagina**
Imposta qualsiasi foglio di lavoro sull'anteprima dell'interruzione di pagina utilizzando il file[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metodo del[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe e passaggio**VERO**come parametro.

 Di seguito viene fornito un esempio completo che dimostra l'uso del formato[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metodo per abilitare la modalità di anteprima dell'interruzione di pagina per il primo foglio di lavoro del file Excel.

Nello screenshot qui sotto, puoi vedere che il file Book1.xls è in visualizzazione normale.

**Book1.xls: Foglio di lavoro prima della modifica** 

![cose da fare:immagine_alt_testo](worksheet-views_1.png)

 Book1.xls viene aperto con il file[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class e la modalità passa all'anteprima dell'interruzione di pagina per il primo foglio di lavoro. Il file modificato viene salvato come output.xls.

**Ouput.xls: foglio di lavoro dopo la modifica** 

![cose da fare:immagine_alt_testo](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Fattore di ingrandimento**
Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare lo zoom o il fattore di ridimensionamento di un foglio di lavoro. Questa funzione aiuta gli utenti a vedere i contenuti del foglio di lavoro in viste più piccole o più grandi. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.

**Impostazione del fattore di zoom utilizzando Microsoft Excel** 

![cose da fare:immagine_alt_testo](worksheet-views_3.png)

Aspose.Cells consente inoltre agli sviluppatori di impostare il fattore di zoom del foglio di lavoro.
### **Controllo del fattore di zoom**
Aspose.Cells fornisce a[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)metodo.

 Di seguito viene fornito un esempio completo che dimostra come utilizzare il file[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)metodo per impostare il fattore di zoom del primo foglio di lavoro in un file Excel.

Nello screenshot qui sotto, puoi vedere il file Book1.xls nella visualizzazione predefinita.

**Book1.xls: foglio di lavoro prima della modifica** 

![cose da fare:immagine_alt_testo](worksheet-views_4.png)

 Il file Book1.xls viene aperto con l'estensione[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class e il fattore di zoom del primo foglio di lavoro è impostato su 75. Il file modificato viene salvato come output.xls.

**Output.xls: foglio di lavoro dopo la modifica** 

![cose da fare:immagine_alt_testo](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Blocca i riquadri**
Blocca riquadri è una funzionalità fornita da Microsoft Excel. Il blocco dei riquadri consente di selezionare i dati in modo che rimangano visibili durante lo scorrimento in un foglio di lavoro.

**Utilizzo dei riquadri bloccati in Microsoft Excel** 

![cose da fare:immagine_alt_testo](worksheet-views_6.png)

Aspose.Cells consente inoltre agli sviluppatori di applicare blocchi di riquadri ai fogli di lavoro in fase di esecuzione.

Aspose.Cells fornisce a[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per configurare i riquadri bloccati, chiamare il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) metodo. Il[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) accetta i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe congelate**, il numero di righe visibili nel riquadro superiore.
- **Colonne congelate**, il numero di colonne visibili nel riquadro sinistro

 Di seguito viene fornito un esempio completo che mostra come utilizzare il file[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) metodo per bloccare righe e colonne (a partire da C4, rappresentato dalla 4a riga e dalla 3a colonna, dove le righe e le colonne iniziano da 0 indici) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Nello screenshot qui sotto, puoi vedere il file Book1.xls senza bloccare i riquadri.

**Book1.xls: visualizzazione del foglio di lavoro prima di qualsiasi modifica** 

![cose da fare:immagine_alt_testo](worksheet-views_7.png)

 Il file Book1.xls viene aperto con l'estensione[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class e quindi alcune righe e colonne vengono congelate nel primo foglio di lavoro. Il file modificato viene salvato come output.xls.

**Outlook.xls: visualizzazione del foglio di lavoro dopo la modifica** 

![cose da fare:immagine_alt_testo](worksheet-views_8.png)
## **Riquadri divisi**
Se devi dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, dividi i riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di poter scorrere ogni riquadro del tuo foglio di lavoro in modo indipendente: i riquadri divisi.

I riquadri funzionano contemporaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzione di riquadri divisi per gli utenti.
### **Applicazione e rimozione di riquadri divisi**
#### **Divisione dei riquadri**
Aspose.Cells fornisce a[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class fornisce un'ampia gamma di proprietà e metodi per la gestione dei file Excel. Per implementare le visualizzazioni divise, utilizzare il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[diviso](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) metodo. Per rimuovere i riquadri divisi, utilizzare il[rimuovereSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) metodo.

Nell'esempio, viene utilizzato un semplice file modello che viene caricato, quindi la funzione Imposta riquadri divisi viene applicata a una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Dopo aver eseguito il codice precedente, il file generato ha una visualizzazione divisa.

**Dividi i riquadri nel file di output** 

![cose da fare:immagine_alt_testo](worksheet-views_9.png)
#### **Rimozione dei riquadri**
 Gli sviluppatori possono rimuovere i riquadri divisi utilizzando il file[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[rimuovereSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Argomenti avanzati**
- [Nascondere la visualizzazione dei valori zero nel foglio di lavoro](/cells/it/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Imposta il colore della scheda del foglio di lavoro](/cells/it/java/set-worksheet-tab-color/)
- [Mostra e nascondi elementi](/cells/it/java/show-and-hide-elements/)
- [Mostra formule invece di valori in un foglio di lavoro](/cells/it/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Usa le opzioni di controllo degli errori](/cells/it/java/use-error-checking-options/)
