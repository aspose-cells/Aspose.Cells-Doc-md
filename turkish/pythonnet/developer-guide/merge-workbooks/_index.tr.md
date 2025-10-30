---
title: Birden Fazla Çalışma Kitabını Birleştirme
linktitle: Çalışma Kitabı Birleştirme
type: docs
weight: 66
url: /tr/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Bazen, çeşitli içeriklere sahip çalışma kitaplarını, örneğin resimler, grafikler ve veriler, tek bir çalışma kitabında birleştirmeniz gerekebilir. Aspose.Cells for Python via .NET bu özelliği destekler. Bu makale, Visual Studio'da bir konsol uygulaması oluşturma ve Aspose.Cells for Python via .NET kullanarak birkaç basit satır kodla çalışma kitaplarını birleştirme yöntemlerini gösterir.

{{% /alert %}}

## **Resimler ve Grafiklerle Çalışma Kitaplarını Birleştirme**

Örnek kod, iki çalışma kitabını Aspose.Cells for Python via .NET kullanarak tek bir çalışma kitabına birleştirir. Kod, kaynak çalışma kitaplarını yükler, [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) metodunu kullanarak birleştirir ve çıktı çalışma kitabını kaydeder.

### **Kaynak Çalışma Kitapları**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Çıktı Çalışma Kitapları**

- [combined.xlsx](5473095.xlsx)

### **Ekran Görüntüleri**

Aşağıda, kaynak ve çıktı çalışma kitaplarının ekran görüntüleri bulunmaktadır.

{{% alert color="primary" %}}

Herhangi bir kaynak çalışma kitabını kullanabilirsiniz. Bu resimler sadece görsel amaçlar içindir.

{{% /alert %}}

**Grafik çalışma kitabının ilk çalışsayfası - yığılmış** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Grafik çalışma kitabının ikinci çalışsayfası - çizgi** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Resim çalışma kitabının ilk çalışma sayfası - resim** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Birleşik çalışma kitabındaki tüm üç çalışma sayfası - yığılmış, çizgi, resim** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Gelişmiş Konular**
- [Birden Fazla Çalışma Sayfasını Tek Bir Çalışma Sayfasına Birleştirme](/cells/tr/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dosyaları Birleştirme](/cells/tr/python-net/merge-files/)

{{< app/cells/assistant language="python-net" >}}
