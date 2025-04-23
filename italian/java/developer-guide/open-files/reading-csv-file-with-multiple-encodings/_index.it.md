---
title: Lettura di file CSV con codifiche multiple
type: docs
weight: 140
url: /it/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

A volte, il file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc.). Aspose.Cells ti consente di caricare tali file CSV e convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}} 

Aspose.Cells fornisce il metodo TxtLoadOptions.setMultiEncoded(), che è necessario impostare su **true** per caricare correttamente il file CSV con più codifiche.

La seguente schermata mostra un file CSV di esempio che contiene due righe. La prima riga è in codifica **ANSI** e la seconda riga è in codifica **Unicode**.

**File di input** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

La seguente schermata mostra il file XLSX convertito dal file CSV precedente senza impostare il metodo TxtLoadOptions.setMultiEncoded() su true. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

**File di output 1: nessuna sistemazione per la codifica multipla** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

La seguente schermata mostra il file XSLX convertito dal file CSV precedente dopo aver impostato il metodo TxtLoadOptions.setMultiEncoded() su true. Come puoi vedere, il testo Unicode è stato convertito correttamente.

**File di output 2: IsMultiEncoded è impostato su true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

Di seguito è riportato il codice di esempio che converte il precedente file CSV nel formato XLSX correttamente.

**Java**

{{< highlight csharp >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
