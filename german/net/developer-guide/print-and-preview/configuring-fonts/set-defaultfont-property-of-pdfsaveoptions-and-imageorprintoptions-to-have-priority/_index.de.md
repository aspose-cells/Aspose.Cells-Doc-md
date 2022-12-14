---
title: Setzen Sie die DefaultFont-Eigenschaft von PdfSaveOptions und ImageOrPrintOptions auf Priorität
type: docs
weight: 30
url: /de/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Mögliche Nutzungsszenarien**

 Beim Einstellen der**Standardschriftart** Eigentum von**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** und**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, könnten Sie erwarten, dass das Speichern in PDF oder Bild diese DefaultFont auf den gesamten Text in einer Arbeitsmappe mit einer fehlenden (nicht installierten) Schriftart festlegen würde.

 Im Allgemeinen versucht Aspose.Cells beim Speichern als PDF oder Bild zuerst, die Standardschriftart von Workbook festzulegen (dh Workbook.DefaultStyle.Font). Wenn die Standardschriftart der Arbeitsmappe den Text immer noch nicht richtig anzeigen/rendern kann, versucht Aspose.Cells, mit der Schriftart zu rendern, die im DefaultFont-Attribut in angegeben ist**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

Um Ihrer Erwartung gerecht zu werden, haben wir eine boolesche Eigenschaft namens "**CheckWorkbookDefaultFont** " in**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . Sie können es einstellen**FALSCH**um die Standardschriftart der Arbeitsmappe zu deaktivieren oder die zu lassen**Standardschriftart** Einstellung in**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** Vorrang haben.

## **Legen Sie die DefaultFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions fest**

 Der folgende Beispielcode öffnet eine Excel-Datei. Die A1-Zelle (im ersten Arbeitsblatt) hat einen Text, der auf „Schriftarttext für die Weihnachtszeit“ eingestellt ist. Der Schriftartname ist „Christmas Time Personal Use“, der nicht auf dem Gerät installiert ist. Legen wir fest***Standardschriftart*** Attribut von**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** zu "Times New Roman". Wir setzen auch**CheckWorkbookDefaultFont** Boolesche Eigenschaft zu**"FALSCH"** Dadurch wird sichergestellt, dass der Text der A1-Zelle mit der Schriftart „Times New Roman“ gerendert wird und nicht die Standardschriftart der Arbeitsmappe („Calibri“ in diesem Fall) verwenden sollte. Der Code rendert das erste Arbeitsblatt in die Bildformate PNG und TIFF. Es wird schließlich in ein PDF-Dateiformat gerendert.

{{% alert color="primary" %}}

 Der Standardwert von***CheckWorkbookDefaultFont*** Attribut ist**Stimmt**.

{{% /alert %}}

 Dies ist der Screenshot der[Vorlagendatei](49446913.xlsx) im Beispielcode verwendet.

![todo: Bild_alt_Text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach dem Festlegen von**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**Eigentum an "Times New Roman".

![todo: Bild_alt_Text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 Siehe Ausgabe[TIFF](48496672.tiff) Bild nach dem Einstellen der**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**Eigentum an "Times New Roman".

Siehe Ausgabe[Pdf](48496673.pdf)Datei nach dem Festlegen der**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**Eigentum an "Times New Roman".

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
