---
title: Esporta dati Excel in DataTable e controlla il tipo di dati misti
type: docs
weight: 280
url: /it/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Scopri come esportare dati Excel in DataTable e controllare il tipo di dati misti tramite Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Possibili scenari di utilizzo**
 Se una colonna contiene dati di vario tipo, il programma genererà un'eccezione di tipo durante l'esportazione dei dati in un DataTable. Per l'esportazione della tabella dati, per impostazione predefinita, Aspose.Cells valuta il tipo di dati per i valori in base al primo valore (cella) nella colonna. Pertanto, se il valore è numerico, significa che il tipo di dati della colonna sarà numerico, il che è ragionevole. Se il primo valore è un numero ma nella colonna sono presenti dati o valori alfanumerici, è necessario assegnare un tipo di dati stringa. Per affrontarlo, si prega di utilizzare[Sovraccarico ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) che comporta[Opzioni ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) e prova a impostare[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Attributo booleano su "true" se una colonna contiene sia valori numerici che stringhe per sfuggire all'errore.

##  **Esporta dati Excel in DataTable e controlla il tipo di dati misti**

 L'esempio seguente spiega l'uso di[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)proprietà per esportare i dati Excel nella tabella dati. Si prega di consultare il[file Excel di esempio](sample.xlsx), il relativo screenshot e l'output della console come riferimento.

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Immagine dello schermo**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Uscita della console**

Di seguito è riportato l'output di debug della console del codice di esempio riportato sopra

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
