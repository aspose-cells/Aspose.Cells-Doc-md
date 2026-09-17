---
title: Aspose.Cells for Python via .NET ile Mini Grafikleri Görüntüye ve HTML'e Dönüştürme
linktitle: Aspose.Cells for Python via .NET ile Mini Grafikleri Görüntüye ve HTML'e Dönüştürme
description: Aspose.Cells mini grafiklerini hücreye gömülmeleri için bağımsız görüntüler olarak işlemeyi ve HtmlSaveOptions kullanarak mini grafik açısından zengin çalışma sayfalarını Python via .NET'te HTML olarak dışa aktarmayı öğrenin.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, mini grafik işleme, mini grafiği görüntüye dönüştürme, mini grafiği HTML'e dışa aktarma
type: docs
weight: 120
url: /tr/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Mini grafikler (sparkline), çalışma sayfası hücrelerinin içine yerleştirilen küçük grafiklerdir. Aspose.Cells, her mini grafiği bağımsız bir görüntü olarak çıkarmanıza (başka bir hücreye veya harici bir rapora gömmek için) ve ayrıca mini grafik açısından zengin tüm çalışma sayfasını tarayıcı tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `cell.embedded_image` özelliği **Aspose.Cells 26.5 ve sonrasında** kullanılabilir.
{{% /alert %}}

## **Introduction**
Mini grafikler, eğilimleri doğrudan çalışma sayfasının içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları onları yerinde görürken, birçok gerçek dünya senaryosunda mini grafiğin hücreden çıkması gerekir; örneğin farklı bir hücreye statik resim olarak gömülmesi, otomatik bir e-postaya eklenmesi veya web'de yayınlanan bir HTML raporunun parçası olarak işlenmesi gibi.
Aspose.Cells bu iki işlemi de destekler. `sparkline.to_image` yöntemi tek bir mini grafiği bir akışa işler ve elde edilen baytlar `cell.embedded_image` özelliğine atanabilir, böylece resim çalışma kitabının tek bir hücresinde saklanır. Ayrıca `HtmlSaveOptions`, tüm çalışma kitabını — mini grafikler dahil — kendi kendine yeten bir HTML dosyasına dönüştürmenize olanak tanır. Bu makale her iki iş akışını da uçtan uca ele alır.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
Bu iş akışında, kaynak değerlerin küçük bir aralığını içeren bir çalışma sayfası oluşturacak, o aralığa üç farklı mini grafik grubu (Çizgi, Sütun ve Yığılmış/Kazanç-Kayıp) ekleyecek, her grubu PNG olarak işleyecek ve bu PNG baytlarını bitişik hücrelere gömülmüş görüntüler olarak yazacaksınız. Son sonuç, hem canlı mini grafikleri hem de işlenmiş resim karşılıklarını içeren tek bir `.xlsx` dosyasıdır.

### **Step-by-Step Instructions**
1. Bir çalışma dizini tanımlayın ve diskte var olduğundan emin olun.
2. Yeni bir `Workbook` oluşturun ve ilk `Worksheet`'e bir referans edinin.
3. `A1` ile `E1` arasındaki hücreleri beş örnek sayısal değerle doldurun (örneğin, günlük satışlar veya sıcaklık ölçümleri).
4. `worksheet.sparkline_groups.add(...)` çağırarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - Veri aralığı `A1:E1` olan, `F1` hücresine sabitlenmiş bir `SparklineType.LINE` grubu.
   - Veri aralığı `A1:E1` olan, `G1` hücresine sabitlenmiş bir `SparklineType.COLUMN` grubu.
   - Veri aralığı `A1:E1` olan, `H1` hücresine sabitlenmiş bir `SparklineType.STACKED` (kazanç/kayıp) grubu.
5. Bir `ImageOrPrintOptions` örneği oluşturun ve `image_type` özelliğini `ImageType.PNG` olarak ayarlayın, böylece her mini grafik şeffaf bir PNG olarak işlenir.
7. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

```python
import aspose.cells as ac
# Create a new workbook and access the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate sample data in cells A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Add a Line sparkline group anchored at F1 (column 5, row 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
# Add a Column sparkline group anchored at G1 (column 6, row 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
# Configure image options for PNG output
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG
# Convert the Line sparkline to image and embed it in cell F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()
# Convert the Column sparkline to image and embed it in cell G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()
# Convert the Win/Loss sparkline to image and embed it in cell H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()
# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")
```

