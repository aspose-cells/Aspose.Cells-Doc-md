---
title: Aspose.Cells for Python via .NET'te Sparkline'ı Görüntüye ve HTML'e Dönüştürme
linktitle: Convert Sparkline to Image and HTML
description: Python via .NET'te Aspose.Cells sparkline'larını hücre gömme için bağımsız görüntüler olarak nasıl işleyeceğinizi ve HtmlSaveOptions kullanarak sparkline açısından zengin çalışma sayfalarını HTML'e nasıl aktaracağınızı öğrenin.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, sparkline işleme, sparkline'ı görüntüye dönüştürme, sparkline'ı HTML'e aktarma
type: docs
weight: 120
url: /tr/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparkline'lar, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells, her bir sparkline'ı bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca sparkline açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML'e aktarmanıza olanak tanır. Bu makalede kullanılan `cell.embedded_image` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Giriş**

Sparkline'lar, trendleri doğrudan bir çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görürken, birçok gerçek dünya senaryosunda bir sparkline'ın hücreden çıkması gerekir — örneğin, farklı bir hücreye statik resim olarak gömülmek, otomatik bir e-postaya eklenmek veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmek üzere.

Aspose.Cells bu iki işlemi de destekler. `sparkline.to_image` yöntemi, tek bir sparkline'ı bir akışa işler ve ortaya çıkan baytlar `cell.embedded_image`'a atanabilir, böylece resim çalışma kitabının tek bir hücresinde saklanır. Ayrı olarak, `HtmlSaveOptions` tüm çalışma kitabını — sparkline'lar dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele almaktadır.

## **İş Akışı 1 — Sparkline'ları Görüntülere İşleyin ve Hücrelere Gömün**

Bu iş akışında, küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı sparkline grubu (Çizgi, Sütun ve Yığılmış/Kazanç-Kayıp) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Sonuç, hem canlı sparkline'ları hem de bunların işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Adım Adım Talimatlar**

1. Bir çalışma dizini tanımlayın ve diskte mevcut olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans elde edin.
3. `A1`'den `E1`'e kadar olan hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık okumaları).
4. `worksheet.sparkline_groups.add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - `F1`'e ankrajlanmış bir `SparklineType.LINE` grubu, veri aralığı `A1:E1`.
   - `G1`'e ankrajlanmış bir `SparklineType.COLUMN` grubu, veri aralığı `A1:E1`.
   - `H1`'e ankrajlanmış bir `SparklineType.STACKED` (kazanç/kayıp) grubu, veri aralığı `A1:E1`.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve `image_type` özelliğini `ImageType.PNG` olarak ayarlayın, böylece her sparkline şeffaf bir PNG olarak işlenir.
6. Üç grubun her biri için, `group.sparklines[0].to_image(memory_stream, image_options)` kullanarak tek sparkline'ını işleyin, `BytesIO` akışını bir `bytes` nesnesine dönüştürün ve diziyi sırasıyla `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` ve `worksheet.cells["H2"].embedded_image`'a atayın.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# A1:E1 hücrelerine örnek veri yerleştir
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# F1 hücresine sabitlenmiş bir Çizgi mini grafik grubu ekle (sütun 5, satır 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# G1 hücresine sabitlenmiş bir Sütun mini grafik grubu ekle (sütun 6, satır 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# H1 hücresine sabitlenmiş bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekle (sütun 7, satır 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# PNG çıktısı için görüntü seçeneklerini yapılandır
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Çizgi mini grafiğini görüntüye dönüştür ve F2 hücresine göm
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Sütun mini grafiğini görüntüye dönüştür ve G2 hücresine göm
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Kazanma/Kaybetme mini grafiğini görüntüye dönüştür ve H2 hücresine göm
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Çalışma kitabını diske kaydet
workbook.save("output_with_sparklines.xlsx")
```

