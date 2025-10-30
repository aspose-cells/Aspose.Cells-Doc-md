---
title: StandardFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions Priorität einräumen
type: docs
weight: 30
url: /de/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Mögliche Verwendungsszenarien**

Beim Setzen der **DefaultFont**-Eigenschaft von [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) könnten Sie erwarten, dass beim Speichern als PDF oder Bild dieser DefaultFont auf den gesamten Text in einer Arbeitsmappe angewendet wird, der eine fehlende (nicht installierte) Schriftart hat.

Generell versucht Aspose.Cells für Python via .NET beim Speichern in PDF oder Bild zuerst, die Standardschriftart des Arbeitsbuchs (d.h. Workbook.DefaultStyle.Font) zu setzen. Falls die Standardschriftart des Arbeitsbuchs immer noch Text nicht richtig anzeigen oder rendern kann, versucht Aspose.Cells für Python via .NET, mit der Schriftart zu rendern, die gegen das DefaultFont-Attribut in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) gesetzt ist.

Um Ihre Erwartungen zu erfüllen, haben wir eine boolesche Eigenschaft namens "**check_workbook_default_font**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Sie können sie auf **false** setzen, um das Verwenden der Standardschriftart des Arbeitsbuchs zu deaktivieren, oder die Einstellung **default_font** in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) priorisieren.

## **StandardFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions festlegen**

Das folgende Beispiel öffnet eine Excel-Datei. Die Zelle A1 (im ersten Arbeitsblatt) enthält den Text "Christmas Time Font text". Der Schriftname ist "Christmas Time Personal Use", der nicht auf dem Computer installiert ist. Wir setzen das Attribut ***default_font*** von [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) auf "Times New Roman". Außerdem setzen wir die boolesche Eigenschaft **check_workbook_default_font** auf **"false"**, damit der Text in A1 mit "Times New Roman" gerendert wird und nicht die Standardschriftart des Arbeitsbuchs (in diesem Fall "Calibri") verwendet wird. Der Code rendert das erste Arbeitsblatt in PNG- und TIFF-Bilder. Schließlich wird in das PDF-Format exportiert.

{{% alert color="primary" %}}

Der Standardwert des ***CheckWorkbookDefaultFont***-Attributs ist **true**.

{{% /alert %}}

Dies ist der Screenshot der im Beispielcode verwendeten [Vorlagendatei](49446913.xlsx).

![todo:image_alt_text](1.png)

Dies ist das Ausgabe-PNG-Bild nach Einstellung der Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) auf "Times New Roman".

![todo:image_alt_text](2.png)

Sehen Sie sich das Ausgabe-TIFF-Bild nach dem Setzen der [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)-Eigenschaft auf "Times New Roman" an.

Sehen Sie sich die Ausgabepdf-Datei nach dem Setzen der [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/)-Eigenschaft auf "Times New Roman" an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
