---
title: Aspose.Cells for Go (C aracılığıyla) ile Excelize, Tealeg/xlsx ve Go OLE karşılaştırması ve performans analizi.
linktitle: İşlevsellik ve performans karşılaştırması
type: docs
weight: 40
url: /tr/go-cpp/comparison-of-functionality-and-performance/
description: Aspose.Cells for Go (C aracılığıyla) ile Excelize, Tealeg/xlsx ve Go OLE nin işlevsellik ve performans karşılaştırması.
keywords: Aspose.Cells, Excel, Formül İzleme Penceresi, Hücreler, Ekleme, C++
---

Aşağıda, Aspose.Cells for Go (C aracılığıyla) ile diğer ana akım Go dilinde Excel işleme kitaplıklarının (Excelize, tealeg/xlsx, go-ole) işlevsellik, performans ve kullanım alanları açısından karşılaştırması yer almaktadır.

## Temel konumlandırma ve yapı farkları

| Kitaplık Adı        |   Tür                          | Temel Uygulama                   |  CGO Bağımlılığı         | Çoklu Platform Uygulama |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells for Go | Ticarî Kitaplık (MIT/Ücretli) | Yerel Motor, Go CGO Yöneticisi  |  ✅  Evet                | Windows, Linux desteği |
| Excelize            | Açık Kaynak Kitaplık (MIT)        | Saf Go Uygulaması               |  ❌  Hayır               | Windows, Linux, MacOS desteği |
| tealeg/xlsx         | Açık Kaynak Kitaplık (BSD)        | Saf Go Uygulaması               |  ❌  Hayır               | Windows, Linux, MacOS desteği |
| go-ole              | Açık Kaynak Kitaplık (BSD)        | Go Windows OLE/COM Arayüzü       |  ✅  Evet (Sadece Windows) | Windows Sadece |

### Temel Farklılıklar

- Aspose.Cells for Go via C++ en tam ve fonksiyonel özelliklere sahip endüstriyel sınıf bir ticarî kitaplıktır, ücretlidir.
- Excelize şu anda en aktif ve açık kaynaklı Go kitaplığıdır, saf Go ile yazılmıştır.
- Tealeg/xlsx daha temel işlevlere sahip erken dönem açık kaynak kitaplığıdır ve bakımı yavaştır.
- Go-ole sadece Windows'ta çalışan, Excel yüklenmesine bağlı olan ve sunucu ortamları için önerilmeyen bir COM otomasyon şemasıdır.

## Özellik Karşılaştırması

### Desteklenen Dosya Formatları Karşılaştırması

| Elektronik Tablo Formatı     |   Aspose.Cells for Go via C++ | Excelize    | Tealeg/xlsx | Go-OLE (Excel Uygulaması)    |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx                   | ✅ Evet                        | ✅ Evet     | ✅ Evet       | ✅ Güvenilir Excel Bağlantısı |
| Xlsb                   | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ✅ Güvenilir Excel Bağlantısı |
| Xls                    | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ✅ Güvenilir Excel Bağlantısı |
| Xlsm                   | ✅ Evet                        | ✅ Evet     | ✅ Evet       | ✅ Güvenilir Excel Bağlantısı |
| Xltm                   | ✅ Evet                        | ✅ Evet     | ✅ Evet       | ✅ Güvenilir Excel Bağlantısı |
| Xltx                   | ✅ Evet                        | ✅ Evet     | ✅ Evet       | ✅ Güvenilir Excel Bağlantısı |
| Csv                    | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ✅ Güvenilir Excel Bağlantısı |
| Ods                    | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ✅ Güvenilir Excel Bağlantısı |
| Html                   | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ❌ Hayır              |
| Numbers                | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ❌ Hayır              |
| Json                   | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ❌ Hayır              |
| Xml                    | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ❌ Hayır              |
| SpreadsheetML          | ✅ Evet                        | ❌ Hayır     | ❌  Hayır       | ❌ Hayır              |

### Desteklenen Elektronik Tablo Özellikleri

| Kütüphane Özellikleri                 |   Aspose.Cells for Go via C++ | Excelize         | Tealeg/xlsx | Go-OLE (Excel Uygulaması) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Okuma/Yazma (dosya formatını destekler)  | ✅ Evet                        | ✅ Evet          | ✅ Evet     | ✅ Evet   |
| Hücre/Satır/Sütun/Elektronik Tablo        | ✅ Evet                        | ✅ Evet          | ✅ Evet     | ✅ Evet   |
| Stil                            | ✅ Evet                        | ✅ Evet          | ✅ Evet     | ✅ Evet   |
| Formül hesaplama               | ✅ Evet                        | ✅ Evet (Kısım)   | ❌  Hayır     | ✅ Evet (Excel ile hesaplandı)  |
| Grafik/Görüntü                    | ✅ Evet                        | ✅ Evet (Kısım)   | ❌  Hayır     | ✅ Evet   |
| PivotTable                        | ✅ Evet                        | ✅ Evet          | ❌  Hayır     | ✅ Evet   |
| Koşullu Biçimlendirme             | ✅ Evet                        | ✅ Evet          | ❌  Hayır     | ✅ Evet   |
| Veri doğrulama                     | ✅ Evet                        | ✅ Evet          | ❌  Hayır     | ✅ Evet   |
| Şifreleme/parola koruma             | ✅ Evet                        | ✅ Evet          | ❌  Hayır     | ✅ Evet   |
| Veri doğrulama                     | ✅ Evet                        | ✅ Evet          | ❌  Hayır     | ✅ Evet   |
| VBA makro                          | ✅ Evet Okuma                 | ❌  Hayır          | ❌  Hayır     | ✅ Evet   |
| Veri doğrulama                     | ✅ Evet                        | ✅ Evet          | ❌  Hayır     | ✅ Evet   |

## Performans Karşılaştırması

- **Test ortamı**：
İşlemci: 12. Nesil Intel(R) Core(TM) i7-12700 (2.10 GHz)
Kurulu RAM: 64.0 GB (63.7 GB kullanılabilir)
İşletim Sistemi Adı: Microsoft Windows 11 Pro
İşletim Sistemi Sürümü: 10.0.26100
İşletim Sistemi Mimarisi: 64-bit
Go sürümü: go version go1.24.5 windows/amd64
Aspose.Cells for Go via C++: 25.9.0
Excelize: 1.4.1

- **Test senaryosu**: büyük bir dosya varsayılarak, 10 çalışma sayfası, 100.000 satır x 250 sütun, biçimlendirme dahil

- **Çalıştırma Sonuçları**:
  - Excelize 35 dakika boyunca çalıştı (Başlangıç Zamanı: 2025-10-09T10:04:16+08:00, Bitiş Zamanı: 2025-10-09T10:39:53+08:00), oluşturulan dosya boyutu: 1.11 GB.
  - Aspose.Cells for Go via C++ (model 1) 27 dakika çalıştı (Başlangıç Zamanı: 2025-10-09T10:57:55+08:00, Bitiş Zamanı: 2025-10-09T11:16:24+08:00), oluşturulan dosya boyutu: 936MB.
  - Aspose.Cells for Go via C++ (model 2) 16 dakika çalıştı (Başlangıç Zamanı: 2025-10-09T12:01:26+08:00, Bitiş Zamanı: 2025-10-09T12:17:17+08:00), oluşturulan dosya boyutu: 1.16GB.
