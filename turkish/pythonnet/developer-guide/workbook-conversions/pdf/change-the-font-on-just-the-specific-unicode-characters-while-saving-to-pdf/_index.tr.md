---
title: Belirli Unicode karakterleri kaydederken Yazı Tipini Değiştirin ve Python.NET ile PDF ye Dönüştürün
linktitle: Belirli Unicode karakterlerinde Yazı Tipini Değiştirin
type: docs
weight: 260
url: /tr/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cells for Python via .NET kullanarak PDF dönüştürme sırasında belirli Unicode karakterleri için yazı tiplerini nasıl değiştireceğinizi öğrenin. Karakter seviyesinde yazı tipi ikamesi ile doğru metin işleme sağlayın.
---

{{% alert color="primary" %}}

Bazı Unicode karakterleri kullanıcı tarafından seçilen yazı tipleriyle görüntülenemez. Bu Unicode karakterlerinden biri **Non-breaking Hyphen** (U+2011) ve Unicode numarası 8209'dur. Bu karakter **Times New Roman** ile gösterilemez, ancak **Arial Unicode MS** gibi fontlar ile gösterilebilir.

Bu tür karakterler belirli bir font ile biçimlendirilmiş metinde (örneğin, Times New Roman) göründüğünde, Aspose.Cells varsayılan olarak tüm kelime/cümle fontunu uyumlu bir fonta (örneğin, Arial Unicode MS) değiştirir. Sadece gösterilemeyen karakterin fontunu değiştirmek isteyen kullanıcılar için, **PdfSaveOptions.is_font_substitution_char_granularity** özelliği ile detaylı kontrol sağlarız.

{{% /alert %}}

## **Örnek Karşılaştırması**

Aşağıdaki ekran görüntüleri farklı ayarlarla alınmış çıktıların örnekleridir. İlk PDF tam metin font ikamesini gösterirken, ikinci PDF yalnızca belirli karakterin fontunu değiştirir.

|**Tam Metin İkamesi**|**Karakter Seviyesinde İkame**|
| :- | :- |
|![Tam Font Değişimi](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Seçmeli Font Değişimi](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **Uygulama Adımları**

Karakter seviyesinde font ikamesini etkinleştirmek için:

1. Bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) nesnesi oluşturun
2. Çalışma sayfası hücrelerine [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) özelliği kullanarak erişin
3. Özel Unicode karakterleri içeren hücre değerlerini ayarlayın
4. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)'yi şu şekilde yapılandırın:
   - `is_font_substitution_char_granularity = True`
5. Çalışma kitabını PDF formatında kaydedin

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **Anahtar Yapılandırma**

Bu temel API bileşenlerini kullanın:

- PDF ayarları için [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) sınıfı
- **is_font_substitution_char_granularity** özelliği karakter seviyesinde font ikamesi için
- Çıktı oluşturma için [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) yöntemi

{{% alert color="note" %}} 
**API Fark Notu**: Python.NET'te, boolean özellikler PascalCase yerine snake_case kullanır (`is_font_substitution_char_granularity`).
{{% /alert %}}
