---
title: Mostrare e Nascondere Fogli e Schede
type: docs
weight: 10
url: /it/net/show-and-hide-worksheets-and-tabs/
description: Questo articolo fornisce del codice di esempio per utilizzare l API C# o la Libreria .NET per mostrare e nascondere programmatticamente un foglio Excel. Inoltre, come mostrare e nascondere le schede del documento Excel.
---

{{% alert color="primary" %}}

Aspose.Cells consente all'utente di mostrare e nascondere elementi di un documento, inclusi fogli e schede.

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

Un file Excel può avere uno o più fogli di lavoro. Ogni volta che creiamo un file Excel, aggiungiamo fogli di lavoro al file Excel in cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dagli altri fogli di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte gli sviluppatori possono richiedere di nascondere alcuni fogli di lavoro e rendere visibili altri fogli di lavoro nel file Excel per il proprio interesse. Quindi, **Aspose.Cells** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei propri file Excel.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio nel file Excel.

Un foglio è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli. Per controllare la visibilità di un foglio, utilizzare la proprietà [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) è una proprietà Booleana, il che significa che può solo memorizzare un valore **true** o **false**.

### **Rendere un foglio di lavoro visibile**

Rendere un foglio visibile impostando la proprietà [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) su **true**

### **Nascondere un foglio di lavoro**

Nascondere un foglio impostando la proprietà [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) su **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Mostrare e Nascondere Schede**

Se osservi attentamente in fondo a un file di Microsoft Excel, vedrai una serie di controlli. Questi includono:

- Schede del foglio.
- Pulsanti di scorrimento delle schede.

Le schede del foglio rappresentano i fogli di lavoro nel file di Excel. Fai clic su qualsiasi scheda per passare a quel foglio di lavoro. Più ci sono fogli di lavoro nel libro, più schede del foglio ci sono. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere attraverso le schede dei fogli.

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede del foglio e dei pulsanti di scorrimento delle schede nei file di Excel.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono utilizzare la proprietà [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) è una proprietà Booleana, il che significa che può solo memorizzare un valore **true** o **false**.

### **Rendere visibili le schede con il metodo {1} della classe {0}.**

Mostrare le schede con la proprietà [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) su **true**.

### **Nascondere le schede**

Nascondere le schede in un file Excel impostando la proprietà [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) a false.

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls. Dopo l'esecuzione del codice, vedrai che le schede del documento sono nascoste.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Controllare la larghezza della barra delle schede**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
