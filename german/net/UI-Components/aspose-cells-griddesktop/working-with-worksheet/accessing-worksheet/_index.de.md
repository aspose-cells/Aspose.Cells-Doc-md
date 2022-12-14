---
title: Zugriff auf das Arbeitsblatt
type: docs
weight: 10
url: /de/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Ein Arbeitsblatt ist ein integraler Bestandteil einer Excel-Datei. Tatsächlich besteht eine Excel-Datei aus einem oder mehreren Arbeitsblättern. Jedes Arbeitsblatt kann nur aus bis zu 65.536 Zeilen und 256 Spalten bestehen. Es ist das Arbeitsblatt, das Daten in einer Excel-Datei enthält.

Aspose.Cells.GridDesktop kann vorhandene und neue Excel-Dateien erstellen und manipulieren, daher gibt es natürlich eine Möglichkeit, mit Aspose.Cells.GridDesktop auf Arbeitsblätter zuzugreifen. In diesem Thema wird erläutert, wie.

{{% /alert %}} 
## **Verwenden des Arbeitsblattindex**
Entwickler können auf eine Instanz eines beliebigen Arbeitsblatts zugreifen, indem sie den Arbeitsblattindex eines beliebigen Arbeitsblatts verwenden, wie unten im Beispiel gezeigt. Dieser Ansatz eignet sich gut zum Durchlaufen einer Reihe von Arbeitsblättern in einer Excel-Datei.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Verwenden des Arbeitsblattnamens**
Wenn der Name des Arbeitsblatts bekannt ist, kann auf ein Arbeitsblatt unter Verwendung seines Namens wie unten gezeigt zugegriffen werden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Zugriff auf ein aktives Arbeitsblatt**
Es ist möglich, dass eine Excel-Datei mehr als ein Arbeitsblatt enthält. Das eine Htat, an dem ein Benutzer arbeitet, wird als aktives Arbeitsblatt bezeichnet. Es ist möglich, auf das aktive Blatt zuzugreifen.

Um auf ein aktives Arbeitsblatt zuzugreifen, bietet Aspose.Cells.GridDesktop zwei Ansätze:
### **Verwenden der AcriveSheetIndex-Eigenschaft**
Eine Möglichkeit, mit dem Aspose.Cells.GridDesktop-Steuerelement auf ein aktives Arbeitsblatt zuzugreifen, besteht darin, die ActiveSheetIndex-Eigenschaft des GridDesktop-Steuerelements zu verwenden. Mit dieser Eigenschaft ist es möglich, den Index des aktiven Arbeitsblatts im Steuerelement Aspose.Cells.GridDesktop abzurufen. Dann kann dieser Index verwendet werden, um wie unten gezeigt auf herkömmliche Weise auf das Arbeitsblatt zuzugreifen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Verwenden der GetActiveWorksheet-Methode**
Der andere Ansatz besteht darin, die GetActiveWorksheet-Methode des GridDesktop-Steuerelements aufzurufen. Diese Methode stellt einen Verweis auf das Arbeitsblatt bereit, das derzeit im Aspose.Cells.GridDesktop-Steuerelement aktiv ist, wie unten gezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
