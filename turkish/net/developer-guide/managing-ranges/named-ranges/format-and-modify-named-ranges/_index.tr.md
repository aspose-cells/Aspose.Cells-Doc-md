---
title: Biçimlendirme ve Adlandırılmış Aralıkları Düzenleme
type: docs
weight: 85
url: /tr/net/format-and-modify-named-ranges/
---

## **Aralıkları Biçimlendirme**

### **Bir Adlandırılmış Aralığa Arkaplan Rengi ve Yazı Tipi Ayarlarını Tanımlama**

Biçimlendirme uygulamak için, stil ayarlarını belirtmek için bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi tanımlayın ve ardından bu ayarları [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesine uygulayın.

Aşağıdaki örnek, bir aralığa katı doldurmalı rengi (gölge rengi) ve yazı tipi ayarlarını nasıl ayarlayacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Bir Adlandırılmış Aralığa Sınırlar Ekleme**

Yalnızca tek bir hücre değil, bir hücre aralığına sınırlar eklemek mümkündür. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesi, hücre aralığına sınır eklemek için aşağıdaki parametreleri alabilen bir [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) yöntemi sağlar.

- Kenar tipi, [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) numaralandırmasından seçilen kenar tipi.
- Çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) numaralandırmasından seçilen çizgi stili.
- Renk, Renk numaralandırmasından seçilen çizgi rengi.

Aşağıdaki örnek, bir aralığa kenarlık eklemeyi gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Aşağıdaki örnek, aralıktaki her hücreye sınırların nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **İsimlendirilmiş Bir Aralığı Yeniden Adlandır**

Aspose.Cells, bir adınızı yeniden adlandırmak için olanak tanır. Adı alabilir ve [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text) özniteliğini kullanarak yeniden adlandırabilirsiniz. Aşağıdaki örnek, bir adını yeniden adlandırmanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Aralıkların Birleşimi**

Aspose.Cells, aralıkların birleşimini almaya yönelik bir [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) yöntemi sağlar, yöntem bir [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8) nesnesi döndürür. Aşağıdaki örnek, aralıkların birleşimini almanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Aralıkların Kesişimi**

Aspose.Cells, iki aralığın kesişimini belirlemek için [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) yöntemini sağlar. Yöntem bir [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesi döndürür. Bir aralığın başka bir aralıkla kesişip kesişmediğini kontrol etmek için [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) yöntemini kullanın, bu yöntem bir Boolean değeri döndürür. Aşağıdaki örnek, aralıkların nasıl kesiştirileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **İsimlendirilmiş Aralıklarda Hücreleri Birleştirme**

Aspose.Cells, aralıktaki hücreleri birleştirmek için bir [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) yöntemi sağlar. Aşağıdaki örnek, bir isimlendirilmiş aralıktaki bireysel hücrelerin nasıl birleştirileceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Adlandırılmış Bir Aralığı Kaldır**

Aspose.Cells, isimlendirdiğiniz aralığın adını silmeniz için [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) yöntemini sağlar. Aralığın içeriğini temizlemek için [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index) yöntemini kullanın. Aşağıdaki örnek, bir adlandırılmış aralığı nasıl kaldıracağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
