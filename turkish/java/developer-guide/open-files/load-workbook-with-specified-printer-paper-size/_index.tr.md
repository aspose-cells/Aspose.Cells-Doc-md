---
title: Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle
type: docs
weight: 790
url: /tr/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Çalışma kitabınızı yüklerken, seçtiğiniz yazıcı kağıt boyutunu [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-) yöntemi ile belirleyebilirsiniz. Lütfen unutmayın, yeni bir dosya oluşturduğunuzda, kağıt boyutunun bilgisayarınızdaki varsayılan yazıcı ayarlarıyla aynı olduğunu görürsünüz.

{{% /alert %}} 
## **Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle**
Aşağıdaki örnek kod, [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-) metodunun kullanımını gösterir. Öncelikle bir çalışma kitabı oluşturur, sonra bu kitabı XLSX formatında bayt dizisi akışına kaydeder. Daha sonra A5 kağıt boyutuyla yükler ve PDF formatında kaydeder. Ardından tekrar A3 kağıt boyutuyla yükler ve yeniden PDF olarak kaydeder. Çıkış PDF'leri açıp kağıt boyutlarını kontrol ederseniz, farklı olduklarını göreceksiniz. Birisi A5, diğeri A3. Lütfen, kod tarafından oluşturulan [A5 çıkış PDF](5473435.pdf) ve [A3 çıkış PDF](5473436.pdf)’yi indirerek inceleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
