---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /it/net/spreadsheetml-xlsx-xml/
---
## **Circa SpreadsheetML**
SpreadsheetML è il nome di una famiglia di formati basati su XML per i fogli di calcolo. Esistono diverse versioni di SpreadsheetML:

1. SpreadsheetML versione 2003 è stata introdotta in Microsoft Word 2003. SpreadsheetML è stato un passo significativo di Microsoft verso l'apertura del formato del documento.
1. [Office OpenXML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) è il nuovo formato basato su XML introdotto nelle applicazioni Microsoft Office 2007. Office Open XML è un formato contenitore per diversi linguaggi di markup specializzati basati su XML. SpreadsheetML versione 2007 è il linguaggio di markup utilizzato da Microsoft Office Excel 2007 per archiviare i propri documenti.
1. Microsoft Excel 2010 memorizza i documenti nella SpreadsheetML versione 2010 come definito nello standard OOXML aggiornato.
## **SpreadsheetML nel Aspose.Cells**
Sono disponibili tre "versioni" di SpreadsheetML:

|**SpreadsheetML “Versione”**|**Norma/Specifica applicabile**|**Supportato in Aspose.Cells for .NET**|
|:- |:- |:- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|sì|
|Microsoft Excel 2007|[OOXMLECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|sì|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|sì|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|sì|
I documenti OOXML SpreadsheetML vengono spesso come file XLSX, che sono pacchetti ZIP. Oltre a XLSX. Aspose.Cells fornisce un ampio supporto per il caricamento, il salvataggio e la conversione di documenti SpreadsheetML. Tale implementazione onnicomprensiva è possibile perché Aspose.Cells è stato progettato tenendo presente la struttura dei documenti Excel Microsoft (e SpreadsheetML è noto per imitare la rappresentazione interna dei documenti Excel Microsoft).
### **OOXML è aperto, perché usare Aspose.Cells?**
È vero che la tecnologia Office Open XML consente di creare applicazioni di elaborazione e generazione di documenti utilizzando solo le classi XML senza fare affidamento su librerie di terze parti come Aspose.Cells. Tuttavia, crediamo fermamente che sia ancora molto vantaggioso utilizzare Aspose.Cells quando si dispone per gestire documenti OOXML, piuttosto che lavorare tramite XML o altre librerie.

La specifica OOXML è lunga diverse migliaia di pagine. Essere aperti e standard non significa essere semplici. Per elaborare o generare correttamente documenti OOXML è necessario investire nell'apprendimento del formato.

Oltre a semplificare l'elaborazione corretta e la generazione di documenti validi, Aspose.Cells fornisce le seguenti importanti funzionalità che non avresti lavorando con file OOXML direttamente tramite XML o altre librerie di terze parti:

- Conversioni di qualità tra molti formati Excel popolari, inclusa la conversione in PDF, HTML, TIFF e la stampa.
- Capacità di costruire documenti da frammenti, da uno o più documenti, unendo automaticamente i dati mediante formattazione stilistica, grafici e grafici.
- Funzioni di alto livello, come l'importazione di dati da diverse origini dati tra cui Array, ArrayList, DataTable, DataColumn, DataGrid, DataView e DataReader o l'esportazione di dati per riempire un DataTable o un Array con una sola riga di codice.
- Robusto motore di calcolo delle formule che supporta quasi tutte le funzioni Excel standard e avanzate Microsoft.

Considera il seguente esempio. Alcune celle contengono il testo "Hello World" in grassetto. Ora immagina di dover scrivere un programma che cerchi tutte le frasi "Hello World" nel foglio di lavoro e le sostituisca con "Goodbye Earth".
### **Un frammento di un documento Office Open XML**
**XML**

{{< highlight "csharp" >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}


L'implementazione anche di una semplice operazione di ricerca e sostituzione in un documento Office Open XML è difficile. Il nostro consiglio: ricorda che aperto e standard non significa semplice, e usa lo Aspose.Cells.
