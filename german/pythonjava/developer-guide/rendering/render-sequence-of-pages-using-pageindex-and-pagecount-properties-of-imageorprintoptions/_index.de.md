---
title: Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions
type: docs
weight: 10
url: /de/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions**
Sie können eine Sequenz von Seiten Ihrer Excel-Datei mit Aspose.Cells und den Eigenschaften [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) und [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) zu Bildern rendern. Diese Eigenschaften sind nützlich, wenn Ihre Arbeitsmappe viele Seiten hat, z.B. Tausende, und Sie nur einige davon rendern möchten. Dadurch wird nicht nur die Verarbeitungszeit gespart, sondern auch der Speicherverbrauch des Renderprozesses.

Der folgende Beispielcode lädt die Muster-Excel-Datei und rendert nur die Seiten 4, 5, 6 und 7 unter Verwendung der Eigenschaften [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) und [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount). Nachstehend sind die Bilder der gerenderten Seiten, die vom Beispielcode generiert wurden.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
