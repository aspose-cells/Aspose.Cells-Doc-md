---
title: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 140
url: /de/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht es Ihnen, solche CSV-Dateien zu laden und in andere Formate wie z.B. PDF oder XLSX zu konvertieren.

{{% /alert %}} 

Aspose.Cells bietet die Methode TxtLoadOptions.setMultiEncoded(), die Sie auf true setzen müssen, um Ihre CSV-Datei mit mehreren Codierungen korrekt zu laden.

Im folgenden Screenshot ist eine Beispiels-CSV-Datei dargestellt, die zwei Zeilen enthält. Die erste Zeile ist in ANSI-Codierung und die zweite Zeile ist in Unicode-Codierung.

**Eingabedatei** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

Im folgenden Screenshot ist die XLSX-Datei dargestellt, die aus der obigen CSV-Datei ohne Setzen der Methode TxtLoadOptions.setMultiEncoded() auf true konvertiert wurde. Wie Sie sehen können, wurde der Unicode-Text nicht korrekt konvertiert.

Ausgabedatei 1: keine Berücksichtigung für mehrere Codierungen 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

Im folgenden Screenshot ist die XSLX-Datei dargestellt, die aus der obigen CSV-Datei nach Setzen der Methode TxtLoadOptions.setMultiEncoded() auf true konvertiert wurde. Wie Sie sehen können, wird der Unicode-Text jetzt korrekt konvertiert.

Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

Im Folgenden finden Sie den Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

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
