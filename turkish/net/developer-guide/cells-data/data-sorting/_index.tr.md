---
title: Veri Sıralama
type: docs
weight: 130
url: /tr/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok kullanışlı özelliğinden biridir. Kullanıcıların taramayı kolaylaştırmak için verileri sıralamasına olanak tanır. Aspose.Cells, geliştiricilerin çalışma sayfası verilerini alfabetik veya sayısal olarak sıralamasına olanak tanır; bu, Excel'in verileri sıralamak için Microsoft ile aynı şekilde çalışır.

{{% /alert %}}

## **Microsoft Excel'de Verileri Sıralama**

Microsoft Excel'de verileri sıralamak için:

1.  Seçme**Veri** dan**Çeşit** Menü. Sırala iletişim kutusu görüntülenecektir.
1. Bir sıralama seçeneği belirleyin.

Genel olarak sıralama, verilerin sütunlarda görüntülendiği bitişik bir veri grubu olarak tanımlanan bir liste üzerinde gerçekleştirilir.

## **Aspose.Cells ile Verileri Sıralama**

 Aspose.Cells şunları sağlar:[**Veri Sıralayıcı**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)verileri artan veya azalan düzende sıralamak için kullanılan sınıf. Sınıfın bazı önemli üyeleri vardır, örneğin Key1 ... Key3 ve Order1 ... Order3 gibi özellikler. Bu üyeler, sıralanmış anahtarları tanımlamak ve anahtar sıralama düzenini belirtmek için kullanılır.

 Veri sıralamayı uygulamadan önce anahtarları tanımlamanız ve sıralama düzenini ayarlamanız gerekir. sınıf sağlar[**Çeşit**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)çalışma sayfasındaki hücre verilerine dayalı olarak veri sıralama gerçekleştirmek için kullanılan yöntem.

 bu[**Çeşit**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)yöntem aşağıdaki parametreleri kabul eder:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), temel alınan çalışma sayfasının hücreleri.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), hücre aralığı. Veri sıralamayı uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulan "Book1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra, veriler uygun şekilde sıralanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 sıralamak istersen*Soldan sağa* , kullan[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) bağlanmak.

{{% /alert %}}

### **Verileri arka plan rengiyle sıralama**

 Excel, verileri arka plan rengine göre sıralamak için özellikler sağlar. Aynı özellik, DataSorter kullanılarak Aspose.Cells kullanılarak sağlanır; burada[**Türe Göre Sırala**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor kullanılabilir[**Anahtar Ekle()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) verileri arka plan rengine göre sıralamak için. Belirtilen rengi içeren tüm hücreler[**Anahtar Ekle()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), işlev Sıralama Düzeni ayarına göre üste veya alta yerleştirilir ve geri kalan hücrelerin sırası hiç değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıdadır:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **ileri konular**
- [Özel Sıralama Listesi ile Verileri Sütunda Sırala](/cells/tr/net/sort-data-in-column-with-custom-sort-list/)
- [Verileri Sıralarken Sıralama Uyarısı Belirtme](/cells/tr/net/specifying-sort-warning-while-sorting-data/)
