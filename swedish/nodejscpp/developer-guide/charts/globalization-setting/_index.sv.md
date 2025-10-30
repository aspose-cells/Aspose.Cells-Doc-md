---
title: Konvertera diagram till lokaliserad bild med Node.js via C++
description: Lär dig hur du ställer in globaliseringsinställningar för diagram med Aspose.Cells for Node.js via C++. Vår guide visar hur man konfigurerar diagrammet för att stödja flera språk och regionala format för att korrekt visa text, datum och nummer på olika språk.
keywords: Aspose.Cells for Node.js via C++, Diagram, Globaliseringsinställningar, Flera språk, Regionala format, Visning, Text, Datum, Nummer.
linktitle: Ställ in lokaliserad region
type: docs
weight: 50
url: /sv/nodejs-cpp/convert-chart-to-localized-image/
alias: [/nodejs-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

I det här avsnittet kommer vi att visa dig hur du konverterar diagram till lokaliserad bild, du kommer att lära dig hur du ställer in lokaliserad region för ett diagram.

{{% /alert %}}

## **Scenario**

I vilket scenario skulle vi behöva ställa in lokaliserat område för ett diagram? 

När du öppnar en xlsx-fil med ett diagram i Excel, i detta fall om du öppnar den med en spansk regional inställning i Excel, kan du se elementen i diagramområdet, som Diagramtitel, Legend, de är översatta till spanska. Men när du sparar detta diagram som en bild med Aspose.Cells kan du stöta på följande problem: 

**![Globalt problem](GlobalIssue.png)**

I detta scenario är diagramlegenden i utdatabilden inte densamma som i Excel; den visas för default på engelska. Nu kan du lösa detta problem genom att ställa in lokaliserat område för diagrammet. Med rätt inställningar kommer följande element att renderas enligt dina lokaliseringsinställningar.

## **Stödda element**

Följande element i diagrammet kan renderas enligt dina lokaliseringsinställningar.

|**Stödda element**|**standardvärde i engelska miljö**|
| :- | :- |
|Titel på axel|Axeltitel|
|Namn på axelenhet|Hundratals, tusentals...|
|Diagramtitelnamn|Diagramtitel|
|Förklara ökning Namn|Ökning|
|Förklara minskning Namn|Minskning|
|Förklara totalt Namn|Totalt|
|Andra Namn|Andra|
|Serienamn|Serie|

## **Operationssteg**

Följande exempel visar i detalj hur du ställer in lokaliserat område för att uppnå önskad effekt.

- [Hur man ställer in kinesisk region för diagram](/cells/sv/nodejs-cpp/convert-chart-to-image-for-chinese-region/)
- [Hur man ställer in japansk region för diagram](/cells/sv/nodejs-cpp/convert-chart-to-image-for-japanese-region/)


{{< app/cells/assistant language="nodejs-cpp" >}}
