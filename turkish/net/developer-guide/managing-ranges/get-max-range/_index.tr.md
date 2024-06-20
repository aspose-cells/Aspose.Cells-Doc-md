---
title: Çalışma sayfasındaki Maksimum Aralığı Al
type: docs
weight: 360
url: /tr/net/get-max-range-in-a-worksheet/
description: Bu makalede, Aspose.Cells for .Net kütüphanesi ile Excel dosyalarının maksimum aralığını, maksimum veri aralığını ve maksimum görüntü aralığını nasıl alacağınızı açıklar.
---

{{% alert color="primary" %}} 

Çalışma sayfasından veri okurken, maksimum alanı bilmemiz gerekmektedir.

Tüm verileri bir çalışma sayfasından kopyalarken, maksimum alanı bilmemiz gerekmektedir.

Belirtilen bir alana html ve pdf olarak veri aktarırken, maksimum alanı bilmemiz gerekmektedir.

Aspose.Cells for .Net, çalışma sayfasındaki maksimum aralığı bulmanın farklı yollarını içermektedir. 


{{% /alert %}} 



## **Maksimum aralığı almak**
Aspose.Cells'te, [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) ve [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) nesneleri başlatılmışsa, boş satır veya sütunlarda veri olmasa bile bu satır ve sütunlar maksimum alana sayılacaktır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Maksimum veri aralığını almak**
Çoğu durumda, yalnızca tüm verileri içeren tüm aralıkları elde etmemiz yeterlidir, aralık dışındaki boş hücreler biçimlendirilse bile.
Ve şekiller, tablolar ve özet tablolar hakkındaki ayarlar görmezden gelinecektir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Maksimum görüntü aralığını almak**
Çalışma sayfasındaki tüm verileri HTML, PDF veya görüntülere dışa aktardığımızda, veri, stiller, grafikler, tablolar ve özet tablolar da dahil olmak üzere tüm görünür nesneleri içeren bir alan elde etmemiz gerekmektedir.
Aşağıdaki kodlar, maksimum görüntü aralığını HTML'e dönüştürmenin nasıl yapıldığını göstermektedir:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

İşte [kaynak excel dosyası](Book1.xlsx).
