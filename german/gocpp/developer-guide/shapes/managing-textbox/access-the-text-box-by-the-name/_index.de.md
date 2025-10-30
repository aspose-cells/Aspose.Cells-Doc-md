---
title: Auf das Textfeld anhand des Namens mit Golang über C++ zugreifen
linktitle: Greifen Sie auf die Textbox über den Namen zu
type: docs
weight: 230
url: /de/go-cpp/access-the-text-box-by-the-name/
description: Erfahren Sie, wie Sie ein Textfeld anhand seines Namens mit Aspose.Cells for C++ zugreifen.
---

##Greifen Sie über den Namen auf die Textbox zu

 Früher wurden Textfelder anhand ihres Index aus der [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/)-Sammlung zugegriffen, jetzt können Sie auch auf das Textfeld nach Name aus dieser Sammlung zugreifen. Dies ist eine bequeme und schnelle Methode, um auf Ihr Textfeld zuzugreifen, wenn Sie bereits seinen Namen kennen.

Das folgende Beispiel erstellt zunächst ein Textfeld, weist ihm Text und einen Namen zu. Im Anschluss greifen wir über den Namen auf dasselbe Textfeld zu und geben dessen Text aus.

### C++-Code zum Zugreifen auf das Textfeld nach Namen

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
