---
title: Orijinal Değerler Kullanarak Veri Arama
type: docs
weight: 380
url: /tr/python-net/search-data-using-original-values/
description: Aspose.Cells for Python via .NET API si aracılığıyla Orijinal Değerleri Kullanarak Veri Arama konusunu öğrenin.
keywords: Python Excel Kütüphanesi, Orijinal Değerleri Kullanarak Veri Arama, Orijinal Değerleri Kullanarak Veri Bulma
---

{{% alert color="primary" %}}

Bazen verinin değeri bir şekilde biçimlendirildiği için gizlidir. Örneğin, D4 hücresinin formülü =Sum(A1:A2) ve değeri 20 ise ancak --- şeklinde biçimlendirilmişse, değer 20 gizlidir ve Microsoft Excel bulma seçeneklerini kullanarak bulunamaz. Ancak Aspose.Cells for Python via .NET kullanarak bulunabilir. [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype) kullanarak.

{{% /alert %}}

Aşağıdaki örnek kod yukarıdaki noktayı açıklar. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan D4 hücresini [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype) kullanarak bulur ancak Aspose.Cells kullanarak bulabilir. Daha fazla bilgi için kod içindeki yorumları okuyun.

## Python kodu kullanarak orijinal değerleri kullanarak veri aramak

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
