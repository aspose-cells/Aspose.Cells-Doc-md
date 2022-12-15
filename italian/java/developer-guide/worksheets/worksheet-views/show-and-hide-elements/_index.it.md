---
title: Mostra e nascondi elementi
type: docs
weight: 60
url: /it/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells consente all'utente di mostrare e nascondere elementi di una cartella di lavoro inclusi fogli di lavoro, righe, colonne, schede, barre di scorrimento, griglie,

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

 Un file Excel può avere uno o più fogli di lavoro. Ogni volta che creiamo un file Excel, aggiungiamo fogli di lavoro al file Excel in cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dall'altro foglio di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte, gli sviluppatori potrebbero richiedere di nascondere alcuni fogli di lavoro e altri visibili nel file Excel per il proprio interesse. Così,**Aspose.Cells** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei loro file Excel.

**Controllo della visibilità dei fogli di lavoro:**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel.[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente di accedere a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class fornisce un'ampia gamma di proprietà e metodi per gestire un foglio di lavoro. Tuttavia, per controllare la visibilità di un foglio di lavoro, gli sviluppatori possono utilizzare[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo del[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

### **Rendere visibile un foglio di lavoro**

 Gli sviluppatori possono rendere visibile un foglio di lavoro passando**VERO** come parametro di[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo del[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

### **Nascondere un foglio di lavoro**

 Gli sviluppatori possono nascondere un foglio di lavoro passando**falso** come parametro di[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo del[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

**Esempio:**

 Di seguito viene fornito un esempio completo che dimostra l'uso di[**setVisibile(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo di[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class per nascondere il primo foglio di lavoro del file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Foglio di lavoro - Prima della modifica:**

 Nello screenshot qui sotto, puoi vederlo**Libro1.xls** file contiene tre fogli di lavoro:**Foglio1** , **Foglio2** e**Foglio3** .

![cose da fare:immagine_alt_testo](show-and-hide-elements_1.png)

**Figura:** Vista del foglio di lavoro prima di qualsiasi modifica

**Foglio di lavoro - Dopo aver eseguito il codice di esempio:**

**Libro1.xls** il file viene aperto utilizzando il file[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe e poi il primo foglio di lavoro del**Libro1.xls** il file viene nascosto. Il file modificato viene salvato come**uscita.xls**file la cui vista pittorica è mostrata di seguito:

![cose da fare:immagine_alt_testo](show-and-hide-elements_2.png)

**Figura:** Vista del foglio di lavoro dopo la modifica

**Impostazione del tipo di visibilità**

 Puoi anche nascondere i fogli di lavoro in un modo speciale. Questa funzione può nascondere il foglio di lavoro in modo che l'unico modo per renderlo nuovamente visibile sia dando[**Tipo di visibilità.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) come valore del parametro per il[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) metodo nel codice (è da notare qui, l'utente non può rendere l'oggetto visibile in MS Excel direttamente utilizzando le sue opzioni di menu). Gli utenti possono anche utilizzare[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) metodo per verificare se un foglio di lavoro è contrassegnato come VeryHidden o meno.

## **Mostra o nascondi le schede**

Se osservi attentamente la parte inferiore di un file Microsoft Excel, vedrai una serie di controlli. Questi includono:

- Schede dei fogli.
- Pulsanti di scorrimento delle schede.

Le schede dei fogli rappresentano i fogli di lavoro nel file Excel. Fare clic su qualsiasi scheda per passare a quel foglio di lavoro. Maggiore è il numero di fogli di lavoro nella cartella di lavoro, maggiore sarà il numero di schede dei fogli. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Pertanto, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere le schede del foglio.

**Schede dei fogli e pulsanti di scorrimento delle schede**

![cose da fare:immagine_alt_testo](show-and-hide-elements_3.png)

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede dei fogli e dei pulsanti di scorrimento delle schede nei file Excel.

**Controllo della visibilità delle schede:**
 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class fornisce un'ampia gamma di proprietà e metodi per la gestione di un file Excel.

### **Nascondere le schede**

 Nascondere le schede in un file Excel impostando il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe'[**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Rendere visibili le schede**

 Rendi visibili le schede con il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe'[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Esempio di codice completo:**

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), ne nasconde le schede e salva il file modificato come output.xls.

Puoi vedere che il file Book1.xls contiene schede nella figura seguente. Dopo che il codice di esempio è stato eseguito, le schede sono nascoste, come puoi vedere dallo screenshot del file output.xls qui sotto.

**book1.xls: file Excel prima di qualsiasi modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_4.png)

**output.xls: file Excel dopo la modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Mostra e nascondi righe e colonne**

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e le colonne hanno valori univoci che vengono utilizzati per identificarle e per identificare le singole celle. Ad esempio, le righe sono numerate – 1, 2, 3, 4, ecc. – e le colonne sono ordinate alfabeticamente – A, B, C, D, ecc. I valori di riga e colonna sono visualizzati nelle intestazioni. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di queste intestazioni di riga e colonna.

**Controllo della visibilità dei fogli di lavoro:**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)classe. La classe Worksheet fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per controllare la visibilità delle intestazioni di righe e colonne, utilizzare la classe Foglio di lavoro'[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metodo.

### **Nascondere le intestazioni di riga/colonna**

 Nascondi le intestazioni di righe e colonne utilizzando il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metodo.

### **Rendere visibili le intestazioni di riga/colonna**

 Rendi visibili le intestazioni di righe e colonne utilizzando il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metodo.

 Di seguito viene fornito un esempio completo che dimostra come utilizzare il file[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metodo per nascondere le intestazioni di riga e colonna del primo foglio di lavoro di un file Excel.

Lo screenshot seguente mostra che Book1.xls contiene tre fogli di lavoro: Sheet1, Sheet2 e Sheet3. Ogni foglio di lavoro mostra le intestazioni di riga e colonna.

**Book1.xls: foglio di lavoro prima della modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_6.png)

 Book1.xls viene aperto utilizzando il file[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class' e le intestazioni di riga e colonna nel primo foglio di lavoro sono nascoste. Il file modificato viene salvato come output.xls.

**Vista del foglio di lavoro dopo la modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Mostra e nascondi le barre di scorrimento**

Le barre di scorrimento sono molto utilizzate per navigare nel contenuto di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:

- Barre di scorrimento verticali
- Barre di scorrimento orizzontali

Microsoft Excel fornisce anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere il contenuto del foglio di lavoro. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.

**Controllo della visibilità delle barre di scorrimento:**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel.[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class fornisce un'ampia gamma di proprietà e metodi per gestire un file Excel. Tuttavia, per controllare la visibilità delle barre di scorrimento nel file Excel, gli sviluppatori possono utilizzare[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metodi del[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe.

### **Nascondere le barre di scorrimento**

 Nascondere le barre di scorrimento impostando il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metodi per**falso**.

### **Rendere visibili le barre di scorrimento**

 Rendi visibili le barre di scorrimento impostando la classe Cartella di lavoro'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metodi per**VERO**.

**Esempio di codice completo:**

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls.

Lo screenshot seguente mostra il file Book1.xls contenente entrambe le barre di scorrimento. Il file modificato viene salvato come file output.xls, anch'esso mostrato di seguito.

**Book1.xls: file Excel prima di qualsiasi modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_8.png)

**output.xls: file Excel dopo la modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Mostra e nascondi le linee della griglia**

Tutti i fogli di lavoro di Microsoft Excel hanno una griglia per impostazione predefinita. Aiutano a delineare le celle, in modo che sia facile inserire dati in celle particolari. Le linee della griglia ci consentono di visualizzare un foglio di lavoro come una raccolta di celle, in cui ogni cella è facilmente identificabile.

Aspose.Cells consente inoltre di controllare la visibilità delle linee della griglia.

### **Controllo della visibilità delle linee della griglia**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per controllare la visibilità delle linee della griglia, utilizzare il file[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metodo.

#### **Rendere visibili le linee della griglia**

 Per rendere visibili le linee della griglia, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metodo.

#### **Nascondere le linee della griglia**

 Nascondere le linee della griglia utilizzando il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setGridlinesVisible(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metodo.

{{% alert color="primary" %}}

Le griglie vengono applicate all'intero foglio. Per "nascondere" le griglie su una sezione di un foglio di lavoro, utilizzare[formattazione del bordo](/cells/it/java/create-table-by-using-border-lines-for-a-range/) per impostare i bordi su un colore che si fonde con la combinazione di colori del foglio.

{{% /alert %}}

**Esempio: nascondere le linee della griglia su un particolare foglio di lavoro**

 L'esempio seguente mostra l'uso di[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**setGridlinesVisible(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metodo per nascondere la griglia del primo foglio di lavoro di un file Excel.

Lo screenshot seguente mostra che il file Book1.xls contiene tre fogli di lavoro: Sheet1, Sheet2 e Sheet3. Tutti questi fogli di lavoro hanno una griglia.

**Vista del foglio di lavoro prima della modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_10.png)

 Il file Book1.xls viene aperto utilizzando il file[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class e quindi le griglie del primo foglio di lavoro sono nascoste. Il file modificato viene salvato come file output.xls.

**Vista del foglio di lavoro dopo la modifica**

![cose da fare:immagine_alt_testo](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **articoli Correlati**

{{% alert color="primary" %}}

- [Funzioni di impostazione della pagina](/cells/it/java/page-setup-features/).
- [Aggiunta di bordi alle celle per creare una tabella](/cells/it/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
