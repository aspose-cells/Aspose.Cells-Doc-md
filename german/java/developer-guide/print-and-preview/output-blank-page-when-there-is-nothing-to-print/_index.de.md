---
title: Leeres Blatt ausgeben, wenn nichts gedruckt werden muss
type: docs
weight: 80
url: /de/java/output-blank-page-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn das Blatt leer ist, wird Aspose.Cells nichts drucken, wenn Sie ein Arbeitsblatt in ein Bild exportieren. Sie können dieses Verhalten ändern, indem Sie die [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) Eigenschaft verwenden. Wenn Sie es auf **true** setzen, wird die leere Seite gedruckt.

## **Leeres Blatt ausgeben, wenn nichts gedruckt werden muss**

Der folgende Beispielcode erstellt die leere Arbeitsmappe, die ein leeres Arbeitsblatt enthält, und rendert das leere Arbeitsblatt als Bild, nachdem die [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) Eigenschaft auf **true** gesetzt wurde. Folglich wird die leere Seite generiert, da nichts zu drucken ist, wie Sie unten sehen können.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
