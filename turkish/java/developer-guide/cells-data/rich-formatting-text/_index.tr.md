---
title: Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 440
url: /tr/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells, hücrenin zengin metin bölümlerine erişmenizi ve bunları güncellemenizi sağlar. Bunun için Cell.getCharacters() ve Cell.setCharacters() metodlarını kullanabilirsiniz. Bu yöntemler, yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi yazı tipinin çeşitli özelliklerine erişmek ve güncellemek için kullanabileceğiniz FontSetting nesneleri dizisini döndürür ve kabul eder.

{{% /alert %}} 
## **Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin**
 Aşağıdaki kod, Cell.getCharacters() ve Cell.setCharacters() yönteminin kullanımını gösterir.[kaynak excel dosyası](5472937.xlsx) verilen bağlantıdan indirebilirsiniz. Kaynak excel dosyasının A1 hücresinde zengin bir metin var. 3 bölümden oluşur ve her bölümün yazı tipi farklıdır. Bu bölümlere erişeceğiz ve ilk bölümü yeni yazı tipi adıyla güncelleyeceğiz. Sonunda çalışma kitabını şu şekilde kaydeder:[çıktı excel dosyası](5472930.xlsx) . Açtığınızda, metnin ilk bölümünün yazı tipinin şu şekilde değiştiğini göreceksiniz:**"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Konsol Çıkışı**
 İşte yukarıdaki örnek kodun konsol çıktısı[kaynak excel dosyası](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
