---
title: Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des standardmäßigen Berechnungsmotors von Aspose.Cells
type: docs
weight: 590
url: /de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem ermöglicht es Ihnen auch, den standardmäßigen Berechnungsmotor zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Benutzerdefinierten Berechnungsmotor implementieren**
Der folgende Code implementiert die Anpassungsberechnungseinheit. Es implementiert die Schnittstelle [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine), welche nur eine Methode [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate-com.aspose.cells.CalculationData-) hat. Diese Methode wird für alle deine Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die Funktion **TODAY** und addieren einen Tag zum Systemdatum. Wenn das aktuelle Datum also 27.07.2023 ist, berechnet die benutzerdefinierte Engine TODAY() als 28.07.2023.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes, der Wert (Datum/Uhrzeit) von A1 mit benutzerdefiniertem Motor sollte einen Tag später sein als das Ergebnis ohne benutzerdefinierten Motor.

### **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
