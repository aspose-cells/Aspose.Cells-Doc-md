---
title: Sürüm Numarasını Kontrol Edin
type: docs
weight: 80
url: /tr/python-net/check-version-number/
---

{{% alert color="primary" %}}

Kullandığınız Aspose.Cells'in hangi sürümü olduğunu merak mı ediyorsunuz? Aspose.Cells'in yeni sürümlerini, hem yeni özellikler tanıtmak hem de düzeltmeler yapmak için düzenli olarak yayınlıyoruz. Sürüm numarası, büyük sürüm numarası, küçük sürüm numarası ve düzeltme sürüm numarasından oluşur. Her sayı, 0'dan yukarı bir tam sayı olmalıdır. Format aşağıdaki gibidir:

büyük.küçük.düzeltme

Yeni bir Aspose.Cells sürümü yayımladığımızda, sürüm numarasını güncelliyoruz.

Bu makale, Aspose.Cells'in yüklü olduğu sürümü manuel olarak ve Aspose.Cells API'sını kullanarak nasıl kontrol edileceğini açıklar.

{{% /alert %}}

## **Sürüm Numarasını Manüel Olarak Kontrol Etme**

Kullandığınız Aspose.Cells'in sürüm numarasını manuel olarak bulmak için:

1. Aspose.Cells.dll dosyasına sağ tıklayın ve **Özellikler** seçeneğini belirleyin.
1. Sürüm (veya Ayrıntılar) sekmesine tıklayarak sürüm numarasını kontrol edin.

## **Aspose.Cells API'sini Kullanarak Sürüm Numarasını Kontrol Etme**

Aspose.Cells kullanarak sürüm numarasını API aracılığıyla bulmak için, CellsHelper sınıfının GetVersion statik yöntemini kullanarak Aspose.Cells'in sürüm numarasını alın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
