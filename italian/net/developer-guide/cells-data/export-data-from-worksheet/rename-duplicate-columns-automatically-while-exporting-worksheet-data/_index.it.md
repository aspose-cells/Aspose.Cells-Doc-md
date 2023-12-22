---
title: Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro
type: docs
weight: 250
url: /it/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Scopri come rinominare automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro tramite Aspose.Cells for .NET API.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Possibili scenari di utilizzo**

 A volte l'utente deve affrontare il problema delle colonne duplicate durante l'esportazione dei dati dal foglio di lavoro alla tabella dati. DataTable non può avere colonne duplicate, pertanto le colonne duplicate devono essere rinominate prima di poter esportare i dati del foglio di lavoro nella tabella dati. Aspose.Cells può rinominare automaticamente le colonne duplicate secondo la strategia da te specificata[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) proprietà. Se specifichi[**Rinomina Strategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, le colonne verranno rinominate come colonna1, colonna2, colonna3, ecc. e se lo specifichi[**Rinomina Strategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Lettera, le colonne verranno rinominate come colonnaA, colonnaB, colonnaC, ecc.

##  **Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro**

Il seguente codice di esempio aggiunge alcuni dati nelle prime tre colonne del foglio di lavoro ma tutte le colonne hanno lo stesso nome, ad esempio *Persone*. Quindi esporta i dati dal foglio di lavoro nella tabella dati specificando[**Rinomina Strategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Strategia delle lettere. Quindi stampa i nomi delle colonne della tabella dati generata da Aspose.Cells. La schermata seguente mostra la tabella dati con i dati esportati nel visualizzatore. Come puoi vedere, le colonne duplicate sono state rinominate PeopleA, PeopleB ecc.

![cose da fare:immagine_alt_testo](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Uscita della console**

Ecco l'output della console del codice di esempio precedente come riferimento.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
