---
title: Returnera ett område av värden med hjälp av AbstractCalculationEngine
description: Den här artikeln introducerar en abstrakt beräkningsmotor som returnerar en serie värden i Microsoft Excel med hjälp av Aspose.Cells biblioteket. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda de metoder som tillhandahålls av Aspose.Cells för att få en serie värden och returnera resultatet. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, en abstrakt beräkningsmotor som returnerar en serie värden
type: docs
weight: 55
url: /sv/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) klass som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

Den här artikeln kommer att förklara hur man returnerar en serie värden från [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

Följande kod visar användningen av [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)-klassen och returnerar en serie värden via dess metod.

Skapa en klass med en funktion *CalculateCustomFunction*. Denna klass implementerar [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Använd nu ovanstående funktion i ditt program.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
