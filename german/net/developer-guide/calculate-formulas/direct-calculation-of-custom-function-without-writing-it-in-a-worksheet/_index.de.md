---
title: Direkte Berechnung einer benutzerdefinierten Funktion ohne sie in einem Arbeitsblatt zu schreiben
description: Dieser Artikel erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um benutzerdefinierte Funktionen in Microsoft Excel direkt zu berechnen, ohne die Funktion in einem Arbeitsblatt zu schreiben. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden nutzen, um die benutzerdefinierte Funktion zu berechnen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, benutzerdefinierte Funktionen, direkte Berechnungen, kein Schreiben erforderlich, Arbeitsblätter
type: docs
weight: 90
url: /de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt**

In diesem Thema wird erläutert, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in einem Arbeitsblatt zu schreiben. Verwenden Sie hierzu die [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)-Methode.

Bitte beachten Sie den folgenden Beispielcode, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens MyCompany.CustomFunction() verwendet und ihren Wert als "Aspose.Cells." selbst berechnet. Dieser Wert wird dann automatisch mit dem Wert der Zelle A1, der "Willkommen bei " durch den Berechnungsmotor, konkateniert und der endgültig berechnete Wert als "Willkommen bei Aspose.Cells." zurückgegeben. Wie Sie im Code sehen können, haben wir unsere benutzerdefinierte Funktion nirgendwo in einem Arbeitsblatt geschrieben und sie wird direkt durch unsere eigene benutzerdefinierte Logik berechnet.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Konsolenausgabe**

Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des standardmäßigen Berechnungsmotors von Aspose.Cells](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
