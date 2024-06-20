---
title: Rückgabe eines Wertebereichs unter Verwendung des abstrakten Berechnungsmotors
description: Dieser Artikel stellt einen abstrakten Berechnungsmotor vor, der unter Verwendung der Aspose.Cells Bibliothek einen Wertebereich in Microsoft Excel zurückgibt. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um einen Wertebereich zu erhalten und das Ergebnis zurückzugeben. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ein abstrakter Berechnungsmotor, der eine Reihe von Werten zurückgibt
type: docs
weight: 55
url: /de/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

In diesem Artikel wird erläutert, wie der Wertebereich von [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) zurückgegeben wird.

{{% /alert %}}

Der folgende Code zeigt die Verwendung der Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) und gibt den Wertebereich über ihre Methode zurück.

Erstellen Sie eine Klasse mit einer Funktion *CalculateCustomFunction*. Diese Klasse implementiert [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Verwenden Sie die obige Funktion nun in Ihrem Programm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
