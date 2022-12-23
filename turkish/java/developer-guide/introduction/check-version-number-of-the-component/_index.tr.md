---
title: Bileşenin Sürüm Numarasını Kontrol Edin
type: docs
weight: 70
url: /tr/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

Bazı durumlarda, ürünün hangi sürümüne sahip olduğunuzu merak edebilirsiniz. Genellikle yeni düzeltmeler (işaret ettikleri kullanıcı senaryoları için hata düzeltmeleri) oluşturur ve bunları acil olarak ihtiyaçları doğrultusunda forumlarda yayınlarız. Sürüm numarası ana sürüm numarası, alt sürüm numarası ve düzeltme sürüm numarasından oluşur. Tanımlanan tüm bileşenler, 0'dan büyük veya 0'a eşit tam sayılar olmalıdır. Sürüm numarasının biçimi aşağıdaki gibidir:

major.minor.hotfix , bir kısmı 1 arttırıp yeni sürüm yapabiliriz. Normalde, son kısmı 1 artırırız ve kullanıcılar için forumlara göndermek için yeni bir düzeltme oluştururuz.

Bu belge, sisteminizde bileşenin hangi sürümünün kurulu olduğunu kontrol etmenin bazı yollarını açıklar.

{{% /alert %}} 
## **Sürüm numarasını kontrol etme**
### **1) Manuel Yol**
Java sürümüne/düzeltmesine (Aspose.Cells for Java) sahipseniz, Aspose.Cells kitaplık jar dosyasını açıp MANIFEST dosyasını not defteri ile açabilir ve değerini kontrol etmek için "Specification-Version:" dizisini aratabilirsiniz.

![yapılacaklar:resim_alternatif_metin](check-version-number-of-the-component_1.png)


**Figür:** Java düzeltmesinin sürüm numarası kontrol ediliyor
### **2) API'leri kullanma**
Ürünün sürüm numarasını almak için aşağıdaki API'leri de kullanabilirsiniz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

