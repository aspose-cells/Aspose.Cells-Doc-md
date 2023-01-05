---
title: Orijinal Değerleri Kullanarak Veri Arama
type: docs
weight: 540
url: /tr/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

 Bazen bir şekilde biçimlendirildiği için verilerin değeri gizlenir. Örneğin, D4 hücresinin =Topla(A1:A2) formülüne sahip olduğunu ve değerinin 20 olduğunu ancak --- olarak biçimlendirildiğini varsayalım, bu durumda 20 değeri gizlenir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Ancak, kullanarak Aspose.Cells kullanarak bulabilirsiniz.[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Orijinal Değerleri Kullanarak Veri Arama**
 Aşağıdaki örnek kod, yukarıdaki noktayı göstermektedir. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan ancak Aspose.Cells kullanılarak bulunamayan D4 hücresini bulur.[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Lütfen daha fazla bilgi için kodun içindeki yorumları okuyun.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsol Çıkışı**
İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
