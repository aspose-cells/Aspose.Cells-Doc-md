---
title: Zurückgeben eines Wertebereichs mithilfe von ICustomFunction
description: In diesem Artikel wird beschrieben, wie Sie die Aspose.Cells-Bibliothek verwenden, um einen Wertebereich mit ICustomFunction in Microsoft Excel zurückzugeben. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen Excel-Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um einen Wertebereich abzurufen und das Ergebnis zurückzugeben. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values
type: docs
weight: 50
url: /de/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Der[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) ist seit der Veröffentlichung von Aspose.Cells for Java 20.8 veraltet. Bitte nutzen Sie die[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) Klasse. Die Verwendung der[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) Die Klasse wird im folgenden Artikel beschrieben.

[Zurückgeben eines Wertebereichs mit AbstractCalculationEngine](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells bietet[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)Schnittstelle, die zum Implementieren benutzerdefinierter oder benutzerdefinierter Funktionen verwendet wird, die von Microsoft Excel nicht als integrierte Funktionen unterstützt werden.

 Meistens, wenn Sie das implementieren[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) Bei der Schnittstellenmethode müssen Sie einen einzelnen Zellenwert zurückgeben. Manchmal müssen Sie jedoch einen Wertebereich zurückgeben. In diesem Artikel wird erläutert, wie Sie den Wertebereich von zurückgeben[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Der folgende Code wird implementiert[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)und gibt über seine Methode den Wertebereich zurück.

Erstellen Sie eine Klasse mit einer Funktion *CalculateCustomFunction*. Diese Klasse implementiert[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Verwenden Sie nun die obige Funktion in Ihrem Programm

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
