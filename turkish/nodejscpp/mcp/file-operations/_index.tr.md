---
title: Excel Dosyası ve Veri İşlemleri
linktitle: Dosya ve Veri İşlemleri
type: docs
weight: 10
url: /tr/nodejs-cpp/mcp/file-operations
keywords: "Excel dosya işlemleri, Excel veri işlemleri, Excel çalışma kitabı oluşturma, Excel çalışma sayfası, Excel verisini okuma, Excel verisine yazma"
description: "Excel dosya ve veri işlemleri  çalışma kitapları oluşturma, çalışma sayfalarını yönetme, AI otomasyonu ile Excel verisini okuma ve yazma"
---

# Excel Dosyası ve Veri İşlemleri

AI destekli otomasyon ile **Excel dosyalarını** ve **veri işlemlerini** yönetin. **Excel çalışma kitapları** oluşturun, **çalışma sayfalarını** yönetin ve **Excel verisi** okuma/yazma işlemleri yapın.

## Kullanılabilir Araçlar

- `create_workbook` - AI Excel otomasyonu ile yeni **Excel çalışma kitapları** oluşturun
- `create_worksheet` - Mevcut **Excel çalışma kitaplarına** **Excel çalışma sayfaları** ekleyin
- `get_workbook_info` - **Excel çalışma kitabı** meta verisi ve bilgileri alın
- `read_data_from_excel` - **AI destekli** hassasiyetle **Excel çalışma sayfalarından** veri okuyun
- `write_data_to_excel` - **Excel MCP** aracılığıyla **Excel çalışma sayfalarına** veri yazın

## Excel Çalışma Kitapları Oluşturma

### Temel Çalışma Kitabı Oluşturma
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Özel Sayfa ile Çalışma Kitabı Oluşturma
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Çalışma Sayfalarını Yönetme

### Yeni Çalışma Sayfası Ekleme
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Çalışma Kitabı Bilgisi Alma
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Excel Verisi Yazma

### Başlıklar ve Veri Yazma
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### Veriyi Özel Konuma Yaz
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Excel Verisi Oku

### Kullanılan Tam Aralığı Oku
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Belirli Aralığı Oku
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### Varsayılan Konumdan Oku
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## Tam İş Akışı Örneği

### 1. İlk Excel Raporunuzu Oluşturun
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Özet Sayfası Ekleyin
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Satış Verisi Yazın
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. Veriyi Doğrula
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. Çalışma Kitabı Yapısını Kontrol Et
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## En İyi Uygulamalar

1. **Dosya Yolları**: Taşınabilirliği artırmak için göreceli yollar kullanın
2. **Sayfa İsimleri**: Sayfa adlarını açıklayıcı kullanın
3. **Veri Yapısı**: Veriyi net başlıklarla düzenleyin
4. **Aralık Okuma**: Büyük veri setleri için aralık belirtin
5. **Hata Yönetimi**: İşlemlerden önce dosya varlığını doğrulayın

## Yaygın Desenler

### Veri İçe Aktarma Deseni
1. Çalışma Kitabı Oluştur
2. Ham veri yaz
3. Doğrulama için geri oku
4. Formüllerle işle

### Çok Sayfalı Raporlar
1. Ana sayfa ile çalışma kitabı oluştur
2. Özet/analiz sayfaları ekle
3. Her sayfaya veri yaz
4. Sayfaları formüllerle bağla

### Veri Doğrulama
1. Veri yaz
2. Belirli aralıkları geri oku
3. Veri bütünlüğünü doğrula
4. Eksik değerleri işle 
{{< app/cells/assistant language="nodejs-cpp" >}}
