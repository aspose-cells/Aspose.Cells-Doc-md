---
title: Aspose.Cells for Java 17.10 Note di rilascio
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-17-10-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.10](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.10/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42423|Annulla il calcolo a esecuzione prolungata del metodo Workbook.calculateFormula|Nuova caratteristica|
|CELLSJAVA-42414|Ottieni il campo SheetId del foglio di lavoro MS Excel|Nuova caratteristica|
|CELLSJAVA-42402|Buon HTML necessario per l'HTML allegato|Aumento|
|CELLSJAVA-42372|La posizione dei trattini lunghi non è la stessa di Microsoft Excel|Aumento|
|CELLSJAVA-42399|I punti delle frecce non sono chiari nell'output Pdf|Insetto|
|CELLSJAVA-42419|Il testo viene troncato nell'HTML di output|Insetto|
|CELLSJAVA-42418|Il colore del bordo non corrisponde a MS Excel nell'output HTML|Insetto|
|CELLSJAVA-42417|Il colore di sfondo non corrisponde a quello di Ms Excel nell'output HTML|Insetto|
|CELLSJAVA-42385|callback IFilePathProvider non viene mai chiamato e quindi il file HTML ha 'null' nel percorso|Insetto|
|CELLSJAVA-42412|Le etichette dell'asse dei valori non sono presenti durante la conversione di Excel in PDF|Insetto|
|CELLSJAVA-42408|Sovrapposizione del testo Problema dopo il rendering del foglio di lavoro nell'immagine|Insetto|
|CELLSJAVA-42420|Cancellazione e problema di memoria insufficiente a causa dell'ampio intervallo di dati del grafico|Insetto|
|CELLSJAVA-42415|Il grafico di output non è come il grafico originale nell'HTML di output|Insetto|
|CELLSJAVA-42410|L'area del grafico, le etichette, le legende e così via vengono visualizzate in modo errato nel PDF e nel PNG di output|Insetto|
|CELLSJAVA-42409|L'area del grafico non viene visualizzata correttamente negli output PDF e PNG del grafico MS Excel|Insetto|
|CELLSJAVA-41046|La sequenza della legenda del grafico è cambiata durante il rendering del foglio di calcolo in formato PDF|Insetto|
|CELLSJAVA-40416|I colori e lo stile del grafico si perdono|Insetto|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge il metodo AbstractCalculationMonitor.Interrupt(string).**
Consente agli utenti di interrompere l'avanzamento dei calcoli delle formule.
### **Aggiunge l'enumerazione HtmlCrossType.MSExport**
Visualizza la stringa come MS Excel che esporta HTML.
### **Aggiunge la proprietà Worksheet.TabId**
Ottiene l'identificatore interno del foglio.
### **Aggiunge enum OLEDBCommandType.None**
Il tipo di comando non è specificato.
### **Aggiunge enum ConnectionDataSourceType**
Rappresenta il tipo di connessione dell'origine dati.
### **Proprietà ExternalConnection.Credentials e ExternalConnection.ReConnectionMethod obsolete**
Usare invece la proprietà ExternalConnection.CredentialsMethodType e ExternalConnection.ReconnectionMethodType.
### **Proprietà WebQueryConnection.EditPage obsoleta**
Utilizzare invece la proprietà WebQueryConnection.EditWebPage.
### **Aggiunge la proprietà Series.ValuesFormatCode**
Rappresenta il codice del formato numerico dei valori della serie.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Impostare il codice del formato dei valori della serie di grafici](/cells/it/java/set-the-values-format-code-of-chart-series/)
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Leggere e scrivere la connessione esterna del file XLSB](/cells/it/java/read-and-write-external-connection-of-xlsb-or-xls-file/)
- [Interrompere o annullare il calcolo della formula della cartella di lavoro](/cells/it/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Specificare come incrociare la stringa nell'HTML di output utilizzando HtmlCrossType](/cells/it/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
