---
title: Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme
type: docs
weight: 30
url: /tr/net/convert-text-to-columns-using-aspose-cells/
---

## **Olası Kullanım Senaryoları**

Metni Sütunlara Çevirebilirsiniz Microsoft Excel kullanarak metni sütunlara çevirebilirsiniz. Bu özellik, *Data* sekmesi altındaki *Data Tools* menüsünden erişilebilir. Bir sütunun içeriğini birden fazla sütuna ayırmak için, verinin Microsoft Excel'in hücre içeriğini birden fazla hücreye ayırdığı belirli bir ayırıcı içermesi gerekmektedir. Aspose.Cells, bu özelliği [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metodu aracılığıyla sağlar.

## **Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme**

Aşağıdaki örnek kod, [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metodunun kullanımını açıklar. Kod öncelikle ilk çalışma sayfasının A sütununa bazı kişi adları ekler. İlk ve soyadı boşluk karakteriyle ayrılmıştır. Ardından A sütununa [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metodu uygular ve çıktı excel dosyası olarak kaydeder. Eğer [çıktı excel dosyasını](25395213.xlsx) açarsanız, ilk isimlerin A sütununda ve soyadlarının B sütununda olduğunu göreceksiniz.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
