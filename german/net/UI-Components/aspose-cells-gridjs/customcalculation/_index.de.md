---
title: Arbeiten mit benutzerdefinierter Berechnungs-Engine für GridJs
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/customcalculation/
description: In diesem Artikel wird beschrieben, wie Sie das benutzerdefinierte Berechnungsmodul für die Bibliothek Aspose.Cells.GridJs verwenden.
---
## **Implementieren Sie eine benutzerdefinierte Berechnungs-Engine**

Aspose.Cells.GridJs hat eine leistungsstarke Berechnungs-Engine, die fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem können Sie die standardmäßige Berechnungs-Engine erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgende Eigenschaft und Klassen werden bei der Implementierung dieser Funktion verwendet.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

Der folgende Code implementiert das benutzerdefinierte Berechnungsmodul. Es implementiert die Schnittstelle**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** das hat ein**[Berechnen (GridCalculationData-Daten)] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** Methode. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die**MYTESTFUNC** Formel und multipliziere mit 2 für den ersten Parameterwert .

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
