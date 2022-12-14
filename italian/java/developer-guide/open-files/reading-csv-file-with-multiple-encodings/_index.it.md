---
title: Lettura di file CSV con codifiche multiple
type: docs
weight: 140
url: /it/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7 ecc.). Aspose.Cells consente di caricare tali file CSV e di convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}} 

 Aspose.Cells fornisce il metodo TxtLoadOptions.setMultiEncoded(), che è necessario impostare su**VERO** per caricare correttamente il tuo file CSV con più codifiche.

 Lo screenshot seguente mostra un file CSV di esempio che contiene due righe. La prima riga è dentro**ANSI** encoding e la seconda riga è in**Unicode** codifica

**File di input** 

![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_1.png)

Lo screenshot seguente mostra il file XLSX convertito dal precedente file CSV senza impostare il metodo TxtLoadOptions.setMultiEncoded() su true. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

**File di output 1: nessuna sistemazione fatta per codifiche multiple** 

![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_2.png)

Lo screenshot seguente mostra il file XSLX convertito dal precedente file CSV dopo aver impostato il metodo TxtLoadOptions.setMultiEncoded() su true. Come puoi vedere, il testo Unicode è ora convertito correttamente.

**File di output 2: IsMultiEncoded è impostato su true** 

![cose da fare:immagine_alt_testo](reading-csv-file-with-multiple-encodings_3.png)

Di seguito è riportato il codice di esempio che converte correttamente il file CSV sopra nel formato XLSX.

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
