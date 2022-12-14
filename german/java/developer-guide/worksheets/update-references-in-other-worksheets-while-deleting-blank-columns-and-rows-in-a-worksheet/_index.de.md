---
title: Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen
type: docs
weight: 700
url: /de/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Wenn Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen, werden seine Verweise in anderen Arbeitsblättern ungültig. Wenn Sie dieses Verhalten vermeiden möchten und möchten, dass diese Referenzen ebenfalls aktualisiert werden, verwenden Sie bitte die[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) und stelle es ein**Stimmt**.

{{% /alert %}} 
## **Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen**
 Bitte sehen Sie sich den folgenden Beispielcode und seine Konsolenausgabe an. Die Zelle E3 im zweiten Arbeitsblatt hat eine Formel =Sheet1!C3, die sich auf Zelle C3 im ersten Arbeitsblatt bezieht. Wenn Sie wollen[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigentum als**Stimmt** , wird diese Formel aktualisiert und wird zu =Sheet1!A1, wenn leere Spalten und Zeilen im ersten Arbeitsblatt gelöscht werden. Allerdings, wenn Sie festlegen[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigentum als**FALSCH**, bleibt die Formel in Zelle E3 des zweiten Arbeitsblatts =Sheet1!C3 und wird ungültig.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Konsolenausgabe**
Dies ist die Konsolenausgabe des obigen Beispielcodes when[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigenschaft wurde festgelegt als**Stimmt**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Dies ist die Konsolenausgabe des obigen Beispielcodes when[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) Eigenschaft wurde festgelegt als**FALSCH**. Wie Sie sehen können, wird die Formel in Zelle E3 des zweiten Arbeitsblatts nicht aktualisiert und ihr Zellenwert ist jetzt 0 statt 4, was ungültig ist.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
