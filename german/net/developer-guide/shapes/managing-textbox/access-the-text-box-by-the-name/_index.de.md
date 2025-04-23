---
title: Greifen Sie auf die Textbox über den Namen zu
type: docs
weight: 230
url: /de/net/access-the-text-box-by-the-name/
---

##Greifen Sie über den Namen auf die Textbox zu

Früher wurden Textfelder anhand des Index aus der [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)-Sammlung abgerufen, aber jetzt können Sie das Textfeld auch anhand seines Namens aus dieser Sammlung abrufen. Dies ist eine bequeme und schnelle Möglichkeit, auf Ihr Textfeld zuzugreifen, wenn Sie seinen Namen bereits kennen.

Der folgende Beispielcode erstellt zunächst eine Textbox und weist ihr einen Text und einen Namen zu. Anschließend greifen wir in den nächsten Zeilen auf dieselbe Textbox anhand ihres Namens zu und drucken ihren Text aus.

###C#-Code zum Zugriff auf die Textbox über den Namen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AccessTextBoxName-AccessTextBoxName.cs" >}}

### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
