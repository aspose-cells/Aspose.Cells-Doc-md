---
title: Aspose.Cells.GridJs Temelleri
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## GridJs'in Temelleri

Aspose.Cells.GridJs, kullanıcılara hızlı ve kolay bir şekilde elektronik tablo dosyasını görüntüleme veya düzenleme olanağı sunan bir kütüphanedir. 

## Neden Aspose.Cells.GridJs Kullanılır


- Gerçek zamanlı güncellemeler, formül desteği ve zengin veri görselleştirme araçlarıyla, geleneksel masaüstü uygulamalarına benzer şekilde, kullanıcıların elektronik tablolar oluşturmasına, düzenlemesine, biçimlendirmesine, işbirliği yapmasına ve güvenli bir şekilde paylaşmasına imkan tanır.
- Veri Girişi ve Düzenleme, Biçim, Elektronik Tablo Navigasyonu, Formül Hesaplama, Veri Manipülasyonu, Grafikler ve Görselleştirmeler, İçe Aktarma ve Dışa Aktarma, Güvenlik, Geliştiricilere yönelik Eklentiler ve Özelleştirme gibi işletmelere özgü ihtiyaçlara göre düzenleyicinin uyarlanmasına olanak tanır.

## Özellikler


- Popüler elektronik tablo formatlarını içe aktarabilir, görüntüleyebilir ve düzenleyebilir.
- Elektronik tabloları çeşitli desteklenen dosya formatlarına dışa aktarabilir.
- Görüntü veya şekil veya grafik dosyalarını gösterebilir ve yönetebilir.
- Izgara tasarımı ve düzen özelleştirmesi gerçekleştirebilir.
- Birden fazla çalışma sayfasını yönetebilir.
- Excel® formülleri oluşturabilir ve hesaplayabilir.

## Desteklenen Dosya Formatları

https://docs.aspose.com/cells/python-net/supported-file-formats/

## Genel Kullanım

Aşağıda GridJs web uygulaması geliştirmek için temel işlem adımları bulunmaktadır.

- Ayarlar depolama dizinini Config.set_file_cache_directory(`dizin`) ile ayarlayın.
- Lisansı Config.set_license(`lisans dizini`) ile ayarlayın.
- Görüntü yolu url'sini GridJsWorkbook.set_image_url_base(`görüntü için yol`) ile ayarlayın.
- `Json`'ı elektronik tablo dosyasından almak için bir yol eylemi kurun. `GridJsWorkbook.ImportExcelFile` ve `GridJsWorkbook.ExportToJson` API'larını kullanabilirsiniz, `GridJs` otomatik olarak elektronik tabloyu önbelleğe kaydeder.
- Güncelleme operasyonu için `json` almak için bir yol eylemi kurun. `GridJsWorkbook.UpdateCell` API'sini kullanabilirsiniz, `GridJs` güncelleme operasyonunu önbelleğe kaydeder ve güncellenmiş `json`'ı döndürür.
- Önbellekteki dosyayı almak için bir yol eylemi kurun, böylece önbellekteki resim/şekil zip dosyasını veya elektronik tabloyu alabiliriz.
- Elektronik tabloyu indirmek için bir yol eylemi kurun. `GridJsWorkbook.SaveToCacheWithFileName` API'sini kullanabilirsiniz.

Aşağıda, Aspose.Cells.GridJs'in kullanımını gösteren temel bir demo bulunmaktadır:

https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 

Demo'da [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) kullanarak istemci tarafı sayfasını oluşturuyoruz.

Herhangi bir sorunuz, gereksiniminiz veya yardıma ihtiyacınız varsa lütfen aşağıdaki web sitesine geri bildirimde bulunun: https://forum.aspose.com/c/cells/9
