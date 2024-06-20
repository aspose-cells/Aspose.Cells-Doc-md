---
title: Daten in einem Bereich suchen und ersetzen
type: docs
weight: 60
url: /de/java/search-and-replace-data-in-a-range/
description: In diesem Artikel wird erklärt, wie Sie in Excel mithilfe von Java Code in einem Bereich nach Daten suchen und diese ersetzen können.
keywords: java Daten in Excel suchen und ersetzen, java Daten in Excel suchen, java Daten in einem Bereich suchen und ersetzen, java Daten in einem Bereich suchen, java Daten in einem Bereich suchen, java Daten in einem Bereich suchen, java Daten in Excel suchen, java Daten in einem Bereich suchen, Daten in Excel mit Java suchen und ersetzen, Daten in einem Bereich mit Java suchen und ersetzen, Daten in einem Bereich mit Java suchen und ersetzen, Daten in einem Bereich mit Java suchen und ersetzen
---

{{% alert color="primary" %}}

Manchmal müssen Sie nach bestimmten Daten in einem Bereich suchen und diese ersetzen, wobei Werte außerhalb des gewünschten Bereichs ignoriert werden. Aspose.Cells ermöglicht es Ihnen, die Suche auf einen bestimmten Bereich zu beschränken. Dieser Artikel erklärt wie.

{{% /alert %}}

Aspose.Cells bietet die Methode [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) zum Angeben eines Bereichs beim Suchen nach Daten.

Angenommen, Sie möchten nach dem Text **"search"** suchen und ihn im Bereich **E3:H6** durch **"ersetzen"** ersetzen. Im unten stehenden Screenshot ist der Text "search" in mehreren Zellen zu sehen, aber wir möchten ihn nur in einem bestimmten Bereich, hier gelb markiert, ersetzen.

**Eingabedatei**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Nach der Ausführung des Codes sieht die Ausgabedatei wie unten aus. Alle "search"-Texte im Bereich wurden durch "ersetzen" ersetzt.

**Ausgabedatei**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Verwandte Artikel

- [Daten suchen oder suchen](/cells/de/java/find-or-search-data/)
