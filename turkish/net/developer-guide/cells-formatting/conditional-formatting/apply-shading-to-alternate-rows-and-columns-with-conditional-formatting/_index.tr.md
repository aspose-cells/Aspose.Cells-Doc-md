---
title: Koşullu Biçimlendirme ile Alternatif Satırlara ve Sütunlara Gölgelendirme Uygulayın
type: docs
weight: 30
url: /tr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells API'ler, koşullu biçimlendirme kurallarını eklemek ve değiştirmek için araçlar sağlar.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)nesne. Bu kurallar, koşullara veya kurallara dayalı olarak istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, koşullu biçimlendirme kuralları ve Excel'in yerleşik işlevleri yardımıyla alternatif satırlara ve sütunlara gölgeleme uygulamak için Aspose.Cells for .NET API'lerin kullanımını gösterecektir.

{{% /alert %}}

Bu makale, Excel'in SATIR, SÜTUN ve MOD gibi yerleşik işlevlerinden yararlanmaktadır. Aşağıda, ileride sağlanan kod parçacığının daha iyi anlaşılması için bu işlevlerin bazı ayrıntıları verilmiştir.

- **SIRA()** işlev, bir hücre başvurusunun satır numarasını döndürür. Referans parametresi atlanırsa, referansın SATIR fonksiyonunun girildiği hücre adresi olduğu varsayılır.
- **KOLON()** işlev, bir hücre başvurusunun sütun numarasını döndürür. Başvuru parametresi atlanırsa, başvurunun COLUMN işlevinin girildiği hücre adresi olduğunu varsayar.
- **MOD()** işlev, bir sayı bir bölenle bölündükten sonra kalanı döndürür; burada işlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değerdir ve ikinci parametre, sayı parametresine bölmek için kullanılan sayıdır. Bölen 0 ise, o zaman #SAYI/0'ı döndürür! hata.

Aspose.Cells for .NET API yardımıyla bu amacı gerçekleştirmek için biraz kod yazmaya başlayalım.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Aşağıdaki anlık görüntü, Excel uygulamasında yüklenen sonuç elektronik tablosunu gösterir.

|![yapılacaklar:resim_alternatif_Metin](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
|:- |

 Gölgelendirmeyi alternatif sütunlara uygulamak için tek yapmanız gereken formülü değiştirmek.**=MOD(SATIR(),2)=0** olarak**=MOD(SÜTUN(),2)=0** , yani; satır dizinini almak yerine, sütun dizinini almak için formülü değiştirin.
Ortaya çıkan elektronik tablo, bu durumda, aşağıdaki gibi görünecektir.

|![yapılacaklar:resim_alternatif_Metin](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
|:- |
