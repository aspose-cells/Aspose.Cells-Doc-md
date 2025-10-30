---
title: Alternatif Satır ve Sütunlara Göre Dolgu Uygula ve Koşullu Biçimlendirme
linktitle: Alternatif Satır ve Sütunlara Gölgelendirme Uygula
description: C++ ile Aspose.Cells kütüphanesini kullanarak alternan satır ve sütunlar için gölgeli koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, C++, Alternatif Satırlar, Alternatif Sütunlar, Gölgeleme
type: docs
weight: 30
url: /tr/go-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) nesnesine koşullu biçimlendirme kuralları ekleme ve buna müdahale etme imkânı sağlar. Bu kurallar, istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, koşullu biçimlendirme kuralları ve Excel'in yerleşik fonksiyonları ile alternatif satırlar ve sütunlara gölgeleme uygulamak için Aspose.Cells for C++ API'lerinin kullanımını gösterecektir.

{{% /alert %}}

Bu makale, Excel'in yerleşik işlevleri ROW, COLUMN ve MOD'u kullanmaktadır. İleride sunulan kod örneğini daha iyi anlayabilmek için bu işlevlerin bazı ayrıntıları aşağıda verilmiştir.

- **ROW()** işlevi, bir hücre başvurusunun satır numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, ROW işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **COLUMN()** işlevi, bir hücre başvurusunun sütun numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, COLUMN işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Hedefe ulaşmak için Aspose.Cells for C++ API'si yardımıyla bazı kodlar yazmaya başlayalım.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyShadingToAlternateRowsAndColumnsWithConditionalFormatting.go" >}}
Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin. 
Bu durumda elde edilen elektronik tablo aşağıdaki gibi görünecektir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
