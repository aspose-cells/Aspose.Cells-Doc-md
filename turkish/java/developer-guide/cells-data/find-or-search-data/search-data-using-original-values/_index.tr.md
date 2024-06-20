---
title: Orijinal Değerler Kullanarak Veri Arama
type: docs
weight: 540
url: /tr/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Bazen verinin değeri biçimlendirildiği için gizlidir. Örneğin, D4 hücresinin formülü =Topla(A1:A2) ve değeri 20 ise ancak --- olarak biçimlendirilmişse, 20 değeri gizlenir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Ancak, [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES) kullanarak Aspose.Cells ile bulabilirsiniz.

{{% /alert %}} 
## **Orijinal Değerler Kullanarak Veri Arama**
Aşağıdaki örnek kod yukarıdaki noktayı anlatır. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan D4 hücresini bulur ancak Aspose.Cells [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES) kullanarak bulabilirsiniz. Daha fazla bilgi için kod içindeki yorumları okuyun.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
