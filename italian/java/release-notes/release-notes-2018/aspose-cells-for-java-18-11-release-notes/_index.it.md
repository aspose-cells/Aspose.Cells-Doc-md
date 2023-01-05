---
title: Aspose.Cells for Java Note sulla versione 18.11
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-18-11-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.11.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42738|Il conteggio errato dei valori di convalida viene letto da XLSX|Aumento|
|CELLSJAVA-42734|Problema durante il trattamento dei delimitatori consecutivi come distinti|Aumento|
|CELLSJAVA-42739|Aspose.Cells.GridWeb (Java) si arresta in modo anomalo quando lo si utilizza contemporaneamente in un ambiente multiutente|Insetto|
|CELLSJAVA-42737|La riga del grafico è mancante nella conversione XLSX->PNG|Insetto|
|CELLSJAVA-42735|Problema con il metodo getActualChartSize|Insetto|
|CELLSJAVA-40861|SmartArt non viene copiato quando la cartella di lavoro viene copiata|Insetto|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà PivotTable.RefreshedByWho**
Ottiene il nome dell'utente che ha aggiornato la tabella pivot l'ultima volta.
### **Aggiunge la proprietà PivotTable.RefreshDate**
Ottiene la data dell'ultimo aggiornamento della tabella pivot.
### **Aggiunge le proprietà CalculationData.CellRow/CellColumn**
Fornisce all'utente un modo efficiente per ottenere gli indici di riga e colonna della cella invece di recuperare l'oggetto Cell.
### **Aggiunge la classe CalculationCell**
Rappresenta i dati di calcolo relativi a una cella calcolata.
### **Aggiunge il metodo AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData).**
Fornisce all'utente un metodo per raccogliere ed elaborare i riferimenti circolari.
### **Aggiunge la proprietà TxtLoadOptions.TreatConsecutiveDelimitersAsOne**
Consente all'utente di scegliere se i delimitatori consecutivi devono essere presi come uno solo durante l'importazione del file CSV.
### **Aggiunge il metodo FormatCondition.SetFormulas(string formula1, string formula2, bool isR1C1, bool isLocal)**
Fornisce un modo efficiente e conveniente per l'utente di impostare le formule per FormatCondition.
### **Aggiunge il metodo Validation.GetListValue(int row, int column).**
Consente all'utente di ottenere il valore per produrre l'elenco per la convalida di una cella specifica.
### **Metodo obsoleto ValidationCollection.Add(Validation validation).**
Usare invece il metodo ValidationCollection.Add(CellArea).
### **Aggiunge il metodo Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions)**
Convalida delle copie.
### **Aggiunge le proprietà CreatedUniversalTime, LastPrintedUniversalTime e LastSavedUniversalTime di BuiltInDocumentPropertyCollection**
Restituisce l'ora UTC relativa alle proprietà incorporate.
### **Aggiunge la proprietà OoxmlSaveOptions.UpdateSmartArt**
Indica se aggiornare la smart art.
### **Aggiunge la classe SmartArtShape**
Rappresenta la forma artistica intelligente.
