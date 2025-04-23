---
title: Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen
type: docs
weight: 700
url: /de/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

Wenn Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen, werden die Verweise in anderen Arbeitsblättern ungültig. Wenn Sie dieses Verhalten vermeiden und diese Verweise ebenfalls aktualisieren möchten, verwenden Sie die [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) und setzen Sie sie auf **true**.

{{% /alert %}} 
## **Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen**
Bitte sehen Sie sich den folgenden Beispielcode und dessen Konsolenausgabe an. Die Zelle E3 im zweiten Arbeitsblatt enthält eine Formel =Sheet1!C3, die auf die Zelle C3 im ersten Arbeitsblatt verweist. Wenn Sie die [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigenschaft auf **true** setzen, wird diese Formel aktualisiert und zu =Sheet1!A1, wenn Sie leere Spalten und Zeilen im ersten Arbeitsblatt löschen. Wenn Sie jedoch die [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigenschaft auf **false** setzen, bleibt die Formel in Zelle E3 des zweiten Arbeitsblatts =Sheet1!C3 und wird ungültig.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Konsolenausgabe**
Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn die [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigenschaft auf **true** gesetzt wurde.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn die [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigenschaft auf **false** gesetzt wurde. Wie Sie sehen können, wird die Formel in Zelle E3 des zweiten Arbeitsblatts nicht aktualisiert und ihr Zellwert ist nun 0 anstelle von 4, was ungültig ist.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
