---
title: Rückgabe eines Wertebereichs unter Verwendung des abstrakten Berechnungsmotors
type: docs
weight: 275
url: /de/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

In diesem Artikel wird erläutert, wie der Wertebereich von [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) zurückgegeben wird.

{{% /alert %}}

Der folgende Code zeigt die Verwendung der Methode [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) und gibt den Wertebereich über ihre Methode zurück.

Erstellen Sie eine Klasse mit einer Funktion *CalculateCustomFunction*. Diese Klasse erweitert [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Verwenden Sie die obige Funktion jetzt in Ihrem Programm.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
{{< app/cells/assistant language="java" >}}
