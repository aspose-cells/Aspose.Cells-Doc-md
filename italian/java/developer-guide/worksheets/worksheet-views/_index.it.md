---
title: Viste del foglio di lavoro
type: docs
weight: 10
url: /it/java/worksheet-views/
---

## **Anteprima interruzioni di pagina**
Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Visualizzazione normale.
- Anteprima interruzioni di pagina.

La visualizzazione normale è la visualizzazione predefinita di un foglio di lavoro. L'anteprima interruzioni di pagina è una visualizzazione di modifica che visualizza un foglio di lavoro come verrà stampato. L'anteprima interruzioni di pagina mostra quali dati andranno su ciascuna pagina in modo da poter regolare l'area di stampa e le interruzioni di pagina. Utilizzando Aspose.Cells gli sviluppatori possono abilitare le modalità di visualizzazione normale o anteprima interruzioni di pagina.
### **Controllo delle modalità di visualizzazione**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di visualizzazione normale o anteprima interruzioni di pagina, utilizzare il metodo [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).
#### **Abilitazione visualizzazione normale**
Impostare qualsiasi foglio di lavoro sulla visualizzazione normale utilizzando il metodo [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) e passando **false** come parametro.
#### **Abilitazione anteprima interruzioni di pagina**
Impostare qualsiasi foglio di lavoro sull'anteprima interruzioni di pagina utilizzando il metodo [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) e passando **true** come parametro.

Di seguito è riportato un esempio completo che dimostra l'uso del metodo [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) per abilitare la modalità anteprima interruzioni di pagina per il primo foglio di lavoro del file Excel.

Nella schermata sottostante, è possibile vedere che il file Book1.xls è in visualizzazione normale.

**Book1.xls: Foglio di lavoro prima della modifica** 

![todo:image_alt_text](worksheet-views_1.png)

Book1.xls viene aperto con la classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) e la modalità viene cambiata in anteprima interruzioni di pagina per il primo foglio di lavoro. Il file modificato viene salvato come output.xls.

**Output.xls: foglio di lavoro dopo la modifica** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Fattore di zoom**
Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare un fattore di zoom o di ridimensionamento di un foglio di lavoro. Questa funzionalità aiuta gli utenti a vedere i contenuti del foglio di lavoro in visualizzazioni più piccole o più ampie. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.

**Impostazione del fattore di zoom utilizzando Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Anche Aspose.Cells consente agli sviluppatori di impostare il fattore di zoom del foglio di lavoro.
### **Controllare il fattore di zoom**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il metodo [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Di seguito è riportato un esempio completo che dimostra come utilizzare il metodo [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) per impostare il fattore di zoom del primo foglio di lavoro in un file Excel.

Nella schermata sottostante, è possibile vedere il file Book1.xls nella visualizzazione predefinita.

**Book1.xls: foglio di lavoro prima della modifica** 

![todo:image_alt_text](worksheet-views_4.png)

Il file Book1.xls viene aperto con la classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) e il fattore di zoom del primo foglio di lavoro viene impostato al 75. Il file modificato viene salvato come output.xls.

**Output.xls: foglio di lavoro dopo la modifica** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Blocco delle celle**
Blocco celle è una funzione fornita da Microsoft Excel. Bloccare le celle consente di selezionare i dati che rimarranno visibili durante lo scorrimento in un foglio di lavoro.

**Utilizzo del blocco delle celle in Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells consente anche agli sviluppatori di applicare il blocco delle celle ai fogli di lavoro in fase di esecuzione.

Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per configurare il blocco celle, chiamare il metodo [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Il metodo [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) richiede i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe bloccate**, il numero di righe visibili nel riquadro superiore.
- **Colonne bloccate**, il numero di colonne visibili nel riquadro sinistro.

Di seguito è riportato un esempio completo che mostra come utilizzare il metodo [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) per bloccare righe e colonne (a partire da C4, rappresentato dalla quarta riga e terza colonna, dove le righe e le colonne partono da indici 0) del primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Nella schermata sottostante, è possibile vedere il file Book1.xls senza blocchi delle celle.

**Book1.xls: vista del foglio di lavoro prima di qualsiasi modifica** 

![todo:image_alt_text](worksheet-views_7.png)

Il file Book1.xls viene aperto con la classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) e poi alcune righe e colonne vengono bloccate sul primo foglio di lavoro. Il file modificato viene salvato come output.xls.

**Outlook.xls: vista del foglio di lavoro dopo la modifica** 

![todo:image_alt_text](worksheet-views_8.png)
## **Divisione dei riquadri**
Se hai bisogno di dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, utilizza la divisione dei riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di scorrere indipendentemente attraverso ciascun riquadro del foglio di lavoro: divisione dei riquadri.

I riquadri funzionano simultaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzionalità di divisione dei riquadri agli utenti.
### **Applicare e rimuovere divisioni dei riquadri**
#### **Divisione dei riquadri**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fornisce un'ampia gamma di proprietà e metodi per gestire i file di Excel. Per implementare le visualizzazioni divise, utilizza il metodo [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\)) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Per rimuovere le divisioni dei riquadri, utilizza il metodo [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\))

Nell'esempio, viene utilizzato un semplice file di modello che viene caricato, poi viene applicata la funzione di divisione dei riquadri su una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Dopo aver eseguito il codice sopra, il file generato ha una visualizzazione divisa.

**Visualizzazione divisa nel file di output** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Rimozione dei riquadri**
Gli sviluppatori possono rimuovere i riquadri divisi utilizzando il metodo [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Argomenti avanzati**
- [Nascondere la visualizzazione dei valori zero nel foglio di lavoro](/cells/it/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Imposta il colore della scheda del foglio di lavoro](/cells/it/java/set-worksheet-tab-color/)
- [Mostra e nascondi elementi](/cells/it/java/show-and-hide-elements/)
- [Mostra le formule invece dei valori in un foglio di lavoro](/cells/it/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Usa le opzioni di controllo degli errori](/cells/it/java/use-error-checking-options/)
