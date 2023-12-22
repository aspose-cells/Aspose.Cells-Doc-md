---
title: Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern
type: docs
weight: 590
url: /de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells verfügt über eine leistungsstarke Berechnungs-Engine, die fast alle Microsoft Excel-Formeln berechnen kann. Dennoch ermöglicht es Ihnen auch, die Standardberechnungs-Engine zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden bei der Implementierung dieser Funktion verwendet.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Berechnungsdaten](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Implementieren Sie eine benutzerdefinierte Berechnungs-Engine**
Der folgende Code implementiert die benutzerdefinierte Berechnungs-Engine. Es implementiert die Schnittstelle[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) das nur eine Methode hat[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die**TODAY** Funktion und addieren Sie einen Tag zum Systemdatum. Wenn das aktuelle Datum also der 27.07.2023 ist, berechnet die benutzerdefinierte Engine TODAY() als 28.07.2023.

###  **Programmierbeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes. Der Wert (Datum und Uhrzeit) von A1 mit benutzerdefinierter Engine sollte einen Tag später sein als das Ergebnis ohne benutzerdefinierte Engine.

###  **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
