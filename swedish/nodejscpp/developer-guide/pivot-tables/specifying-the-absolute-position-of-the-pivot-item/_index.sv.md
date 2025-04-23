---
title: Specificera den absoluta positionen för pivotposten
type: docs
weight: 50
url: /sv/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Ibland behöver användaren ange pivottitemättets absoluta position, API:et för Aspose.Cells for Node.js via C++ har introducerat några nya egenskaper och en metod för att tillgodose användarens krav.

- Lagt till egenskapen [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) som kan användas för att ange positionens index för alla PivotItems oavsett föräldernod. Lagt till egenskapen [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) som kan användas för att ange positionens index för PivotItems under samma föräldernod.
- Lagt till metoden [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) för att flytta posten upp eller ner baserat på räkningsvärdet, där räkningsvärdet är antalet positioner att flytta PivotItem upp eller ner. Om räkningsvärdet är mindre än noll kommer posten att flyttas upp, medan om räkningsvärdet är större än noll kommer PivotItem att flyttas ner, Boolean typen isSameParent-parameter specificerar om flytoperationen måste utföras i samma föräldernod eller inte.
- Obsoletade metoden [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) *PivotItem.move(int count)* därför rekommenderas det att använda den nyare tillagda metoden [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) istället.

{{% /alert %}}

Följande provkod skapar en pivottabell och sedan specificerar den pivotpostens positioner i samma föräldernod. Du kan ladda ner [käll-Excel](5112632.xlsx)- och [utdata-Excel](5112619.xlsx)-filer för din referens. Om du öppnar utdata-Excel-filen kommer du att se att pivotposten "4H12" är på 0: e position i förälder "K11" och "DIF400" är på 3: e position. På samma sätt är CA32 på position 1 och AAA3 är på position 2.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Observera att det är nödvändigt att använda metoderna [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) och [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) i början av applikationen, det vill säga; innan du kallar några andra objekt i Aspose.Cells API.

{{% /alert %}}

