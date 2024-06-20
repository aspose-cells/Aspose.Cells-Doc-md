---
title: Esportare i dati di Excel in DataTable e controllare il tipo di dati misti
type: docs
weight: 280
url: /it/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Scopri come esportare i dati di Excel in DataTable e controllare il tipo di dati misti tramite l API Aspose.Cells for .NET.
keywords: Esportare i dati di Excel in DataTable e controllare il tipo di dati misti, Esportare i dati del foglio di lavoro in DataTable e controllare il tipo di dati misti, Esportare i dati in DataTable e controllare il tipo di dati misti, Esportare i dati del foglio di lavoro in DataTable e controllare il tipo di dati misti.
---

## **Possibili Scenari di Utilizzo**
Se una colonna contiene dati di vari tipi, il programma genererà un'eccezione di tipo durante l'esportazione dei dati in una DataTable. Per l'esportazione della tabella dei dati, per impostazione predefinita, Aspose.Cells valuta il tipo di dati per i valori in base al primo valore (cella) nella colonna. Quindi, se il valore è un numero, significa che il tipo di dati della colonna sarebbe numerico, il che è ragionevole. Se il primo valore è un numero ma ci sono dati alfanumerici o valori nella colonna, dovrebbe essere assegnato un tipo di dati stringa. Per far fronte a ciò, si prega di utilizzare il sovraccarico [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) che coinvolge [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) e prova a impostare l'attributo booleano [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) su "true" se una colonna ha sia valori numerici che stringa per evitare errori.

## **Esportare i dati di Excel in DataTable e controllare il tipo di dati misti**

Il seguente esempio spiega l'uso della proprietà [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) per esportare i dati di Excel in una tabella. Si prega di consultare il [file Excel di esempio](sample.xlsx), la relativa schermata e l'output della console per un riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Screenshot**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Output della console**

Di seguito è riportato l'output di debug della console del codice di esempio precedente

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
