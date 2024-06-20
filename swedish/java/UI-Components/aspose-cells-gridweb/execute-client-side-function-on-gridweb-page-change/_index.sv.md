---
title: Utför klientens sida funktion på GridWeb sidbyte
type: docs
weight: 70
url: /sv/java/execute-client-side-function-on-gridweb-page-change/
---

## **Möjliga användningsscenario**
Ibland behöver du köra din klient sida funktion när GridWeb-sidan ändras. Aspose.Cells.GridWeb tillhandahåller egenskapen OnPageChangeClientFunction för detta ändamål. Ange denna egenskap med klient sida funktion som du vill köra.
## **Utför klientens sidofunktion på GridWeb sidbyte**
Följande javakod förklarar hur man använder egenskapen GridWebBean.setOnPageChangeClientFunction(). Den ställer in egenskapen med klient sida funktionen som heter MyOnPageChange. Observera att denna egenskap är giltig endast om du har aktiverat paginering, dvs GridWebBean.setEnablePaging(true). Nu, varje gång du ändrar GridWeb-sidan, kommer den att anropa klient sida funktionen MyOnPageChange som skriver ut ** aktuell sida index ** på ** konsolen ** som visas på detta skärmbild.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Exempelkod**
Detta är koden för klientens sidofunktion MyOnPageChange som kommer att köras på grund av den här raden dvs. Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Följande kod förklarar hur man aktiverar sidindelning och ställer in egenskapen OnPageChangeClientFunction.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
