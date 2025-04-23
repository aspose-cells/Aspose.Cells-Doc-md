---
title: Birden Fazla Çalışma Kitabını Birleştirme
linktitle: Çalışma Kitabı Birleştirme
type: docs
weight: 66
url: /tr/net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Bazen, resimler, grafikler ve veri gibi çeşitli içerikler içeren çalışma kitaplarını tek bir çalışma kitabı içinde birleştirmeniz gerekebilir. Aspose.Cells bu özelliği destekler. Bu makale, Aspose.Cells kullanarak birkaç basit kod satırıyla Visual Studio'da bir konsol uygulaması nasıl oluşturulacağını ve çalışma kitaplarını nasıl birleştirileceğini gösterir.

{{% /alert %}}

## **Resimler ve Grafiklerle Çalışma Kitaplarını Birleştirme**

Örnek kod, Aspose.Cells kullanarak iki çalışma kitabını tek bir çalışma kitabına birleştirir. Kod, kaynak çalışma kitaplarını yükler, bunları birleştirmek için [**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) yöntemini kullanır ve çıktı çalışma kitabını kaydeder.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Gelişmiş Konular**
- [Birden Fazla Çalışma Sayfasını Tek Bir Çalışma Sayfasına Birleştirme](/cells/tr/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dosyaları Birleştirme](/cells/tr/net/merge-files/)
{{< app/cells/assistant language="csharp" >}}
