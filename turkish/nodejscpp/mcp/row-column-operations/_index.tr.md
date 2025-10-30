---
title: Excel Satır ve Sütun İşlemleri
linktitle: Satır ve Sütun İşlemleri
type: docs
weight: 50
url: /tr/nodejs-cpp/mcp/row-column-operations
keywords: "Excel satır işlemleri, Excel sütun işlemleri, Excel düzen yönetimi, satır ekleme, sütun silme, Excel hücrelerini yeniden boyutlandırma"
description: "Excel satır ve sütun işlemleri  AI otomasyonu ile satır ve sütun ekleme, silme, yeniden boyutlandırma, gizleme/görünür hale getirme"
---

# Excel Satır ve Sütun İşlemleri

AI destekli otomasyon ile **Excel satır ve sütun işlemlerini** yönetin. Mükemmel tablo düzeni yönetimi için **Excel satırları** ve **sütunları** ekleyin, silin, yeniden boyutlandırın, gizleyin/görünür yapın.

## Mevcut Araçlar

- `row_column_operations` - **Excel satır/sütun işlemleri** (ekleme, silme, yeniden boyutlandırma, gizleme/görünür yapma) ile **AI Excel**
- `row_column_operations_batch` - Birden fazla **Excel satır/sütun işlemi**ni toplu olarak **Excel MCP** kullanarak yapın

## Tek İşlemler

### Satır Ekle
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### Sütun Sil
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### Satır Yüksekliği Ayarla
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### Sütun Genişliğini Ayarla
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## Toplu İşlemler

### Kapsamlı Düzenleme Ayarı
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### Ekleme ve Silme İşlemleri
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### Gizle ve Göster İşlemleri
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### Otomatik Sığdırma İşlemleri
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## İşlem Türleri Referansı

### Ekleme İşlemleri
- `insert_rows` - Belirtilen konuma yeni satırlar ekle
- `insert_columns` - Belirtilen konuma yeni sütunlar ekle

### Silme İşlemleri  
- `delete_rows` - Belirtilen satırları sil
- `delete_columns` - Belirtilen sütunları sil

### Yeniden Boyutlandırma İşlemleri
- `set_row_height` - Belirli satır yüksekliğini puan cinsinden ayarla
- `set_column_width` - Belirli sütun genişliğini karakter cinsinden ayarla
- `auto_fit_rows` - Satırları içerik yüksekliğine otomatik ayarla
- `auto_fit_columns` - Sütunları içerik genişliğine otomatik ayarla

### Görünürlük İşlemleri
- `hide_rows` - Belirtilen satırları gizle
- `unhide_rows` - Gizli satırları göster
- `hide_columns` - Belirtilen sütunları gizle
- `unhide_columns` - Gizli sütunları göster

## Aralık Tanımlamaları

### Satır Aralıkları
- `"1"` - Tek satır (satır 1)
- `"1:3"` - Satır aralığı (satırlar 1 ile 3)
- `"5:10"` - Birden fazla ardışık satır

### Sütun Aralıkları
- `"A"` - Tek sütun (sütun A)
- `"A:C"` - Sütun aralığı (sütun A'dan C'ye kadar)
- `"D:F"` - Birden fazla ardışık sütun

## Gelişmiş Örnekler

### Rapor Başlık Ayarı
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### Veri Tablosu Düzeni
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### Sunum Düzeni
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## Ölçüm Kılavuzları

### Satır Yükseklikleri (Puan)
- `15` - Varsayılan satır yüksekliği
- `20` - Okunabilirliği artırmak için biraz daha yüksek
- `25` - Başlıklar için iyi
- `30` - Büyük başlıklar
- `40` - Başlıklar için ekstra büyük

### Sütun Genişlikleri (Karakter)
- `8` - Dar sütunlar (tarihler, kodlar)
- `12` - Standart veri sütunları
- `15` - Orta metin sütunları
- `20` - Geniş metin sütunları
- `25` - Açıklamalar için ekstra geniş
- `30` - Uzun metinler için çok geniş

## En İyi Uygulamalar

1. **Başlık Boyutu**: Vurgu için başlıkları daha yüksek ve geniş yapın
2. **Veri Tutarlılığı**: Veri satırları için tutarlı satır yüksekliği kullanın
3. **Otomer uyumu**: Dinamik içerik boyutlandırması için otomatik uyumu kullanın
4. **Kullanılmayanı Gizle**: Daha temiz görünüm için boş satır/sütunları gizleyin
5. **Mantıklı Gruplama**: İlgili yeniden boyutlandırma işlemlerini toplu gruplandırın

## Yaygın Kalıplar

### Rapor Hazırlama Kalıbı
1. En üstte başlık satırları ekleyin
2. Başlık satırı yüksekliği ayarlayın
3. Otomatik sığdır veri sütunları
4. Standart veri satırı yüksekliği ayarla
5. Kullanılmayan alanları gizle

### Veri İçe Aktarma Deseni
1. Yeni veri için satırlar ekle
2. Sütunları içeriğe göre otomatik sığdır
3. Satır yüksekliğini standartlaştır
4. Hesaplama sütunlarını gizle

### Sunum Deseni
1. Detay satırları/sütunları gizle
2. Özet alanlarını büyüt
3. Sunuma uygun boyutlar belirle
4. Sadece ilgili verileri göster

## Hata Yönetimi

### Geçersiz Satır Aralığı
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**Sonuç**: Hata - satır numaraları 1’den başlar

### Geçersiz Sütun Aralığı
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**Sonuç**: Başarılı olabilir ama tipik kullanımın ötesinde

### Gerekli Parametreler Eksik
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**Sonuç**: Hata - yüksekliği parametresi gerekir 
{{< app/cells/assistant language="nodejs-cpp" >}}
