---
title: Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel
type: docs
weight: 40
url: /it/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Possibili Scenari di Utilizzo**
A volte gli sviluppatori vogliono impedire ad Excel di includere i file * .bin * delle impostazioni della stampante nei file XLSX salvati. I file di impostazioni della stampante si trovano sotto * "[file \"root\"] \ xl \ printerSettings" *. Questo documento spiega come rimuovere le impostazioni della stampante esistenti utilizzando le API di Aspose.Cells.
## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**
Aspose.Cells consente di rimuovere le impostazioni della stampante esistenti specificate per diversi fogli nel file Excel. Il seguente codice di esempio illustra come rimuovere le impostazioni della stampante esistenti per tutti i fogli di lavoro nel documento. Si prega di vedere il suo [file Excel di esempio](45056023.xlsx), [file Excel di output](45056024.xlsx), l'output della console e uno screenshot a titolo di riferimento.
## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Output della console**
{{< highlight java >}}

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
{{< app/cells/assistant language="java" >}}
