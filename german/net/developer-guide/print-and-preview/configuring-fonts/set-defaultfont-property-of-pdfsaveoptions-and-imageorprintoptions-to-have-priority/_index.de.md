---
title: StandardFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions Priorität einräumen
type: docs
weight: 30
url: /de/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Mögliche Verwendungsszenarien**

Beim Setzen der **DefaultFont**-Eigenschaft von [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) könnten Sie erwarten, dass beim Speichern als PDF oder Bild dieser DefaultFont auf den gesamten Text in einer Arbeitsmappe angewendet wird, der eine fehlende (nicht installierte) Schriftart hat.

Im Allgemeinen wird Aspose.Cells beim Speichern als PDF oder Bild zuerst versuchen, die Standard-Schriftart der Arbeitsmappe festzulegen (d.h. Workbook.DefaultStyle.Font). Wenn die Standard-Schriftart der Arbeitsmappe den Text immer noch nicht korrekt anzeigen/rendern kann, wird Aspose.Cells versuchen, mit der in der DefaultFont-Eigenschaft in [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) angegebenen Schriftart zu rendern.

Um Ihren Erwartungen gerecht zu werden, haben wir eine boolesche Eigenschaft mit dem Namen "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). Sie können es auf **false** setzen, um das Versuches der Verwendung der Standard-Schriftart der Arbeitsmappe zu deaktivieren oder die Einstellung **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) die Priorität zu haben lassen.

## **StandardFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions festlegen**

Der folgende Beispielscode öffnet eine Excel-Datei. Die Zelle A1 (im ersten Arbeitsblatt) hat einen Text, der auf "Weihnachtszeit Schrifttext" festgelegt ist. Der Schriftname ist "Weihnachtszeit Persönlich Gebrauch", der nicht auf dem Gerät installiert ist. Wir setzen  ***DefaultFont***-Attribut von [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) auf "Times New Roman". Wir setzen auch die Boolesche Eigenschaft **CheckWorkbookDefaultFont** auf **"false"**, was sicherstellt, dass der Text der Zelle A1 mit der Schriftart "Times New Roman" gerendert wird und nicht die Standardschriftart der Arbeitsmappe verwendet wird (in diesem Fall "Calibri"). Der Code rendert das erste Arbeitsblatt in PNG- und TIFF-Bildformate. Schließlich wird in ein PDF-Dateiformat gerendert.

{{% alert color="primary" %}}

Der Standardwert des ***CheckWorkbookDefaultFont***-Attributs ist **true**.

{{% /alert %}}

Dies ist der Screenshot der im Beispielcode verwendeten [Vorlagendatei](49446913.xlsx).

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach Einstellung der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) auf "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Sehen Sie sich das Ausgabe-TIFF-Bild nach dem Setzen der [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)-Eigenschaft auf "Times New Roman" an.

Sehen Sie sich die Ausgabepdf-Datei nach dem Setzen der [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)-Eigenschaft auf "Times New Roman" an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
