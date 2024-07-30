---
title: Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle
type: docs
weight: 430
url: /tr/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Belirtilen Yazıcı Kağıdı Boyutu ile Çalışma Kitabını Yükle

{{% /alert %}}

Aşağıdaki örnek kod, [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/) yönteminin kullanımını açıklar. Öncelikle bir çalışma kitabı oluşturur, ardından XLSX formatında bellek akışında kaydeder. Daha sonra A5 kağıt boyutuyla yükler ve PDF formatında kaydeder. Daha sonra tekrar A3 kağıt boyutuyla yükler ve yine PDF formatında kaydeder. Çıktı olan PDF'leri açıp kağıt boyutlarını kontrol ederseniz farklı olduklarını göreceksiniz. Biri A5 diğeri A3. Lütfen kod tarafından oluşturulan [A5 çıktı PDF](PrinterSize-a5_out.pdf) ve [A3 çıktı PDF](PrinterSize-a3_out.pdf) dosyalarını indirin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
