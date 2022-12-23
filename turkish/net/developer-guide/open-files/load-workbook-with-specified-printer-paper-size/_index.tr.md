---
title: Çalışma Kitabını Belirtilen Yazıcı Kağıt Boyutuyla Yükleyin
type: docs
weight: 430
url: /tr/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 kullanarak çalışma kitabınızı yüklerken tercih ettiğiniz yazıcı kağıt boyutunu belirtebilirsiniz.[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) yöntem. MS Excel'de yeni bir dosya oluşturursanız, kağıt boyutunun makinenizdeki varsayılan yazıcının ayarıyla aynı olacağını lütfen unutmayın.

{{% /alert %}}

 Aşağıdaki örnek kod, kullanımını göstermektedir[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) yöntem. Önce bir çalışma kitabı oluşturur, ardından onu XLSX biçiminde bellek akışına kaydeder. Ardından A5 kağıt boyutunda yükler ve PDF formatında kaydeder. Ardından tekrar A3 kağıt boyutunda yükler ve tekrar PDF formatında kaydeder. Çıktı PDF'lerini açıp kağıt boyutlarını kontrol ederseniz, farklı olduklarını göreceksiniz. Biri A5, diğeri A3. Lütfen indirin[A5 çıkışı PDF](5115234.pdf) ve[A3 çıkışı PDF](5115233.pdf) referansınız için kod tarafından oluşturulur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
