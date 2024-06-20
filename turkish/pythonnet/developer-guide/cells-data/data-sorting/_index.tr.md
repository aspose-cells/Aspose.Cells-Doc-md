---
title: Veri Sıralama
type: docs
weight: 130
url: /tr/python-net/sort-data-of-excel/
description: Aspose.Cells için Python via .NET API sını kullanarak veriyi sıralamanın nasıl yapıldığını öğrenin.
keywords: Python Excel Kütüphanesi, Python Verileri artan veya azalan sıralama, Python Arkaplan rengine göre verileri sıralama.
---

{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'ın birçok kullanışlı özelliklerinden biridir. Kullanıcılara verileri tararken daha kolay hale getirmek için verileri düzenleme imkanı sunar. Aspose.Cells for Python via .NET, geliştiricilere çalışma sayfası verilerini alfabetik veya sayısal olarak sıralama imkanı tanır, bu da verileri sıralama konusunda Microsoft Excel'in yaptığı gibi çalışır.

{{% /alert %}}

## **Microsoft Excel'de Veri Sıralama**

Microsoft Excel'de veri sıralamak için:

1. **Veri**'yi **Sırala** menüsünden seçin. Sırala iletişim kutusu görüntülenecektir.
1. Sıralama seçeneğini seçin.

Genellikle, sıralama bir liste üzerinde yapılır - verilerin sütunlarda gösterildiği, verilerin bağlantılı bir grup olduğu.

## **Python Excel Kütüphanesi ile Veri Sıralama**

Python via .NET için Aspose.Cells, artan veya azalan sırada veri sıralamak için kullanılan [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) sınıfını sağlar. Sınıfın bazı önemli üyeleri bulunmaktadır, örneğin Key1 ... Key3 ve Order1 ... Order3 gibi özellikler. Bu üyeler, sıralı anahtarları tanımlamak ve anahtar sıralama düzenini belirtmek için kullanılır.

Veri sıralaması gerçekleştirmeden önce anahtarları tanımlamalı ve sıralama düzenini belirlemelisiniz. Sınıf, çalışsayadaki hücre verilerine dayalı veri sıralamasını gerçekleştirmek için kullanılan [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) yöntemini sağlar.

[**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) yöntemi aşağıdaki parametreleri kabul eder:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), altındaki çalışsayadaki hücreler.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), hücre aralığı. Veri sıralaması uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulmuş "Book1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra, veri uygun bir şekilde sıralanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

*Soldan Sağa* sıralamak istiyorsanız, [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/) özniteliğini kullanın.

{{% /alert %}}

### **Aspose.Cells için Python Excel Kütüphanesi Kullanarak Arkaplan Rengi Kullanarak Veri Sıralama**

Excel, verileri arka plan rengine göre sıralama imkanı sağlar. Aynı özellik, Aspose.Cells için Python via .NET kullanılarak [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/) tarafından sağlanır. CellColor, verinin arka plan rengine göre sıralanması için [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) içinde kullanılabilir. Belirli bir rengi içeren tüm hücreler, SortOrder ayarına ve geri kalan hücrelerin sırasına göre en üste veya en alta yerleştirilir ve geri kalan hücrelerin sırası hiç değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Gelişmiş Konular**
- [Özel Sıralama Listesi ile Sütunda Verileri Sıralama](/cells/tr/python-net/sort-data-in-column-with-custom-sort-list/)
- [Veri Sıralama Sırasında Uyarıyı Belirtme](/cells/tr/python-net/specifying-sort-warning-while-sorting-data/)
