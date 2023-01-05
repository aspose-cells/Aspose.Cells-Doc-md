---
title: Conversione
type: docs
weight: 30
url: /it/net/conversion/
---
Aspose.Cells caratteristica unica che fornisce flessibilità nelle conversioni di versione senza influire sul lavoro.
SaveFormat è un'enumerazione che può convertire il documento nelle estensioni indicate di seguito nella tabella.

|**Nome del membro** |**Valore** |**Descrizione** |
|:- |:- |:- |
|CSV |1 | Rappresenta un file CSV.|
| Xlsx|6 | Rappresenta un file xlsx.|
| XLSM|7 | Rappresenta un file xlsm che abilita le macro.|
| XLTX|8 | Rappresenta un file xltx.|
| Xltm|9 | Rappresenta un file xltm che abilita le macro.|
|TabDelimited |11 | Rappresenta un file di testo delimitato da tabulazioni.|
| HTML|12 | Rappresenta un file html.|
| HTML|17 | Rappresenta un file mhtml.|
|ODS |14 | Rappresenta un file ods.|
| Excel97To2003|5 | Rappresenta un file xls Excel97-2003.|
|SpreadsheetML |15 | Rappresenta un file xml di Excel 2003.|
| Xlsb|16 | Rappresenta un file xlsb.|
| Auto|0 | Se si salva il file sul disco, il formato del file corrisponde all'estensione del nome del file.<br>Se si salva il file nello stream, il formato del file è xlsx.|
| Sconosciuto|255 | Rappresenta un formato non riconosciuto, non può essere salvato.|
| PDF|13 | Rappresenta un file Pdf.|
|XPS |20 | Rappresenta un file XPS.|
|TIFF |21 | Rappresenta un file TIFF.|
|SVG |22 | Rappresenta un file SVG.|
| dif|30 | Formato di scambio dati.|
Di seguito è riportato uno snippet di codice che mostra la conversione da xls a xlsx, puoi farlo anche viceversa

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
