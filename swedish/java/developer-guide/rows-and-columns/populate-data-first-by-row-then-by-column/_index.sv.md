---
title: Populera Data Först per Rad och sedan per Kolumn
type: docs
weight: 10
url: /sv/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

Att fylla i ett kalkylblad med data först per rad och sedan per kolumn förbättrar den övergripande prestandan.

{{% /alert %}}

## Populera Data Först per Rad och sedan per Kolumn

Att placera data i sekvensen A1, B1, A2, B2 går snabbare än A1, A2, B1, B2. Om det finns många celler i ett kalkylblad och du följer den andra sekvensen, det vill säga fyller i data rad för rad, kan detta tips göra programmet mycket snabbare.

## Java-kod för att fylla data först per rad och sedan per kolumn

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
