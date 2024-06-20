---
title: Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen
type: docs
weight: 5000
url: /de/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

Wenn Sie leere Spalten und Zeilen in einer Tabelle löschen, werden die Verweise in anderen Tabellen ungültig. Wenn Sie dieses Verhalten vermeiden möchten und möchten, dass diese Verweise auf die aktuelle Tabelle in anderen Tabellen ebenfalls aktualisiert werden, verwenden Sie bitte die [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)-Eigenschaft und setzen Sie sie auf **true**.

{{% /alert %}}

## **Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen**

Bitte beachten Sie den folgenden Beispielcode und seine Konsolenausgabe. Die Zelle E3 in der zweiten Tabelle hat eine Formel =Blatt1!C3, die sich auf die Zelle C3 in der ersten Tabelle bezieht. Wenn Sie [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) auf **true** setzen, wird diese Formel aktualisiert und wird zu =Blatt1!A1, wenn Sie leere Spalten und Zeilen in der ersten Tabelle löschen. Wenn Sie jedoch [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) auf **false** setzen, bleibt die Formel in Zelle E3 der zweiten Tabelle =Blatt1!C3 und wird ungültig.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) auf **true** gesetzt wurde.

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

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) auf **false** gesetzt wurde. Wie Sie sehen können, wurde die Formel in Zelle E3 der zweiten Tabelle nicht aktualisiert und ihr Zellenwert beträgt jetzt 0 statt 4, was ungültig ist.

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
