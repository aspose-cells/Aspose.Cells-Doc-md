---
title: Aggiungi campo calcolato nella tabella pivot
type: docs
weight: 130
url: /it/python-net/add-calculated-field-in-pivot-table/
description: Come aggiungere un campo calcolato nella tabella pivot con Aspose.Cells per Python via .NET.
keywords: Aspose.Cells per Python Excel, libreria Excel Python, Aggiunta di un campo calcolato nella tabella pivot utilizzando la libreria Excel Python.
---

## **Possibili Scenari di Utilizzo**
Quando crei una tabella pivot basata su dati noti, scopri che i dati al suo interno non sono quelli che desideri. I dati che desideri sono la combinazione di questi dati originali. Ad esempio, è necessario aggiungere, sottrarre, moltiplicare e dividere i dati originali prima di volerli. A questo punto, è necessario creare un campo calcolato e impostare la formula corrispondente per il calcolo. Quindi eseguire alcune statistiche e altre operazioni sul campo calcolato. 

## **Come aggiungere un campo calcolato nella tabella pivot in Excel**
Inserisci un campo calcolato in una tabella pivot in Excel, segui questi passaggi:

1. Seleziona la tabella pivot a cui desideri aggiungere un campo calcolato. 
2. Vai alla scheda Analizza tabella pivot nel menu a nastro.
3. Fai clic su "Campi, elementi e set" e quindi seleziona "Campo calcolato" dal menu a discesa.
4. Nel campo "Nome", inserire un nome per il campo calcolato.
5. Nel campo "Formula", inserire la formula per il calcolo che si desidera eseguire utilizzando i nomi dei campi del PivotTable appropriati e gli operatori matematici. 
<br>
<img src="1.png" width=80% />
6. Fare clic su "ok" per creare il campo calcolato.
7. Il nuovo campo calcolato apparirà nell'elenco dei campi del PivotTable nella sezione dei Valori.
8. Trascinare il campo calcolato nella sezione dei Valori del PivotTable per visualizzare i valori calcolati.
<br>
<img src="2.png" width=80% />

## **Come aggiungere un campo calcolato nella tabella pivot utilizzando la libreria Excel Aspose.Cells per Python**
Aggiungere un campo calcolato al file Excel utilizzando Aspose.Cells per la libreria Python via .NET. Si prega di consultare il codice di esempio seguente. Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot con campo calcolato al foglio di lavoro.
1. Impostare i dati originali e creare una tabella pivot. 
2. Creare il campo calcolato in base al PivotField esistente nella tabella pivot.
3. Aggiungere il campo calcolato all'area dati. 
4. Infine, salvare il libro di lavoro nel formato [output XLSX](out.xlsx). 

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
