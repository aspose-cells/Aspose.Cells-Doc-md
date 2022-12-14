---
title: Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel
type: docs
weight: 60
url: /it/net/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Possibili scenari di utilizzo**
A volte gli sviluppatori vogliono impedire l'inclusione di Excel*.bidone* file delle impostazioni della stampante nei file XLSX salvati. I file delle impostazioni della stampante si trovano in*“[file "root"]\xl\impostazioni stampante”.* Questo documento spiega come rimuovere le impostazioni della stampante esistenti utilizzando le API Aspose.Cells.
## **Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel**
Aspose.Cells consente di rimuovere le impostazioni della stampante esistenti specificate per diversi fogli nel file Excel. Il codice di esempio riportato di seguito illustra come rimuovere le impostazioni della stampante esistenti per tutti i fogli di lavoro della cartella di lavoro. Si prega di vedere il suo[esempio di file Excel](45056020.xlsx), [file Excel di output](45056021.xlsx), l'output della console e lo screenshot per riferimento.
## **Immagine dello schermo**
![cose da fare:immagine_alt_testo](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Uscita console**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
