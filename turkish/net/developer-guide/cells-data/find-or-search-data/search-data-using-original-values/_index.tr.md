---
title: Orijinal Değerler Kullanarak Veri Arama
type: docs
weight: 380
url: /tr/net/search-data-using-original-values/
description: Aspose.Cells for .NET API aracılığıyla Orijinal Değerleri Kullanarak Veri Aramayı Öğrenin.
keywords: Orijinal Değerleri Kullanarak Veri Arama, Orijinal Değerleri Kullanarak Veri Bulma, Orijinal Değerlerle Veri Arama, Orijinal Değerlerle Veri Bulma
---

{{% alert color="primary" %}}

Bazen verinin değeri bazı şekilde biçimlendirildiği için gizlidir. Örneğin, D4 hücresinin değeri =Sum(A1:A2) ve değeri 20'dir ancak --- olarak biçimlendirilmiştir, bu nedenle 20 değeri gizlidir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Bununla birlikte, Aspose.Cells kullanarak [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) kullanarak bulunabilir.

{{% /alert %}}

Aşağıdaki örnek kod yukarıdaki noktayı açıklar. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan D4 hücresini [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) kullanarak bulur ancak Aspose.Cells kullanarak bulabilir. Daha fazla bilgi için kod içindeki yorumları okuyun.

Orijinal değerleri kullanarak veri aramak için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
