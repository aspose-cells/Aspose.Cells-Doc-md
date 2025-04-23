---
title: Hücrenin Zengin Metin Kısımlarına Erişim ve Güncelleme
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 440
url: /tr/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells, hücrenin zengin metninin bölümlerine erişmenizi ve güncellemenizi sağlar. Bu amaçla, Cell.getCharacters() ve Cell.setCharacters() metotlarını kullanabilirsiniz. Bu metotlar, font adı, font rengi, kalın olma vb. gibi fontun çeşitli özelliklerine erişmeniz ve bunları güncellemeniz için kullanabileceğiniz FontSetting nesnelerinin dizisini döndürecek ve kabul edecektir.

{{% /alert %}} 
## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**
Aşağıdaki kod, [kaynak excel dosyasını](5472937.xlsx) kullanarak Cell.getCharacters() ve Cell.setCharacters() metodlarının kullanımını gösterir. Kaynak excel dosyasında A1 hücresinde zengin metin bulunmaktadır. 3 kısmı vardır ve her bir kısmı farklı bir yazı tipine sahiptir. Bu kısımlara erişeceğiz ve ilk kısmı yeni yazı tipi ile güncelleyeceğiz. Son olarak, çalışma kitabını [çıktı excel dosyası](5472930.xlsx) olarak kaydeder. Bu dosyayı açtığınızda, metnin ilk kısmının yazı tipinin **"Arial"** olarak değiştiğini göreceksiniz.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı için [kaynak excel dosyası](5472937.xlsx) kullanılarak konsol çıktısı verilmiştir.

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
