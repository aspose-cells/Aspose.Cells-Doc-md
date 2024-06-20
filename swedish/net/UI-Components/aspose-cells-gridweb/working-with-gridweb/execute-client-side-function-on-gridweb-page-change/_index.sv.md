---
title: Utför klientens sida funktion på GridWeb sidbyte
type: docs
weight: 140
url: /sv/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Denna artikel introducerar hur man arbetar med klientens js funktion i GridWeb.
---

## **Möjliga användningsscenario**
Ibland behöver du köra din klient sida funktion när GridWeb-sidan ändras. Aspose.Cells.GridWeb tillhandahåller egenskapen OnPageChangeClientFunction för detta ändamål. Ange denna egenskap med klient sida funktion som du vill köra.
## **Utför klientens sidofunktion på GridWeb sidbyte**
Följande aspx-markering förklarar hur man använder egenskapen OnPageChangeClientFunction. Den ställer egenskapen till klientens funktion med namnet MyOnPageChange. Observera att denna egenskap endast är giltig om du har aktiverat paginering, det vill säga EnablePaging="true". Nu, när du ändrar GridWeb-sidan, kommer den att anropa klientens funktion MyOnPageChange som skriver ut **aktuell sidindex** på **konsolen** enligt skärmdumpen.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Exempelkod**
Detta är koden för klientens funktion MyOnPageChange som kommer att köras på grund av inställningen OnPageChangeClientFunction ="MyOnPageChange" i GridWeb. Detta är den kompletta aspx-sidans märkning.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
