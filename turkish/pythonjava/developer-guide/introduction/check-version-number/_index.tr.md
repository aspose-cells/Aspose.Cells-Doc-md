---
title: Sürüm Numarasını Kontrol Et
type: docs
weight: 80
url: /tr/python-java/check-version-number/
---
{{% alert color="primary" %}}

Aspose.Cells'in hangi sürümünü kullandığınızı merak mı ediyorsunuz? Hem yeni özellikler sunmak hem de sorunları gidermek için düzenli olarak Aspose.Cells'in yeni sürümlerini yayınlıyoruz. Sürüm numarası ana sürüm numarası, alt sürüm numarası ve düzeltme sürüm numarasından oluşur. Her sayı 0'dan yukarı bir tam sayı olmalıdır. Biçim aşağıdaki gibidir:

büyük.küçük.düzeltme

Aspose.Cells'in yeni bir derlemesini yayınladığımızda, sürüm numarasını güncelleriz.

Bu makalede, Aspose.Cells'in hangi sürümünün sistemde yüklü olduğunun manuel olarak ve Aspose.Cells API kullanılarak nasıl kontrol edileceği açıklanmaktadır.

{{% /alert %}}

## **Sürüm Numarasını Manuel Olarak Kontrol Edin**

Aspose.Cells'in hangi sürümünü manuel olarak kullandığınızı öğrenmek için:

1.  Aspose.Cells.dll dosyasına sağ tıklayın ve seçin**Özellikler**.
1. Sürüm numarasını kontrol etmek için Sürüm (veya Ayrıntılar) sekmesine tıklayın.

## **Aspose.Cells API'i Kullanarak Versiyon Numarasını Kontrol Edin**

 Aspose.Cells'in hangi versiyonunu kullandığınızı API üzerinden öğrenmek için,[HücrelerYardımcısı](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper) Aspose.Cell'in sürüm numarasını almak için sınıf GetVersion statik yöntemi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}
