---
title: Ange DBNum anpassad mönsterformatering med Golang via C++
linktitle: Ange DBNum anpassad pattern formatering
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som stöder formatering av datum och nummer med hjälp av anpassade formateringsmönster. Den här artikeln visar hur man använder Aspose.Cells biblioteket för att specificera det anpassade formatmönstret dbnum så att användare får mer kontroll över hur nummer visas.
keywords: Aspose.Cells, C++ bibliotek, elektroniskt kalkylblad, anpassat formatmönster, formatering, dbnum , kontrollera visning
type: docs
weight: 110
url: /sv/go-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Möjliga användningsscenario**

Aspose.Cells stöder *DBNum* anpassat mönsterformat. Till exempel, om din cellvärde är 123 och du specificerar dess anpassade formatering som [DBNum2][$-804]Allmänt, kommer det att visas som 壹佰贰拾叁. Du kan specificera din anpassade formatering av cellen med [**Cell.GetStyle()**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)-metoden och [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-egenskapen.

## **Exempelkod**

Följande exempel visar hur man specificerar anpassad *DBNum*-mönsterformatering. Kontrollera dess [utdata PDF](43352081.pdf) för mer hjälp.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingDbnumCustomPatternFormatting.go" >}}
