---
title: Koşullu Biçimlendirmeyle Alternatif Satırlar ve Sütunlara Gölgelendirme Uygulayın
description: Alternatif satırlar ve sütunlar için koşullu biçimlendirme gölgeleri uygulamak üzere C#'deki Aspose.Cells kitaplığı nasıl kullanılır? Bu kriterleri ayarlayarak hücrelerin nasıl görüneceği ve görüneceği üzerinde daha fazla kontrole sahip olursunuz.
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /tr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells API'ler, koşullu biçimlendirme kurallarını ekleme ve değiştirme araçlarını sağlar.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)nesne. Bu kurallar, koşullara veya kurallara göre istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makalede, koşullu biçimlendirme kuralları ve Excel'in yerleşik işlevleri yardımıyla alternatif satırlara ve sütunlara gölgelendirme uygulamak için Aspose.Cells for .NET API'lerin kullanımı gösterilecektir.

{{% /alert %}}

Bu makalede Excel'in SATIR, SÜTUN VE MOD gibi yerleşik işlevleri kullanılmaktadır. Aşağıda verilen kod pasajının daha iyi anlaşılması için bu işlevlere ilişkin bazı ayrıntılar verilmiştir.

- **ROW()** işlevi, hücre başvurusunun satır numarasını döndürür. Referans parametresi atlanırsa, referansın SATIR fonksiyonunun girildiği hücre adresi olduğu varsayılır.
- **COLUMN()**işlevi, hücre başvurusunun sütun numarasını döndürür. Referans parametresi atlanırsa, referansın COLUMN fonksiyonunun girildiği hücre adresi olduğu varsayılır.
- **MOD()** işlevi, bir sayı bir bölene bölündükten sonra kalanı döndürür; işlevin ilk parametresi, geri kalanını bulmak istediğiniz sayısal değerdir ve ikinci parametre, sayı parametresine bölmek için kullanılan sayıdır. Bölen 0 ise #BÖL/0! değerini döndürür. hata.

Bu hedefe ulaşmak için Aspose.Cells for .NET API yardımıyla bazı kodlar yazmaya başlayalım.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Aşağıdaki anlık görüntü, Excel uygulamasına yüklenen sonuçtaki elektronik tabloyu göstermektedir.

|![yapılacak şey:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

 Gölgelendirmeyi alternatif sütunlara uygulamak için formülü değiştirmeniz yeterlidir.**=MOD(SATIR();2)=0** *=MOD(COLUMN(),2)=0** olarak, yani; satır indeksini almak yerine, sütun indeksini almak için formülü değiştirin.
Bu durumda ortaya çıkan elektronik tablo aşağıdaki gibi görünecektir.

|![yapılacak şey:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
