---
title: Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern
type: docs
weight: 590
url: /de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells hat eine leistungsstarke Berechnungsmaschine, die fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem können Sie die standardmäßige Berechnungs-Engine erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgende Eigenschaft und Klassen werden bei der Implementierung dieser Funktion verwendet.

- [Berechnungsoptionen.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Berechnungsdaten](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implementieren Sie eine benutzerdefinierte Berechnungs-Engine**
Der folgende Code implementiert das benutzerdefinierte Berechnungsmodul. Es implementiert die Schnittstelle[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) die nur eine Methode hat[berechnen(Berechnungsdaten daten)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die**SUMME** Formel und erhöht ihren Wert um 30. Wenn also der berechnete Wert von Aspose.Cells 20 ist, dann macht unsere benutzerdefinierte Engine 50, indem sie 30 addiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
