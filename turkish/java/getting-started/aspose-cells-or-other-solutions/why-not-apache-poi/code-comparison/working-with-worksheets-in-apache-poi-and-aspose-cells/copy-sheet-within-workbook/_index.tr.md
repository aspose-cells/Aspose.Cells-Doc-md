---
title: Çalışma Kitabı İçindeki Sayfayı Kopyala
type: docs
weight: 40
url: /tr/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Çalışma Kitabı İçinde Sayfa Taşıma veya Kopyalama**
Çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşıma adımları aşağıdaki gibidir.

1. Çalışma kitaplarının içinde veya arasında sayfaları taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. Alınacak kitap kutusunda, sayfaları alacak olan çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için, **yeni kitap**'ı tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için, **Bir kopya oluştur** onay kutusunu seçin.
## **Aspose.Cells - Çalışma Kitabı İçinde Sayfa Kopyalama**
{{% alert color="primary" %}} 

Aspose.Cells, mevcut bir çalışma sayfasından veri kopyalamak için kullanılan bir yöntem olan WorksheetCollection.addCopy() metodunu sağlar. Yöntemin bir versiyonu, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer versiyon, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{% /alert %}} 

Aspose.Cells kullanarak sayfaları kopyalama

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Çalışma Kitabı İçinde Sayfa Kopyalama**
{{% alert color="primary" %}} 

Workbook.cloneSheet(), çalışma kitabı ile sayfaları kopyalamak için kullanılır.

{{% /alert %}} 

Apache POI SS kullanarak sayfaları kopyalama

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

Daha fazla detay için [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/java/calisma-sayfalarini-kopyalama-ve-tasima) sayfasını ziyaret edin.

{{% /alert %}}
