---
title: Esporta dati dalla scheda in .NET
linktitle: Esporta dati dalla scheda
type: docs
weight: 180
url: /it/net/export-data-from-worksheet/
description: Questo articolo spiega come esportare o importare dati dalla scheda in un datatable usando C#.
keywords: C# Esporta dati dalla scheda, C# Esporta dati in DataTable, Colonne contenenti dati fortemente tipizzati, Colonne contenenti dati non fortemente tipizzati, C# Esporta intervallo con flag per saltare il nome della colonna, C# Come esportare intervallo con intestazione.
---

## Panoramica

Questo articolo spiega come esportare i dati della tua scheda in DataTable usando C#. Copre i seguenti argomenti

_Formato_: **Excel**
- [C# Excel in DataTable](#csharp-excel-to-datatable)
- [C# Converti Excel in DataTable](#csharp-convert-excel-to-datatable)
- [C# Importa Excel in DataTable](#csharp-import-excel-to-datatable)
- [C# Esporta in DataTable da Excel](#csharp-export-to-datatable-from-excel)

_Formato_: **XLS**
- [C# XLS in DataTable](#csharp-xls-to-datatable)
- [C# Converti XLS in DataTable](#csharp-convert-xls-to-datatable)
- [C# Importa XLS in DataTable](#csharp-import-xls-to-datatable)
- [C# Esporta in DataTable da XLS](#csharp-export-to-datatable-from-xls)

_Formato_: **XLSX**
- [C# XLSX in DataTable](#csharp-xlsx-to-datatable)
- [C# Convertire XLSX in DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importare XLSX in DataTable](#csharp-import-xlsx-to-datatable)
- [C# Esportare in DataTable da XLSX](#csharp-export-to-datatable-from-xlsx)

Formato: ODS
- [C# ODS in DataTable](#csharp-ods-to-datatable)
- [C# Convertire ODS in DataTable](#csharp-convert-ods-to-datatable)
- [C# Importare ODS in DataTable](#csharp-import-ods-to-datatable)
- [C# Esportare in DataTable da ODS](#csharp-export-to-datatable-from-ods)

## **Come esportare dati di Excel usando C#**

{{% alert color="primary" %}}

Questo articolo discute alcune tecniche di esportazione dati a cui i programmatori possono accedere tramite Aspose.Cells.

{{% /alert %}}

## **Come esportare dati dalla scheda**

Aspose.Cells non solo facilita ai suoi utenti l'importazione di dati nelle schede da fonti di dati esterne, ma consente loro anche di esportare i dati della scheda in un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). Come sappiamo che [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) fa parte di ADO.NET e viene utilizzato per contenere dati. Una volta che i dati sono memorizzati in un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), possono essere utilizzati in qualsiasi modo in base alle esigenze degli utenti. I programmatori possono anche memorizzare questi dati (memorizzati in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) direttamente in un database se lo desiderano. Quindi, possiamo vedere che diventa più facile per i programmatori manipolare i dati della scheda se vengono esportati in un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Come esportare dati in DataTable usando Aspose.Cells**

I programmatori possono facilmente esportare i dati della scheda in un oggetto [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) chiamando il metodo [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) o [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Entrambi i metodi vengono utilizzati in scenari diversi, che vengono discussi più in dettaglio di seguito.

## **Colonne contenenti dati fortemente tipizzati**

Sappiamo che un foglio di calcolo memorizza i dati come una sequenza di righe e colonne. Se tutti i valori nelle colonne di una scheda sono fortemente tipizzati (cioè tutti i valori in una colonna devono avere lo stesso tipo di dati) allora possiamo esportare il contenuto della scheda chiamando il metodo [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Il metodo [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) richiede i seguenti parametri per esportare i dati della scheda come un oggetto [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8):

- Numero riga, il numero di riga del primo dato della cella che sarà esportato.
- Numero colonna, il numero di colonna della prima cella da cui verranno esportati i dati.
- Numero di righe, il numero di righe da esportare.
- Numero di colonne, il numero di colonne da esportare.
- **Esporta nomi delle colonne**, una proprietà booleana che indica se i dati nella prima riga del foglio di lavoro dovrebbero essere esportati come nomi delle colonne del [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) o meno.

_Passaggi: Esportare i dati in un DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Passaggi:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Passaggi:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Passaggi:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Passaggi:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Passaggi:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Passaggi:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Passaggi:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Passaggi:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Passaggi:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Passaggi:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Passaggi:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Passaggi:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Passaggi:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Passaggi:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Passaggi:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Passaggi:</em> Export to DataTable from ODS in C#</strong></a>

_Passaggi del codice:_

1. Carica il tuo file Excel nell'oggetto [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/).
   - L'oggetto [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) può caricare formati file Excel come ad esempio XLS, XLSX, XLSM, ODS etc.
3. Accedi al primo [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) nel file Excel.
4. Scegli la tua area di esportazione come ad esempio 7 righe e 2 colonne a partire dalla prima cella del **DataTable**.
5. Utilizza il metodo [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) per esportare i dati in un DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Colonne contenenti dati non fortemente tipizzati**

Se tutti i valori nelle colonne di un foglio di lavoro non sono fortemente tipizzati (cioè i valori in una colonna possono avere tipi di dati diversi), allora possiamo esportare il contenuto del foglio di lavoro chiamando il metodo [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Il metodo [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) richiede lo stesso insieme di parametri del metodo [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) per esportare i dati del foglio di lavoro come oggetto [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Come esportare un intervallo con intestazione**

I dati da un intervallo possono essere esportati in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) dove è disponibile un flag per saltare la riga di intestazione nei dati esportati. Il codice seguente esporta un intervallo di dati in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) con un argomento [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) che contiene il flag [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname). Viene impostato su **true** se le informazioni dell'intestazione sono presenti, quindi non verranno incluse nei dati e impostato su **false** se non c'è intestazione e tutte le righe devono essere considerate come dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Argomenti avanzati**
- [Esporta dati Excel in DataTable senza alcuna formattazione](/cells/it/net/export-excel-data-to-datatable-without-any-formatting/)
- [Esporta il valore della stringa HTML delle celle nel DataTable](/cells/it/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Esporta dati righe visibili dal foglio di lavoro](/cells/it/net/export-visible-rows-data-from-worksheet/)
- [Ignora le colonne nascoste durante l'esportazione dei dati del foglio di lavoro nel DataTable](/cells/it/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro](/cells/it/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
{{< app/cells/assistant language="csharp" >}}
