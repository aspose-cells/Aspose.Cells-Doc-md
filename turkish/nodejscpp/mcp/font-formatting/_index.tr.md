---
title: Excel Yazı Tipi ve Metin Biçimlendirme
linktitle: Yazı Tipi ve Metin Biçimlendirme
type: docs
weight: 30
url: /tr/nodejs-cpp/mcp/font-formatting
keywords: "Excel yazı tipi biçimlendirme, Excel metin biçimlendirme, Excel yazı tipi ayarları, yapay zeka Excel yazı tipi stilleri, Excel yazı tipi otomasyonu"
description: "Excel yazı tipi ve metin biçimlendirme  yapay zeka otomasyonu ile yazı tipi stilleri, renkler, boyutlar ve metin efektleri uygula"
---

# Excel Yazı Tipi ve Metin Biçimlendirme

Yapay zeka destekli otomasyon ile profesyonel **Excel yazı tipi biçimlendirmesi** uygula. **Excel metnini** formlar, renkler, boyutlar ve özel efektlerle stilize et, şık tablolar oluştur.

## Mevcut Araçlar

- `font_settings` - **Excel yazı tipi stili** (aile, boyut, kalın, italik, renk vb.) **Yapay Zeka Excel** hassasiyeti ile
- `font_settings_batch` - Birden çok alana **Excel yazı tipi ayarları** toplu halde **spreadsheet MCP** kullanarak uygula

## Tek Yazı Tipi İşlemleri

### Temel Yazı Tipi Stilizasyonu
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/styled-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "font_name": "Arial",
    "font_size": 14,
    "bold": true,
    "font_color": "#FFFFFF"
  }
}
```

### Metin Efektleri
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/effects-demo.xlsx",
    "sheet_name": "Sheet1",
    "range": "A2",
    "italic": true,
    "underline": true,
    "strikethrough": true,
    "font_color": "#FF0000"
  }
}
```

### Özel Karakterler
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "range": "A3",
    "font_size": 10,
    "subscript": true
  }
}
```

## Toplu Yazı Tipi İşlemleri

### Tam Başlık Stilizasyonu
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/professional-report.xlsx",
    "sheet_name": "Summary Report",
    "font_ranges": [
      {
        "range": "C3:G3",
        "font_name": "Arial Black",
        "font_size": 16,
        "bold": true,
        "italic": true,
        "underline": true,
        "font_color": "#FF0000"
      },
      {
        "range": "D4:D6",
        "font_name": "Calibri",
        "font_size": 12,
        "bold": true,
        "font_color": "#0066CC"
      },
      {
        "range": "E4:E6",
        "font_name": "Times New Roman",
        "italic": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

### Özel Metin Efektleri Gösterimi
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/text-effects.xlsx",
    "sheet_name": "Effects Demo",
    "font_ranges": [
      {
        "range": "A3",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "B3",
        "font_size": 10,
        "superscript": true
      },
      {
        "range": "C3",
        "strikethrough": true,
        "underline": true,
        "font_color": "#CC0000"
      }
    ]
  }
}
```

### Profesyonel Rapor Stilizasyonu
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "font_ranges": [
      {
        "range": "A1:F1",
        "font_name": "Arial",
        "font_size": 14,
        "bold": true,
        "font_color": "#FFFFFF"
      },
      {
        "range": "A5:F5",
        "bold": true,
        "font_size": 12
      },
      {
        "range": "F2:F5",
        "bold": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

## Yazı Tipi Parametreleri Referansı

### Yazı Tipi Aileleri
- `"Arial"` - Temiz, modern sans-serif
- `"Calibri"` - Microsoft Office varsayılanı
- `"Times New Roman"` - Geleneksel serif
- `"Arial Black"` - Kalın gösterim yazı tipi
- `"Courier New"` - Monospace yazı tipi

### Yazı Boyutları
- `8` - Çok küçük metin
- `10` - Küçük metin
- `11` - Varsayılan boyut
- `12` - Standart gövde metni
- `14` - Büyük metin
- `16` - Başlık boyutu
- `18` - Büyük başlık

### Yazı Tipi Renkleri (Hex Kodları)
- `"#000000"` - Siyah
- `"#FFFFFF"` - Beyaz
- `"#FF0000"` - Kırmızı
- `"#0066CC"` - Mavi
- `"#006600"` - Yeşil
- `"#FF6600"` - Turuncu
- `"#800080"` - Mor

### Metin Efektleri
- `bold: true` - Kalın yazı
- `italic: true` - İtalik yazı
- `underline: true` - Altı çizili yazı
- `strikethrough: true` - Çarpı işareti ile çizili yazı
- `subscript: true` - Alt simge (H₂O)
- `superscript: true` - Üst simge (x²)

## Gelişmiş Yazı Tipi Stili

### Bilimsel Gösterim Örneği
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "font_ranges": [
      {
        "range": "A1",
        "font_name": "Times New Roman",
        "font_size": 12,
        "bold": true
      },
      {
        "range": "B1",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "C1",
        "font_size": 10,
        "superscript": true
      }
    ]
  }
}
```

### Renk Kodlu Veri
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/color-coded.xlsx",
    "sheet_name": "Status Report",
    "font_ranges": [
      {
        "range": "A2:A5",
        "font_color": "#008000",
        "bold": true
      },
      {
        "range": "B2:B5",
        "font_color": "#FF8C00",
        "italic": true
      },
      {
        "range": "C2:C5",
        "font_color": "#DC143C",
        "strikethrough": true
      }
    ]
  }
}
```

## En İyi Uygulamalar

1. **Tutarlılık**: Raporlarda tutarlı yazı tipleri kullanın
2. **Hiyerarşi**: Görsel hiyerarşi oluşturmak için yazı tipi boyutlarını kullanın
3. **Okunabilirlik**: Metin ve arka plan arasında yeterli kontrast sağlayın
4. **Efektler**: Vurgulama için yazı efektlerini ölçülü kullanın
5. **Profesyonellik**: Raporlar için standart iş yazı tiplerine sadık kalın

## Yaygın Kullanım Durumları

### Rapor Başlıkları
- Kalın, büyük font büyüklüğü
- Çekici renkler
- Profesyonel yazı tipleri

### Veri Vurgusu
- Önemli değerler için kalın veya italik
- Durum göstergeleri için renk kodlama
- Güncelliği geçmiş veriler için çizgi geçirme

### Bilimsel Belgeler
- Kimyasal formüller için alt simge
- Matematiksel ifadeler için üst simge
- Kod veya veri için Monoasepenk

## Hata Yönetimi

### Geçersiz Yazı Tipi Ailesi
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_name": "NonExistentFont"
  }
}
```
**Sonuç**: Varsayılan sistem yazı tipine geçilir

### Geçersiz Renk Kodu
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_color": "invalid-color"
  }
}
```
**Sonuç**: Varsayılan siyah renk kullanılır 
{{< app/cells/assistant language="nodejs-cpp" >}}
