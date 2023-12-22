---
title: Orijinal Değerleri Kullanarak Veri Arama
type: docs
weight: 380
url: /tr/net/search-data-using-original-values/
description: Aspose.Cells for .NET API numaralı telefondan Orijinal Değerleri Kullanarak Veri Aramayı öğrenin.
keywords: Search Data using Original Values, Find Data using Original Values, Search Data by Original Values, Find Data by Original Values
---
{{% alert color="primary" %}}

 Bazen verinin değeri bir şekilde biçimlendirildiğinden dolayı gizlenir. Örneğin, D4 hücresinin =Toplam(A1:A2) formülüne sahip olduğunu ve değerinin 20 olduğunu ancak --- olarak biçimlendirildiğini varsayalım; bu durumda 20 değeri gizlenir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Ancak Aspose.Cells'i kullanarak bulabilirsiniz.[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Aşağıdaki örnek kod yukarıdaki noktayı göstermektedir. Microsoft Excel bulma seçeneklerini kullanarak bulunamayan D4 hücresini bulur ancak Aspose.Cells kullanarak bulabilir.[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Daha fazla bilgi için lütfen kodun içindeki yorumları okuyun.

##  Orijinal değerleri kullanarak veri aramak için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Örnek kod tarafından oluşturulan konsol çıktısı

Yukarıdaki örnek kodun konsol çıktısı aşağıdadır.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
