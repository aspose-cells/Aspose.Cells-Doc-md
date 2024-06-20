---
title: Veri Sıralama
type: docs
weight: 90
url: /tr/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok kullanışlı özelliğinden biridir. Kullanıcılara verileri tararken kolaylaştırmak adına verileri düzenleme imkanı sağlar.

Aspose.Cells, çalışma sayfası verilerini alfabetik veya sayısal olarak sıralamanıza olanak tanır. Verileri sıralarken Microsoft Excel'in aynı şekilde çalışır.

{{% /alert %}}

## **Microsoft Excel'de Veri Sıralama**

Microsoft Excel'de veri sıralamak için:

1. **Sırala** menüsünden **Veri**'yi seçin.
   Sıralama ile genellikle bir liste üzerinde gerçekleştirilir - verilerin sütunlarda görüntülendiği bitişik bir veri grubu olarak tanımlandı.
1. Sıralama seçeneğini seçin.

Genellikle, sıralama bir liste üzerinde yapılır - verilerin sütunlarda gösterildiği, verilerin bağlantılı bir grup olduğu.

Microsoft Excel'de **Sırala** iletişim kutusu

![todo:image_alt_text](data-sorting_1.png)

## **Aspose.Cells ile Veri Sıralama**

Aspose.Cells, verileri artan veya azalan sırada sıralamak için kullanılan [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) sınıfını sağlar. Sınıf bazı önemli üyeler, örneğin [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) methodları gibi, [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) ve [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) gibi. Bu üyeler sıralı anahtarları tanımlamak ve anahtar sıralama sırasını belirtmek için kullanılır.

Veri sıralaması gerçekleştirmeden önce anahtarları tanımlamalı ve sıralama düzenini belirlemelisiniz. Sınıf, çalışsayadaki hücre verilerine dayalı veri sıralamasını gerçekleştirmek için kullanılan [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) yöntemini sağlar.

[**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) yöntemi aşağıdaki parametreleri kabul eder:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), çalışma sayfasının hücreleri.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), hücre aralığı. Veri sıralaması uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Aspose.Cells API'sını kullanarak veri sıralamayı nasıl gerçekleştireceğinizi gösterir. Örnek, ilk çalışma sayfasındaki (A1:B14) veri aralığı için "Book1.xls" örnek dosyasını kullanır:

Bu örnek, Microsoft Excel'de oluşturulan "Book1.xls" adlı şablon dosyasını kullanır.

**Veri ekranını içeren Excel şablonu tamamlandı**

![todo:image_alt_text](data-sorting_2.png)

Aşağıdaki kodu uyguladıktan sonra veriler uygun şekilde sıralanır ve çıktı Excel dosyasından görebilirsiniz.

**Veri sıralama sonrası çıktı Excel dosyası**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

Sıralamak için *Soldan Sağa* sıralama özelliğini kullanın.

{{% /alert %}}

## **Arka plan rengine göre veri sıralama**

Excel, arka plan rengine göre veri sıralamak için özellik sağlar. Aynı özellik Aspose.Cells kullanılarak [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) içerisinde [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) kullanılarak sağlanır ve tüm hücrelerde belirtilen renkte olan hücreler Sıralama Ayarı'na ve geri kalan hücrelerin sıralama sırasına göre altta veya üstte yer alır ve geri kalan hücrelerin sıralaması hiç değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Gelişmiş Konular**
- [Özel Sıralama Listesi ile Sütunda Verileri Sıralama](/cells/tr/java/sort-data-in-column-with-custom-sort-list/)
- [Veri Sıralama Sırasında Uyarıyı Belirtme](/cells/tr/java/specifying-sort-warning-while-sorting-data/)

