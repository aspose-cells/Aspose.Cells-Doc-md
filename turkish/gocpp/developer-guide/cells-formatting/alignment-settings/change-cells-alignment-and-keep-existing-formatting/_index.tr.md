---
title: Golang kullanarak C++ ile Hücreleri Hizalama ve Mevcut Biçimlendirmeyi Koruma
description: Hücre düzenini değiştirmek ve mevcut biçimi korumak için Aspose.Cells kütüphanesini kullanın
keywords: Aspose.Cells, C++, Hücre hizalaması, mevcut biçimlendirmeyi koru
type: docs
weight: 340
url: /tr/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazen, birden çok hücrenin hizalamasını değiştirmek istersiniz ama mevcut biçimlendirmeyi de korumak istersiniz. Aspose.Cells, bu işlemi [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/) özelliği ile yapmanızı sağlar. Eğer **true** olarak ayarlarsanız, hizalamadaki değişiklikler gerçekleşir, aksi takdirde gerçekleşmez. Lütfen unutmayın, [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) nesnesi [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) metoduna parametre olarak geçirilir ve bu metod aslında hücre aralığına biçimlendirme uygular.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338585.xlsx) yükler, aralık oluşturur ve yatay ve dikey olarak ortalayıp mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338586.xlsx) karşılaştırır ve hücrelerin mevcut biçimlendirmesinin aynı olduğunu ancak hücrelerin şimdi yatay ve dikey olarak merkezlenmiş olduğunu gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
