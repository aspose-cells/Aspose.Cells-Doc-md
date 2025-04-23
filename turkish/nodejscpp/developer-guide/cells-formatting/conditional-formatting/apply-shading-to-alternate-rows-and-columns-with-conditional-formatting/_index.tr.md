---
title: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
linktitle: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
description: Node.js de C++ kullanarak Aspose.Cells kitaplığını, ardışık satır ve sütunlar için gölge uygulamak amacıyla koşullu biçimlendirme gölgeleri nasıl kullanılır. Bu kriterleri ayarlayarak, hücrelerin görünüşü ve görüntüsü üzerinde daha fazla kontrol sahibi olabilirsiniz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Node.js C++ üzerinden, Alternatif Satırlar, Alternatif Sütunlar, Gölge
type: docs
weight: 30
url: /tr/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) nesnesi için koşullu biçimlendirme kuralları eklemek ve bunları değiştirmek için araçlar sağlar. Bu kurallar, koşullara veya kurallara dayalı olarak istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, koşullu biçimlendirme kuralları ve Excel'in yerleşik fonksiyonleri yardımıyla alternatif satır ve sütunlara gölge uygulamak için Aspose.Cells for Node.js via C++ API'lerini kullanmayı gösterecektir.

{{% /alert %}}

Bu makale, Excel'in yerleşik işlevleri ROW, COLUMN ve MOD'u kullanmaktadır. İleride sunulan kod örneğini daha iyi anlayabilmek için bu işlevlerin bazı ayrıntıları aşağıda verilmiştir.

- **ROW()** fonksiyonu, bir hücre referansının satır numarasını döner. Referans parametresi belirtilmediyse, fonksiyonun girildiği hücrenin adresi referans alınır.
- **COLUMN()** fonksiyonu, bir hücre referansının sütun numarasını döner. Referans parametresi belirtilmediyse, fonksiyonun girildiği hücrenin adresi referans alınır.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Bu hedefe ulaşmak için bazı kodlar yazmaya başlayalım ve Aspose.Cells for Node.js via C++ API'sinden yardım alalım.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin.  
Bu durumda elde edilen elektronik tablo aşağıdaki gibi görünecektir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
