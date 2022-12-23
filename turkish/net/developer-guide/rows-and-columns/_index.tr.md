---
title: Satırları ve Sütunları Biçimlendir
linktitle: Satırlar ve Sütunlar
type: docs
weight: 100
url: /tr/net/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}}

Elektronik tablolarla çalışırken ve satırlara veya sütunlara veri eklerken, satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen, satırlara veya sütunlara biçimlendirme uygulamak, verileri göstermek için geçerli yükseklik veya genişliğin değişmesi gerektiği anlamına gelir. Normalde, kullanıcılar bir WYSIWYG ortamında Microsoft Excel kullanarak satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak, Aspose.Cells ile geliştiriciler bu işlemleri çalışma zamanında gerçekleştirebilir.

{{% /alert %}}

## **Satırlarla Çalışmak**

### **Satır Yüksekliğini Ayarlama**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmaktadır.

### **Bir Satırın Yüksekliğini Ayarlama**

 çağırarak tek bir satırın yüksekliğini ayarlamak mümkündür.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonun[**Satır Yüksekliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) yöntem. bu[**Satır Yüksekliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)method aşağıdaki gibi parametreleri alır:

- **Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanacak satır yüksekliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**

 Geliştiricilerin çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamaları gerekirse, bunu[**Standart Yükseklik**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) mülkiyeti[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak.

**Örnek vermek:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Sütunlarla Çalışmak**

### **Bir Sütunun Genişliğini Ayarlama**

 öğesini çağırarak bir sütunun genişliğini ayarlayın.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonun[**Sütun Genişliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) yöntem. bu[**Sütun Genişliğini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)yöntem aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Sütun Genişliğini Piksel Olarak Ayarlama**

öğesini çağırarak bir sütunun genişliğini ayarlayın.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyonun[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)yöntem. bu[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)yöntem aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**piksel cinsinden istenen sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**

 Çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak üzere[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonun[**Standart Genişlik**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **ileri konular**
- [Satırları ve Sütunları Otomatik Sığdır](/cells/tr/net/autofit-rows-and-columns/)
- [Aspose.Cells'i kullanarak Metni Sütunlara Dönüştür](/cells/tr/net/convert-text-to-columns-using-aspose-cells/)
- [Satırları ve Sütunları Kopyalama](/cells/tr/net/copying-rows-and-columns/)
- [Çalışma Sayfasındaki Boş Satırları ve Sütunları Silme](/cells/tr/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Satırları ve Sütunları Gruplandırma ve Grubu Çözme](/cells/tr/net/grouping-and-ungrouping-rows-and-columns/)
- [Satırları ve Sütunları Gizleme ve Gösterme](/cells/tr/net/hiding-and-showing-rows-and-columns/)
- [Excel Çalışma Sayfasına Satır Ekleme veya Silme](/cells/tr/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excel dosyasına Satır ve Sütun Ekleme ve Silme](/cells/tr/net/inserting-and-deleting-rows-and-columns/)
- [Çalışma Sayfasındaki yinelenen satırları kaldırın](/cells/tr/net/remove-duplicate-rows-in-a-worksheet/)
- [Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin](/cells/tr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
