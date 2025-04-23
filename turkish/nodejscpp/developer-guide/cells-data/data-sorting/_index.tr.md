---
title: Veri Sıralama
type: docs
weight: 130
url: /tr/nodejs-cpp/sort-data-of-excel/
description: Aspose.Cells for Node.js via C++ API sini kullanarak veriyi sıralamayı öğrenin.
keywords: Verileri artan veya azalan sırada, arka plan rengine göre sıralama
---

{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in pekçok kullanışlı özelliklerinden biridir. Kullanıcıların veriyi daha kolay taraması için düzenler. Aspose.Cells for Node.js via C++, geliştiricilere, Excel'in yaptığı gibi, alfabetik veya sayısal olarak çalışma sayfası verilerini sıralama imkanı sağlar.

{{% /alert %}}

## **Microsoft Excel'de Veri Sıralama**

Microsoft Excel'de veri sıralamak için:

1. **Veri**'yi **Sırala** menüsünden seçin. Sırala iletişim kutusu görüntülenecektir.
1. Sıralama seçeneğini seçin.

Genellikle, sıralama bir liste üzerinde yapılır - verilerin sütunlarda gösterildiği, verilerin bağlantılı bir grup olduğu.

## **Aspose.Cells ile Veri Sıralama**

Aspose.Cells for Node.js via C++, sıralama yapmak için [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) sınıfını sağlar. Bu sınıf, Key1 ... Key3 ve Order1 ... Order3 gibi önemli üyeler içerir. Bu üyeler, sıralanacak anahtarları tanımlamak ve anahtar sıralama düzenini belirtmek için kullanılır.

Veri sıralaması gerçekleştirmeden önce anahtarları tanımlamalı ve sıralama düzenini belirlemelisiniz. Sınıf, çalışsayadaki hücre verilerine dayalı veri sıralamasını gerçekleştirmek için kullanılan [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) yöntemini sağlar.

[**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) yöntemi aşağıdaki parametreleri kabul eder:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), altındaki çalışsayadaki hücreler.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), hücre aralığı. Veri sıralaması uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulmuş "Book1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra, veri uygun bir şekilde sıralanır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

*Soldan Sağa* sıralamak istiyorsanız, [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-) özniteliğini kullanın.

{{% /alert %}}

### **Arka plan rengine göre veri sıralama**

Excel, arka plan rengine göre veri sıralama özellikleri sağlar. Aynı özellik, Aspose.Cells for Node.js via C++'ü DataSorter kullanarak sağlar, burada [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor kullanılarak [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) içinde veriler sıralanabilir. Belirtilen renkteki tüm hücreler, SortOrder ayarına göre en üstte veya en altta yerleştirilir ve diğer hücrelerin sırası değiştirilmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Gelişmiş Konular**
- [Özel Sıralama Listesi ile Sütunda Verileri Sıralama](/cells/tr/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Veri Sıralama Sırasında Uyarıyı Belirtme](/cells/tr/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

