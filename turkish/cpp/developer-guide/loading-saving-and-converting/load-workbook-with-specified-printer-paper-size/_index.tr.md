---
title: Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle
type: docs
weight: 430
url: /tr/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Belirtilen Yazıcı Kağıdı Boyutu ile Çalışma Kitabını Yükle

{{% /alert %}}

Aşağıdaki örnek kod, [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/) metodunun kullanımını açıklar. Önce bir çalışma kitabı oluşturur, ardından bellek akışında XLSX formatında kaydeder. Daha sonra A5 kağıt boyutuyla yükler ve PDF formatında kaydeder. Sonra tekrar A3 kağıt boyutuyla yükler ve tekrar PDF olarak kaydeder. Çıkış PDF'lerini açıp kağıt boyutlarını kontrol ederseniz, farklı olduklarını göreceksiniz. Bir A5, diğeri A3. Lütfen kodun oluşturduğu [A5 çıktı PDF'sini](PrinterSize-a5_out.pdf) ve [A3 çıktı PDF'sini](PrinterSize-a3_out.pdf) indiriniz, referans için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
