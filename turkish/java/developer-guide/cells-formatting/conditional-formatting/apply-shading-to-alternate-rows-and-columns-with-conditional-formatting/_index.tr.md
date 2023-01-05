---
title: Koşullu Biçimlendirme ile Alternatif Satırlara ve Sütunlara Gölgelendirme Uygulayın
type: docs
weight: 10
url: /tr/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells API'ler, koşullu biçimlendirme kurallarını eklemek ve değiştirmek için araçlar sağlar.[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesne. Bu kurallar, koşullara veya kurallara dayalı olarak istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, koşullu biçimlendirme kuralları ve Excel'in yerleşik işlevleri yardımıyla alternatif satırlara ve sütunlara gölgeleme uygulamak için Aspose.Cells for Java API'in kullanımını gösterecektir.

{{% /alert %}} 
## **Koşullu Biçimlendirmeyi Kullanarak Alternatif Satırlara ve Sütunlara Gölgelendirme Uygulayın**
Bu makale, Excel'in SATIR, SÜTUN ve MOD gibi yerleşik işlevlerinden yararlanmaktadır. İleride sağlanan kod parçacığının daha iyi anlaşılması için bu işlevlerin küçük ayrıntılarını burada bulabilirsiniz.

- **SIRA()** işlev, bir hücre başvurusunun satır numarasını döndürür. Başvuru atlanırsa, başvurunun SATIR işlevinin girildiği hücre adresi olduğunu varsayar.
- **KOLON()**işlev, bir hücre başvurusunun sütun numarasını döndürür. Başvuru atlanırsa, başvurunun COLUMN işlevinin girildiği hücre adresi olduğu varsayılır.
- **MOD()** işlev, bir sayı bir bölenle bölündükten sonra kalanı döndürür; burada işlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değerdir ve ikinci parametre, sayı parametresine bölmek için kullanılan sayıdır. Bölen 0 ise, o zaman #SAYI/0'ı döndürür! hata.

Aspose.Cells for Java API yardımıyla hedefe ulaşmak için bazı kodlar yazmaya başlayalım.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Aşağıdaki anlık görüntü, Excel uygulamasında yüklenen sonuç elektronik tablosunu gösterir.

![yapılacaklar:resim_alternatif_metin](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

 Gölgelendirmeyi alternatif sütunlara uygulamak için tek yapmanız gereken formülü değiştirmek.**=MOD(SATIR(),2)=0** olarak**=MOD(SÜTUN(),2)=0** , yani; satır dizinini almak yerine, sütun dizinini almak için formülü değiştirin.
Ortaya çıkan elektronik tablo, bu durumda, aşağıdaki görüntü gibi görünecektir.

![yapılacaklar:resim_alternatif_metin](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
