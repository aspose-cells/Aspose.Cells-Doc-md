---
title: Bileşenin Sürüm Numarasını Kontrol Et
type: docs
weight: 70
url: /tr/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

Bazı durumlarda, ürünün hangi sürümüne sahip olduğunuzu merak edebilirsiniz. Sıklıkla, yeni düzeltmeler oluşturur (kullanıcı senaryoları için hata düzeltmeleri) ve bunları kullanıcıların acil ihtiyaçlarına karşı forumlara göndeririz. Sürüm numarası, ana sürüm numarası, yan sürüm numarası ve hata düzeltme sürüm numarasından oluşur. Tüm tanımlı bileşenler 0 veya daha büyük tamsayılar olmalıdır. Sürüm numarasının formatı şöyledir:

ana.yan.hataDüzeltme, bir kısmı 1 artırabilir ve yeni bir sürüm oluşturabiliriz. Genellikle en son parçayı 1 arttırır ve kullanıcılar için yeni bir düzeltme oluşturarak bunu forumlara göndeririz.

Bu belge, bileşenin hangi sürümünün sistemde yüklü olduğunu kontrol etmenin bazı yollarını açıklar.

{{% /alert %}} 
## **Sürüm numarasını kontrol etme**
### **1) El ile Yöntem**
Java sürüm/düzeltmeniz varsa (Aspose.Cells for Java), Aspose.Cells kitaplık jar dosyasını klasörden çıkarabilir, MANIFEST dosyasını notepad ile açabilir ve 'Specification-Version: ' dizesini arayarak değerini kontrol edebilirsiniz.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Şekil:** Java düzeltmesinin sürüm numarasını kontrol etme
### **2) API'leri Kullanma**
Ürünün sürüm numarasını almak için aşağıdaki API'leri de kullanabilirsiniz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

{{< app/cells/assistant language="java" >}}
