---
title: Aspose.Cells for .NET 7.3.1 Note di rilascio
type: docs
weight: 40
url: /it/net/aspose-cells-for-net-7-3-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 7.3.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.3.1/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells per .NETv7.3.1 per gli utenti!



\1) Aspose.Cells 



 Nuove caratteristiche

- Formattazione condizionale: include i campi mancanti del tipo DataBar
- Formattazione condizionale: include i valori mancanti del tipo IconSet
- Formattazione condizionale - Supporto
- Leggi le regole di formattazione condizionale con le formule tra fogli
- Supporta le proprietà Cells.MinDataColumn e Cells.MinDataRow
- Supporta i colori di sfondo Cell con formattazione condizionale (MS Excel 2010)
- Sono supportati i filtri dati della tabella pivot
- È supportata la convalida avanzata dei dati di MS Excel 2010



 Miglioramenti

- Genera CellsException quando si modifica la parte della formula di matrice
- Tipi e stili di indicatori nei grafici di Excel 2007/2010
- Forme degli indicatori personalizzati nel grafico
- Come creare marker personalizzati
- I grafici secondari non sono accessibili

 -Forme automatiche nell'output HTML

- DataBars: formattazione condizionale nella tabella pivot
- Perdita di query Web nei formati MS Excel 2007
- Gestisci gli intervalli di dati esterni e le relative proprietà
- Dimensione del file XLSB di MS Excel Problema



 Eccezioni

- Il metodo statico CellsHelper.DetectFileFormat() genera un'eccezione
- Cerco una soluzione allo Aspose.Cells
- Eccezione: "L'indice era fuori intervallo"
- Il caricamento della cartella di lavoro genera: "La stringa di input non era in un formato corretto"
- Da forma a immagine Errore in Excel alla funzione PDF



 Insetti

- La formattazione della modalità colore dell'immagine non viene mantenuta durante il salvataggio di un file Excel
- Proprietà personalizzate del foglio di lavoro MS Excel 2003 danneggiate
- ERRORE nel calcolo delle formule
- L'apertura e il salvataggio di un file con formattazione condizionale non sono riusciti
- Lo stile in grassetto non è visibile nella cella di intestazione di ListObject
- Problema dei marcatori di serie

 -Citazioni nel file delimitato da tabulazioni salvato

- CSV lettura/scrittura non "andata e ritorno" per alcuni input

 -StringValue restituisce un valore errato

- 2 piccoli problemi con l'implementazione della funzione CELL
- Problemi con la funzione CELL
- Problema di calcolo della formula GETPIVOTDATA
- La formula PPMT sta causando il ripristino del file dopo aver chiamato il metodo Workook.CalculateFormula()
- Problema con la combinazione IFERROR e VLOOKUP
- La formula CONTA.SE non valuta il valore corretto
- Problemi di calcolo della funzione OFFSET
- Problemi di calcolo della funzione MODE
- Problemi di calcolo della funzione CELL

 - Bug della funzione CERCA.VERT

 - Problemi di calcolo della funzione TRIM

- Salva come HTML mostra la colonna nascosta nell'output
- Il salvataggio cancella la formattazione
- Grafica nell'output HTML
- HTML problemi di formattazione (relativi ai bordi extra)

 -SheetRender's XPS e problema di formato numerico personalizzato

 -Salva come PDF non conserva la formattazione

- Problemi con la formattazione XLSX in Excel e output PDF
- La tabella pivot di Excel visualizzata in PDF non è corretta
- Caratteri personalizzati in PDF
- Problema di rendering dell'allineamento verticale di Cell
- Testo mancante all'estremità più a destra
- Alcune formattazioni condizionali non vengono visualizzate correttamente
- Problema con la formattazione nella riga totale nella tabella pivot
- Office per Mac-Os 2k11 si arresta in modo anomalo dopo l'apertura di un file Excel

-Perché questo codice non funziona?

- Il campo calcolato della tabella pivot viene modificato
- Problema durante il salvataggio della cartella di lavoro con membri calcolati
- Layout compatto per tavolo pivot
- File danneggiato durante l'aggiornamento delle tabelle pivot
- ChangeDataSource() non funziona
- SheetRender disegna il contenuto della casella di testo in grassetto
- La casella di testo di Excel viene ridimensionata in modo errato durante il rendering dell'immagine
- SheetRender esporta la forma in modo errato

 \2) ReteWeb



 Insetti

 40838 - La formattazione di GridWeb non viene salvata

- Il ridimensionamento della colonna lo rende nascosto

 40722 - Formattazione personalizzata con percentuale

 40826 - Problema di bordo superiore in GridWeb

 40831 - Problemi cross-browser per Aspose.Cells.GridWeb

 40822 - L'utente deve premere due volte il tasto per registrarsi quando si accede a una nuova cella - Problema con Firefox

- Aggiornamento aAspose.Cells.Problema di versione GridWeb
- GroupRow con IndentLevel, maschera di testo e problemi relativi ai gruppi nascosti




