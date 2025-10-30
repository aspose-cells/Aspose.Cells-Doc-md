---
title: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
description: Aspose.Cells for Python via .NET kütüphanesini kullanarak hücre hizalamasını değiştirme ve mevcut biçimlendirmeyi koruma
keywords: Aspose.Cells for Python via .NET, Python Hücre hizalaması, mevcut biçimlendirmeyi koruma
type: docs
weight: 340
url: /tr/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazen, birden çok hücrenin hizalamasını değiştirmek istiyorsunuz fakat mevcut biçimlendirmeyi korumak istiyorsunuz. Aspose.Cells for Python via .NET bunu [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments) özelliği kullanarak yapmanıza olanak tanır. Eğer **true** olarak ayarlanırsa, hizalama değişiklikleri yapılır; aksi takdirde yapılmaz. Lütfen, [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) nesnesinin [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) yöntemiyle biçimlendirmeyi hücre aralığına uyguladığını unutmayın.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338585.xlsx) yükler, aralık oluşturur ve yatay ve dikey olarak ortalayıp mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338586.xlsx) karşılaştırır ve hücrelerin mevcut biçimlendirmesinin aynı olduğunu ancak hücrelerin şimdi yatay ve dikey olarak merkezlenmiş olduğunu gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
