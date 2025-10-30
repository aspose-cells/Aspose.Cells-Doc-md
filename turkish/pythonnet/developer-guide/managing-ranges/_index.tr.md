---
title: Aralıkları Yönetme
linktitle: Aralıklar
type: docs
weight: 105
url: /tr/python-net/managing-ranges/
description: Bu makale, Aspose.Cells for Python via .NET API sı ile aralıkları nasıl yöneteceğinizi göstermektedir.
keywords: Python Excel Kütüphanesi, Python aralıklarını yönet, Python da aralık oluştur, Python da Hücrelerin Aralığına Değer Koy, Python da Aralığın Hücrelerinin Stilini Ayarla, Python da Aralığın CurrentRegion ını Al.
---

## **Giriş**

Excel'de fare kutu seçimi ile birden fazla hücre seçebilirsiniz, seçilen hücrelerin setine "Aralık" denir.

Örneğin, Excel'in "A1" hücresine sol fare düğmesine tıklayabilir ve ardından "C4" hücresine sürükleyebilirsiniz. Seçtiğiniz dikdörtgen alanı, Aspose.Cells for Python via .NET kullanılarak kolayca bir nesne olarak da oluşturulabilir.

Aralık oluşturma, değer koyma, stil ayarlama ve "Aralık" nesnesine daha fazla işlem yapmanın yolları.

## **Python Excel Kütüphanesi ile Aralıkları Yönetme**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu sağlar.

## **Aralık Oluşturma Nasıl Yapılır**

A1:C4 üzerine uzanan bir dikdörtgen alan oluşturmak istediğinizde aşağıdaki kodu kullanabilirsiniz:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **Aralığın Hücrelerine Değer Koyma Nasıl Yapılır**

A1:C4 üzerine uzanan bir hücre aralığınız varsa, matris 4 * 3 = 12 hücre oluşturur. Bireysel aralık hücreleri ardışık olarak düzenlenmiştir.

Aşağıdaki örnek, Aralık hücrelerine bazı değerleri girme işlemini göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Aralığın Hücrelerinin Stilini Ayarlama**

Aşağıdaki örnek, Aralığın hücrelerinin stilini ayarlamanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Aralığın CurrentRegion'ını Alma**

CurrentRegion, mevcut bir bölgeyi temsil eden bir Aralık nesnesi döndüren bir özelliktir. 

Mevcut bölge, herhangi bir kombinasyonla sınırlandırılmış bir aralıktır. Salt okunur.

Excel'de, CurrentRegion alanını şu şekilde alabilirsiniz:
1. Fare kutusu ile bir alan (range1) seçin.
2. "Ana Sayfa - Düzenleme - Bul & Seç - Özel Git - Gelen bölge" yi tıklayın veya "Ctrl+Shift+*" kullanarak, excel otomatik olarak bir bölge (range2) seçmenize yardımcı olacaktır, şimdi başardınız, range2 range1'in CurrentRegion'ıdır.

Aspose.Cells for Python via .NET kullanarak, aynı işlevi gerçekleştirmek için "Range.current_region" özelliğini kullanabilirsiniz.

Lütfen aşağıdaki test dosyasını indirin, excel'de açın, bir alanı seçmek için fare kutusunu kullanın "A1:D7", sonra "Ctrl+Shift+*" tıklayın, "A1:C3" alanının seçildiğini göreceksiniz.

[current_region.xlsx](current_region.xlsx)

Şimdi lütfen aşağıdaki örneği çalıştırın, Aspose.Cells for Python via .NET içinde nasıl çalıştığını görün:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Gelişmiş Konular**
- [Excel dosyasının Otomatik Doldurması](/cells/tr/python-net/autofill-ranges/)
- [Excel'in Aralıklarını Kopyala](/cells/tr/python-net/copy-ranges-of-excel/)
- [Yalnızca Aralık Verisini Kopyala](/cells/tr/python-net/copy-range-data-only/)
- [Yalnızca Aralık Verisiyle Kopyala](/cells/tr/python-net/copy-range-data-with-style/)
- [Yalnızca Aralık Stiliyle Kopyala](/cells/tr/python-net/copy-range-style-only/)
- [Birleşik Aralık Oluştur](/cells/tr/python-net/create-union-range/)
- [Aralığı Kes ve Yapıştır](/cells/tr/python-net/cut-and-paste-cells/)
- [Aralıkları Sil](/cells/tr/python-net/delete-ranges-from-excel/)
- [Aralığın Adresini, Hücre Sayısını ve Konumunu, Tüm Sütunu ve Tüm Satırı Al](/cells/tr/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Aralık Ekle](/cells/tr/python-net/insert-ranges-to-excel/)
- [Hücreleri Birleştir veya Birleşikliği Kaldır](/cells/tr/python-net/merge-or-unmerge-range-of-cells/)
- [Çalışma Sayfasında Hücre Aralığını Taşıma](/cells/tr/python-net/move-range-of-cells-in-a-worksheet/)
- [Çalışma Kitabı ve Çalışma Sayfası Kapsamlı Adlandırılan Aralıkları Oluştur](/cells/tr/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Aralıktaki Veriyi Arama ve Değiştirme](/cells/tr/python-net/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="python-net" >}}
