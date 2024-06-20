---
title: Problema Tabella Pivot
type: docs
weight: 50
url: /it/net/pivot-table-issue/
---

## **Sintomo**
"Ho provato ad aprire il file Excel generato dal pulsante "Apri" di IE. L'Excel è stato generato leggendo un modello di Excel. Mentre faccio clic sul pulsante Apri si apre e contemporaneamente appare un messaggio di errore che dice "Impossibile aprire il file di origine della tabella pivot.....".

Ma quando salvo il file Excel generato utilizzando il pulsante "Salva" e lo apro dal file dalla directory salvata si apre correttamente senza errori.
### **Soluzione**
Aspose.Cells imposta il formato dati di un'area pivot e obbliga MS Excel a creare un rapporto di tabella pivot e altre attività di calcolo in base alla fonte dati quando il foglio di lavoro viene aperto in MS Excel. Pertanto, si dovrebbe utilizzare **SaveType.OpenInBrowser** anziché utilizzare **SaveType.OpenInExcel**. Uno dei tanti motivi è quando si utilizza l'opzione OpenInExcel durante il salvataggio del file generato in uscita in MS Excel a tempo di esecuzione utilizzando il pulsante "Apri" della finestra di dialogo di download, MS Excel potrebbe non analizzare i dati del foglio di lavoro per generare un rapporto di tabella pivot. Ciò è causato dal problema del nome file, è la consuetudine di IE poiché aggiunge qualcosa come "[1]" per renderlo come "nomefile"+ "[1]"+ ".xls" al nome originale e quindi nulla a che fare con Aspose.Cells.  (ovvero... aggiunge sempre "[1]" per fare "nomefile"+ "[1]"+ ".xls" e non come nomefile.xls). In breve, se un file contiene una tabella pivot, non può essere aperto utilizzando l'opzione SaveType OpenInExcel e questo si applicherà sia se si crea il file da zero o si utilizza un file modello per i dati di origine per creare il rapporto di tabella pivot. Quindi, si dovrebbe utilizzare l'opzione SaveType OpenInBrowser se il file contiene dati della tabella pivot per creare un rapporto di tabella pivot.

Dovresti modificare il tuo codice e aggiornare a SaveType.OpenInBrowser se stai utilizzando il metodo Workbook.Save()

O modifica il tuo codice per utilizzare "inline" se stai utilizzando l'opzione "attachment" nel tuo codice. cioè,



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
