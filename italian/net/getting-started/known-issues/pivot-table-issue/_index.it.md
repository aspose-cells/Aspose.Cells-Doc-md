---
title: Problema con la tabella pivot
type: docs
weight: 50
url: /it/net/pivot-table-issue/
---
## **Sintomo**
"Ho provato ad aprire il file excel generato dal pulsante "Apri" di IE. L'excel è stato generato leggendo un modello excel. Mentre clicco sul pulsante Apri si sta aprendo e allo stesso tempo sta spuntando un messaggio di errore che dice "Impossibile aprire il file di origine della tabella pivot .....".

Ma quando salvo il file excel generato utilizzando il pulsante "Salva" e lo apro dal file dal percorso salvato, si apre correttamente senza alcun errore. "
### **Soluzione**
Aspose.Cells imposta il formato dei dati pivot e impone a MS Excel di creare report tabella pivot e altre attività di calcolo basate sull'origine dati quando la cartella di lavoro si apre in MS Excel. Quindi si dovrebbe usare**SaveType.OpenInBrowser** piuttosto che usare**SaveType.OpenInExcel**Uno dei tanti motivi è che quando si utilizza l'opzione OpenInExcel durante il salvataggio del file generato in output in MS Excel in fase di esecuzione utilizzando il pulsante "Apri" della finestra di dialogo di download, MS Excel non è in grado di analizzare i dati della cartella di lavoro per generare il rapporto della tabella pivot. Ciò è causato dal problema del nome file, è la routine di IE in quanto aggiunge qualcosa come "[1]" per renderlo come "fileName" + "[1]" + ".xls" al nome originale e quindi niente da fare con Aspose.Cells. (cioè... aggiunge sempre "[1]" per fare "fileName"+ "[1]"+ ".xls" e non come fileName.xls). In breve, se un file contiene una tabella pivot, non può essere aperto utilizzando l'opzione OpenInExcel SaveType e ciò si applicherà a entrambi, ad esempio se si crea il file da zero o si utilizza un file modello per i dati di origine per creare un report della tabella pivot. Pertanto, è necessario utilizzare l'opzione OpenInBrowser SaveType se il file contiene dati della tabella pivot per creare un report della tabella pivot.

È necessario modificare il codice e aggiornare a SaveType.OpenInBrowser se si utilizza il metodo Workbook.Save()

Oppure modifica il tuo codice per utilizzare "inline" se stai utilizzando l'opzione "attachment" nel tuo codice. cioè



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
