---
title: PDF'ye kaydederken Yazı Tipini yalnızca belirli Unicode karakterlerinde değiştirin
type: docs
weight: 150
url: /tr/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Bazı Unicode karakterler, kullanıcı tarafından belirlenen yazı tipi tarafından görüntülenemez. Böyle bir Unicode karakter**Bölünemez Tire** (U+2011) ve Unicode numarası 8209'dur. Bu karakter ile görüntülenemez.**Times New Roman** , ancak diğer yazı tipleriyle birlikte görüntülenebilir.**Arial Unicode MS**.

Böyle bir karakter, Times New Roman gibi belirli bir yazı tipinde olan bir kelime veya cümlenin içinde geçtiğinde, Aspose.Cells, tüm kelimenin veya cümlenin yazı tipini, bu karakteri Arial Unicode gibi MS'e görüntüleyebilecek yazı tipine değiştirir.

Ancak bu, bazı kullanıcılar için istenmeyen bir davranıştır ve tüm kelime veya cümlenin yazı tipini değiştirmek yerine yalnızca belirli bir karakterin yazı tipinin değiştirilmesini isterler.

 Bu sorunla başa çıkmak için Aspose.Cells şunları sağlar:[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) ayarlanması gereken özellik**doğru**böylece yalnızca görüntülenemeyen belirli karakterin yazı tipi değiştirilir ve kelimenin veya cümlenin geri kalanı için yazı tipi aynı kalır.

{{% /alert %}}

## **Örnek**

 Aşağıdaki ekran görüntüsü, aşağıdaki örnek kod tarafından oluşturulan iki çıktı PDF'sini karşılaştırır. Biri ayar yapılmadan oluşturuldu[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) özellik ve diğeri ayarlandıktan sonra oluşturuldu[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) mülkiyet**doğru**. İlk PDF'de görebileceğiniz gibi, Non-Breaking Tire nedeniyle tüm cümlenin yazı tipi Times New Roman'dan Arial Unicode MS'ye değişti. İkinci PDF'de ise, yalnızca Bölünemez Tire'nin yazı tipi değişti.

![yapılacaklar:resim_alternatif_Metin](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
