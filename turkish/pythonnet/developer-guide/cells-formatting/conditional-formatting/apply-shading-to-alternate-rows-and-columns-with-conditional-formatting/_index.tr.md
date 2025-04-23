---
title: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
description: Aspose.Cells kütüphanesini Python da kullanarak sıralı satırlar ve sütunlar için gölgelendirme koşullu biçimlendirme uygulama. Bu kriterleri ayarlayarak, hücrelerin görünümüne ve görünüşüne daha fazla kontrol sahibi olursunuz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Python Alternatif Satırlar, Alternatif Sütunlar, Gölgeleme
type: docs
weight: 30
url: /tr/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET API'leri, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) nesnesi için koşullu biçimlendirme kuralları ekleme ve yönetme imkanı sağlar. Bu kurallar, koşullara veya kurallara dayalı olarak istenilen biçimlendirmeyi almak için çeşitli şekillerde uyarlanabilir. Bu makale, Aspose.Cells for Python via .NET API'lerini kullanarak koşullu biçimlendirme kurallarıyla alternatifi satıralara ve sütunlara gölgeleme uygulamayı gösterecek ve Excel'in yerleşik fonksiyonlerini kullanacaktır.

{{% /alert %}}

Bu makale, Excel'in yerleşik işlevleri ROW, COLUMN ve MOD'u kullanmaktadır. İleride sunulan kod örneğini daha iyi anlayabilmek için bu işlevlerin bazı ayrıntıları aşağıda verilmiştir.

- **ROW()** işlevi, bir hücre başvurusunun satır numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, ROW işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **COLUMN()** işlevi, bir hücre başvurusunun sütun numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, COLUMN işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Bu hedefe ulaşmak için biraz kod yazmaya başlayalım, Aspose.Cells for Python via .NET API'sinin yardımıyla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyShadingToAlternateRowsColumns-1.py" >}}

Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

|![todo:image_alt_text](1.png)|
| :- |

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin. 
Bu durumda elde edilen elektronik tablo aşağıdaki gibi görünecektir.

|![todo:image_alt_text](2.png)|
| :- |

