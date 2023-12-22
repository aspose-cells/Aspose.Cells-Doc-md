---
title: Veri Sıralama
type: docs
weight: 130
url: /tr/net/sort-data-of-excel/
description: Aspose.Cells for .NET API numaralı telefonu kullanarak verileri nasıl sıralayacağınızı öğrenin.
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok yararlı özelliğinden biridir. Kullanıcıların taramayı kolaylaştırmak için verileri sipariş etmelerine olanak tanır. Aspose.Cells, geliştiricilerin çalışma sayfası verilerini alfabetik veya sayısal olarak sıralamasına olanak tanır; bu, Excel'in verileri sıralamak için yaptığı Microsoft ile aynı şekilde çalışır.

{{% /alert %}}

##  **Microsoft Excel'de Verileri Sıralama**

Microsoft Excel'deki verileri sıralamak için:

1.  Seçme**Veri** itibaren**Düzenlemek** Menü. Sırala iletişim kutusu görüntülenecektir.
1. Bir sıralama seçeneği seçin.

Genellikle sıralama, verilerin sütunlar halinde görüntülendiği bitişik bir veri grubu olarak tanımlanan bir listede gerçekleştirilir.

##  **Aspose.Cells ile Verileri Sıralama**

 Aspose.Cells şunları sağlar[**Veri Sıralayıcı**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)Verileri artan veya azalan düzende sıralamak için kullanılan sınıf. Sınıfın bazı önemli üyeleri vardır; örneğin Key1 ... Key3 ve Order1 ... Order3 gibi özellikler. Bu üyeler sıralanmış anahtarları tanımlamak ve anahtar sıralama düzenini belirtmek için kullanılır.

 Veri sıralamayı uygulamadan önce anahtarları tanımlamanız ve sıralama düzenini ayarlamanız gerekir. Sınıf şunları sağlar:[**Düzenlemek**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)Bir çalışma sayfasındaki hücre verilerine göre veri sıralaması yapmak için kullanılan yöntem.

[**Düzenlemek**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)yöntem aşağıdaki parametreleri kabul eder:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), temel çalışma sayfasının hücreleri.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), hücre aralığı. Veri sıralamayı uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulan "Kitap1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra veriler uygun şekilde sıralanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 *Soldan Sağa* sıralamak istiyorsanız,[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) bağlanmak.

{{% /alert %}}

###  **Verileri arka plan rengine göre sıralama**

Excel, verileri arka plan rengine göre sıralamak için özellikler sağlar. Aynı özellik, DataSorter kullanılarak Aspose.Cells kullanılarak sağlanır;[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor kullanılabilir[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) verileri arka plan rengine göre sıralamak için. Belirtilen rengi içeren tüm hücreler[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), fonksiyon SortOrder ayarına göre üste veya aşağıya yerleştirilir ve geri kalan hücrelerin sırası hiçbir şekilde değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda verilmiştir:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[çıktıörneğiBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **İleri konular**
- [Özel Sıralama Listesiyle Sütundaki Verileri Sıralama](/cells/tr/net/sort-data-in-column-with-custom-sort-list/)
- [Verileri Sıralarken Sıralama Uyarısını Belirtme](/cells/tr/net/specifying-sort-warning-while-sorting-data/)
