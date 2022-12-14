---
title: Fyll i data först efter rad och sedan efter kolumn
type: docs
weight: 10
url: /sv/java/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}}

Att fylla ett kalkylblad med data först efter rad och sedan efter kolumn förbättrar den övergripande prestandan.

{{% /alert %}}

## Fyll i data först efter rad och sedan efter kolumn

Att lägga data i sekvensen A1, B1, A2, B2 är snabbare än A1, A2, B1, B2. Om det finns många celler i ett kalkylblad och du följer den andra sekvensen, det vill säga du fyller i data rad för rad, kan detta tips göra programmet mycket snabbare.

## Java-kod för att fylla i data först efter rad och sedan efter kolumn

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
