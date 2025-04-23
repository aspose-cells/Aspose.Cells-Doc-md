---
title: Leeres Blatt ausgeben, wenn nichts gedruckt werden muss
type: docs
weight: 90
url: /de/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn das Blatt leer ist, wird Aspose.Cells für Python via .NET beim Exportieren des Arbeitsblatts in ein Bild nichts ausgeben. Dieses Verhalten können Sie ändern, indem Sie die [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print)-Eigenschaft verwenden. Wenn Sie sie auf **true** setzen, wird die leere Seite gedruckt.

## **Leeres Blatt ausgeben, wenn nichts gedruckt werden muss**

Der folgende Beispielcode erstellt die leere Arbeitsmappe mit einem leeren Arbeitsblatt und rendert das leere Arbeitsblatt nach dem Setzen der [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print)-Eigenschaft als **true** in ein Bild. Daraus resultiert die Generierung einer leeren Seite, da nichts gedruckt werden muss, wie im folgenden Bild zu sehen ist.

![todo:image_alt_text](1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

