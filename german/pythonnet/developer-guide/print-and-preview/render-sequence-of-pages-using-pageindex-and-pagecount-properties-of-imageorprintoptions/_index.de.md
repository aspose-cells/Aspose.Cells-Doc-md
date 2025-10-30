---
title: Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions
type: docs
weight: 110
url: /de/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Mögliche Verwendungsszenarien**

Sie können eine Sequenz von Seiten Ihrer Excel-Datei mit Aspose.Cells für Python via .NET in Bilder rendern, indem Sie die Eigenschaften [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) und [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count) verwenden. Diese Eigenschaften sind nützlich, wenn Ihre Arbeitsmappe sehr viele Seiten enthält, z.B. Tausende, und Sie nur einige davon rendern möchten. Dies spart nicht nur die Verarbeitungszeit, sondern auch den Speicherverbrauch des Renderings.

## **Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](55541781.xlsx) und rendert nur die Seiten 4, 5, 6 und 7 unter Verwendung der Eigenschaften [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) und [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Hier sind die von dem Code generierten gerenderten Seiten.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
