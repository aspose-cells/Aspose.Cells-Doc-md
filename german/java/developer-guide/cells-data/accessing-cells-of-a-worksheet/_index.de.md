---
title: Zugriff auf Cells eines Arbeitsblatts
type: docs
weight: 10
url: /de/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Wir wissen, dass alle Arbeitsblätter Daten enthalten können, die grundsätzlich in Zellen gespeichert sind (aus denen ein Arbeitsblatt besteht). Eine Zelle ist ein grundlegender Teil eines Arbeitsblatts, der verwendet wird, um das gesamte Arbeitsblatt als eine Folge von Zeilen und Spalten zu erstellen. Bevor wir versuchen, auf Daten aus einem Arbeitsblatt zuzugreifen, müssen wir Zugriff auf seine Zellen erhalten. Daher werden wir in diesem Thema einige grundlegende Ansätze für den Zugriff auf Arbeitsblattzellen zur Laufzeit mit Aspose.Cells erörtern.

{{% /alert %}} 
## **Zugriff auf Cells**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Wir können die verwenden[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung, um auf Zellen in einem Arbeitsblatt zuzugreifen. Aspose.Cells bietet verschiedene grundlegende Ansätze für den Zugriff auf Zellen:

1. [Zellname verwenden](/cells/de/java/accessing-cells-of-a-worksheet/).
1. [Zeilen- und Spaltenindex verwenden](/cells/de/java/accessing-cells-of-a-worksheet/).
### **Verwendung des Namens Cell**
 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie ihren Zellennamen an die übergeben[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung der[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse.

 Wenn Sie zu Beginn ein leeres Arbeitsblatt erstellen, wird die Anzahl der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung ist null. Wenn Sie diesen Ansatz verwenden, um auf eine Zelle zuzugreifen, wird überprüft, ob diese Zelle in der Sammlung vorhanden ist oder nicht. Wenn ja, gibt es das Zellobjekt in der Sammlung zurück, andernfalls erstellt es ein neues[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Objekt, fügt das Objekt dem hinzu[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung und gibt dann das Objekt zurück. Dieser Ansatz ist der einfachste Weg, um auf die Zelle zuzugreifen, wenn Sie mit Microsoft Excel vertraut sind, aber er ist langsamer als andere Ansätze.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Verwenden des Zeilen- und Spaltenindex von Cell**
 Entwickler können auf jede bestimmte Zelle zugreifen, indem sie die Indizes ihrer Zeile und Spalte an die übergeben[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung der[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse.

Dieser Ansatz funktioniert genauso wie der erste Ansatz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **In Verbindung stehende Artikel**
{{% alert color="primary" %}} 

- [Benannte Bereiche](/cells/de/java/named-ranges/)

{{% /alert %}} 
## **Zugriff auf den maximalen Anzeigebereich des Arbeitsblatts**
Aspose.Cells ermöglicht Entwicklern den Zugriff auf den maximalen Anzeigebereich eines Arbeitsblatts. Der maximale Anzeigebereich – der Zellbereich zwischen der ersten und der letzten Zelle mit Inhalt – ist nützlich, wenn Sie den gesamten Inhalt eines Arbeitsblatts in einem Bild kopieren, auswählen oder anzeigen müssen.

 Mit können Sie auf den maximalen Anzeigebereich eines Arbeitsblatts zugreifen[Arbeitsblatt.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

In der folgenden Abbildung ist der maximale Anzeigebereich des ausgewählten Arbeitsblatts A1:G15.

**Zeigt den maximalen Anzeigebereich dieses Arbeitsblatts an** 

![todo: Bild_alt_Text](accessing-cells-of-a-worksheet_1.png)

 Der folgende Beispielcode veranschaulicht den Zugriff auf die[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)Eigentum. Der Code generiert die folgende Ausgabe.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
