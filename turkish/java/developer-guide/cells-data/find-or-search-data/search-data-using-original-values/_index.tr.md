---
title: Orijinal Değerler Kullanarak Veri Arama
type: docs
weight: 540
url: /tr/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Bazen verinin değeri gizlidir çünkü belirli bir biçimle biçimlendirilmiştir. Örneğin, D4 hücresinde =Sum(A1:A2) formülü varsa ve değeri 20 ise, ancak --- biçiminde biçimlendirilmişse, 20 değeri gizlidir ve Microsoft Excel'de arama seçenekleriyle bulunamaz. Ancak, Aspose.Cells kullanarak [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES) ile bulabilirsiniz.

{{% /alert %}} 
## **Orijinal Değerler Kullanarak Veri Arama**
Aşağıdaki örnek kod yukarıdaki noktayı açıklamaktadır. Microsoft Excel arama seçenekleriyle bulunamayan D4 hücresini Aspose.Cells kullanarak [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES) ile bulur. Daha fazla bilgi için kodun içindeki yorumları okuyunuz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
