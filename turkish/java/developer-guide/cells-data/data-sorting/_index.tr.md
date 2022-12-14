---
title: Veri Sıralama
type: docs
weight: 90
url: /tr/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok kullanışlı özelliğinden biridir. Kullanıcıların taramayı kolaylaştırmak için verileri sıralamasına olanak tanır.

Aspose.Cells, çalışma sayfası verilerini alfabetik veya sayısal olarak sıralamanızı sağlar. Microsoft Excel'in verileri sıralamak için yaptığı gibi çalışır.

{{% /alert %}}

## **Microsoft Excel'de Verileri Sıralama**

Microsoft Excel'de verileri sıralamak için:

1.  Seçme**Veri** dan**Çeşit** Menü.
 Sırala iletişim kutusu görüntülenir.
1. Bir sıralama seçeneği belirleyin.

Genel olarak sıralama, verilerin sütunlarda görüntülendiği bitişik bir veri grubu olarak tanımlanan bir liste üzerinde gerçekleştirilir.

**Microsoft Excel'deki Sırala iletişim kutusu**

![yapılacaklar:resim_alternatif_Metin](data-sorting_1.png)

## **Aspose.Cells ile Verileri Sıralama**

 Aspose.Cells şunları sağlar:[**Veri Sıralayıcı**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) verileri artan veya azalan düzende sıralamak için kullanılan sınıf. Sınıfın bazı önemli üyeleri vardır, örneğin, aşağıdakiler gibi yöntemler:[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) ve[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Bu üyeler, sıralanmış anahtarları tanımlamak ve anahtar sıralama düzenini belirtmek için kullanılır.

 Veri sıralamayı uygulamadan önce anahtarları tanımlamanız ve sıralama düzenini ayarlamanız gerekir. sınıf sağlar[**çeşit**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) bir çalışma sayfasındaki hücre verilerine göre veri sıralama yapmak için kullanılan yöntem.

 bu[**çeşit**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) yöntemi aşağıdaki parametreleri kabul eder:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), çalışma sayfasının hücreleri.
- [**hücre alanı**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), hücre aralığı. Veri sıralamayı uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Aspose.Cells API kullanılarak verilerin nasıl sıralanacağını gösterir. Örnek, "Book1.xls" şablon dosyasını kullanır ve ilk çalışma sayfasındaki veri aralığı (A1:B14) için verileri sıralar:

Bu örnek, Microsoft Excel'de oluşturulan "Book1.xls" şablon dosyasını kullanır.

**Verilerle birlikte şablon Excel dosyası**

![yapılacaklar:resim_alternatif_Metin](data-sorting_2.png)

Aşağıdaki kodu çalıştırdıktan sonra, çıktı Excel dosyasından da görebileceğiniz gibi veriler uygun şekilde sıralanır.

**Verileri sıraladıktan sonra çıktı Excel dosyası**

![yapılacaklar:resim_alternatif_Metin](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Sıralamak*Soldan sağa* , kullan[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) bağlanmak.

{{% /alert %}}

## **Verileri arka plan rengiyle sıralama**

 Excel, verileri arka plan rengine göre sıralama özelliği sağlar. Aynı özellik Aspose.Cells kullanılarak sağlanır.[**Veri Sıralayıcı**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) nerede[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) kullanılabilir[**anahtar ekle()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) arka plan rengine göre verileri sıralamak için. Belirtilen rengi içeren tüm hücreler[**anahtar ekle()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), işlev Sıralama Düzeni ayarına göre üste veya alta yerleştirilir ve geri kalan hücrelerin sırası hiç değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıdadır:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **ileri konular**
- [Özel Sıralama Listesi ile Verileri Sütunda Sırala](/cells/tr/java/sort-data-in-column-with-custom-sort-list/)
- [Verileri Sıralarken Sıralama Uyarısı Belirtme](/cells/tr/java/specifying-sort-warning-while-sorting-data/)

