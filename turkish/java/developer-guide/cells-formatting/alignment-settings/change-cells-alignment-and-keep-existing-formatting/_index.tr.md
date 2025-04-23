---
title: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
type: docs
weight: 260
url: /tr/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazen, birden çok hücrenin hizasını değiştirmek isteyebilirsiniz ancak mevcut biçimlendirmeyi korumak isteyebilirsiniz. Aspose.Cells bu işlemi [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) özelliğini kullanarak gerçekleştirmenize olanak tanır. Eğer **true** değerini ayarlarsanız, hizasındaki değişiklikler gerçekleşecek aksi halde gerçekleşmeyecektir. Lütfen dikkat edin, [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) nesnesi [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) metoduna parametre olarak iletilmektedir ve aslında hücrelerin aralığına biçimlendirme uygular.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338592.xlsx) yükler, aralık oluşturur, yatay ve dikey olarak merkezi hizaya getirir ve mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338591.xlsx) karşılaştırır ve tüm hücrelerin mevcut biçimlendirmesinin aynı olduğunu, ancak hücrelerin artık yatay ve dikey olarak merkez hizalandığını gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
{{< app/cells/assistant language="java" >}}
