---
title: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Alın
type: docs
weight: 230
url: /tr/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells, hücrenin biçimlendirmesi olsun ya da olmasın, hücrenin string değerini almak için kullanılabilen [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) metodunu sağlar. Diyelim ki, değeri 0.012345 olan ve yalnızca iki ondalık basamağını göstermek için biçimlendirilmiş bir hücreniz var. Bu, Excel'de 0.01 olarak gösterilir. İster 0.01 ister 0.012345 olarak alabilirsiniz. [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) metodunu kullanarak iki farklı şekilde değer alabilirsiniz. Bu metod, [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) enum parametresi alır ve aşağıdaki değerleri içerir

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın**
Aşağıdaki örnek kod, [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)  yönteminin kullanımını açıklar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
