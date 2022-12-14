---
title: Mostra e nascondi fogli di lavoro e schede
type: docs
weight: 10
url: /it/net/show-and-hide-worksheets-and-tabs/
---
{{% alert color="primary" %}}

Aspose.Cells consente all'utente di mostrare e nascondere elementi di una cartella di lavoro inclusi fogli di lavoro e schede.

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

 Un file Excel può avere uno o più fogli di lavoro. Ogni volta che creiamo un file Excel, aggiungiamo fogli di lavoro al file Excel in cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dall'altro foglio di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte, gli sviluppatori potrebbero richiedere di nascondere alcuni fogli di lavoro e altri visibili nel file Excel per il proprio interesse. Così,**Aspose.Cells** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei loro file Excel.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class fornisce un'ampia gamma di proprietà e metodi per gestire i fogli di lavoro. Per controllare la visibilità di un foglio di lavoro, utilizzare il[**È visibile**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) proprietà del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe.[**È visibile**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) è una proprietà booleana, il che significa che può memorizzare solo a**VERO** o**falso** valore.

### **Rendere visibile un foglio di lavoro**

 Rendi visibile un foglio di lavoro impostando il file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**È visibile**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) proprietà a**VERO**

### **Nascondere un foglio di lavoro**

 Nascondere un foglio di lavoro impostando il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**È visibile**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) proprietà a**falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Mostra e nascondi le schede**

Se osservi attentamente la parte inferiore di un file Excel Microsoft, vedrai una serie di controlli. Questi includono:

- Schede dei fogli.
- Pulsanti di scorrimento delle schede.

Le schede dei fogli rappresentano i fogli di lavoro nel file Excel. Fare clic su qualsiasi scheda per passare a quel foglio di lavoro. Maggiore è il numero di fogli di lavoro nella cartella di lavoro, maggiore sarà il numero di schede dei fogli. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere le schede del foglio.

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede dei fogli e dei pulsanti di scorrimento delle schede nei file Excel.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class fornisce un'ampia gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono utilizzare il file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) proprietà.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) è una proprietà booleana, il che significa che può memorizzare solo a**VERO** o**falso** valore.

### **Rendere visibili le schede**

 Rendi visibili le schede con il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) proprietà a**VERO**.

### **Nascondere le schede**

 Nascondere le schede in un file Excel impostando il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)proprietà a false.

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), ne nasconde le schede e salva il file modificato come output.xls. Dopo l'esecuzione del codice, vedrai che le schede della cartella di lavoro sono nascoste.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Controllo della larghezza della barra delle linguette**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
