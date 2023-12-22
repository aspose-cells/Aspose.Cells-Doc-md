---
title: Satırları ve Sütunları Biçimlendirme
linktitle: Satırlar ve Sütunlar
type: docs
weight: 100
url: /tr/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET, satır yüksekliğini veya sütun genişliğini değiştirmenin yanı sıra satırlara veya sütunlara biçimlendirme uygulamayı destekleyebilir.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

Elektronik tablolarla çalışırken ve satırlara veya sütunlara veri eklerken satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara format uygulamak, verileri göstermek için geçerli yüksekliğin veya genişliğin değişmesi gerektiği anlamına gelir. Normalde kullanıcılar, Microsoft Excel'i kullanarak WYSIWYG ortamında satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak geliştiriciler Aspose.Cells ile bu işlemleri çalışma zamanında gerçekleştirebilirler.

{{% /alert %}}

##  **Satırlar ile Çalışmak**

###  **Satır Yüksekliği Nasıl Ayarlanır**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Bu, Excel dosyasındaki her çalışma sayfasına erişime izin verir. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmaktadır.

###  **Satırın Yüksekliği Nasıl Ayarlanır**

 Tek bir satırın yüksekliğini çağırarak ayarlamak mümkündür.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Koleksiyonun[**Satır Yüksekliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) yöntem.[**Satır Yüksekliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)yöntem aşağıdaki parametreleri aşağıdaki gibi alır:

- *Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- *Satır yüksekliği**, satıra uygulanacak satır yüksekliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**

 Geliştiricilerin çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlaması gerekiyorsa bunu şunu kullanarak yapabilirler:[**Standart Yükseklik**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) mülkiyeti[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak.

**Örnek:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **Sütunlarla Çalışmak**

###  **Sütun Genişliği Nasıl Ayarlanır**

 çağırarak bir sütunun genişliğini ayarlayın.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Koleksiyonun[**Sütun Genişliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) yöntem.[**Sütun Genişliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)yöntem aşağıdaki parametreleri alır:

- *Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- *Sütun genişliği**, istenen sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **Sütun Genişliğini Piksel Olarak Ayarlama**

çağırarak bir sütunun genişliğini ayarlayın.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Koleksiyonun[**Sütun Genişliğini AyarlaPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)yöntem.[**Sütun Genişliğini AyarlaPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)yöntem aşağıdaki parametreleri alır:

- *Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- *Sütun genişliği**, piksel cinsinden istenen sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliği Nasıl Ayarlanır**

 Çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak için[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Koleksiyonun[**Standart Genişlik**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **İleri konular**
- [Satırları ve Sütunları Otomatik Sığdır](/cells/tr/net/autofit-rows-and-columns/)
- [Aspose.Cells'i kullanarak Metni Sütunlara Dönüştür](/cells/tr/net/convert-text-to-columns-using-aspose-cells/)
- [Satırları ve Sütunları Kopyalama](/cells/tr/net/copying-rows-and-columns/)
- [Çalışma Sayfasındaki Boş Satırları ve Sütunları Silme](/cells/tr/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Satırları ve Sütunları Gruplama ve Grubu Çözme](/cells/tr/net/grouping-and-ungrouping-rows-and-columns/)
- [Satırları ve Sütunları Gizleme ve Gösterme](/cells/tr/net/hiding-and-showing-rows-and-columns/)
- [Excel Çalışma Sayfasına Satır Ekleme veya Silme](/cells/tr/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excel Dosyasının Satır ve Sütunlarını Ekleme ve Silme](/cells/tr/net/inserting-and-deleting-rows-and-columns/)
- [Çalışma Sayfasındaki yinelenen satırları kaldırma](/cells/tr/net/remove-duplicate-rows-in-a-worksheet/)
- [Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin](/cells/tr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
