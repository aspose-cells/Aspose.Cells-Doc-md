---
title: Returnera ett område av värden med hjälp av ICustomFunction
type: docs
weight: 270
url: /sv/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) klassen är nedlagd sedan versionen Aspose.Cells for Java 20.8. Använd istället [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) klassen. Användningen av [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) klassen beskrivs i följande artikel.

[Returnera ett område av värden med hjälp av AbstractCalculationEngine](/cells/sv/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) gränssnitt som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

Mestadels när du implementerar [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) gränssnittet metod, behöver du returnera ett enskilt cellvärde. Men ibland behöver du returnera ett område av värden. Den här artikeln kommer att förklara hur man returnerar en serie värden från [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Returnera ett område av värden med hjälp av ICustomFunction**

Följande kod implementerar [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) och returnerar området av värden via dess metod. Vänligen se den [utmatade Excel-filen](5472922.xlsx) och [pdf](5472925.pdf) som genererats med koden för din referens.

Skapa en klass med en funktion *CalculateCustomFunction*. Denna klass implementerar [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Använd nu den ovanstående funktionen i ditt program.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
