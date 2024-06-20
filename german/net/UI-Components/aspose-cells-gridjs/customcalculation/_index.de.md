---
title: Arbeiten mit benutzerdefiniertem Berechnungsmotor für GridJs
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/customcalculation/
keywords: GridJs,custom,calculation,customcalculation
description: In diesem Artikel wird beschrieben, wie der benutzerdefinierte Berechnungsmotor für die Aspose.Cells.GridJs Bibliothek verwendet wird.
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells.GridJs verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem können Sie den standardmäßigen Berechnungsmotor erweitern, um Ihnen mehr Leistung und Flexibilität zu bieten.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

Der folgende Code implementiert den benutzerdefinierten Berechnungsmotor. Es implementiert das Interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine), das eine [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)-Methode hat. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die **MYTESTFUNC**-Formel und multiplizieren mit 2 für ihren ersten Parametewert.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

