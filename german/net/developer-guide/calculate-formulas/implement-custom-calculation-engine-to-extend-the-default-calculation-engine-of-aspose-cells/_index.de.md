---
title: Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern
description: In diesem Artikel wird beschrieben, wie Sie die Standardberechnungs-Engine erweitern, indem Sie mithilfe der Bibliothek Aspose.Cells eine benutzerdefinierte Berechnungs-Engine implementieren. Indem wir eine vorhandene Excel-Datei laden oder eine neue erstellen, können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um eine benutzerdefinierte Berechnungs-Engine zu implementieren und die Ergebnisse zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Implementieren Sie eine benutzerdefinierte Berechnungs-Engine**

Aspose.Cells verfügt über eine leistungsstarke Berechnungs-Engine, die fast alle Microsoft Excel-Formeln berechnen kann. Dennoch ermöglicht es Ihnen auch, die Standardberechnungs-Engine zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden bei der Implementierung dieser Funktion verwendet.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Berechnungsdaten](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Der folgende Code implementiert die benutzerdefinierte Berechnungs-Engine. Es implementiert die Schnittstelle**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** das hat eine**[Berechnen(CalculationData-Daten)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** Methode. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die**TODAY** Funktion und addieren Sie einen Tag zum Systemdatum. Wenn das aktuelle Datum also der 27.07.2023 ist, berechnet die benutzerdefinierte Engine TODAY() als 28.07.2023.

###  **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes. Der Wert (Datum und Uhrzeit) von A1 mit benutzerdefinierter Engine sollte einen Tag später sein als das Ergebnis ohne benutzerdefinierte Engine.

###  **Verwandter Artikel**

{{% alert color="primary" %}}

[Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
