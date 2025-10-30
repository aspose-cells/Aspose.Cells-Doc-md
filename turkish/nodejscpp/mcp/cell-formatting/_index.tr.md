---
title: Excel Hücre Biçimlendirme
linktitle: Hücre Biçimlendirme
type: docs
weight: 40
url: /tr/nodejs-cpp/mcp/cell-formatting
keywords: "Excel hücre biçimlendirmesi, Excel hücre stilleri, Excel kenarlıklar, Excel hizalama, Excel arka plan renkleri, Yapay Zeka Excel biçimlendirme"
description: "Excel hücre biçimlendirmesi  yapay zeka otomasyonuyla arka planlar, kenarlıklar, hizalama, sayı biçimleri ve hücre stilleri uygulayın"
---

# Excel Hücre Biçimlendirme

Yapay zeka destekli otomasyon ile profesyonel **Excel hücre biçimlendirmesi** uygulayın. **Excel hücreleri** arka planlar, kenarlıklar, hizalama, sayı biçimleri ve gelişmiş hücre özellikleriyle stillendirin.

## Mevcut Araçlar

- `cell_format` - **Excel hücre biçimlendirmesi** (arka plan, kenarlıklar, hizalama, sayı biçimi) **Excel MCP** ile
- `cell_format_batch` - Çoklu aralıklar üzerinde toplu **Excel hücre biçimlendirmesi** uygulamak için **Yapay Zeka otomasyonu** ile

## Tek Hücre Biçimlendirmesi

### Temel Hücre Stilizasyonu
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/formatted-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "background_color": "#4472C4",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "text_wrap": true
  }
}
```

### Profesyonel Başlık Biçimlendirmesi
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "range": "A1:F1",
    "background_color": "#2E5984",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "border_color": "#000000",
    "text_wrap": true
  }
}
```

### Sayı Biçimlendirmesi
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/financial.xlsx",
    "sheet_name": "Budget",
    "range": "C2:C10",
    "number_format": "$#,##0.00",
    "horizontal_align": "right"
  }
}
```

## Toplu Hücre Biçimlendirme

### Tam Rapor Stilizasyonu
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A1:F1",
        "background_color": "#2E5984",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "border_style": "thick",
        "border_color": "#000000"
      },
      {
        "range": "B2:B4",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "C2:C4",
        "number_format": "0",
        "horizontal_align": "center"
      },
      {
        "range": "D2:F5",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "A5:F5",
        "border_style": "thick",
        "border_sides": ["top"]
      }
    ]
  }
}
```

### Gelişmiş Kenarlık Stilleri
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/border-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A5:A7",
        "border_style": "thin",
        "border_color": "#000000",
        "border_sides": ["all"]
      },
      {
        "range": "B5:B7",
        "border_style": "medium",
        "border_color": "#FF0000",
        "border_sides": ["outline"]
      },
      {
        "range": "C5:C7",
        "border_style": "dashed",
        "border_color": "#0000FF",
        "border_sides": ["top", "bottom"]
      },
      {
        "range": "D5:D7",
        "border_style": "dotted",
        "border_color": "#00FF00",
        "border_sides": ["left", "right"]
      },
      {
        "range": "E5:E7",
        "border_style": "double",
        "border_color": "#FF00FF",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Metin Hizalama Gösterisi
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/alignment-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A10",
        "horizontal_align": "left",
        "vertical_align": "top",
        "background_color": "#FFE6E6"
      },
      {
        "range": "B10",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "background_color": "#E6FFE6"
      },
      {
        "range": "C10",
        "horizontal_align": "right",
        "vertical_align": "bottom",
        "background_color": "#E6E6FF"
      },
      {
        "range": "D10",
        "horizontal_align": "justify",
        "vertical_align": "justify",
        "text_wrap": true,
        "background_color": "#FFFFE6"
      },
      {
        "range": "E10",
        "horizontal_align": "fill",
        "indent": 2,
        "background_color": "#FFE6FF"
      }
    ]
  }
}
```

### Metin Döndürme Efektleri
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/rotation-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D1",
        "text_rotation": 45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "E1",
        "text_rotation": -45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "F1",
        "text_rotation": 90,
        "horizontal_align": "center",
        "vertical_align": "middle"
      }
    ]
  }
}
```

## Formatlama Parametreleri Referansı

### Arka Plan Renkleri
- `"#FFFFFF"` - Beyaz
- `"#4472C4"` - Profesyonel mavi
- `"#E6F3FF"` - Açık mavi
- `"#FFFF00"` - Sarı
- `"#FFE6E6"` - Açık kırmızı
- `"#E6FFE6"` - Açık yeşil
- `"#F0F8FF"` - Alice mavisi

