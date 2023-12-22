---
title: Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben
description: In diesem Artikel wird erläutert, wie Sie die Bibliothek Aspose.Cells verwenden, um benutzerdefinierte Funktionen in Microsoft Excel direkt zu berechnen, ohne die Funktion in ein Arbeitsblatt zu schreiben. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen Excel-Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um die benutzerdefinierte Funktion zu berechnen und das Ergebnis zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben**

 In diesem Thema wird erklärt, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in ein Arbeitsblatt zu schreiben. Bitte nutzen Sie die[**Worksheet.CalculateFormula(Stringformel, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)Methode für diesen Zweck.

Bitte sehen Sie sich den folgenden Beispielcode an, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens MyCompany.CustomFunction() verwendet und berechnen ihren Wert als „Aspose.Cells“. von uns selbst und dann wird dieser Wert automatisch mit dem Wert von Zelle A1 verkettet, der von der Berechnungs-Engine „Willkommen bei“ ist, und der endgültig berechnete Wert wird als „Willkommen bei Aspose.Cells“ zurückgegeben. Wie Sie in einem Code sehen können, den wir haben Unsere benutzerdefinierte Funktion wurde nirgendwo in einem Arbeitsblatt geschrieben und wird direkt von unserer eigenen benutzerdefinierten Logik berechnet.

###  **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **Konsolenausgabe**

Unten finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **Verwandter Artikel**

{{% alert color="primary" %}}

[Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
