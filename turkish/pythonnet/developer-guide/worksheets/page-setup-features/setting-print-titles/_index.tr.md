---
title: Python.NET ile Yazdırma Başlıklarını Ayarla
linktitle: Yazdırma Başlıklarını Ayarlama
type: docs
weight: 200
url: /tr/python-net/how-to-set-print-titles/
description: Aspose.Cells for Python via .NET kullanarak basılan sayfalarda tekrar eden satır/kolon başlıklarının nasıl yapılandırılacağını öğrenin.
keywords: Python tekrar yazdırma başlıkları, Python yazdırma başlıklarını ayarlama, Python yazdırma başlıklarını temizleme, Excel sayfa ayarı Python, Python.NET hesap tablosu yazdırma
---

## **Olası Kullanım Senaryoları**

Excel'de yazdırma başlıklarını ayarlamak, belirli satır veya kolonların her yazdırılan sayfada tekrarlanmasını sağlar, bu özellik büyük elektronik tablolar için özellikle faydalıdır. İşte birkaç neden:

1. Artırılmış Okunabilirlik: Yazdırma başlıkları, başlıkları tüm sayfalarda görünür tutarak veriyi anlamaya yardımcı olur, böylece her seferinde ilk sayfaya dönmeden bilgileri yorumlamak daha kolay hale gelir.

1. Profesyonel Sunum: Her sayfada tutarlı bir şekilde başlıklar veya etiketler göstermek, yazdırılmış belgeler için daha düzgün ve profesyonel bir görünüm sağlar.

1. Gelişmiş Navigasyon: Geniş veriler içeren belgelerde, her sayfada başlıkların tekrarlanması, daha hızlı gezinme ve referans sağlar, böylece sayfalar arasında geri dönüp gitme ihtiyacını azaltır.

1. Hata Azaltma: Her sayfada başlıklar olduğunda, yanlış anlamalar veya veri giriş hataları minimize edilir, kullanıcılar verilerin bağlamını kolayca görebilir.

1. Tutarlılık: Kolon başlıkları veya satır etiketleri gibi önemli bilgilerin her zaman görünür olması, belge genelinde tutarlılık ve açıklık sağlar.

## **Excel’de Yazdırma Başlıklarını Nasıl Ayarlarsınız**

Excel’de yazdırma başlıklarını ayarlamak için şu adımları izleyin:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Başlıklarına Erişin: "Sayfa Ayarı" grubunda "Yazdırma Başlıkları"na tıklayın.
1. Satırları Tekrarlamak İçin Ayarlayın: "Sayfa Ayarı" iletişim kutusunda, "Sayfa" sekmesine gidin. "Yazdırma başlıkları" bölümünde, "Üstte tekrarlanacak satırlar" kutusuna tıklayın ve tekrarlanmasını istediğiniz satırları seçin.
1. Kolonları Tekrarlamak İçin Ayarlayın (gerekirse): Aynı şekilde, "Sol tarafta tekrarlanacak kolonlar" kutusuna tıklayın ve tekrarlanmasını istediğiniz kolonları seçin.
<br>
<img src="3.png" width=60% />

1. Onaylayın ve Yazdırın: "Tamam"a tıklayarak ayarları uygulayın. Çalışma sayfasını yazdırdığınızda, belirttiğiniz satırlar veya kolonlar her sayfada görünecektir.

## **Excel’de Yazdırma Başlıklarını Nasıl Temizlersiniz**

Excel’de yazdırma başlıklarını temizlemek için, her yazdırılan sayfada tekrarlanan satır veya kolonları kaldırmanız gerekir. İşte nasıl yapılır:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Başlıklarına Erişin: "Sayfa Ayarı" grubunda "Yazdırma Başlıkları"na tıklayın.
1. Yazdırma Başlıklarını Temizle: "Sayfa Ayarı" iletişim kutusunda, "Sayfa" sekmesine gidin. "Üstte tekrarlanacak satırlar" ve "Sol tarafta tekrarlanacak kolonlar" metin kutularını temizleyin ve içlerindeki içerikleri silin.
<br>
<img src="4.png" width=60% />

1. Onaylayın ve Kapatın: Değişiklikleri uygulamak için "Tamam"a tıklayın.

## **Aspose.Cells kullanarak Yazdırma Başlıklarını Nasıl Ayarlarsınız**

Belirli bir çalışma sayfasında yazdırma başlıklarını ayarlamak için: Öncelikle, [örnek dosyayı](input.xlsx) yükleyin, ardından [**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/) ve [**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) nesnesinin. Bu özellikleri bir alan dizesi olarak ayarlamak, yazdırma başlıklarını yapılandırır.

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells kullanarak Yazdırma Başlıklarını Temizleme**

Yazdırma başlıklarını temizlemek için, yazdırma başlığı özelliklerini boş dizeler olarak ayarlayın:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

Çıktı sonucu:
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
