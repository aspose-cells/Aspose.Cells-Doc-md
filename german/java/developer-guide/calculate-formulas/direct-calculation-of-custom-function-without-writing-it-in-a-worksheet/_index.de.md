---
title: Direkte Berechnung einer benutzerdefinierten Funktion ohne sie in einem Arbeitsblatt zu schreiben
type: docs
weight: 650
url: /de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Dieser Artikel erklärt, wie du deine benutzerdefinierten Funktionen direkt berechnen kannst, ohne sie zuerst in einem Arbeitsblatt zu schreiben. Bitte verwende dazu die Methode [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-)

{{% /alert %}} 
## **Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt**
Bitte sehen Sie sich den folgenden Beispielcode an, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens *MyCompany.CustomFunction()* verwendet und ihren Wert als "Aspose.Cells." selbst berechnet, und dann wird dieser Wert automatisch mit dem Wert der Zelle A1, der "Willkommen bei " ist, von der Berechnungsmaschine konkateniert und der endgültige berechnete Wert als "Willkommen bei Aspose.Cells." zurückgegeben. Wie Sie im Code sehen können, haben wir unsere benutzerdefinierte Funktion nirgendwo in einem Arbeitsblatt geschrieben und sie wird direkt durch unsere eigene benutzerdefinierte Logik berechnet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Konsolenausgabe**
Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
