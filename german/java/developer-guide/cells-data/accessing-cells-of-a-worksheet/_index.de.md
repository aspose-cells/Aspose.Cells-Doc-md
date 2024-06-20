---
title: Zugriff auf Zellen eines Arbeitsblatts
type: docs
weight: 10
url: /de/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die im Wesentlichen in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Bestandteil eines Arbeitsblatts, der dazu verwendet wird, das gesamte Arbeitsblatt als Abfolge von Zeilen und Spalten aufzubauen. Bevor wir versuchen, Daten aus einem Arbeitsblatt abzurufen, müssten wir Zugriff auf seine Zellen erhalten. Daher werden wir in diesem Thema einige grundlegende Ansätze zur Laufzeitzugriff auf Arbeitsblattzellen erörtern, die Aspose.Cells verwendet.

{{% /alert %}} 
## **Zugriff auf Zellen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung, die alle Zellen in der Arbeitsmappe repräsentiert.

Wir können die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung verwenden, um auf Zellen in einer Arbeitsmappe zuzugreifen. Aspose.Cells bietet verschiedene grundlegende Ansätze zum Zugriff auf Zellen:

1. [Verwenden des Zellennamens](/cells/de/java/accessing-cells-of-a-worksheet/).
1. [Verwenden von Zeilen- und Spaltenindex](/cells/de/java/accessing-cells-of-a-worksheet/).
### **Verwendung des Zellnamens**
Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie ihren Zellennamen an die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) übergeben.

Wenn Sie eine leere Arbeitsmappe zu Beginn erstellen, ist die Anzahl der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung null. Wenn Sie diesen Ansatz zum Zugriff auf eine Zelle verwenden, wird überprüft, ob diese Zelle in der Sammlung existiert oder nicht. Wenn ja, wird das Zellenobjekt in der Sammlung zurückgegeben, andernfalls wird ein neues [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-Objekt erstellt, das Objekt der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung hinzugefügt und dann das Objekt zurückgegeben. Dieser Ansatz ist der einfachste Weg, auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber er ist langsamer als andere Ansätze.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Verwenden von Zeilen- und Spaltenindex der Zelle**
Entwickler können auf eine beliebige bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) übergeben.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Verwandte Artikel**
{{% alert color="primary" %}} 

- [Benannte Bereiche](/cells/de/java/named-ranges/)

{{% /alert %}} 
## **Zugriff auf den maximalen Anzeigebereich des Arbeitsblatts**
Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich - der Bereich der Zellen zwischen der ersten und der letzten Zelle mit Inhalt - ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

Sie können den maximalen Anzeigebereich einer Arbeitsmappe mit [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange) abrufen.

Im folgenden Bild ist der ausgewählte maximale Anzeigebereich der Arbeitsmappe A1:G15.

**Anzeige des maximalen Anzeigebereichs dieser Arbeitsmappe** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

Der folgende Beispielcode veranschaulicht, wie auf die Eigenschaft [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange) zugegriffen wird. Der Code erzeugt die folgende Ausgabe.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
