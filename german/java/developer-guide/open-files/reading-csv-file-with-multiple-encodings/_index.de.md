﻿---
title: Lesen von CSV-Datei mit mehreren Codierungen
type: docs
weight: 140
url: /de/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Mit Aspose.Cells können Sie solche CSV-Dateien laden und in andere Formate konvertieren, z. B. PDF oder XLSX.

{{% /alert %}} 

 Aspose.Cells stellt die Methode TxtLoadOptions.setMultiEncoded() bereit, die Sie festlegen müssen**wahr** um Ihre CSV-Datei mit mehreren Kodierungen richtig zu laden.

 Der folgende Screenshot zeigt eine Beispieldatei CSV, die zwei Zeilen enthält. Die erste Zeile ist drin**ANSI** Codierung und die zweite Zeile ist in**Unicode** Codierung

**Eingabedatei** 

![todo: Bild_alt_Text](reading-csv-file-with-multiple-encodings_1.png)

Der folgende Screenshot zeigt die XLSX-Datei, die aus der obigen CSV-Datei konvertiert wurde, ohne die TxtLoadOptions.setMultiEncoded()-Methode auf true zu setzen. Wie Sie sehen können, wurde der Unicode-Text nicht richtig konvertiert.

**Ausgabedatei 1: keine Anpassung an Mehrfachcodierung vorgenommen** 

![todo: Bild_alt_Text](reading-csv-file-with-multiple-encodings_2.png)

Der folgende Screenshot zeigt die XSLX-Datei, die aus der obigen Datei CSV konvertiert wurde, nachdem die Methode TxtLoadOptions.setMultiEncoded() auf true gesetzt wurde. Wie Sie sehen können, wird der Unicode-Text jetzt korrekt konvertiert.

**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt** 

![todo: Bild_alt_Text](reading-csv-file-with-multiple-encodings_3.png)

Unten ist der Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

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
