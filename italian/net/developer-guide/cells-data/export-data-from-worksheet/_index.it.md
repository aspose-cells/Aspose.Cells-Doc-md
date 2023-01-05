---
title: Esporta dati dal foglio di lavoro in .NET
linktitle: Esporta dati dal foglio di lavoro
type: docs
weight: 180
url: /it/net/export-data-from-worksheet/
description: Questo articolo spiega come esportare o importare dati dal foglio di lavoro in datatable utilizzando C#.
---
## Panoramica

Questo articolo spiega come esportare i dati del foglio di lavoro in DataTable utilizzando C#. Copre i seguenti argomenti

_Formato_: **Eccellere**
- [C# Da Excel a DataTable](#csharp-excel-to-datatable)
- [C# Converti Excel in DataTable](#csharp-convert-excel-to-datatable)
- [C# Importa Excel in DataTable](#csharp-import-excel-to-datatable)
- [C# Esporta in DataTable da Excel](#csharp-export-to-datatable-from-excel)

_Formato_: **XLS**
- [C# XLS a DataTable](#csharp-xls-to-datatable)
- [C# Converti XLS in DataTable](#csharp-convert-xls-to-datatable)
- [C# Importa XLS in DataTable](#csharp-import-xls-to-datatable)
- [C# Esporta in DataTable da XLS](#csharp-export-to-datatable-from-xls)

_Formato_: **XLSX**
- [C# XLSX a DataTable](#csharp-xlsx-to-datatable)
- [C# Converti XLSX in DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importa XLSX in DataTable](#csharp-import-xlsx-to-datatable)
- [C# Esporta in DataTable da XLSX](#csharp-export-to-datatable-from-xlsx)

_Formato_: **ODS**
- [C# ODS a DataTable](#csharp-ods-to-datatable)
- [C# Converti ODS in DataTable](#csharp-convert-ods-to-datatable)
- [C# Importa ODS in DataTable](#csharp-import-ods-to-datatable)
- [C# Esporta in DataTable da ODS](#csharp-export-to-datatable-from-ods)

## **C# Esporta dati Excel**

{{% alert color="primary" %}}

Questo articolo discute alcune tecniche di esportazione dei dati a cui gli sviluppatori hanno accesso tramite Aspose.Cells.

{{% /alert %}}

## **Esporta dati dal foglio di lavoro**

 Aspose.Cells non solo facilita ai suoi utenti l'importazione di dati in fogli di lavoro da fonti di dati esterne, ma consente anche loro di esportare i dati del foglio di lavoro in un[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Come lo sappiamo[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) è la parte di ADO.NET e viene utilizzato per contenere i dati. Una volta che i dati sono stati archiviati in un file[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , può essere utilizzato in qualsiasi modo in base alle esigenze degli utenti. Gli sviluppatori possono anche archiviare questi dati (memorizzati in[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) direttamente in un database, se lo desiderano. Quindi, possiamo vedere che diventa più facile per gli sviluppatori manipolare i dati del foglio di lavoro se vengono esportati in un file[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Esportazione di dati in DataTable utilizzando Aspose.Cells**

 Gli sviluppatori possono facilmente esportare i dati del proprio foglio di lavoro in un file[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) oggetto chiamando entrambi[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) o[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe. Entrambi i metodi vengono utilizzati in diversi scenari, descritti di seguito in modo più dettagliato.

## **Colonne contenenti dati fortemente tipizzati**

Sappiamo che un foglio di calcolo memorizza i dati come una sequenza di righe e colonne. Se tutti i valori nelle colonne di un foglio di lavoro sono fortemente tipizzati (ciò significa che tutti i valori in una colonna devono avere lo stesso tipo di dati), allora possiamo esportare il contenuto del foglio di lavoro chiamando il[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) Il metodo accetta i seguenti parametri per esportare i dati del foglio di lavoro come[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)oggetto:

- **Numero di riga**, verrà esportato il numero di riga dei dati della prima cella.
- **Numero di colonna**, il numero di colonna della prima cella da cui verranno esportati i dati.
- **Numero di righe**, il numero di righe da esportare.
- **Numero di colonne**, il numero di colonne da esportare.
- **Esporta i nomi delle colonne** , una proprietà booleana che indica se i dati nella prima riga del foglio di lavoro devono essere esportati come nomi di colonna del[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)o no.

_Passaggi: esportazione dei dati in DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Passi:</em> Da Excel a DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Passi:</em> XLS a DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Passi:</em> XLSX a DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Passi:</em> ODS a DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Passi:</em> Converti Excel in DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Passi:</em>Converti XLS in DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Passi:</em>Converti XLSX in DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Passi:</em>Converti ODS in DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Passi:</em> Importa Excel in DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Passi:</em> Importa XLS in DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Passi:</em> Importa XLSX in DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Passi:</em> Importa ODS in DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Passi:</em> Esporta in DataTable da Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Passi:</em> Esporta in DataTable da XLS a C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Passi:</em> Esporta in DataTable da XLSX a C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Passi:</em> Esporta in DataTable da ODS a C#</strong></a>

_Passaggi del codice:_

1.  Carica il tuo file Excel[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook/) oggetto.
   - [Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook/) l'oggetto può caricare formati di file Excel, ad esempio XLS, XLSX, XLSM, ODS ecc.
 3. Accedi al primo[Foglio di lavoro](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) nel file Excel.
 4. Scegli la tua area di esportazione, ad esempio 7 righe e 2 colonne a partire dalla prima cella di**Tabella dati**.
 5. Usa[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) metodo per esportare i dati in DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Colonne contenenti dati non fortemente tipizzati**

 Se tutti i valori nelle colonne di un foglio di lavoro non sono fortemente tipizzati (ciò significa che i valori in una colonna possono avere i diversi tipi di dati), allora possiamo esportare il contenuto del foglio di lavoro chiamando il metodo[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)Il metodo accetta lo stesso set di parametri di quello di[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)metodo per esportare i dati del foglio di lavoro come a[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)oggetto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Esporta intervallo con flag per ignorare il nome della colonna**

 dati di un intervallo possono essere esportati in[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) dove è disponibile un flag per saltare la riga di intestazione nei dati esportati. Il codice seguente esporta un intervallo di dati in[**Tabella dati**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) con un argomento[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) che contiene[**Esporta nome colonna**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) bandiera. È impostato su**VERO** se le informazioni di intestazione sono presenti, quindi non saranno incluse nei dati e impostate su**falso** se non è presente alcuna intestazione e tutte le righe devono essere considerate come dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Argomenti avanzati**
- [Esporta i dati di Excel in DataTable senza alcuna formattazione](/cells/it/net/export-excel-data-to-datatable-without-any-formatting/)
- [Esporta il valore stringa HTML di Cells nel DataTable](/cells/it/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Esporta i dati delle righe visibili dal foglio di lavoro](/cells/it/net/export-visible-rows-data-from-worksheet/)
- [Ignora le colonne nascoste durante l'esportazione dei dati del foglio di lavoro nella tabella dati](/cells/it/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Rinomina automaticamente le colonne duplicate durante l'esportazione dei dati del foglio di lavoro](/cells/it/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
