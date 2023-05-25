---
title: Aggiungi campo calcolato nella tabella pivot
type: docs
weight: 130
url: /it/net/add-calculated-field-in-pivot-table/
description: Come aggiungere un campo calcolato nella tabella pivot con Aspose.Cells.
keywords: Adding a calculated field in pivot table.
---
##  **Possibili scenari di utilizzo**
 Quando crei una tabella pivot basata su dati noti, scopri che i dati in essa contenuti non sono quelli desiderati. I dati desiderati sono la combinazione di questi dati originali. Ad esempio, è necessario aggiungere, sottrarre, moltiplicare e dividere i dati originali prima di desiderare i dati. A questo punto, è necessario creare un campo calcolato e impostare la formula corrispondente per il calcolo. Quindi eseguire alcune statistiche e altre operazioni sul campo calcolato.

##  **Aggiungi campo calcolato nella tabella pivot in Excel**
Inserisci un campo calcolato in una tabella pivot in Excel, segui questi passaggi:

1.  Seleziona la tabella pivot a cui desideri aggiungere un campo calcolato.
2. Passare alla scheda Analizza tabella pivot sulla barra multifunzione.
3. Fare clic su "Campi, articoli e set" e quindi selezionare "Campo calcolato" dal menu a discesa.
4. Nel campo "Nome", inserire un nome per il campo calcolato.
 5. Nel campo "Formula", immettere la formula per il calcolo che si desidera eseguire utilizzando i nomi dei campi della tabella pivot e gli operatori matematici appropriati.
<br>
<img src="1.png" width=80% />
6. Fare clic su "ok" per creare il campo calcolato.
7. Il nuovo campo calcolato verrà visualizzato nell'elenco dei campi della tabella pivot nella sezione Valori.
8. Trascinare il campo calcolato nella sezione Valori della tabella pivot per visualizzare i valori calcolati.
<br>
<img src="2.png" width=80% />

##  **Aggiungi campo calcolato nella tabella pivot utilizzando C#**
Aggiungi il campo calcolato al file Excel utilizzando Aspose.Cells. Consulta il seguente codice di esempio. Dopo aver eseguito il codice di esempio, al foglio di lavoro viene aggiunta una tabella pivot con campo calcolato.
1.  Imposta i dati originali e crea una tabella pivot.
2. Creare il campo calcolato in base al PivotField esistente nella tabella pivot.
 3. Aggiungere il campo calcolato all'area dati.
 4. Infine, salva la cartella di lavoro in[uscita XLSX](out.xlsx) formato.

##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-calculated-field-in-PivotTable.cs" >}}