Yukarıdaki kod, her bir mini grafiğin görsel gösteriminin iki biçimde çoğaltıldığı bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı, yerel mini grafik ve 2. satırdaki bitişik bir hücreye doğrudan gömülmüş statik bir PNG resmi. Resimler dosyanın kendisinde bulunduğundan, çalışma kitabı e-postayla gönderilebilen veya gömülmüş görüntü referansları bozulmadan arşivlenebilen tek bir kendi kendine yeten yapı olarak kalır. Her mini grafik grubunu PNG olarak işleyin, `BytesIO` akışını bir `bytes` nesnesine dönüştürün ve baytları hedef hücrenin `embedded_image` özelliğine atayın — atama işlemi, resmi hücrenin saklanan içeriğinin bir parçası haline getiren şeydir.

{{% alert color="primary" %}}
Her mini grafik grubu tek bir hücreye sabitlendiğinden, bir `for` döngüsü ile numaralandırmak yerine `group.sparklines[0]` indeksleyicisi aracılığıyla ona erişebilirsiniz. Bu, işleme kodunu kısa tutar ve tipik "sabitlenmiş hücre başına bir mini grafik" kalıbıyla eşleşir. Resim baytlarını `cell.embedded_image` ile saklamak için Aspose.Cells 26.5 veya sonrası gereklidir.

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Çalışma kitabı canlı mini grafikler (ve isteğe bağlı olarak gömülmüş resim karşılıkları) içerdiğinde, tüm çalışma sayfası HTML olarak kaydedilerek web'de yayınlanabilir. `HtmlSaveOptions` sınıfı, bu dışa aktarmayı kontrol etmek için ihtiyaç duyduğunuz ayar düğmelerini sunar; bu iş akışında İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasını yeniden kullanacak ve onu temiz, tek sayfalık bir HTML belgesine dönüştüreceksiniz.

### **Step-by-Step Instructions**
1. İş Akışı 1 tarafından üretilen `output_with_sparklines.xlsx` dosyasının çalışma dizininizde diskte mevcut olduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. `HtmlSaveOptions` örneği oluşturun ve `export_active_worksheet_only` özelliğini `True` olarak ayarlayın, böylece ortaya çıkan HTML dosyası yalnızca tüm çalışma kitabı yerine yalnızca etkin çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", html_options)` çağırın.

```python
import aspose.cells as ac
workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Yukarıdaki kod, İş Akışı 1'den gelen mini grafik açısından zengin çalışma kitabını taşınabilir bir HTML dosyasına dönüştürür. Mini grafikler, dışa aktarma moduna bağlı olarak oluşturulan HTML içinde satır içi SVG veya PNG işlemeleri olarak korunur, böylece son kullanıcılar Excel yüklemeye gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `export_active_worksheet_only` özelliğini `True` olarak ayarlayarak, gizli sayfaları veya yardımcı verileri yanlışlıkla yayınlamaktan kaçınırsınız — yalnızca kullanıcının o anda görebildiği çalışma sayfası dışa aktarılır.
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı, çıktıyı ince ayar yapmak için `export_hidden_worksheet`, `export_images_as_base64` ve `encoding` gibi ek özellikler sunar. Bunları dağıtım hedefinize göre gerektiği şekilde ayarlayın.

## **API Summary**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.
- `SparklineGroup` ve koleksiyon erişimcisi `worksheet.sparkline_groups`, her mini grafik grubu için türü (Çizgi, Sütun, Yığılmış), veri aralığını ve sabitlenmiş hücreyi bildirmek için kullanılır. Bu makalede her grup tek bir hücreye sabitlendiğinden, gruba `worksheet.sparkline_groups[i]` aracılığıyla erişilir.
- `Sparkline` ve `group.sparklines[0]` indeksleyicisi, bir grup içindeki tek tek mini grafiği döndürür. Örnekteki her grup tam olarak bir mini grafik içerdiğinden `for` döngüsü gerekmez.
- `sparkline.to_image(Stream, ImageOrPrintOptions)`, mini grafiğin bir resmini sağlanan bir akışa yazan işleme yöntemidir. Yöntem `None` döndürür; baytları çağrıdan sonra akıştan okursunuz.
- `html_save_options.export_active_worksheet_only` (bir `bool`) HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar üretirken `HtmlSaveOptions` üzerindeki en sık kullanılan özelliklerden biridir.
- `image_or_print_options.image_type` özelliği `aspose.cells.drawing` ad alanında bulunur ve `to_image` ile işleme ve çalışma sayfalarını görüntülere yazdırma sırasında kullanılan resim biçimini seçer (örneğin, `ImageType.PNG`).

## **Related Articles**
- [Hücreye Görüntü Ekleme](/cells/tr/python-net/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="python" >}}