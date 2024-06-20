---
title: Zugriff auf Arbeitsblatt
type: docs
weight: 10
url: /de/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop, Arbeitsblatt
description: Dieser Artikel stellt vor, wie man mit Arbeitsblättern in GridDesktop arbeitet.
---

{{% alert color="primary" %}} 

Ein Arbeitsblatt ist ein integraler Bestandteil einer Excel-Datei. Tatsächlich besteht eine Excel-Datei aus einem oder mehreren Arbeitsblättern. Jedes Arbeitsblatt kann nur aus bis zu 65.536 Zeilen und 256 Spalten bestehen. Das Arbeitsblatt enthält die Daten in einer Excel-Datei.

Aspose.Cells.GridDesktop kann vorhandene Excel-Dateien erstellen und bearbeiten, daher gibt es natürlich eine Möglichkeit, Arbeitsblätter mit Aspose.Cells.GridDesktop zu öffnen. Dieser Artikel behandelt dieses Thema.

{{% /alert %}} 
## **Verwendung des Arbeitsblattindexes**
Entwickler können eine Instanz eines beliebigen Arbeitsblatts anhand des Arbeitsblattindexes eines beliebigen gewünschten Arbeitsblatts zugreifen, wie im folgenden Beispiel gezeigt. Dieser Ansatz ist gut geeignet, um durch eine Anzahl von Arbeitsblättern in einer Excel-Datei zu iterieren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Verwendung des Arbeitsblattnamens**
Wenn der Name des Arbeitsblatts bekannt ist, ist es möglich, auf ein Arbeitsblatt anhand seines Namens wie folgend gezeigt zuzugreifen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Zugriff auf ein aktives Arbeitsblatt**
Es ist möglich, dass eine Excel-Datei mehr als ein Arbeitsblatt hat. Dasjenige, an dem ein Benutzer arbeitet, wird als aktives Arbeitsblatt bezeichnet. Es ist möglich, auf das aktive Blatt zuzugreifen.

Um auf ein aktives Arbeitsblatt zuzugreifen, bietet Aspose.Cells.GridDesktop zwei Ansätze:
### **Verwendung der AcriveSheetIndex-Eigenschaft**
Eine Möglichkeit, auf ein aktives Arbeitsblatt unter Verwendung der Aspose.Cells.GridDesktop-Steuerung zuzugreifen, besteht darin, die ActiveSheetIndex-Eigenschaft der GridDesktop-Steuerung zu verwenden. Unter Verwendung dieser Eigenschaft ist es möglich, den Index des aktiven Arbeitsblatts in der Aspose.Cells.GridDesktop-Steuerung zu erhalten. Dann kann dieser Index verwendet werden, um auf das Arbeitsblatt in herkömmlicher Weise zuzugreifen, wie unten gezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Verwendung der GetActiveWorksheet-Methode**
Der andere Ansatz besteht darin, die GetActiveWorksheet-Methode der GridDesktop-Steuerung aufzurufen. Diese Methode liefert eine Referenz auf das Arbeitsblatt, das sich derzeit in der Aspose.Cells.GridDesktop-Steuerung befindet, wie unten gezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
