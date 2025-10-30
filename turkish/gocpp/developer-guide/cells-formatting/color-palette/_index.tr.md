---
title: Golang ve C++ ile Renk Paletini Kullanma
linktitle: Renk Paletini Nasıl Kullanılır
type: docs
weight: 80
url: /tr/go-cpp/excel-color-palette/
description: Paletteye özel renkler eklemek ve Aspose.Cells for C++ API ile Excel renk paletini kullanmak için C++ kodu.
keywords: c++ ile palete özel renkler ekleme, programlı olarak Excel renk paleti kullanımı, çalışma kitabında renk paletini nasıl kullanırım, c++ ile excel de renk paletini nasıl kullanırım
---

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells ile sadece paletin mevcut renklerini değil aynı zamanda özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, önce paletine ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

## **Paletine Özel Renkler Ekleyin**

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, paleti değiştirmek için özel bir renk eklemek için aşağıdaki parametreleri alan bir [**ChangePalette**](https://reference.aspose.com/cells/go-cpp/workbook/changepalette/) yöntemi sağlar:

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ColorPalette.go" >}}
{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}
