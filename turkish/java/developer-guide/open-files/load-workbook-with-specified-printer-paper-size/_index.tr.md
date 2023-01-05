---
title: Çalışma Kitabını Belirtilen Yazıcı Kağıt Boyutuyla Yükleyin
type: docs
weight: 790
url: /tr/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 kullanarak çalışma kitabınızı yüklerken tercih ettiğiniz yazıcı kağıt boyutunu belirtebilirsiniz.[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) yöntem. MS Excel'de yeni bir dosya oluşturursanız, kağıt boyutunun makinenizdeki varsayılan yazıcı ayarıyla aynı olacağını lütfen unutmayın.

{{% /alert %}} 
## **Çalışma Kitabını Belirtilen Yazıcı Kağıt Boyutuyla Yükleyin**
 Aşağıdaki örnek kod, kullanımını göstermektedir[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) yöntem. Önce bir çalışma kitabı oluşturur, ardından onu XLSX biçiminde bayt dizisi akışında kaydeder. Ardından A5 kağıt boyutunda yükler ve PDF formatında kaydeder. Ardından tekrar A3 kağıt boyutunda yükler ve tekrar PDF formatında kaydeder. Çıktı PDF'lerini açıp kağıt boyutlarını kontrol ederseniz, farklı olduklarını göreceksiniz. Biri A5, diğeri A3. Lütfen indirin[A5 çıkışı PDF](5473435.pdf) ve[A3 çıkışı PDF](5473436.pdf) referansınız için kod tarafından oluşturulur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
