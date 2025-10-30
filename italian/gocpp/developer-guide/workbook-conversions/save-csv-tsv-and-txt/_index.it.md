---
title: Converti Excel in CSV, TSV e Txt con Golang tramite C++
linktitle: Salva come CSV, TSV e Txt
type: docs
weight: 40
url: /it/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Converti facilmente i file Excel in formati CSV, TSV e TXT usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile convertire file Excel, ODS, JSON e altri formati in CSV, TSV e TXT.

{{% /alert %}}

## **Salvataggio Workbook in formato testo o CSV**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un intero workbook in formato testo. Carica il workbook di origine che potrebbe essere un file di fogli di calcolo Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

Puoi modificare lo stesso esempio per salvare il file in formato CSV. Per impostazione predefinita, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) è una virgola, quindi non specificare un separatore se si salva in formato CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Salvataggio file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Argomenti avanzati**
- [Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV](/cells/it/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV](/cells/it/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
