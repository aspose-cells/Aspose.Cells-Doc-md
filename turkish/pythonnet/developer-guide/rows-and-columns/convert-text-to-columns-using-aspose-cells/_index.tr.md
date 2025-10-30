---
title: Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme
type: docs
weight: 30
url: /tr/python-net/convert-text-to-columns-using-aspose-cells/
description: Bu makale, Aspose.Cells for Python via .NET API sini kullanarak Metni Sütunlara Dönüştürmeyi göstermektedir.
keywords: Python Excel Kütüphanesi, Python Metni Sütunlara Dönüştürme, Metni Python da Sütunlara Dönüştürme, Python da Metni Sütunlara Dönüştürme.
---

## **Olası Kullanım Senaryoları**

Metni Sütunlara Dönüştürmek için Microsoft Excel'i kullanabilirsiniz. Bu özellik, *Veri Araçları* altındaki *Veri* sekmesinden kullanılabilir. Bir sütunun içeriğini birden fazla sütuna bölmek için, verinin, Microsoft Excel'in bir hücredeki içeriği birden çok hücreye bölmek için kullandığı gibi virgül (veya başka herhangi bir karakter) gibi belirli bir ayraç içermesi gerekmektedir. Aspose.Cells for Python via .NET ayrıca [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) methodunu kullanarak bu özelliği sağlar.

## **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Metni Sütunlara Dönüştürme**

Aşağıdaki örnek kod, [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) metodunun kullanımını açıklar. Kod öncelikle ilk çalışma sayfasının A sütununa bazı kişi adları ekler. İlk ve soyadı boşluk karakteriyle ayrılmıştır. Ardından A sütununa [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) metodu uygular ve çıktı excel dosyası olarak kaydeder. Eğer [çıktı excel dosyasını](25395213.xlsx) açarsanız, ilk isimlerin A sütununda ve soyadlarının B sütununda olduğunu göreceksiniz.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
