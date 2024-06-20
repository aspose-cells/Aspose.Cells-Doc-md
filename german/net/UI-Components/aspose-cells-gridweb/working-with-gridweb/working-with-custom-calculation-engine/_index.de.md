---
title: Arbeiten mit benutzerdefinierter Berechnungsmaschine
type: docs
weight: 70
url: /de/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, benutzerdefiniert, Berechnung, CalculationEngine, GridAbstractCalculationEngine
description: Dieser Artikel zeigt, wie man GridAbstractCalculationEngine verwendet, um den Berechnungsprozess in GridWeb anzupassen.
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells.Gridweb verfügt über eine leistungsstarke Berechnungsmaschine, die fast alle Microsoft Excel-Formeln berechnen kann. Dennoch ermöglicht es Ihnen auch, die Standardberechnungsmaschine zu erweitern, was Ihnen eine größere Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

Der folgende Code implementiert den benutzerdefinierten Berechnungsmotor. Es implementiert das Interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine), das eine [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)-Methode hat. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die **MYTESTFUNC**-Formel und multiplizieren mit 2 für ihren ersten Parametewert.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

