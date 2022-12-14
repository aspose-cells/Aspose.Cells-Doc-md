---
title: Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben
type: docs
weight: 650
url: /de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 In diesem Artikel wird erläutert, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in ein Arbeitsblatt zu schreiben. Bitte verwenden Sie die[Worksheet.calculateFormula (String-Formel, CalculationOptions-Optionen)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) Methode zu diesem Zweck.

{{% /alert %}} 
## **Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben**
Bitte sehen Sie sich den folgenden Beispielcode an, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens verwendet*MeineFirma.CustomFunction()*und wir berechnen seinen Wert als „Aspose.Cells“. von uns selbst und dann wird dieser Wert automatisch mit dem Wert von Zelle A1 verkettet, der von der Berechnungs-Engine "Willkommen bei" ist, und der endgültig berechnete Wert wird als "Willkommen bei Aspose.Cells." zurückgegeben. Wie Sie in einem Code sehen können, haben wir unsere benutzerdefinierte Funktion nirgendwo in ein Arbeitsblatt geschrieben und sie wird direkt von unserer eigenen benutzerdefinierten Logik berechnet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Konsolenausgabe**
Unten ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
