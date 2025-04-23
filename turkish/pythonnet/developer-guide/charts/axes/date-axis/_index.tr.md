---
title: Tarih Ekseni
description: Aspose.Cells for Python via .NET kullanarak tarih eksenini nasıl yönetileceğinizi öğrenin. Kılavuzumuz, çeşitli tarih biçimleri, zaman ölçekleri ve tekerlek çubuğu etiket frekanslarıyla çalışma konusunda size yardımcı olacaktır.
keywords: Aspose.Cells for Python via .NET, tarih ekseni, yönetim, tarih formatları, zaman ölçekleri, tik etiketleri sıklığı.
type: docs
weight: 200
url: /tr/python-net/date-axis/
---

## **Olası Kullanım Senaryoları**
Tarih kullanılan çalışma sayfası verilerinden bir grafik oluşturduğunuzda ve tarihler grafikte yatay (kategori) eksende çizilmişse, Aspose.Cells otomatik olarak kategori ekseni tarih (zaman ölçeği) ekseni olarak değiştirir.
Tarih ekseni, çalışma sayfasındaki tarihleri belirli aralıklarda veya temel birimlerde, örneğin gün, ay veya yıl sayısını kronolojik sırada görüntüler, hatta çalışma sayfasındaki tarihler sıralı veya aynı temel birimlerde değilse bile.
Varsayılan olarak, Aspose.Cells, çalışma sayfasındaki herhangi iki tarih arasındaki en küçük farka dayanarak tarih ekseni için temel birimleri belirler. Örneğin, çalışma sayfasında tarih farkı en küçük olan yedi gün ise, Excel temel birimi gün olarak ayarlar, ancak stok performansını daha uzun bir süre boyunca görmek istiyorsanız, temel birimi aylar veya yıllara değiştirebilirsiniz.

## **Microsoft Excel gibi Tarih Ekseni Yönetimi**
Yeni bir Excel dosyası oluşturan ve grafik değerlerini ilk çalışma sayfasına koyan aşağıdaki örnek kodu inceleyin. 
Ardından bir grafik ekleriz ve [**Axis**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis) tipini ayarlarız 
[**TIME_SCALE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/categorytype/) 'e ayarlar dikkate alınarak, base units için Days olarak ayarlarız.

![todo:image_alt_text](excel.png)

## **Örnek Kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DateAxis.py" >}}
