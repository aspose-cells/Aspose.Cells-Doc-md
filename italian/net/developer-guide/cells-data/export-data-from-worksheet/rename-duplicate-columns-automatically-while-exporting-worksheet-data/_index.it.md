---
title: Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro
type: docs
weight: 250
url: /it/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **Possibili scenari di utilizzo**

 volte l'utente deve affrontare un problema di colonne duplicate durante l'esportazione dei dati dal foglio di lavoro nella tabella dei dati. DataTable non può avere colonne duplicate, quindi le colonne duplicate devono essere rinominate prima di poter esportare i dati del foglio di lavoro nella tabella dati. Aspose.Cells può rinominare automaticamente le colonne duplicate in base alla strategia specificata dall'utente con[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) proprietà. Se specifichi[**RinominaStrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, le colonne verranno rinominate come colonna1, colonna2, colonna3, ecc. e se lo specifichi[**RinominaStrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, quindi le colonne verranno rinominate come colonna A, colonna B, colonna C, ecc.

## **Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro**

 Il seguente codice di esempio aggiunge alcuni dati nelle prime tre colonne del foglio di lavoro, ma tutte le colonne hanno lo stesso nome, ad es*Le persone* . Quindi esporta i dati dal foglio di lavoro nella tabella dei dati specificando[**RinominaStrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Strategia della lettera. Quindi stampa i nomi delle colonne della tabella dati generata da Aspose.Cells. La schermata seguente mostra la tabella dati con i dati esportati nel visualizzatore. Come puoi vedere, le colonne duplicate sono state rinominate in PeopleA, PeopleB ecc.

![cose da fare:immagine_alt_testo](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Uscita console**

Ecco l'output della console del codice di esempio precedente come riferimento.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