Yukarıdaki kod, her bir sparkline görsel temsilinin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra ankrajlanmış canlı, yerel sparkline ve 2. satırdaki komşu bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisi içinde yaşadığı için, çalışma kitabı gömülü görüntü referanslarını bozmadan e-posta ile gönderilebilen veya arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her sparkline grubunu PNG olarak işleyin, `BytesIO` akışını bir `bytes` nesnesine dönüştürün ve baytları hedef hücrenin `embedded_image` özelliğine atayın — atama, resmin hücrenin saklanan içeriğinin bir parçası olmasını sağlayan şeydir.

{{% alert color="primary" %}}
Her sparkline grubu tek bir hücreye ankrajlandığı için, bir `for` döngüsü ile numaralandırmak yerine `group.sparklines[0]` indeksleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "ankraj hücresi başına bir sparkline" deseniyle eşleşir. Resim baytlarını `cell.embedded_image` aracılığıyla saklamak Aspose.Cells 26.5 veya sonrasını gerektirir.
{{% /alert %}}

## **İş Akışı 2 — Sparkline Çalışma Sayfasını HTML'e Aktarın**

Çalışma kitabı canlı sparkline'ları (ve isteğe bağlı olarak gömülü resim karşılıklarını) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarımı kontrol etmek için ihtiyaç duyduğunuz düğmeleri sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Adım Adım Talimatlar**

1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions`'ı örnekleyin ve `export_active_worksheet_only` özelliğini `True` olarak ayarlayın, böylece ortaya çıkan HTML dosyası tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", html_options)` çağırın.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Yukarıdaki kod, İş Akışı 1'deki sparkline açısından zengin çalışma kitabını alır ve onu taşınabilir bir HTML dosyasına dönüştürür. Sparkline'lar, dışa aktarma moduna bağlı olarak, oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan trendleri herhangi bir modern tarayıcıda görüntüleyebilir. `export_active_worksheet_only`'i `True` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcının o anda gördüğü çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `export_hidden_worksheet`, `export_images_as_base64` ve `encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği gibi ayarlayın.
{{% /alert %}}

## **API Özeti**

Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.

- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparkline_groups`, her sparkline grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve ankraj hücresini bildirmek için kullanılır. Bu makalede her grup tek bir hücreye ankrajlandığı için, gruba `worksheet.sparkline_groups[i]` aracılığıyla ulaşılır.
- `Sparkline` ve indeksleyici `group.sparklines[0]`, grup içindeki tek tek sparkline'ı döndürür. Örnekteki her grup tam olarak bir sparkline içerdiğinden, `for` döngüsü gerekmez.
- `sparkline.to_image(Stream, ImageOrPrintOptions)`, sparkline'ın bir resmini sağlanan akışa yazan işleme yöntemidir. Yöntem `None` döndürür; baytları çağrıdan sonra akıştan okursunuz.
- `cell.embedded_image`, tek bir hücrenin içine bir resim saklayan bir `bytes` özelliğidir. **Aspose.Cells 26.5 ve sonrasında** kullanılabilir ve `to_image` tarafından işlenen bir sparkline'ı aynı çalışma kitabına geri döndürmenin önerilen yoludur.
- `html_save_options.export_active_worksheet_only` (bir `bool`), HTML dışa aktarımını etkin çalışma sayfasıyla sınırlandırır. Tek sayfalık raporlar oluştururken `HtmlSaveOptions`'ın en sık kullanılan özelliklerinden biridir.
- `image_or_print_options.image_type`, `aspose.cells.drawing` ad alanında bulunur ve `to_image` ile işlenirken ve çalışma sayfaları görüntülere yazdırılırken kullanılan resim formatını (örneğin, `ImageType.PNG`) seçer.

## **İlgili Makaleler**

- [Aspose.Cells for Python via .NET'te Sparkline'lar](/cells/tr/python-net/sparkline/)
- [Hücreye Görüntü Ekleme](/cells/tr/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Tek Hücreli Dizi İşleme | Aspose.Cells for Python via .NET](/cells/tr/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}