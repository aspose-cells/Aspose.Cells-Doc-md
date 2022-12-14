---
title: Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo in formato CSV
type: docs
weight: 100
url: /it/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Possibili scenari di utilizzo**

A volte, il tuo file Excel o CSV ha colonne o righe vuote iniziali. Ad esempio, considera questa linea

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV di questo tipo in Microsoft Excel, Microsoft Excel scarta queste righe e colonne vuote iniziali.

 Per impostazione predefinita, Aspose.Cells non elimina le colonne e le righe vuote iniziali durante il salvataggio, ma se si desidera rimuoverle proprio come fa Excel Microsoft, Aspose.Cells fornisce**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** proprietà. Si prega di impostarlo su**VERO**e quindi tutte le righe e le colonne vuote iniziali verranno scartate durante il salvataggio.

{{% alert color="primary" %}}

 Prima del rilascio di Aspose.Cells for .NET 20.4, il valore predefinito di**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** era**falso** . Dalla versione 20.4, il valore predefinito di**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** è**VERO.**

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo in formato CSV**

 Il codice di esempio seguente carica il file[file excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote iniziali. Prima salva il file excel in formato CSV senza alcuna modifica e poi si imposta**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** proprietà a**VERO** e lo salva di nuovo. Lo screenshot mostra il[file excel di origine](sampleTrimBlankColumns.xlsx), [output file CSV senza ritaglio](outputWithoutTrimBlankColumns.csv), e il[output file CSV con ritaglio](outputTrimBlankColumns.csv).

![cose da fare:immagine_alt_testo](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
