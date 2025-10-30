---
title: Biçimlendirme ve Adlandırılmış Aralıkları Düzenleme
type: docs
weight: 85
url: /tr/python-net/format-and-modify-named-ranges/
description: Bu makale, Aspose.Cells for Python via .NET API sı ile Adlandırılmış Aralıkları Biçimlendirme ve Değiştirme işlemlerini göstermektedir.
keywords: Python Excel Kütüphanesi, Python Adlandırılmış Aralıkları Biçimlendirme ve Değiştirme, Python Aralığa Arka Plan Rengi ve Yazı Tipi Öznitelikleri Ayarlama, Python Adlandırılmış Aralığa Kenarlık Ekleme, Python Bir Adlandırılmış Aralığı Yeniden Adlandırma, Python Aralıkların Birleşimi, Python Aralıkların Kesişimi, Python Adlandırılmış Aralıktaki Hücreleri Birleştirme.
---

## **Aralıkları Biçimlendirme**

### **Bir Adlandırılmış Aralığa Arka Plan Rengi ve Yazı Tipi Öznitelikleri Nasıl Ayarlanır**

Biçimlendirme uygulamak için, stil ayarlarını belirtmek için bir [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesi tanımlayın ve ardından bu ayarları [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesine uygulayın.

Aşağıdaki örnek, bir aralığa katı doldurmalı rengi (gölge rengi) ve yazı tipi ayarlarını nasıl ayarlayacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Bir Adlandırılmış Aralığa Kenarlık Ekleme**

Yalnızca tek bir hücre değil, bir hücre aralığına sınırlar eklemek mümkündür. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesi, hücre aralığına sınır eklemek için aşağıdaki parametreleri alabilen bir [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) yöntemi sağlar.

- Kenar tipi, [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) numaralandırmasından seçilen kenar tipi.
- Çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) numaralandırmasından seçilen çizgi stili.
- Renk, Renk numaralandırmasından seçilen çizgi rengi.

Aşağıdaki örnek, bir aralığa kenarlık eklemeyi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Bir Adlandırılmış Aralığı Yeniden Adlandırma**

Aspose.Cells, bir adınızı yeniden adlandırmak için olanak tanır. Adı alabilir ve [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text) özniteliğini kullanarak yeniden adlandırabilirsiniz. Aşağıdaki örnek, bir adını yeniden adlandırmanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Aralıkların Birleşimi Nasıl Alınır**

Aspose.Cells, aralıkların birleşimi için [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) yöntemi sağlar. Aşağıdaki örnek, aralıkların birleşimi için nasıl kullanılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Aralıkların Kesişimini Nasıl Hesaplanır**

Aspose.Cells, iki aralığın kesişimini belirlemek için [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) yöntemini sağlar. Yöntem bir [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesi döndürür. Bir aralığın başka bir aralıkla kesişip kesişmediğini kontrol etmek için [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) yöntemini kullanın, bu yöntem bir Boolean değeri döndürür. Aşağıdaki örnek, aralıkların nasıl kesiştirileceğini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Adlandırılmış Aralıktaki Hücreleri Birleştirmek**

Aspose.Cells, aralıktaki hücreleri birleştirmek için bir [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) yöntemi sağlar. Aşağıdaki örnek, bir isimlendirilmiş aralıktaki bireysel hücrelerin nasıl birleştirileceğini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
