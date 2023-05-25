---
title: Cancella filtro nella tabella pivot
type: docs
weight: 130
url: /it/net/clear-filter-in-pivot-table/
description: Come cancellare PivotFilter dallo specifico PivotField nella tabella pivot con Aspose.Cells.
keywords: Clear PivotFilter in pivot table.
---
##  **Possibili scenari di utilizzo**
 Quando crei una tabella pivot con dati noti e desideri filtrare la tabella pivot, devi imparare e utilizzare il filtro. Può aiutarti a filtrare i dati che desideri in modo efficace. Utilizzando Aspose.Cells API, è possibile utilizzare il filtro sui valori dei campi nelle tabelle pivot.

##  **Cancella filtro nella tabella pivot in Excel**
Cancella filtro nella tabella pivot in Excel, attenersi alla seguente procedura:

1.  Selezionare la tabella pivot per cui si desidera cancellare il filtro.
2. Fare clic sulla freccia dell'elenco a discesa per il filtro che si desidera cancellare nella tabella pivot.
3. Selezionare "Cancella filtro" dal menu a discesa.
<img src="1.png" width=80% />
4. Se si desidera cancellare tutti i filtri dalla tabella pivot, è anche possibile fare clic sul pulsante "Cancella filtri" nella scheda Analizza tabella pivot sulla barra multifunzione in Excel.
<img src="2.png" width=80% />

##  **Cancella filtro nella tabella pivot utilizzando C#**
 Cancella filtro nella tabella pivot utilizzando Aspose.Cells. Vedere il seguente codice di esempio.
1.  Imposta i dati e crea una tabella pivot basata su di essi.
2. Aggiungi un filtro sul campo riga della tabella pivot.
 3. Salva la cartella di lavoro in[uscita XLSX](out_add.xlsx) formato. Dopo aver eseguito il codice di esempio, al foglio di lavoro viene aggiunta una tabella pivot con filtro top10.
 4. Cancellare il filtro su un pivotfield specifico. Dopo aver eseguito il codice per cancellare il filtro, il filtro sullo specifico pivotfield verrà cancellato. Si prega di controllare[uscita XLSX](out_delete.xlsx).

##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}