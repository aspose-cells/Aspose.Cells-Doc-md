---
title: Veri Sıralama
type: docs
weight: 130
url: /tr/net/sort-data-of-excel/
description: Aspose.Cells for .NET API sını kullanarak verileri nasıl sıralayacağınızı öğrenin.
keywords: Verileri artan veya azalan sırada, arka plan rengine göre sıralama
---

{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok kullanışlı özelliklerinden biridir. Kullanıcılara verileri taramayı kolaylaştırmak için sıralama imkanı sağlar. Aspose.Cells, geliştiricilere çalışma sayfası verilerini alfabetik veya sayısal olarak sıralama imkanı sunar, bu da Microsoft Excel'in verileri nasıl sıraladığına benzer şekilde çalışır.

{{% /alert %}}

## **Microsoft Excel'de Veri Sıralama**

Microsoft Excel'de veri sıralamak için:

1. **Veri**'yi **Sırala** menüsünden seçin. Sırala iletişim kutusu görüntülenecektir.
1. Sıralama seçeneğini seçin.

Genellikle, sıralama bir liste üzerinde yapılır - verilerin sütunlarda gösterildiği, verilerin bağlantılı bir grup olduğu.

## **Aspose.Cells ile Veri Sıralama**

Aspose.Cells, verileri artan veya azalan sırada sıralamak için kullanılan [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter) sınıfını sağlar. Sınıf, örneğin Key1 ... Key3 ve Order1 ... Order3 gibi önemli üyelere sahiptir. Bu üyeler sıralı anahtarları tanımlamak ve anahtar sıralama sırasını belirlemek için kullanılır.

Veri sıralaması gerçekleştirmeden önce anahtarları tanımlamalı ve sıralama düzenini belirlemelisiniz. Sınıf, çalışsayadaki hücre verilerine dayalı veri sıralamasını gerçekleştirmek için kullanılan [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index) yöntemini sağlar.

[**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) yöntemi aşağıdaki parametreleri kabul eder:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), altındaki çalışsayadaki hücreler.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), hücre aralığı. Veri sıralaması uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulmuş "Book1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra, veri uygun bir şekilde sıralanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

*Soldan Sağa* sıralamak istiyorsanız, [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) özniteliğini kullanın.

{{% /alert %}}

### **Arka plan rengine göre veri sıralama**

Excel, arka plan rengine göre verileri sıralama özelliği sunar. Aynı özellik, Aspose.Cells kullanılarak DataSorter kullanılarak sağlanır, burada [**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor, arka plan rengine göre verilere sıralama yapmak için [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) içinde kullanılabilir. Belirtilen renkteki tüm hücreler, [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), işlevinde belirtilen sırada yerleştirilir ve geri kalan hücrelerin sırası hiç değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Gelişmiş Konular**
- [Özel Sıralama Listesi ile Sütunda Verileri Sıralama](/cells/tr/net/sort-data-in-column-with-custom-sort-list/)
- [Veri Sıralama Sırasında Uyarıyı Belirtme](/cells/tr/net/specifying-sort-warning-while-sorting-data/)
