---
title: Arbeiten mit benutzerdefinierter Berechnungs-Engine
type: docs
weight: 70
url: /de/net/working-with-custom-calculation-engine/
---
## **Implementieren Sie eine benutzerdefinierte Berechnungs-Engine**

Aspose.Cells.Gridweb hat eine leistungsstarke Berechnungsmaschine, die fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem können Sie die standardmäßige Berechnungs-Engine erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgende Eigenschaft und Klassen werden bei der Implementierung dieser Funktion verwendet.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

Der folgende Code implementiert das benutzerdefinierte Berechnungsmodul. Es implementiert die Schnittstelle**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** das hat ein**[Berechnen (GridCalculationData-Daten)] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** Methode. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die**MYTESTFUNC** Formel und multipliziere mit 2 für den ersten Parameterwert .

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

