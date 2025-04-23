---
title: Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des standardmäßigen Berechnungsmotors von Aspose.Cells
description: In diesem Artikel wird beschrieben, wie Sie den standardmäßigen Berechnungsmotor durch Implementierung eines benutzerdefinierten Berechnungsmotors mithilfe der Aspose.Cells Bibliothek erweitern können. Indem wir eine vorhandene Excel Datei laden oder eine neue erstellen, können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um einen benutzerdefinierten Berechnungsmotor zu implementieren und die Ergebnisse zu erhalten. Abschließend speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, benutzerdefinierter Berechnungsmotor, erweitert den standardmäßigen Berechnungsmotor
type: docs
weight: 80
url: /de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem ermöglicht es Ihnen auch, den standardmäßigen Berechnungsmotor zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

Der folgende Code implementiert den benutzerdefinierten Berechnungsmotor. Er implementiert die Schnittstelle [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine), die eine Methode [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate) hat. Diese Methode wird für alle Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die Funktion **TODAY** und fügen ein Tag zum Systemdatum hinzu. Wenn das aktuelle Datum beispielsweise der 27/07/2023 ist, berechnet der benutzerdefinierte Motor TODAY() als 28/07/2023.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes, der Wert (Datum/Uhrzeit) von A1 mit benutzerdefiniertem Motor sollte einen Tag später sein als das Ergebnis ohne benutzerdefinierten Motor.

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt zu schreiben](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
