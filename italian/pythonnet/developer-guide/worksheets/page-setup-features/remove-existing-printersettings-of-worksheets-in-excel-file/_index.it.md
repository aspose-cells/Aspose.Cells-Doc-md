---
title: Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel
type: docs
weight: 60
url: /it/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In questo articolo, imparerai come rimuovere le impostazioni della stampante esistenti del foglio di lavoro all interno del file Excel attraverso l oggetto Impostazione Pagina in modo programmato con il codice di esempio usando la Libreria Python Excel Aspose.Cells.
keywords: Libreria Python Excel, Rimuovi le impostazioni di stampa del foglio di lavoro in Python, Rimuovi le impostazioni di stampa del foglio di lavoro in Excel di Python.
---

## **Possibili Scenari di Utilizzo**
A volte gli sviluppatori vogliono impedire ad Excel di includere file *.bin* di impostazioni di stampa nei file XLSX salvati. I file delle impostazioni di stampa si trovano in *"[file "root"]\xl\printerSettings".* Questo documento spiega come rimuovere le impostazioni di stampante esistenti utilizzando le API Aspose.Cells per Python via .NET.

## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**
Aspose.Cells per Python via .NET ti permette di rimuovere le impostazioni di stampa esistenti specificate per fogli diversi nel file Excel. Il seguente codice di esempio illustra come rimuovere le impostazioni di stampa esistenti per tutti i fogli di lavoro nel workbook. Si prega di vedere il [file Excel di esempio](45056020.xlsx), [file Excel di output](45056021.xlsx), output della console e lo screenshot per un riferimento.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
