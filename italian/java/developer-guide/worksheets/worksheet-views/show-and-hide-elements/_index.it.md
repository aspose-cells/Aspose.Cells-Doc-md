---
title: Mostra e nascondi elementi
type: docs
weight: 60
url: /it/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells consente all'utente di mostrare e nascondere elementi di un libro di lavoro, inclusi fogli di lavoro, righe, colonne, schede, barre di scorrimento, griglie,

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

Un file Excel può avere uno o più fogli di lavoro. Ogni volta che creiamo un file Excel, aggiungiamo fogli di lavoro al file Excel in cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dagli altri fogli di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte gli sviluppatori possono richiedere di nascondere alcuni fogli di lavoro e rendere visibili altri fogli di lavoro nel file Excel per il proprio interesse. Quindi, **Aspose.Cells** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei propri file Excel.

**Controllo della visibilità dei fogli di lavoro:**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire un foglio di lavoro. Ma, per controllare la visibilità di un foglio di lavoro, gli sviluppatori possono utilizzare il metodo [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Rendere un foglio di lavoro visibile**

Gli sviluppatori possono rendere un foglio di lavoro visibile passando **true** come parametro al metodo [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Nascondere un foglio di lavoro**

Gli sviluppatori possono nascondere un foglio di lavoro passando **false** come parametro al metodo [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

**Esempio:**

Di seguito è riportato un esempio completo che dimostra l'uso del metodo [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) per nascondere il primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Foglio di lavoro - Prima della modifica:**

Nella schermata sottostante, è possibile vedere che il file **Book1.xls** contiene tre fogli di lavoro: **Sheet1**, **Sheet2** e **Sheet3**.

![todo:image_alt_text](show-and-hide-elements_1.png)

**Figura:** Vista del foglio di lavoro prima di qualsiasi modifica

**Foglio di lavoro - Dopo l'esecuzione del codice di esempio:**

Il file **Book1.xls** è aperto utilizzando la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) e quindi il primo foglio di lavoro del file **Book1.xls** è reso nascosto. Il file modificato è salvato come file **output.xls** la cui vista pittorica è mostrata di seguito:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Figura:** Vista del foglio di lavoro dopo la modifica

**Impostazione del tipo di visibilità**

Puoi anche nascondere i fogli di lavoro in modo speciale. Questa funzione può nascondere il foglio di lavoro in modo che l'unico modo per renderlo di nuovo visibile sia fornire [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) come valore del parametro per il metodo [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) nel codice (è da notare qui che gli utenti non possono rendere l'oggetto visibile in MS Excel direttamente utilizzando le opzioni del menu). Gli utenti possono anche utilizzare il metodo [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) per controllare se un foglio di lavoro è contrassegnato come Molto nascosto o no.

## **Mostra o Nascondi Schede**

Se osservi attentamente in fondo a un file di Microsoft Excel, vedrai una serie di controlli. Questi includono:

- Schede del foglio.
- Pulsanti di scorrimento delle schede.

Le schede del foglio rappresentano i fogli di lavoro nel file di Excel. Fai clic su qualsiasi scheda per passare a quel foglio di lavoro. Più ci sono fogli di lavoro nel libro, più schede del foglio ci sono. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere attraverso le schede dei fogli.

**Schede del foglio e pulsanti di scorrimento delle schede**

![todo:image_alt_text](show-and-hide-elements_3.png)

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede del foglio e dei pulsanti di scorrimento delle schede nei file di Excel.

**Controllo della visibilità delle schede:**
Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file di Excel.

### **Nascondere le schede**

Nascondi le schede in un file di Excel impostando il metodo [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Rendere visibili le schede con il metodo {1} della classe {0}.**

Rendere visibili le schede con il metodo della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) di [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Esempio di codice completo:**

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls.

Puoi vedere che il file Book1.xls contiene delle schede nella figura sottostante. Dopo l'esecuzione del codice di esempio, le schede vengono nascoste, come puoi vedere dalla schermata del file output.xls sottostante.

**book1.xls: File Excel prima di qualsiasi modifica**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: File Excel dopo la modifica**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Mostra e nascondi righe e colonne**

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e colonne hanno valori univoci che vengono utilizzati per identificarle e per identificare singole celle. Ad esempio, le righe sono numerate - 1, 2, 3, 4, ecc. - e le colonne sono ordinate in ordine alfabetico - A, B, C, D, ecc. I valori di riga e colonna vengono visualizzati negli intestazioni. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di queste intestazioni di riga e colonna.

**Controllo della visibilità dei fogli di lavoro:**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe Worksheet fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per controllare la visibilità delle intestazioni di riga e colonna, utilizzare il metodo [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) della classe Worksheet.

### **Nascondere le intestazioni di riga/colonna**

Nascondi le intestazioni di riga e colonna utilizzando il metodo [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Rendere visibili le intestazioni di riga/colonna**

Rendi visibili le intestazioni di riga e colonna utilizzando il metodo [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Di seguito è riportato un esempio completo che dimostra come utilizzare il metodo [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) per nascondere le intestazioni di riga e colonna del primo foglio di lavoro di un file Excel.

La schermata sottostante mostra che Book1.xls contiene tre fogli di lavoro: Foglio1, Foglio2 e Foglio3. Ogni foglio di lavoro mostra le intestazioni di riga e colonna.

**Book1.xls: foglio di lavoro prima della modifica**

![todo:image_alt_text](show-and-hide-elements_6.png)

Book1.xls viene aperto utilizzando la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) e le intestazioni di riga e colonna sul primo foglio di lavoro vengono nascoste. Il file modificato viene salvato come output.xls.

**Vista del foglio di lavoro dopo la modifica**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Mostra e nascondi le barre di scorrimento**

Le barre di scorrimento sono molto utilizzate per navigare i contenuti di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:

- Barre di scorrimento verticali
- Barre di scorrimento orizzontali

Microsoft Excel fornisce anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere i contenuti del foglio di lavoro. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.

**Controllo della visibilità delle barre di scorrimento:**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Tuttavia, per controllare la visibilità delle barre di scorrimento nel file Excel, gli sviluppatori possono utilizzare i metodi [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

### **Nascondere le barre di scorrimento**

Nascondere le barre di scorrimento impostando i metodi [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) su **false**.

### **Rendere visibili le barre di scorrimento**

Rendere visibili le barre di scorrimento impostando i metodi [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) della classe Workbook su **true**.

**Esempio di codice completo:**

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls.

Nella schermata sottostante è mostrato il file Book1.xls contenente entrambe le barre di scorrimento. Il file modificato è salvato come file output.xls, anche mostrato di seguito.

**Book1.xls: File Excel prima di qualsiasi modifica**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: File Excel dopo la modifica**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Mostrare e nascondere le linee della griglia**

Tutti i fogli di lavoro di Microsoft Excel hanno linee della griglia per impostazione predefinita. Aiutano a delimitare le celle, in modo che sia facile inserire dati in particolari celle. Le linee della griglia ci consentono di visualizzare un foglio di lavoro come una raccolta di celle, dove ogni cella è facilmente identificabile.

Aspose.Cells consente anche di controllare la visibilità delle linee della griglia.

### **Controllo della visibilità delle linee della griglia**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per controllare la visibilità delle linee della griglia, utilizza il metodo [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **Rendere Visibili le Linee della Griglia**

Per rendere visibili le linee della griglia, utilizzare il metodo [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **Nascondere le Linee della Griglia**

Nascondi le linee della griglia utilizzando il metodo [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{% alert color="primary" %}}

Le linee della griglia sono applicate all'intero foglio. Per 'nascondere' le linee della griglia su una sezione di un foglio di lavoro, utilizzare la formattazione dei bordi per impostare i bordi di un colore che si fondono con lo schema di colori del foglio.

{{% /alert %}}

**Esempio: Nascondere le Linee della Griglia su un Foglio di Lavoro Particolare**

L'esempio seguente dimostra l'uso del metodo [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) per nascondere le linee della griglia del primo foglio di lavoro di un file Excel.

Lo screenshot sotto mostra che il file Book1.xls contiene tre fogli di lavoro: Foglio1, Foglio2 e Foglio3. Tutti questi fogli di lavoro hanno le linee della griglia.

**Vista del foglio di lavoro prima della modifica**

![todo:image_alt_text](show-and-hide-elements_10.png)

Il file Book1.xls viene aperto utilizzando la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) e poi le linee della griglia del primo foglio di lavoro vengono nascoste. Il file modificato viene salvato come file output.xls.

**Vista del foglio di lavoro dopo la modifica**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Articoli Correlati**

{{% alert color="primary" %}}

- [Funzionalità Impostazione Pagina](/cells/it/java/page-setup-features/).
- [Aggiungere bordi alle celle per creare una tabella](/cells/it/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
