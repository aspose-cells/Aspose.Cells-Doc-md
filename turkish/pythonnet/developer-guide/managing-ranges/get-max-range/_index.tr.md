---
title: Çalışma sayfasındaki Maksimum Aralığı Al
type: docs
weight: 360
url: /tr/python-net/get-max-range-in-a-worksheet/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi ile Excel dosyalarının maksimum aralığını, maksimum veri aralığını ve maksimum görüntü aralığını nasıl elde edeceğinizi açıklar.
keywords: Python Excel Kütüphanesi, Python maksimum aralığı al, Python maksimum veri aralığı al, Python maksimum görüntü aralığı al.
---

{{% alert color="primary" %}} 

Çalışma sayfasından veri okurken, maksimum alanı bilmemiz gerekmektedir.

Tüm verileri bir çalışma sayfasından kopyalarken, maksimum alanı bilmemiz gerekmektedir.

Belirtilen bir alana html ve pdf olarak veri aktarırken, maksimum alanı bilmemiz gerekmektedir.

Aspose.Cells for Python via .NET, çalışma sayfasında maksimum aralığı bulmanın farklı yollarını içerir. 


{{% /alert %}} 



## **Maksimum Aralığı Nasıl Alınır**
Aspose.Cells for Python via .NET'de [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) ve [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) nesneleri başlatılırsa, bu satır ve sütunlar, boş satırlarda veya sütunlarda veri olmasa bile maksimum alana sayılacaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **Maksimum Veri Aralığı Nasıl Alınır**
Çoğu durumda, yalnızca tüm verileri içeren tüm aralıkları elde etmemiz yeterlidir, aralık dışındaki boş hücreler biçimlendirilse bile.
Ve şekiller, tablolar ve özet tablolar hakkındaki ayarlar görmezden gelinecektir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **Maksimum Görüntü Aralığını Nasıl Alınır**
Çalışma sayfasındaki tüm verileri HTML, PDF veya görüntülere dışa aktardığımızda, veri, stiller, grafikler, tablolar ve özet tablolar da dahil olmak üzere tüm görünür nesneleri içeren bir alan elde etmemiz gerekmektedir.
Aşağıdaki kodlar, maksimum görüntü aralığını HTML'e dönüştürmenin nasıl yapıldığını göstermektedir:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

İşte [kaynak excel dosyası](Book1.xlsx).
