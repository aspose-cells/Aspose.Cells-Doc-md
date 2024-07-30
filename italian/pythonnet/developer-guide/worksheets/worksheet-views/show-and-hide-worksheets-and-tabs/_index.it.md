---
title: Mostrare e Nascondere Fogli e Schede
type: docs
weight: 10
url: /it/python-net/show-and-hide-worksheets-and-tabs/
description: Questo articolo fornisce un codice di esempio per utilizzare l API Aspose.Cells per Python via .NET per visualizzare e nascondere in modo programmatico un foglio di lavoro di Excel. Inoltre, come mostrare e nascondere le schede dei fogli di lavoro di Excel.
keywords: Libreria Excel Python, Mostra e Nascondi un Foglio di Lavoro, Mostra e Nascondi le Schede, Controlla la larghezza della Barra delle Schede.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET consente all'utente di mostrare e nascondere elementi di un libro di lavoro, inclusi fogli di lavoro e schede.

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

Un file di Excel può avere uno o più di un foglio di lavoro. Ogniqualvolta creiamo un file di Excel, aggiungiamo i fogli di lavoro al file di Excel in cui lavoriamo. Ogni foglio di lavoro in un file di Excel è indipendente dagli altri fogli di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte gli sviluppatori possono avere bisogno di nascondere alcuni fogli di lavoro e renderne visibili altri nel file di Excel per il proprio interesse. Quindi, **Aspose.Cells per Python via .NET** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei propri file di Excel.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file di Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ogni foglio di lavoro nel file di Excel.

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

Utilizzando Aspose.Cells per Python via .NET, gli sviluppatori possono controllare la visibilità delle schede e i pulsanti di scorrimento delle schede nei file di Excel.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono utilizzare la proprietà [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) è una proprietà Booleana, il che significa che può memorizzare solo un valore **true** o **false**.

### **Rendere visibili le schede con il metodo {1} della classe {0}.**

Mostrare le schede con la proprietà [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) su **true**.

### **Nascondere le schede**

Nascondere le schede in un file Excel impostando la proprietà [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) a false.

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls. Dopo l'esecuzione del codice, vedrai che le schede del documento sono nascoste.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Controllare la larghezza della barra delle schede**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
