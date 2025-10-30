---
title: Excel Hücre İşlemleri
linktitle: Hücre İşlemleri
type: docs
weight: 60
url: /tr/nodejs-cpp/mcp/cell-operations
keywords: "Excel hücre işlemleri, Excel hücreleri birleştirme, kopyala yapıştır, Excel hücre manipülasyonu, Yapay Zeka ile Excel hücre işlemleri"
description: "Excel hücre işlemleri  birleştirme, kopyala/yapıştırma, içerik temizleme ve gelişmiş hücre manipülasyonu Yapay Zeka otomasyonuyla"
---

# Excel Hücre İşlemleri

Yapay Zeka destekli otomasyon ile gelişmiş **Excel hücre işlemleri** yapın. Hücreleri birleştirin, kopyala-yapıştır işlemleri gerçekleştirin, içerik temizleyin ve **Excel hücrelerini** hassasiyetle manipüle edin.

## Mevcut Araçlar

- `cell_operations` - **Excel hücre işlemleri** (birleştirme, kopyalama/yapıştırma, temizleme) **Yapay Zeka destekli** otomasyon ile
- `cell_operations_batch` - Çoklu **Excel hücre işlemleri**ni toplu olarak **spreadsheet MCP** aracılığıyla yapın

## Tekli Hücre İşlemleri

### Hücreleri Birleştir
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/merged-layout.xlsx",
    "sheet_name": "Report",
    "operation": "merge_cells",
    "range": "A1:C1"
  }
}
```

### Hücreleri Birleştirmeyi Kaldır
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/unmerged.xlsx",
    "sheet_name": "Data",
    "operation": "unmerge_cells",
    "range": "A1:C1"
  }
}
```

### Hücreleri Kopyala
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Source",
    "operation": "copy_cells",
    "source_range": "A1:D5"
  }
}
```

### Değerleri Yapıştır
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Target",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```

### İçeriği Temizle
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Data",
    "operation": "clear_contents",
    "range": "A1:Z100"
  }
}
```

## Toplu Hücre İşlemleri

### Birleştirme ve Kopyalama İş akışını Tamamla
```json
{
  "tool": "cell_operations_batch", 
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A7:C7"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:F1",
        "destination_range": "A9"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F1", 
        "destination_range": "A12"
      }
    ]
  }
}
```

### Sayfa Çaprazı İşlemler
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet.xlsx",
    "sheet_name": "Summary",
    "operation": "paste_values",
    "source_range": "A1:F5",
    "source_sheet": "Data",
    "destination_range": "A1"
  }
}
```

### Veri Temizleme İşlemleri
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/cleanup-demo.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "clear_contents",
        "range": "A1:A10"
      },
      {
        "operation": "clear_formats",
        "range": "B1:B10"
      },
      {
        "operation": "clear_all",
        "range": "C1:C10"
      }
    ]
  }
}
```

## İşlem Türleri Referansı

### Birleştirme İşlemleri
- `merge_cells` - Hücreleri tek hücreye birleştir
- `unmerge_cells` - Birleştirilmiş hücreleri tekrar bireysel hücrelere ayır
- `merge_across` - Satırlar boyunca hücreleri birleştirirken satırları ayırmaya devam et

### Kopyala/Yapıştır İşlemleri
- `copy_cells` - Hücre aralığını panoğa kopyala
- `paste_values` - Sadece değerleri yapıştır (biçimlendirme veya formüller olmadan)
- `paste_formulas` - Sadece formülleri yapıştır (değer veya biçimlendirme olmadan)
- `paste_formats` - Sadece biçimlendirmeyi yapıştır (değer veya formüller olmadan)
- `transpose_paste` - Tersine çevrilmiş düzenle yapıştır (satırlar↔sütunlar)

### Temizleme İşlemleri
- `clear_contents` - Hücre içeriğini temizle (biçimlendirmeyi koru)
- `clear_formats` - Hücre biçimlendirmesini temizle (içeriği koru)
- `clear_all` - Hem içeriği hem de biçimlendirmeyi temizle

## Gelişmiş Örnekler

### Rapor Başlığı Ayarı
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/title-report.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A1:F1"
      },
      {
        "operation": "merge_cells",
        "range": "A2:F2"
      },
      {
        "operation": "merge_cells",
        "range": "A3:C3"
      },
      {
        "operation": "merge_cells",
        "range": "D3:F3"
      }
    ]
  }
}
```

