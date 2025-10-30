---
title: Python.NET ile Excel sayfasını Fit edilmiş Sayfalar Geniş ve Yüksek olarak Yazdırma
linktitle: Excel i Geniş ve Yüksek olarak Yazdırma
type: docs
weight: 200
url: /tr/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Aspose.Cells for Python via .NET API kullanarak Excel yazdırma için fit_to_pages_wide ve fit_to_pages_tall özelliklerini ayarlamayı öğrenin.
keywords: Python Excel Yazdırma, Python Sayfaya Sığdırma Ayarları, Python FitToPagesWide, Python FitToPagesTall, Python Tek Sayfa Olarak Sayfa Yazdırma, Python Tüm Sütunları Tek Sayfa Olarak Yazdırma
---

## **Giriş**

fit_to_pages_wide ve fit_to_pages_tall ayarları, yazdırma sırasında tabloyu ölçeklendirir. Bu ayarlar, baskıya alınan çıktının belirli sayfa boyutları içinde olmasını sağlar:

1. **fit_to_pages_wide**: Yazdırma için yatay sayfa sayısını belirtir
1. **fit_to_pages_tall**: Yazdırma için dikey sayfa sayısını belirtir

## **Neden FitToPagesWide ve FitToPagesTall Kullanılır**
Ana faydalar şunları içerir:
1. Hassas yazdırma düzeni kontrolü
1. Tutarlı çok sayfalı biçimlendirme
1. Profesyonel belge sunumu

## **Excel'de Dosyayı Geniş ve Yüksek olarak Yazdırmak için nasıl yapılır**
Microsoft Excel'de yapılandırmak için:
1. Çalışma kitabını açın ve çalışma sayfasını seçin
1. **Sayfa Düzeni** → **Sayfa Ayarı** iletişim kutusuna gidin
1. **Sayfa** sekmesinde, **Ölçeklendirme** altında:
   - "Genişliğe göre sığdır" seçeneğini seçin
   Sayfaları geniş (yatay) ve yüksek (dikey) olarak belirt

<br>
<img src="2.png" width=60% />

## **Aspose.Cells kullanarak Excel'i Uyumlu Sayfalar Geniş ve Yüksek olarak Yazdırma Yöntemi**
Programatik olarak yapılandırmak için:
1. [örnek dosya](input.xlsx) yükle
1. Çalışma sayfasının [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) nesnesine eriş
1. [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) ve [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/) özelliklerini ayarla

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Çalışma Sayfasını Tek Sayfa Olarak Yazdırma**
Tek sayfa çıktı almak için:
1. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) kullan
1. [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/) özelliğini ayarla

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

Çıktı sonucu:
<br>
<img src="3.png" width=60% />

## **Tüm Sütunları Bir Sayfada Yazdırma Yöntemi**
Sütunları yatay olarak birleştirmek için:
1. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) yapılandır
1. [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/) özelliğini etkinleştir

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

Çıktı sonucu:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
