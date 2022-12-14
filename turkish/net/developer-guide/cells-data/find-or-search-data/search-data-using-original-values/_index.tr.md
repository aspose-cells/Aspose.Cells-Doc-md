---
title: Orijinal Değerleri Kullanarak Veri Arama
type: docs
weight: 380
url: /tr/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 Bazen bir şekilde biçimlendirildiği için verilerin değeri gizlenir. Örneğin, D4 hücresinin =Topla(A1:A2) formülüne sahip olduğunu ve değerinin 20 olduğunu ancak --- olarak biçimlendirildiğini varsayalım, bu durumda 20 değeri gizlenir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Ancak, kullanarak Aspose.Cells kullanarak bulabilirsiniz.[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Aşağıdaki örnek kod, yukarıdaki noktayı göstermektedir. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan ancak Aspose.Cells kullanılarak bulunamayan D4 hücresini bulur.[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Lütfen daha fazla bilgi için kodun içindeki yorumları okuyun.

## Orijinal değerleri kullanarak veri aramak için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Örnek kod tarafından oluşturulan konsol çıktısı

İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
