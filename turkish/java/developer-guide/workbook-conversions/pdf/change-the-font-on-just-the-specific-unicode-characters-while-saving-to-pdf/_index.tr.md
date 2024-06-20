---
title: PDF ye kaydederken belirli Unicode karakterlerinin yazı tipini değiştirin
type: docs
weight: 150
url: /tr/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Bazı Unicode karakterleri, kullanıcı tarafından belirtilen font tarafından görüntülenemez. Bu tür bir Unicode karakter **Bilinmeyen Kesme** (U+2011)'dır ve Unicode numarası 8209'dur. Bu karakter **Times New Roman** ile görüntülenemez, ancak **Arial Unicode MS** gibi diğer fontlarla görüntülenebilir.

Böyle bir karakter belirli bir fontta, örneğin Times New Roman'da meydana geldiğinde, Aspose.Cells bu karakteri görüntüleyebilen Arial Unicode MS gibi bir fonta değiştirir. Ancak, bu, bazı kullanıcılar için istenmeyen bir davranıştır ve yalnızca belirli karakterin fontunu değiştirmek istemektedirler.

Bu sorunu ele almak için, Aspose.Cells {0} özelliğini sağlar ve yalnızca görüntülenemeyen özel karakterin fontunun değiştirilmesi ve kelimenin/paragrafın geri kalanı için aynı fontun kalması gerektiği için **true** olarak ayarlanmalıdır.

Örnek

{{% /alert %}}

## **Örnek**

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kod tarafından oluşturulan iki çıktı PDF'yi karşılaştırır. Birincisi [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) özelliği ayarlanmadan oluşturulmuştu ve diğeri [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) özelliğine **true** olarak ayarlandıktan sonra oluşturulmuştu. Önceki PDF'de, Tüm cümle Times New Roman'dan Arial Unicode MS'ye dönüştü çünkü Bilinmeyen Kesme nedeniyle. İkinci PDF'de ise, yalnızca Bilinmeyen Kesme'nin fontu değişmişti.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
