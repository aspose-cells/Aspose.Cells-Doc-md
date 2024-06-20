---
title: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
type: docs
weight: 10
url: /tr/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells API'leri, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesnesi için koşullu biçimlendirme kurallarını eklemek ve değiştirmek için olanak sağlar. Bu kurallar, koşullar veya kurallara dayalı olarak istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, koşullu biçimlendirme kuralları ve Excel'in yerleşik işlevlerinin yardımıyla sıradaki satır ve sütunlara gölge uygulama Aspose.Cells for Java API'nin kullanımını gösterecektir.

{{% /alert %}} 
## **Koşullu Biçimlendirme Kullanarak Sıradaki Sütunlara Gölge Uygula**
Bu makale, ROW, COLUMN ve MOD gibi Excel'in yerleşik işlevlerinden yararlanmaktadır. İşte bu işlevler hakkında daha fazla anlayış sağlamak için sağlanan kod parçacığının daha iyi anlaşılmasına yönelik küçük ayrıntılar.

- **ROW()** işlevi, bir hücre referansının satır numarasını döndürür. Referans belirtilmemişse, ROW işlevinin girildiği hücre adresini varsayarsınız.
- **COLUMN()** işlevi, bir hücre referansının sütun numarasını döndürür. Referans belirtilmemişse, COLUMN işlevinin girildiği hücre adresini varsayarsınız.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Aspose.Cells for Java API'sinin yardımıyla hedefe ulaşmak için kod yazmaya başlayalım.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin. 
Bu durumda, elde edilen elektronik tablo aşağıdaki resimdeki gibi görünecektir.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
