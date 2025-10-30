---
title: Hämta arbetsblad för diagrammet med Golang via C++
linktitle: Hämta kalkylbladet för diagrammet
description: Lär dig hur du hämtar kalkylbladet som är kopplat till ett Excel diagram med Aspose.Cells for C++. Vår guide visar hur du får tillgång till kalkylbladet och utför operationer på det för att manipulera diagrammets underliggande data.
keywords: Aspose.Cells for C++, Excel diagram, kalkylblad, datamanipulation, underliggande data, operationer.
type: docs
weight: 1000
url: /sv/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du få åtkomst till ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller metoden [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

Följande exempel visar hur man använder metoden [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/). Koden skriver först ut namnet på kalkylbladet, accessar sedan det första diagrammet på kalkylbladet. Den skriver sedan ut kalkylbladets namn igen, med hjälp av metoden [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
Nedan är konsolresultatet som exempelkoden leder till. Som du kan se skriver den ut arbetsbladsnamnet samma namn båda gångerna.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
