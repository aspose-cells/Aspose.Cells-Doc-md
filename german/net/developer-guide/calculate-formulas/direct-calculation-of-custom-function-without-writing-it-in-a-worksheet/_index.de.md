---
title: Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben
type: docs
weight: 90
url: /de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben**

 In diesem Thema wird erläutert, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in ein Arbeitsblatt schreiben zu müssen. Bitte verwenden Sie die[**Worksheet.CalculateFormula (String-Formel, CalculationOptions-Optionen)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)Methode zu diesem Zweck.

Bitte sehen Sie sich den folgenden Beispielcode an, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens MyCompany.CustomFunction() verwendet und berechnen ihren Wert als „Aspose.Cells“. von uns selbst und dann wird dieser Wert automatisch mit dem Wert von Zelle A1 verkettet, der von der Berechnungs-Engine "Willkommen bei" ist, und der endgültig berechnete Wert wird als "Willkommen bei Aspose.Cells" zurückgegeben. Wie Sie in einem Code sehen können, den wir haben Unsere benutzerdefinierte Funktion wurde nicht irgendwo in ein Arbeitsblatt geschrieben und wird direkt von unserer eigenen benutzerdefinierten Logik berechnet.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Konsolenausgabe**

Unten ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
