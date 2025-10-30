---
title: Birden Çok Çalışma Kitabını Golang kullanarak Tek Kitaba Birleştirme C++ ile
linktitle: Çalışma Kitabı Birleştirme
type: docs
weight: 66
url: /tr/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aspose.Cells kullanarak Golang ile birden çok çalışma kitabını nasıl tek bir kitaba birleştireceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazen, resimler, grafikler ve veriler gibi çeşitli içeriklere sahip iş kitaplarını tek bir dosyada birleştirmeniz gerekebilir. Aspose.Cells bu özelliği destekler. Bu makale, Visual Studio'da nasıl bir konsol uygulaması oluşturacağınızı ve birkaç basit satır kodla Aspose.Cells kullanarak iş kitaplarını nasıl birleştireceğinizi gösterir.

{{% /alert %}}

## **Resimler ve Grafiklerle Çalışma Kitaplarını Birleştirme**

Örnek kod, Aspose.Cells kullanarak iki çalışma kitabını tek bir çalışma kitabına birleştirir. Kod, kaynak çalışma kitaplarını yükler, bunları birleştirmek için [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) yöntemini kullanır ve çıktı çalışma kitabını kaydeder.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Gelişmiş Konular**
- [Birden Fazla Çalışma Sayfasını Tek Bir Çalışma Sayfasına Birleştirme](/cells/tr/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dosyaları Birleştirme](/cells/tr/cpp/merge-files/)
