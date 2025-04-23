---
title: Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel
type: docs
weight: 60
url: /it/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In questo articolo imparerai come rimuovere le impostazioni della stampante esistenti del foglio di lavoro all interno del file Excel attraverso l oggetto Impostazione pagina in modo programmato con codice di esempio utilizzando API C# o libreria .NET.
keywords: rimuovere le impostazioni della stampante del foglio di lavoro c#, rimuovere le impostazioni della stampante del foglio di lavoro di excel c#
---

## **Possibili Scenari di Utilizzo**
A volte gli sviluppatori vogliono impedire ad Excel di includere i file *.bin* delle impostazioni della stampante nei file XLSX salvati. I file delle impostazioni della stampante si trovano in *"[file "root"]\xl\printerSettings".* Questo documento spiega come rimuovere le impostazioni della stampante esistenti utilizzando le API di Aspose.Cells.
## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**
Aspose.Cells consente di rimuovere le impostazioni della stampante esistenti specificate per fogli diversi nel file Excel. Il seguente codice di esempio illustra come rimuovere le impostazioni della stampante esistenti per tutti i fogli di lavoro nella cartella di lavoro. Si prega di consultare il [file Excel di esempio](45056020.xlsx), [file Excel di output](45056021.xlsx), output della console e la schermata per un riferimento.
## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Output della console**
{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
