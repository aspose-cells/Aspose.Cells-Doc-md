---
title: Utför klientsidans funktion på GridWeb-sidaändring
type: docs
weight: 140
url: /sv/net/execute-client-side-function-on-gridweb-page-change/
---
## **Möjliga användningsscenarier**
Ibland behöver du köra din klientsidefunktion när GridWeb-sidan ändras. Aspose.Cells.GridWeb tillhandahåller egenskapen OnPageChangeClientFunction för detta ändamål. Vänligen ställ in den här egenskapen med klientsidans funktion som du vill köra.
## **Utför klientsidans funktion på GridWeb-sidaändring**
Följande aspx-uppmärkning förklarar hur du använder egenskapen OnPageChangeClientFunction. Den ställer in egenskapen med klientsidans funktion som heter MyOnPageChange. Observera att den här egenskapen endast är giltig om du har aktiverat personsökning, dvs. EnablePaging="true". När du nu ändrar GridWeb-sidan kommer den att anropa klientsidans funktion MyOnPageChange som skriver ut**aktuellt sidindex** på**trösta** som visas i denna skärmdump.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Exempelkod**
Detta är koden för klientsidans funktion MyOnPageChange som kommer att exekveras på grund av inställningen av OnPageChangeClientFunction ="MyOnPageChange"-egenskapen i GridWeb. Detta är den fullständiga aspx-sidans uppmärkning.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
