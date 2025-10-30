---
title: Returnera ett intervall av värden med AbstractCalculationEngine med Golang via C++
linktitle: Returnera ett område av värden med hjälp av AbstractCalculationEngine
description: Denna artikel introducerar en abstrakt beräkningsmotor som returnerar ett intervall av värden i Microsoft Excel med Aspose.Cells biblioteket med Golang via C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda Aspose.Cells metoder för att få ett intervall av värden och returnera resultatet. Slutligen sparar vi den ändrade Excel filen till disk.
keywords: Aspose.Cells, Excel, en abstrakt beräkningsmotor som returnerar en serie värden
type: docs
weight: 55
url: /sv/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) klass som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

Den här artikeln kommer att förklara hur man returnerar en serie värden från [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{% /alert %}}

Följande kod visar användningen av [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) klassen och returnerar värdeintervallet via dess metod.

 Skapa en klass med en funktion `CalculateCustomFunction`. Denna klass implementerar [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
 Använd nu ovanstående funktion i ditt program.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
