---
title: Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel
type: docs
weight: 60
url: /it/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In questo articolo, imparerai come rimuovere le impostazioni della stampante esistenti del foglio di lavoro all’interno del file Excel tramite l’oggetto Page Setup con esempi di codice usando Aspose.Cells per Python Excel Library.
keywords: Libreria Python Excel, rimuovere impostazioni stampante del foglio di lavoro, rimuovere impostazioni stampante di un foglio Excel tramite Python.
---

## **Possibili Scenari di Utilizzo**
A volte gli sviluppatori vogliono evitare che Excel includa i file *.bin* delle impostazioni della stampante nei file XLSX salvati. I file delle impostazioni della stampante si trovano sotto *“[file "root"]\xl\printerSettings”.* Questo documento spiega come rimuovere le impostazioni esistenti della stampante usando le API Aspose.Cells per Python via .NET.

## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**
Aspose.Cells per Python via .NET permette di rimuovere le impostazioni della stampante esistenti specificate per diversi fogli nel file Excel. Il seguente esempio di codice illustra come rimuovere le impostazioni della stampante per tutti i fogli di lavoro nel workbook. Consulta anche il [file Excel di esempio](45056020.xlsx), [file Excel di output](45056021.xlsx), output sulla console e lo screenshot per riferimento.

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
