---
title: Excel Formülü İşlemleri  Excel Formülü MCP
linktitle: Formül İşlemleri  Excel Formülü MCP
type: docs
weight: 20
url: /tr/nodejs-cpp/mcp/apply-formula
keywords: "Excel Formülü MCP, Excel formülleri, AI Excel formülleri, Excel formülü otomasyonu, Excel hesaplamaları"
description: "Excel Formülü MCP  AI otomasyonu ile Excel formülleri uygulama, tek ve toplu Excel formülü işlemleri"
---

# Excel Formülü İşlemleri

**Excel Formülü MCP** güçlü **Excel formülü** otomasyonu sağlar ve AI entegrasyonu ile çalışır. **Excel formülleri** tek hücreye veya toplu işlemler halinde birden fazla hücreye uygulayın.

## Mevcut Araçlar

- `apply_formula` - **Excel Formülü MCP** kullanarak tek hücreye **Excel formülleri** uygulama
- `apply_formula_batch` - **AI Excel** kullanarak toplu halde birkaç hücreye **Excel formülleri** uygulama

## Tekli Formül İşlemleri

### Eşittir İşareti ile Formül Uygulama
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/calculations.xlsx",
    "sheet_name": "Data",
    "cell": "D2",
    "formula": "=B2*C2"
  }
}
```

### Eşittir İşareti olmadan Formül Uygulama
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/calculations.xlsx",
    "sheet_name": "Data",
    "cell": "E2",
    "formula": "SUM(B2:D2)"
  }
}
```

### Yaygın Excel Formülleri
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Summary",
    "cell": "F2",
    "formula": "=AVERAGE(A2:E2)"
  }
}
```

## Toplu Formül İşlemleri

### Satış Raporu Toplamlarını Hesapla
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "formulas": [
      { "cell": "E2", "formula": "=C2*D2" },
      { "cell": "E3", "formula": "=C3*D3" },
      { "cell": "E4", "formula": "=C4*D4" },
      { "cell": "E5", "formula": "=SUM(E2:E4)" }
    ]
  }
}
```

### Vergi Hesaplamalı Finansal Rapor
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "formulas": [
      { "cell": "D2", "formula": "=B2*C2" },
      { "cell": "D3", "formula": "=B3*C3" },
      { "cell": "D4", "formula": "=B4*C4" },
      { "cell": "E2", "formula": "=D2*0.1" },
      { "cell": "E3", "formula": "=D3*0.1" },
      { "cell": "E4", "formula": "=D4*0.1" },
      { "cell": "F2", "formula": "=D2+E2" },
      { "cell": "F3", "formula": "=D3+E3" },
      { "cell": "F4", "formula": "=D4+E4" },
      { "cell": "D5", "formula": "=SUM(D2:D4)" },
      { "cell": "E5", "formula": "=SUM(E2:E4)" },
      { "cell": "F5", "formula": "=SUM(F2:F4)" }
    ]
  }
}
```

### Karışık Formül Sözdizimi
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data",
    "formulas": [
      { "cell": "F4", "formula": "=D4*2" },
      { "cell": "F5", "formula": "D5*2" },
      { "cell": "F6", "formula": "=D6*2" },
      { "cell": "G4", "formula": "=D4+10" },
      { "cell": "G5", "formula": "=D5+10" },
      { "cell": "G6", "formula": "=D6+10" },
      { "cell": "G7", "formula": "=SUM(G4:G6)" }
    ]
  }
}
```

## Yaygın Excel Fonksiyonları

### Matematiksel Fonksiyonlar
- `SUM(aralık)` - Aralıktaki değerleri topla
- `AVERAGE(aralık)` - Ortalamayı hesapla
- `MIN(aralık)` - En küçük değeri bul
- `MAX(aralık)` - En büyük değeri bul
- `COUNT(aralık)` - Sayısal hücreleri sayar

### Mantıksal Fonksiyonlar
- `IF(koşul, doğru_değer, yanlış_değer)` - Koşullu mantık
- `AND(koşul1, koşul2)` - Mantıksal VE
- `OR(koşul1, koşul2)` - Mantıksal VEYA

### Metin Fonksiyonları
- `CONCATENATE(metin1, metin2)` - Metinleri birleştir
- `LEFT(metin, karakter_sayısı)` - Soldaki karakterleri çıkar
- `RIGHT(metin, karakter_sayısı)` - Sağdaki karakterleri çıkar
- `LEN(metin)` - Metin uzunluğu

## En İyi Uygulamalar

1. **Formül Sözdizimi**: Hem `=SUM(A1:A10)` hem de `SUM(A1:A10)` çalışır
2. **Hücre Referansları**: Gerekirse mutlak referans (`$A$1`) kullanın
3. **Hata İşleme**: Formülleri önce basit verilerle test edin
4. **Toplu İşlemler**: Birden fazla benzer formül için toplu işlemler kullanın
5. **Formül Doğrulama**: Formülleri uyguladıktan sonra sonuçları kontrol edin

## Hata İşleme

### Boş Formüller Dizisi
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "formulas": []
  }
}
```
**Sonuç**: Boş dizi için doğrulama hatası

### Geçersiz Formül
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "cell": "A1",
    "formula": "=INVALID_FUNCTION(A1)"
  }
}
```
**Sonuç**: Formül sözdizimi hatası
{{< app/cells/assistant language="nodejs-cpp" >}}
