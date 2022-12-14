---
title: Adlandırılmış Aralıkları Biçimlendirin ve Değiştirin
type: docs
weight: 85
url: /tr/net/format-and-modify-named-ranges/
---
## **Aralıkları Biçimlendir**

### **Arka Plan Rengini ve Yazı Tipi Niteliklerini Adlandırılmış Aralığa Ayarlama**

 Biçimlendirmeyi uygulamak için bir tanımlayın[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) stil ayarlarını belirlemek ve onu nesneye uygulamak için nesne[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range)nesne.

Aşağıdaki örnek, yazı tipi ayarlarıyla düz dolgu renginin (gölgeleme rengi) bir aralığa nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Adlandırılmış Aralığa Kenarlıklar Ekleme**

 Tek bir hücre yerine bir dizi hücreye kenarlık eklemek mümkündür. bu[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne sağlar[**SetOutlineSınır**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)hücre aralığına kenarlık eklemek için aşağıdaki parametreleri alan yöntem:

-  Kenarlık türü, kenarlık türü,[**Kenarlık Türü**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)numaralandırma.
-  Çizgi stili, çizgi stili,[**Hücre Sınır Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)numaralandırma.
- Renk, renk numaralandırmasından seçilen çizgi rengi.

Aşağıdaki örnek, bir aralığa anahat kenarlığının nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Aşağıdaki örnek, aralıktaki her bir hücrenin etrafına kenarlıkların nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Adlandırılmış Aralığı Yeniden Adlandırma**

 Aspose.Cells, ihtiyacınıza göre adlandırılmış bir aralığı yeniden adlandırmanızı sağlar. Adlandırılmış aralığı alabilir ve kullanarak yeniden adlandırabilirsiniz.[**İsim.Metin**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)bağlanmak. Aşağıdaki örnek, adlandırılmış bir aralığın nasıl yeniden adlandırılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Menzil Birliği**

 Aspose.Cells sağlar[**Menzil.Birlik**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)Aralıklar için birliği alma yöntemi, yöntem bir döndürür[*Dizi Listesi*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)nesne. Aşağıdaki örnek, aralıklar için birleşimin nasıl alınacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Aralıkların Kesişimi**

 Aspose.Cells şunları sağlar:[**Menzil.Kesişim**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) iki aralığı kesiştirme yöntemi. Yöntem bir döndürür[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne. Bir aralığın başka bir aralıkla kesişip kesişmediğini kontrol etmek için[**Menzil.Kesişim**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)bir Boole değeri döndüren yöntem. Aşağıdaki örnek, aralıkların nasıl kesişeceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Cells'i Adlandırılmış Aralıkta Birleştirme**

 Aspose.Cells sağlar[**Aralık.Birleştirme()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)aralıktaki hücreleri birleştirme yöntemi. Aşağıdaki örnek, adlandırılmış bir aralığın tek tek hücrelerinin nasıl birleştirileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Adlandırılmış Aralığı Kaldırma**

 Aspose.Cells şunları sağlar:[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) aralığın adını silme yöntemi. Aralığın içeriğini temizlemek için şunu kullanın:[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)yöntem. Aşağıdaki örnek, adlandırılmış bir aralığın içeriğiyle birlikte nasıl kaldırılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
