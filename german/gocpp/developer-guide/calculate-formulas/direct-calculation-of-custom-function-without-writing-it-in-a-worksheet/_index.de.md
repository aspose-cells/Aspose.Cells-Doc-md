---
title: Direkte Berechnung einer benutzerdefinierten Funktion ohne sie in einem Arbeitsblatt zu schreiben mit Golang über C++
linktitle: Direkte Berechnung einer benutzerdefinierten Funktion
description: Dieser Artikel erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um benutzerdefinierte Funktionen in Microsoft Excel direkt zu berechnen, ohne die Funktion in einem Arbeitsblatt zu schreiben. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden nutzen, um die benutzerdefinierte Funktion zu berechnen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, benutzerdefinierte Funktionen, direkte Berechnungen, kein Schreiben erforderlich, Arbeitsblätter
type: docs
weight: 90
url: /de/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkte Berechnung einer benutzerdefinierten Funktion ohne sie in einem Arbeitsblatt zu schreiben**

Dieses Thema erklärt, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in einem Arbeitsblatt zu schreiben. Bitte verwenden Sie dafür die [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/)-Methode.

 Bitte sehen Sie sich den folgenden Beispielcode an, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens MyCompany::CustomFunction() verwendet und ihren Wert selbst auf "Aspose.Cells." berechnet. Dieser Wert wird dann automatisch mit dem Wert der Zelle A1, der "Willkommen bei" ist, durch die Berechnungs-Engine verkettet, und der endgültige berechnete Wert wird als "Willkommen bei Aspose.Cells." zurückgegeben. Wie im Code sichtbar, haben wir unsere benutzerdefinierte Funktion nirgendwo in einem Arbeitsblatt geschrieben; sie wird direkt durch unsere eigene Logik berechnet.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Konsolenausgabe**

Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
