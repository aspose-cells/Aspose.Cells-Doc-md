---
title: Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel
type: docs
weight: 40
url: /it/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Possibili scenari di utilizzo**
A volte gli sviluppatori vogliono impedire l'inclusione di Excel*.bidone* file delle impostazioni della stampante nei file XLSX salvati. I file delle impostazioni della stampante si trovano in*“[file "radice"]\xl\impostazioni stampante”*. Questo documento spiega come rimuovere le impostazioni della stampante esistenti utilizzando le API Aspose.Cells.
## **Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel**
Aspose.Cells consente di rimuovere le impostazioni della stampante esistenti specificate per diversi fogli nel file Excel. Il codice di esempio riportato di seguito illustra come rimuovere le impostazioni della stampante esistenti per tutti i fogli di lavoro della cartella di lavoro. Si prega di vedere il suo[esempio di file Excel](45056023.xlsx), [file Excel di output](45056024.xlsx)output della console e uno screenshot per riferimento.
## **Immagine dello schermo**
![cose da fare:immagine_alt_testo](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Uscita console**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
