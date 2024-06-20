---
title: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Alın
type: docs
weight: 230
url: /tr/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells, biçimlendirme ile veya olmadan hücrenin dize değerini almak için [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) yöntemini sağlar. Örneğin, 0.012345 değerinde bir hücreye sahipseniz ve bu hücreyi yalnızca iki ondalık basamak göstermesi için biçimlendirdiyseniz, Excel'de 0.01 olarak görüntülenir. [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) yöntemiyle 0.01 ve 0.012345 olarak dize değerlerini alabilirsiniz. [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) enum'u parametre olarak alır ve aşağıdaki değerlere sahiptir

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın**
Aşağıdaki örnek kod, [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) yönteminin kullanımını açıklar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
