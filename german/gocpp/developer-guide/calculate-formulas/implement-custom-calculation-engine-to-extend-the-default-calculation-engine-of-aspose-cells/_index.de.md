---
title: Implementieren Sie eine benutzerdefinierte Berechnungs Engine, um die Standardsberechnungs Engine von Aspose.Cells mit Golang über C++ zu erweitern
linktitle: Implementieren Sie eine benutzerdefinierte Berechnungs Engine
description: Dieser Artikel beschreibt, wie man die Standardsberechnungs Engine durch Implementierung einer benutzerdefinierten Berechnungs Engine mit der Aspose.Cells Bibliothek mit Golang über C++ erweitert. Durch das Laden einer bestehenden Excel Datei oder das Erstellen einer neuen können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um eine benutzerdefinierte Berechnungs Engine zu implementieren und die Ergebnisse zu erhalten. Schließlich speichern wir die bearbeitete Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, benutzerdefinierte Berechnungs Engine, erweitert die Standard Berechnungs Engine, C++
type: docs
weight: 80
url: /de/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem ermöglicht es Ihnen auch, den standardmäßigen Berechnungsmotor zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

Der folgende Code implementiert den benutzerdefinierten Berechnungsmotor. Er implementiert die Schnittstelle [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/), die eine Methode [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) hat. Diese Methode wird für alle Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die Funktion **TODAY** und fügen ein Tag zum Systemdatum hinzu. Wenn das aktuelle Datum beispielsweise der 27/07/2023 ist, berechnet der benutzerdefinierte Motor TODAY() als 28/07/2023.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes, der Wert (Datum/Uhrzeit) von A1 mit benutzerdefiniertem Motor sollte einen Tag später sein als das Ergebnis ohne benutzerdefinierten Motor.

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt zu schreiben](/cells/de/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
