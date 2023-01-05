---
title: Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değerini Alın
type: docs
weight: 230
url: /tr/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells bir yöntem sağlar[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) herhangi bir biçimlendirme olsun ya da olmasın hücrenin dize değerini almak için kullanılabilir. 0.012345 değerine sahip bir hücreniz olduğunu ve onu yalnızca iki ondalık basamak gösterecek şekilde biçimlendirdiğinizi varsayalım. Daha sonra Excel'de 0.01 olarak görüntülenecektir. Dize değerlerini hem 0.01 hem de 0.012345 olarak alabilirsiniz.[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) yöntem. Alır[CellValueFormatStrateji](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum aşağıdaki değerlere sahip bir parametre olarak

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değerini Alın**
 Aşağıdaki örnek kod, kullanımını açıklar[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Konsol Çıkışı**
Aşağıda, yukarıdaki örnek kodun konsol çıktısı bulunmaktadır.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
