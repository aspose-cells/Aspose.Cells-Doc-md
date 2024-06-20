---
title: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
description: Hücre düzenini değiştirmek ve mevcut biçimi korumak için Aspose.Cells kütüphanesini kullanın
keywords: Aspose.Cells, C#, Hücre düzeni, mevcut biçimi koruma
type: docs
weight: 340
url: /tr/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, hücrelerin düzenini değiştirmek isteyebilirsiniz ancak mevcut biçimi korumak istersiniz. Aspose.Cells, bu işlemi [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) özelliğini kullanarak yapmanıza olanak tanır. Eğer **true** olarak ayarlarsanız, düzen değişiklikleri yapılacaktır, aksi takdirde yapılmayacaktır. Lütfen dikkat edin, bir hücre aralığına biçimlendirme uygulayan [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) metoduna [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) nesnesi parametre olarak iletilir.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338585.xlsx) yükler, aralık oluşturur ve yatay ve dikey olarak ortalayıp mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338586.xlsx) karşılaştırır ve hücrelerin mevcut biçimlendirmesinin aynı olduğunu ancak hücrelerin şimdi yatay ve dikey olarak merkezlenmiş olduğunu gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
