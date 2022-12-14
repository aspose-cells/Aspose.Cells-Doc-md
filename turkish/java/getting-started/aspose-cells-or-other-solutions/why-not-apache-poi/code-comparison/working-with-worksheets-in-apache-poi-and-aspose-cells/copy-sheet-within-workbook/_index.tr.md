---
title: Çalışma Kitabı İçinde Sayfayı Kopyala
type: docs
weight: 40
url: /tr/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - Çalışma Kitabında Sayfaları Taşıma veya Kopyalama**
Çalışma sayfalarını çalışma kitaplarının içinde veya arasında kopyalamak ve taşımak için gereken adımlar aşağıdadır.

1. Çalışma kitaplarının içinde veya arasında sayfaları taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1.  Üzerinde**Düzenlemek** menü, tıklayın**Sayfayı Taşı veya Kopyala**.
1. Kitaba kutusunda, sayfaları almak için çalışma kitabına tıklayın.
1.  Seçilen sayfaları yeni bir çalışma kitabına taşımak veya kopyalamak için**yeni kitap**.
1.  İçinde**sayfadan önce** kutusunda, taşınan veya kopyalanan sayfaları eklemek istediğiniz sayfayı tıklayın.
1.  Sayfaları taşımak yerine kopyalamak için**Bir kopya oluştur** onay kutusu.
## **Aspose.Cells - Çalışma Kitabı İçinde Sayfayı Kopyala**
{{% alert color="primary" %}} 

Aspose.Cells, koleksiyona bir çalışma sayfası eklemek ve mevcut bir çalışma sayfasından veri kopyalamak için kullanılan aşırı yüklenmiş bir yöntem olan WorksheetCollection.addCopy() sağlar. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde varolan bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{% /alert %}} 

Aspose.Cells kullanarak sayfaları kopyalayın

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Çalışma Kitabında Sayfayı Kopyala**
{{% alert color="primary" %}} 

Workbook.cloneSheet(), çalışma kitabıyla sayfaları kopyalamak için kullanılır.

{{% /alert %}} 

Apache POI SS kullanarak sayfaları kopyalayın

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/java/copying-and-moving-worksheets).

{{% /alert %}}
