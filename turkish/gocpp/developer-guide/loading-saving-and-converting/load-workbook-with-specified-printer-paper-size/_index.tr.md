---
title: Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle
type: docs
weight: 430
url: /tr/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Çalışma kitabınızı [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/) yöntemiyle yüklerken yazıcı kağıt boyutunu belirtebilirsiniz. Not: Yeni bir dosya oluşturduğunuzda, kağıt boyutunun, makinenizdeki varsayılan yazıcı ayarına göre olacağını unutmayın.

{{% /alert %}}

Aşağıdaki örnek kod, [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/) yönteminin kullanımını gösterir. İlk olarak, bir çalışma kitabı oluşturur ve bellek akışına XLSX formatında kaydeder. Daha sonra, A5 kağıt boyutuyla yükler ve PDF olarak kaydeder. Sonra tekrar, A3 kağıt boyutuyla yükler ve yine PDF olarak kaydeder. Çıktı PDF'leri açıp kağıt boyutlarını kontrol ederseniz, farklı olduklarını göreceksiniz. Birisi A5, diğeri A3 sayfa boyutundadır. Lütfen kod tarafından oluşturulan [A5 çıktı PDF'si](PrinterSize-a5_out.pdf) ve [A3 çıktı PDF'sini](PrinterSize-a3_out.pdf) indirin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
