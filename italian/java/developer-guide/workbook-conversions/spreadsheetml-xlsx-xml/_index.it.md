---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /it/java/spreadsheetml-xlsx-xml/
---

## **Informazioni su SpreadsheetML**
SpreadsheetML è un nome per una famiglia di formati basati su XML per documenti di fogli di calcolo. Ci sono diverse versioni di SpreadsheetML:

1. La versione 2003 di SpreadsheetML è stata introdotta in Microsoft Word 2003. SpreadsheetML è stato un passo significativo di Microsoft verso l'apertura del formato del documento.
1. [Office Open XML](https://it.wikipedia.org/wiki/Office_Open_XML) (OOXML) è il nuovo formato basato su XML introdotto nelle applicazioni di Microsoft Office 2007. Office Open XML è un formato contenitore per diversi linguaggi di markup basati su XML specializzati. La versione 2007 di SpreadsheetML è il linguaggio di markup utilizzato da Microsoft Office Excel 2007 per memorizzare i suoi documenti.
1. Microsoft Excel 2010 e versioni successive memorizzano i documenti nella versione 2010 di SpreadsheetML come definito nello standard aggiornato di OOXML.
## **SpreadsheetML in Aspose.Cells**
Ci sono tre "versioni" di SpreadsheetML disponibili:

|**SpreadsheetML "Versione"**|**Standard/Specifiche applicabili**|**Supportato in Aspose.Cells for Java**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://it.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Sì|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Sì|
|Microsoft Excel 2010 e versioni successive|OOXML ISO/IEC DIS 29500|Sì|
I documenti OOXML SpreadsheetML arrivano più spesso come file XLSX, che sono pacchetti ZIP. Oltre a XLSX, Aspose.Cells fornisce un ampio supporto per il caricamento, il salvataggio e la conversione dei documenti SpreadsheetML. Un'implementazione così completa è possibile perché Aspose.Cells è stato progettato con la struttura dei documenti di Microsoft Excel in mente (e si sa che SpreadsheetML imita la rappresentazione interna dei documenti di Microsoft Excel).

**Un documento XLSX generato da Aspose.Cells e aperto in Microsoft Excel** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_1.png)

**Il documento XLSX generato da Aspose.Cells segue la Convenzione per l'Impacchettamento Aperto e può essere aperto in un'applicazione in grado di gestire file ZIP** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_2.png)
## **OOXML è aperto, perché usare Aspose.Cells?**
È vero che la tecnologia Office Open XML consente di costruire applicazioni di generazione e elaborazione documenti utilizzando solo le classi XML senza affidarsi a librerie di terze parti come Aspose.Cells. Tuttavia, crediamo fortemente che sia comunque molto vantaggioso utilizzare Aspose.Cells quando si deve lavorare con documenti OOXML, piuttosto che lavorare tramite XML o altre librerie.

La specifica OOXML è lunga diverse migliaia di pagine. Essere aperti e standard non significa essere semplici. Per elaborare o generare correttamente documenti OOXML bisogna investire nello studio del formato.

Oltre a semplificare l'elaborazione corretta e la generazione di documenti validi, Aspose.Cells fornisce le seguenti importanti funzionalità che non si avrebbero lavorando direttamente con file OOXML tramite XML o altre librerie di terze parti:

- Conversioni di qualità tra molti popolari formati Excel, inclusa la conversione in PDF, HTML, TIFF e stampa.
- Capacità di creare documenti da frammenti, da uno o più documenti, mentre si fondono automaticamente i dati tramite formattazione stilistica, grafici e grafici.
- Funzioni di alto livello, come l'importazione di dati da diverse origini di dati tra cui Array, ArrayList, DataTable, DataColumn, DataGrid, DataView e DataReader o l'esportazione di dati per riempire un DataTable o un Array con una sola riga di codice.
- Motore di calcolo delle formule robusto che supporta quasi tutte le funzioni standard e avanzate di Microsoft Excel.

Considerate il seguente esempio. Alcune celle contengono il testo “Hello World” in grassetto. Ora immaginate di dover scrivere un programma che cerca tutte le frasi “Hello World” nel foglio di lavoro e le sostituisce con “Goodbye Earth”.
## **Un frammento di un Documento Office Open XML**
**XML**

{{< highlight csharp >}}

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

Implementare anche una semplice operazione di ricerca e sostituzione in un documento Office Open XML è difficile.

**Il nostro consiglio:** ricordate che aperto e standard non significa semplice e utilizzate Aspose.Cells.
