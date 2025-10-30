---
title: Converti il file Excel in formato PDF compatibile con PDFA 1a con Golang tramite C++
linktitle: Converti il file Excel nel formato PDF compatibile con PDFA 1a
type: docs
weight: 130
url: /it/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Impara come convertire file Excel in formato PDF/A 1a conforme usando Aspose.Cells con Golang tramite C++.
---

## **Possibili Scenari di Utilizzo**

PDF/A è una versione unica di PDF progettata per la preservazione a lungo termine dei documenti. PDF/A è una versione standardizzata ISO del formato Portable Document Format (PDF) che include tutti i font utilizzati nel documento all’interno del file PDF. PDF/A si differenzia dal PDF proibendo funzionalità come il collegamento di font (anziché l’incorporamento dei font) e la crittografia. Aspose.Cells ti permette di salvare i file Excel in file PDF conformi a PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, e PDF/A-3u sono supportati). Questo argomento descrive come salvare il workbook Excel in un file PDF conforme a PDF/A (PDF/A-1a).

## **Convertire file Excel nel formato PDF compatibile con PDF/A-1a**

Gli sviluppatori possono usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) per impostare attributi diversi per la conversione. Impostare proprietà diverse della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) ti dà il controllo su impostazioni di stampa, font, sicurezza e compressione per il PDF di output. La proprietà più importante è [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) che permette di salvare i file Excel come file PDF conformi a PDF/A.

Il seguente codice di esempio spiega come convertire un file Excel nel formato PDF compatibile con PDF/A-1a. Consulta il suo [output PDF](outputCompliancePdfA1a.pdf) e uno screenshot a scopo di riferimento.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
