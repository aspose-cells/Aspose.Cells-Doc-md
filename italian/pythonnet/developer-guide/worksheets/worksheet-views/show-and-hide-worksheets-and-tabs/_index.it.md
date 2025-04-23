---
title: Mostrare e Nascondere Fogli e Schede
type: docs
weight: 10
url: /it/python-net/show-and-hide-worksheets-and-tabs/
description: Questo articolo fornisce codice di esempio per usare l API Aspose.Cells per Python via .NET per visualizzare e nascondere programmaticamente un foglio di lavoro Excel. Inoltre, come mostrare e nascondere le schede di un documento Excel.
keywords: Biblioteca Python Excel, mostra e nascondi un foglio di lavoro, mostra e nascondi schede, controlla la larghezza della barra delle schede.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET permette all'utente di mostrare e nascondere gli elementi di un libro di lavoro, inclusi fogli e schede.

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

Un file Excel può avere uno o più fogli di lavoro. Quando creiamo un file Excel, aggiungiamo i fogli di lavoro nel file con cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dall'altro, avendo i propri dati e impostazioni di formattazione, ecc. A volte, gli sviluppatori potrebbero aver bisogno di nascondere alcuni fogli e rendere visibili altri nel file Excel per i propri interessi. Quindi, **Aspose.Cells per Python via .NET** permette agli sviluppatori di controllare la visibilità dei fogli di lavoro nei loro file Excel.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che permette l'accesso a ogni foglio di lavoro nel file Excel.

Un foglio è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli. Per controllare la visibilità di un foglio, utilizzare la proprietà [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) è una proprietà Booleana, il che significa che può solo memorizzare un valore **true** o **false**.

### **Rendere un foglio di lavoro visibile**

Rendere un foglio visibile impostando la proprietà [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) su **true**

### **Nascondere un foglio di lavoro**

Nascondere un foglio impostando la proprietà [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) su **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Mostrare e Nascondere Schede**

Se osservi attentamente in fondo a un file di Microsoft Excel, vedrai una serie di controlli. Questi includono:

- Schede del foglio.
- Pulsanti di scorrimento delle schede.

Le schede del foglio rappresentano i fogli di lavoro nel file di Excel. Fai clic su qualsiasi scheda per passare a quel foglio di lavoro. Più ci sono fogli di lavoro nel libro, più schede del foglio ci sono. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere attraverso le schede dei fogli.

Usando Aspose.Cells per Python via .NET, gli sviluppatori possono controllare la visibilità delle schede dei fogli e dei pulsanti di scorrimento delle schede nei file Excel.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) offre molte proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono usare la proprietà [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) della classe [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) è una proprietà Booleana, il che significa che può memorizzare solo un valore **true** o **false**.

### **Rendere visibili le schede con il metodo {1} della classe {0}.**

Mostrare le schede con la proprietà [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) su **true**.

### **Nascondere le schede**

Nascondere le schede in un file Excel impostando la proprietà [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) a false.

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls. Dopo l'esecuzione del codice, vedrai che le schede del documento sono nascoste.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Controllare la larghezza della barra delle schede**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
