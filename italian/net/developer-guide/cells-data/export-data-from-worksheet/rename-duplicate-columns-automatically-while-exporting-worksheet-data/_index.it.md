---
title: Rinomina automaticamente le colonne duplicate durante l esportazione dei dati del foglio di lavoro
type: docs
weight: 250
url: /it/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Scopri come rinominare automaticamente le colonne duplicate durante l esportazione dei dati del foglio di lavoro attraverso l API Aspose.Cells for .NET.
keywords: Rinomina le colonne duplicate durante l esportazione dei dati del foglio di lavoro, Rinomina automaticamente le colonne duplicate durante l esportazione dei dati nella DataTable
---

## **Possibili Scenari di Utilizzo**

A volte l'utente si trova di fronte al problema delle colonne duplicate durante l'esportazione dei dati dal foglio di lavoro nella tabella dati. DataTable non può avere colonne duplicate, quindi le colonne duplicate devono essere rinominate prima di poter esportare i dati del foglio di lavoro nella tabella dati. Aspose.Cells può rinominare automaticamente le colonne duplicate in base alla strategia da te specificata con la proprietà [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy). Se si specifica [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit, le colonne verranno rinominate come colonna1, colonna2, colonna3, ecc. e se si specifica [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, le colonne verranno rinominate come colonnaA, colonnaB, colonnaC, ecc.

## **Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro**

Il seguente codice di esempio aggiunge alcuni dati nelle prime tre colonne del foglio di lavoro, ma tutte le colonne hanno lo stesso nome, ovvero *Persone*. Poi esporta i dati dal foglio di lavoro nella tabella dati specificando la strategia [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter. Poi stampa i nomi delle colonne della tabella dati generata da Aspose.Cells. La seguente schermata mostra la tabella dati con i dati esportati nel visualizzatore. Come si può vedere, le colonne duplicate sono state rinominate in PersoneA, PersoneB ecc.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Output della console**

Ecco l'output della console del codice di esempio sopra come riferimento.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
