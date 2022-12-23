---
title: Aspose.Cells for .NET 8.6.3 Note di rilascio
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-8-6-3-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.6.3](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.3/)

{{% /alert %}}

Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells

## 1) Aspose.Cells

### **Altri miglioramenti e modifiche**

### **Nuove caratteristiche**

(CELLSNET-44084) - Analizza i tag Html durante l'importazione di dati in blocco

(CELLSNET-40889) - Opzione di caricamento: apre solo i fogli visibili

### **Miglioramenti**

(CELLSNET-44133) - Supporto per formato pagina di stampa Thermal 3x11

(CELLSNET-44095) - Supporto lettura/scrittura tabella collegata esterna.

(CELLSNET-44093) - Eccezione offuscata generata durante il caricamento di una cartella di lavoro non valida

(CELLSNET-43425) - Cells.ImportGridView non importa riga di intestazione

(CELLSNET-41718) - Supporto per la raccolta di oggetti nidificati negli Smart Marker

(CELLSNET-41482) - Supporto per DateTime durante l'unione mediante Smart Markers

### **Prestazione**

(CELLSNET-44096) - Workbook.CalculateFormula rimane bloccato per un tempo indefinito

(CELLSNET-44102) - Ritardo nelle prestazioni durante la conversione del foglio di lavoro in EMF

### **Insetti**

(CELLSNET-44092) - Problema durante la lettura di Hyperlink.Address con caratteri cirillici

(CELLSNET-44090) - Il file XLSB con tabella pivot viene danneggiato nella v8.6.2

(CELLSNET-44073) - La conversione in HTML con HtmlHiddenColDisplayType.Remove crea un grafico vuoto

(CELLSNET-43917) - Testo tagliato durante la conversione del foglio di calcolo in HTML

(CELLSNET-43914) - Il testo supera la casella durante il rendering del foglio di calcolo in PDF

(CELLSNET-44111) - L'indirizzo del collegamento ipertestuale contenente caratteri cinesi non viene convertito correttamente

(CELLSNET-44080) - Il testo Cells è stato leggermente spostato a destra durante la conversione in PDF

(CELLSNET-44125) - Il salvataggio in PDF non riesce per un documento Excel

(CELLSNET-44117) - Conversione errata per il titolo e la legenda del grafico

(CELLSNET-44086) - L'asse orizzontale del grafico all'interno del file pdf è ridimensionato in modo errato e invertito

(CELLSNET-44079) - Alcune voci della legenda del grafico vengono perse durante il salvataggio in PDF

(CELLSNET-44046) - Chart.ToImage modifica l'allineamento delle etichette

(CELLSNET-44134) - #VALORE! restituito per SUMPRODUCT in base a ListObject

(CELLSNET-44132) - La formula restituisce "#REF!" value all'inserimento di nuove righe nel file di output

(CELLSNET-44131) - Alcune formule errate vengono visualizzate in giro a seconda del numero di righe inserite

(CELLSNET-44128) - Salva in XLSB interrompe le formule come =SOMMA(Tabella[Col])

(CELLSNET-44082) - Aspose.Cells mostra gli stili nascosti durante il salvataggio

(CELLSNET-44081) - Quando si combinano due cartelle di lavoro si ottiene un file danneggiato

(CELLSNET-44076) - ListObject.ListColumns[i].Name non è corretto quando la cartella di lavoro apre il file XLS

(CELLSNET-44028) - La tabella pivot non si aggiorna quando si fa clic sul pulsante Dati>Aggiorna tutto

(CELLSNET-43084) - Il file di output è danneggiato durante la copia di un foglio

(CELLSNET-43083) - Il riferimento alla cella denominata non è valido "#Nome?" durante la copia di un foglio

(CELLSNET-42114) - Problemi riscontrati durante la conversione da xml a XLSX

(CELLSNET-41886) - Grafico non aggiornato con ListObject ridimensionato

(CELLSNET-41492) - Enorme quantità di convalide

### **Eccezioni**

(CELLSNET-44097) - La stringa di input non era in un formato corretto, in Workbook.Save

(CELLSNET-44099) - CalculateFormula genera un'eccezione

(CELLSNET-44127) - Il salvataggio nel flusso di file/memoria PDF causa un'eccezione

(CELLSNET-44085) - System.Exception durante il caricamento di ODS

(CELLSNET-43720) - Errore di area sconosciuta durante la combinazione di cartelle di lavoro con tabelle pivot

## 2) Aspose.Cells Griglia Suite

### **Altri miglioramenti e modifiche**

### **Insetti**

(CELLSNET-44123) - Impossibile serializzare lo stato della sessione System.Collections.Specialized.BitVector32

(CELLSNET-44108) - Worksheet.RemoveColumn/RemoveRow non funzionante in GridDesktop

(CELLSNET-44105) - Facendo clic sul pulsante Salva senza modificare lo stato attivo su GridWeb non si aggiorna il contenuto della cella nella tabella dati esportata

(CELLSNET-44104) - L'utilizzo dell'evento OnCellClickOnAjax rende impossibile la navigazione con il pulsante delle chiavi dalla cella modificabile

(CELLSNET-44100) - Lo zoom indietro sul foglio di lavoro GridDesktop provoca la riduzione del contenuto nell'angolo in alto a sinistra

### **Eccezioni**

(CELLSNET-44107) - Si è verificata un'eccezione durante l'inserimento della colonna in GridDesktop

### **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

Aggiunge la proprietà ImportTableOptions.IsHtmlString.

Indica se il valore stringa nella tabella dati contiene tag html.

Aggiunge il metodo Workbook.CreateBuiltinStyle(BuiltinStyleType type).

Crea uno stile integrato in base al tipo specificato.

Obsoleti Cells.Fine proprietà.

Utilizzare invece la proprietà Cells.LastCell.

Aggiunge il metodo Cells.ImportGridView(GridView gridView, int firstRow, int firstColumn,ImportTableOptions options).

Importa una vista griglia in queste celle con opzioni

Aggiunge la proprietà ImportTableOptions.ConvertGridStyle.

Indica se applicare lo stile della vista griglia alle celle.

 Metodo obsoleto Cells.ImportGridView(GridView gridView,int firstRow,int firstColumn, bool insertRows, bool convertStringToNumber, bool convertStyle).

Usa Cells.ImportGridView(GridView gridView, int firstRow, int firstColumn,ImportTableOptions options).

Aggiunge la proprietà LoadDataOption.OnlyVisibleWorksheet.

Carica solo i dati del foglio di lavoro visibile.

Metodo Worksheet.CopyConditionalFormatting obsoleto.

Utilizzare invece il metodo Cells.CopyRows() o Range.Copy().
