---
title: Aggiungi campo calcolato nella tabella pivot
type: docs
weight: 130
url: /it/java/add-calculated-field-in-pivot-table/
description: Come aggiungere un campo calcolato nella tabella pivot con Aspose.Cells.
keywords: Aggiunta di un campo calcolato nella tabella pivot.
---

## **Possibili Scenari di Utilizzo**
Quando crei una tabella pivot basata su dati noti, scopri che i dati al suo interno non sono quelli che desideri. I dati che desideri sono la combinazione di questi dati originali. Ad esempio, è necessario aggiungere, sottrarre, moltiplicare e dividere i dati originali prima di volerli. A questo punto, è necessario creare un campo calcolato e impostare la formula corrispondente per il calcolo. Quindi eseguire alcune statistiche e altre operazioni sul campo calcolato. 

## **Aggiungi campo calcolato nella tabella pivot in Excel**
Inserisci un campo calcolato in una tabella pivot in Excel, segui questi passaggi:

1. Seleziona la tabella pivot a cui desideri aggiungere un campo calcolato. 
2. Vai alla scheda Analizza tabella pivot nel menu a nastro.
3. Fai clic su "Campi, elementi e set" e quindi seleziona "Campo calcolato" dal menu a discesa.
4. Nel campo "Nome", inserire un nome per il campo calcolato.
5. Nel campo "Formula", inserire la formula che si desidera eseguire utilizzando i nomi dei campi di PivotTable appropriati e gli operatori matematici. 
<br>
<img src="1.png" width=80% />
6. Fare clic su "ok" per creare il campo calcolato.
7. Il nuovo campo calcolato apparirà nell'elenco dei campi del PivotTable nella sezione dei Valori.
8. Trascinare il campo calcolato nella sezione dei Valori del PivotTable per visualizzare i valori calcolati.
<br>
<img src="2.png" width=80% />

## **Aggiungi un campo calcolato nella tabella pivot.**
Si prega di vedere il seguente codice di esempio. Il codice imposta prima i dati originali e crea una tabella pivot. Quindi crea il campo calcolato in base al campo di PivotField esistente nella tabella pivot e aggiunge il campo calcolato all'area dati. Infine, salva il file di lavoro nel formato [output XLSX](out.xlsx). Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot con campo calcolato al foglio di lavoro.

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
