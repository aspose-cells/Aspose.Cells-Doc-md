---
title: Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern
type: docs
weight: 80
url: /de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Implementieren Sie eine benutzerdefinierte Berechnungs-Engine**

Aspose.Cells hat eine leistungsstarke Berechnungsmaschine, die fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem können Sie die standardmäßige Berechnungs-Engine erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgende Eigenschaft und Klassen werden bei der Implementierung dieser Funktion verwendet.

- **[Berechnungsoptionen.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Berechnungsdaten](https://reference.aspose.com/cells/net/aspose.cells/berechnungsdaten)**

Der folgende Code implementiert das benutzerdefinierte Berechnungsmodul. Es implementiert die Schnittstelle**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** das hat ein**[Berechnen (Berechnungsdatendaten)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** Methode. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die**Summe** Formel und erhöht ihren Wert um 30. Wenn also der berechnete Wert von Aspose.Cells 20 ist, dann macht unsere benutzerdefinierte Engine 50, indem sie 30 addiert.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
