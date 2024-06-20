---
title: Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle
type: docs
weight: 790
url: /tr/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Yüklerken çalışma kitabınıza istediğiniz yazıcı kağıdı boyutunu [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) yöntemini kullanarak belirleyebilirsiniz. Lütfen not edin, eğer bir dosya MS Excel'de oluşturursanız, kağıt boyutunun, makinenizdeki varsayılan yazıcı ayarına bağlı olduğunu göreceksiniz.

{{% /alert %}} 
## **Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle**
Aşağıdaki örnek kod, [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) yönteminin kullanımını göstermektedir. Öncelikle bir çalışma kitabı oluşturur, ardından XLSX formatında bir byte dizisi akışında kaydeder. Daha sonra bunu A5 kağıt boyutuyla yükler ve PDF formatında kaydeder. Sonra bunu tekrar A3 kağıt boyutuyla yükler ve tekrar PDF formatında kaydeder. Çıktı PDF'leri açar ve kağıt boyutlarını kontrol ederseniz, farklı olduklarını göreceksiniz. Bir tanesi A5, diğeri A3'dür. Referans için kod tarafından üretilen [A5 çıktı PDF'si](5473435.pdf) ve [A3 çıktı PDF'si](5473436.pdf)'ni indirin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