### Veri Şablonu Oluşumu
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "templates/data-template.xlsx",
    "sheet_name": "Template",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F1"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A10"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A20"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A30"
      }
    ]
  }
}
```

### Veri Konsolidasyonu
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/consolidated.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q1Data",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q2Data", 
        "destination_range": "A12"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q3Data",
        "destination_range": "A22"
      }
    ]
  }
}
```

### Formül ve Format Ayrımı
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/separated.xlsx",
    "sheet_name": "Analysis",
    "operations": [
      {
        "operation": "paste_formulas",
        "source_range": "A1:F10",
        "source_sheet": "Calculations",
        "destination_range": "A1"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F10", 
        "source_sheet": "Formatting",
        "destination_range": "A1"
      }
    ]
  }
}
```

## Sayfalararası İşlemler

### Sayfalar Arası Kopyalama
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet-copy.xlsx",
    "sheet_name": "Destination",
    "operation": "paste_values",
    "source_range": "A1:D10",
    "source_sheet": "Source",
    "destination_range": "B2"
  }
}
```

### Özet Sayfası Oluşumu
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/summary-creation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "January",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "February",
        "destination_range": "E2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "March",
        "destination_range": "I2"
      }
    ]
  }
}
```

## Veri Dönüşümü

### Veriyi Transpoze Et
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/transposed.xlsx",
    "sheet_name": "Data",
    "operation": "transpose_paste",
    "source_range": "A1:E5",
    "destination_range": "G1"
  }
}
```

### Sadece Değerleri Kopyala
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/values-only.xlsx",
    "sheet_name": "Clean Data",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F20",
        "source_sheet": "Raw Data"
      },
      {
        "operation": "paste_values",
        "destination_range": "A1"
      }
    ]
  }
}
```

## En İyi Uygulamalar

1. **Stratejik Birleştir**: Başlıklar ve unvanlar için birleştirme kullanın, veri alanları için değil
2. **Kopyala ve Yapıştırmadan Önce Kopyala**: Her zaman kaynak aralığını kopyalayın, yapıştırma işlemlerinden önce
3. **Uygun Şekilde Temizle**: İhtiyacınıza uygun temizleme işlemini seçin
4. **Sayfalararası Planlama**: Çok sayfalı işlemleri çatışmaları önlemek için planlayın
5. **Toplu İşlemler**: Daha iyi performans için ilgili işlemleri gruplayın

## Yaygın Kullanım Durumları

### Rapor Başlıkları
- Başlıklar için hücreleri birleştirin
- Başlık biçimlendirmeyi kopyala
- Tutarlı stil uygulama

### Veri Temizleme
- Eski içeriği temizle
- Biçimlendirmeyi kaldır
- Hücre durumlarını sıfırla

### Şablon Oluşturma
- Biçimlendirme örüntülerini kopyala
- Yapıyı veriler olmadan yapıştır
- Tekrar kullanılabilir düzenler oluştur

### Veri Birleştirme
- Birden fazla sayfadaki verileri birleştir
- Formül çakışmalarını önlemek için yalnızca değerleri yapıştır
- Veriyi Transpoze et

## Hata İşleme

### Geçersiz Birleştirme Aralığı
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "merge_cells",
    "range": "A1"
  }
}
```
**Sonuç**: Hata - tek hücre birleştirilemiyor

### Kaynak Aralığı Eksik
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```
**Sonuç**: Hata - kopyalanmış veri mevcut değil

### Geçersiz Sayfa Referansı
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "source_range": "A1:B2",
    "source_sheet": "NonExistentSheet",
    "destination_range": "A1"
  }
}
```
**Sonuç**: Hata - kaynak sayfa bulunamadı 
{{< app/cells/assistant language="nodejs-cpp" >}}
