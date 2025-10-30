---
title: Golang ve C++ kullanarak Bir Çalışmada En Çok Aralık Alın
linktitle: Çalışma sayfasındaki Maksimum Aralığı Al
type: docs
weight: 360
url: /tr/go-cpp/get-max-range-in-a-worksheet/
description: Bu makale, Aspose.Cells for C++ kütüphanesi ile Excel dosyalarının maksimum aralığını, maksimum veri aralığını ve maksimum görüntüleme aralığını nasıl alacağınızı anlatmaktadır.
---

{{% alert color="primary" %}} 

Çalışma sayfasından veri okurken, maksimum alanı bilmemiz gerekmektedir.

Tüm verileri bir çalışma sayfasından kopyalarken, maksimum alanı bilmemiz gerekmektedir.

Belirli bir alanın HTML ve PDF'ye dışa aktarılırken, maksimum alanı bilmemiz gerekir.

Aspose.Cells for C++, bir çalışma sayfasında maksimum aralığı bulmak için farklı yollar içerir. 

{{% /alert %}} 

## **Maksimum aralığı almak**
Aspose.Cells'te, [**Row**](https://reference.aspose.com/cells/go-cpp/row/) ve [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) nesneleri başlatılmışsa, bunlar boş satır veya sütunlar olmasa bile maksimum alan olarak sayılır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **Maksimum veri aralığını almak**
Çoğu durumda, yalnızca tüm verileri içeren tüm aralıkları elde etmemiz yeterlidir, aralık dışındaki boş hücreler biçimlendirilse bile.
Ve şekiller, tablolar ve pivot tablolar ile ilgili ayarlar göz ardı edilecektir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **Maksimum görüntü aralığını almak**
Çalışma sayfasındaki tüm verileri HTML, PDF veya görüntülere dışa aktardığımızda, veri, stiller, grafikler, tablolar ve özet tablolar da dahil olmak üzere tüm görünür nesneleri içeren bir alan elde etmemiz gerekmektedir.
Aşağıdaki kodlar, maksimum görüntüleme alanını HTML'ye nasıl aktaracağını gösterir:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
İşte [kaynak excel dosyası](Book1.xlsx).
