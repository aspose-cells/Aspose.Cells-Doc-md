---
title: Rückgabe eines Wertebereichs unter Verwendung von ICustomFunction
description: Dieser Artikel beschreibt, wie die Aspose.Cells Bibliothek verwendet wird, um mit ICustomFunction in Microsoft Excel einen Wertebereich zurückzugeben. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um einen Wertebereich zu erhalten und das Ergebnis zurückzugeben. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ICustomFunction, gibt eine Reihe von Werten zurück
type: docs
weight: 50
url: /de/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

Das [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) ist seit der Veröffentlichung von Aspose.Cells for Java 20.8 veraltet. Bitte verwenden Sie die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine). Die Verwendung der Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) wird in folgendem Artikel beschrieben.

[Rückgabe eines Wertebereichs unter Verwendung des abstrakten Berechnungsmotors](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells bietet die Schnittstelle [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

Meistens, wenn Sie die Methode der Schnittstelle [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) implementieren, müssen Sie einen einzelnen Zellwert zurückgeben. Manchmal müssen jedoch Wertebereiche zurückgegeben werden. Dieser Artikel erläutert, wie der Wertebereich von [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) zurückgegeben wird.

{{% /alert %}}

Der folgende Code implementiert [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) und gibt den Wertebereich über seine Methode zurück.

Erstellen Sie eine Klasse mit einer Funktion *CalculateCustomFunction*. Diese Klasse implementiert [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Verwenden Sie die obige Funktion nun in Ihrem Programm.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
