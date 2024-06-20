---
title: Conversione
type: docs
weight: 30
url: /it/net/conversion/
---

Caratteristica unica di Aspose.Cells che offre flessibilità nelle conversioni di versione senza influenzare il lavoro.
SaveFormat è un'enumerazione che può convertire il documento nelle estensioni elencate di seguito nella tabella.

|**Nome Membro** |**Valore** |**Descrizione** |
| :- | :- | :- |
|CSV |1 |Rappresenta un file CSV. |
|Xlsx |6 |Rappresenta un file xlsx. |
|Xlsm |7 |Rappresenta un file xlsm che abilita i macro. |
|Xltx |8 |Rappresenta un file xltx. |
|Xltm |9 |Rappresenta un file xltm che abilita i macro. |
|TabDelimited |11 |Rappresenta un file di testo delimitato da tabulazioni. |
|Html |12 |Rappresenta un file html. |
|MHtml |17 |Rappresenta un file mhtml. |
|ODS |14 |Rappresenta un file ods. |
|Excel97To2003 |5 |Rappresenta un file xls di Excel 97-2003. |
|SpreadsheetML |15 |Rappresenta un file xml di Excel 2003. |
|Xlsb |16 |Rappresenta un file xlsb. |
|Auto |0 |Se si salva il file su disco, il formato del file corrisponde all'estensione del nome del file. <br>Se si salva il file nello stream, il formato del file è xlsx. |
|Unknown |255 |Rappresenta un formato non riconosciuto, non può essere salvato. |
|Pdf |13 |Rappresenta un file Pdf. |
|XPS |20 |Rappresenta un file XPS. |
|TIFF |21 |Rappresenta un file TIFF. |
|SVG |22 |Rappresenta un file SVG. |
|Dif |30 |Formato di interscambio dati. |
Di seguito è riportato un frammento di codice che mostra la conversione da xls a xlsx, è possibile farlo anche al contrario

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