### Yatay Hizalama
- `"left"` - Sola hizalanmış
- `"center"` - Ortaya hizalanmış
- `"right"` - Sağa hizalanmış
- `"justify"` - Yere göre hizalanmış
- `"fill"` - Hücreyi doldur

### Dikey Hizalama
- `"top"` - Üst hizalanmış
- `"middle"` - Ortada hizalanmış
- `"bottom"` - Aşağı hizalanmış
- `"justify"` - Dikey olarak hizalı

### Kenarlık Stilleri
- `"none"` - Kenarlık yok
- `"thin"` - İnce çizgi
- `"medium"` - Orta çizgi
- `"thick"` - Kalın çizgi
- `"dashed"` - Kesikli çizgi
- `"dotted"` - Noktalı çizgi
- `"double"` - Çift çizgi

### Kenarlık Yanları
- `["all"]` - Tüm kenarlar
- `["top", "bottom"]` - Üst ve alt
- `["left", "right"]` - Sol ve sağ
- `["outline"]` - Sadece dış sınırlar
- `["inside"]` - Sadece iç sınırlar

### Sayı Formatları
- `"General"` - Varsayılan format
- `"0"` - Tam sayı
- `"0.00"` - İki ondalık basamağı
- `"0%"` - Yüzde
- `"$#,##0.00"` - Binlik ayırıcıyla para birimi
- `"yyyy-mm-dd"` - Tarih Formatı
- `"h:mm AM/PM"` - Saat formatı

### Metin Özellikleri
- `text_wrap: true` - Hücrede metni kaydır
- `text_rotation: 45` - Metni döndür (derece)
- `indent: 2` - Metin seviyesini girintile
- `locked: true` - Hücreyi koruma amacıyla kilitle
- `hidden: true` - Hücre formülünü gizle

## Gelişmiş Formatlama Örnekleri

### Finansal Rapor Stili
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-complete.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D2:D5",
        "background_color": "#F0F8FF"
      },
      {
        "range": "E2:E5",
        "background_color": "#FFF0F0"
      },
      {
        "range": "F2:F5",
        "background_color": "#F0FFF0",
        "border_style": "double",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Veri Doğrulama Vurgulama
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/data-validation.xlsx",
    "sheet_name": "Data",
    "format_ranges": [
      {
        "range": "A2:A10",
        "background_color": "#90EE90"
      },
      {
        "range": "B2:B10",
        "background_color": "#FFB6C1"
      },
      {
        "range": "C2:C10",
        "background_color": "#87CEEB",
        "border_style": "thin",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Koruma Ayarları
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/protected.xlsx",
    "sheet_name": "Sheet1",
    "range": "B1:B5",
    "locked": false,
    "hidden": true
  }
}
```

## En İyi Uygulamalar

1. **Renk Uyumu**: Profesyonel görünüm için tamamlayıcı renkler kullanın
2. **Kontrast**: Metnin arka plan renklerine karşı okunabilir olduğundan emin olun
3. **Tutarlılık**: Benzer veriler arasında tutarlı formatlama uygulayın
4. **Kenar Çizgileri**: Bölümleri ayırmak ve önemli verileri vurgulamak için kenarlıklar kullanın
5. **Sayı Formatları**: Veri tiplerine uygun sayı formatları uygulayın

## Yaygın Kullanım Durumları

### Rapor Başlıkları
- Koyu arka plan ile beyaz metin
- Ortalanmış hizalama
- Kalın sınırlar
- Metin kaydırma etkin

### Mali Veri
- Para birimi biçimi
- Sayılar için sağ hizalama
- Negatif değerleri vurgulama
- Binlik ayırıcılar

### Durum Göstergeleri
- Renk kodlu arka planlar
- Ortalanmış hizalama
- Kalın sınırlar
- Açık görsel ayrım

### Veri Tabloları
- Alternatif satır renkleri
- Tutarlı sütun genişlikleri
- Uygun sayı formatları
- Açık başlık stili

## Hata Yönetimi

### Geçersiz Renk Kodu
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "background_color": "invalid-color"
  }
}
```
**Sonuç**: Varsayılan arka plan rengi kullanır

### Geçersiz Sayı Formatı
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "number_format": "invalid-format"
  }
}
```
**Sonuç**: Yedek olarak Genel format kullanır 
{{< app/cells/assistant language="nodejs-cpp" >}}
