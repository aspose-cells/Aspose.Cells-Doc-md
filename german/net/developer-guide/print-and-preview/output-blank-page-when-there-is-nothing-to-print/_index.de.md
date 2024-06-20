---
title: Leeres Blatt ausgeben, wenn nichts gedruckt werden muss
type: docs
weight: 90
url: /de/net/output-blank-page-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn das Blatt leer ist, druckt Aspose.Cells nichts, wenn Sie das Arbeitsblatt in ein Bild exportieren. Sie können dieses Verhalten ändern, indem Sie die [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint)-Eigenschaft verwenden. Wenn Sie es auf **true** setzen, wird die leere Seite gedruckt.

## **Leeres Blatt ausgeben, wenn nichts gedruckt werden muss**

Der folgende Beispielcode erstellt die leere Arbeitsmappe mit einem leeren Arbeitsblatt und rendert das leere Arbeitsblatt nach dem Setzen der [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint)-Eigenschaft als **true** in ein Bild. Daraus resultiert die Generierung einer leeren Seite, da nichts gedruckt werden muss, wie im folgenden Bild zu sehen ist.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
