---
title: Returnera ett värdeintervall med ICustomFunction
type: docs
weight: 270
url: /sv/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 De[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) är utfasad sedan lanseringen av Aspose.Cells for Java 20.8. Vänligen använd[**AbstractCalculation Engine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) klass. Användningen av[**AbstractCalculation Engine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) klass beskrivs i följande artikel.

[Returnera ett värdeintervall med AbstractCalculationEngine](/cells/sv/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)gränssnitt som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

 Mest när du implementerar[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) gränssnittsmetod måste du returnera ett enskilt cellvärde. Men ibland måste du returnera en rad värden. Den här artikeln kommer att förklara hur du returnerar värdeintervallet från[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Returnera ett värdeintervall med ICustomFunction**

 Följande kod implementerar[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) och returnerar värdeintervallet via sin metod. Vänligen kontrollera[output excel-fil](5472922.xlsx) och[pdf](5472925.pdf) genereras med koden för din referens.

Skapa en klass med en funktion*CalculateCustomFunction*. Denna klass implementerar[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Använd nu ovanstående funktion i ditt program.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
