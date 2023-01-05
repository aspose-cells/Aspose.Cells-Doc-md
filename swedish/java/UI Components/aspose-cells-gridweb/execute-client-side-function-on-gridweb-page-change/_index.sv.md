---
title: Utför klientsidans funktion på GridWeb-sidaändring
type: docs
weight: 70
url: /sv/java/execute-client-side-function-on-gridweb-page-change/
---
## **Möjliga användningsscenarier**
Ibland behöver du köra din klientsidefunktion när GridWeb-sidan ändras. Aspose.Cells.GridWeb tillhandahåller egenskapen OnPageChangeClientFunction för detta ändamål. Vänligen ställ in den här egenskapen med klientsidans funktion som du vill köra.
## **Utför klientsidans funktion på GridWeb-sidaändring**
Följande java-kod förklarar hur du använder egenskapen GridWebBean.setOnPageChangeClientFunction(). Den ställer in egenskapen med klientsidans funktion som heter MyOnPageChange. Observera att den här egenskapen endast är giltig om du har aktiverat personsökning, dvs. GridWebBean.setEnablePaging(true). När du nu ändrar GridWeb-sidan kommer den att anropa klientsidans funktion MyOnPageChange som skriver ut**aktuellt sidindex** på**trösta** som visas i denna skärmdump.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Exempelkod**
Detta är koden för klientsidans funktion MyOnPageChange som kommer att exekveras på grund av denna rad, dvs Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Följande kod förklarar hur du aktiverar personsökning och ställer in egenskapen OnPageChangeClientFunction.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
