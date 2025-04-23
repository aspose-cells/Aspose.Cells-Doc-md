---
title: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
description: Aspose.Cells kitaplığını C# kullanarak koşullu biçimlendirmeleri sırasıyla satır ve sütunlara uygulama. Bu kriterleri ayarlayarak, hücrelerin görünümlerini ve görünümlerini daha fazla kontrol edebilirsiniz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, C#, Sıralı Satırlar, Sıralı Sütunlar, Gölge
type: docs
weight: 30
url: /tr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, koşullu biçimlendirme kurallarını [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesnesi için eklemek ve işlemek için olanak sağlar. Bu kurallar, koşullara veya kurallara dayalı istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, **Aspose.Cells for .NET** API'lerini kullanarak koşullu biçimlendirme kurallarını kullanarak alternatif satır ve sütunlara gölge uygulamanın nasıl olduğunu gösterecektir.

{{% /alert %}}

Bu makale, Excel'in yerleşik işlevleri ROW, COLUMN ve MOD'u kullanmaktadır. İleride sunulan kod örneğini daha iyi anlayabilmek için bu işlevlerin bazı ayrıntıları aşağıda verilmiştir.

- **ROW()** işlevi, bir hücre başvurusunun satır numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, ROW işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **COLUMN()** işlevi, bir hücre başvurusunun sütun numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, COLUMN işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Hadi, Aspose.Cells for .NET API'sının yardımıyla bu hedefe ulaşmak için biraz kod yazmaya başlayalım.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin. 
Bu durumda elde edilen elektronik tablo aşağıdaki gibi görünecektir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
