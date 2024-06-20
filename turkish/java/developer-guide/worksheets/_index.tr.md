---
title: Çalışsayfaları Yönet
linktitle: Çalışma Sayfaları
type: docs
weight: 60
url: /tr/java/manage-worksheets/
---

{{% alert color="primary" %}}

Geliştiriciler, Aspose.Cells'in esnek API'sını kullanarak Excel dosyalarında çalışma sayfaları oluşturabilir ve yönetebilirler. Bu konuda, Excel dosyalarına çalışma sayfaları eklemek ve kaldırmak için bazı yaklaşımları tartışacağız.

{{% /alert %}}

Aspose.Cells kullanarak çalışma sayfalarını yönetmek ABC kadar kolaydır. Bu bölümde şunları açıklayacağız:

1. Sıfırdan yeni bir Excel dosyası oluşturun ve içine bir çalışma sayfası ekleyin
1. Tasarımcı elektronik tablolara çalışma sayfaları ekleyin
1. Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme
1. Bir çalışma sayfasını sayfa adı kullanarak bir Excel dosyasından kaldırma
1. Sayfa Endeksini Kullanarak Bir Çalışma Sayfasını Bir Excel Dosyasından Kaldırma

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir yelpazede özellik ve yöntemler sağlar. Bu temel API'ların nasıl kullanılabileceğini görelim.

## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**

Programlama yoluyla yeni bir Excel dosyası oluşturmak için geliştiricilerin, Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı nesnesi oluşturmaları gerekir. Sonra geliştiriciler, [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) yöntemini [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) üzerinde çağırabilirler. [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) yöntemini çağırdığımızda, boş bir çalışma sayfası otomatik olarak Excel dosyasına eklenir, bu yeni eklenen çalışma sayfasının sayfa endeksini [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) yöntemine geçirerek referans alabiliriz. Çalışma sayfası referansı elde edildikten sonra, geliştiriciler gereksinimlerine göre çalışma sayfaları üzerinde çalışabilirler. Çalışma sayfaları üzerinde çalışma bittiğinde, geliştiriciler, yeni oluşturulan Excel dosyasını yeni çalışma sayfalarıyla birlikte [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfının [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemini çağırarak kaydedebilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**

Tasarımcı elektronik tabloya çalışma sayfaları eklemenin süreci yukarıdaki yaklaşımla tamamen aynıdır, yalnızca Excel dosyası zaten oluşturulmuş ve bir çalışma sayfası eklemek için önce bu Excel dosyasını açmamız gerekiyor. Bir tasarımcı elektronik tablosu, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını başlatırken dosya yolunu veya akışı geçirerek açılabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Sayfa Adını Kullanarak Çalışsayfalara Erişme**

Geliştiriciler, adını veya endeksini belirterek herhangi bir çalışma sayfasına erişebilir veya alabilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**

Bazen, geliştiriciler mevcut Excel dosyalarından çalışma sayfalarını kaldırmak isteyebilir ve bu görevi [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) koleksiyonunun [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) yöntemini çağırarak gerçekleştirebilirler. Bir belirli çalışma sayfasını kaldırmak için [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) yöntemine sayfa adını geçirebiliriz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**

Yukarıdaki çalışma sayfalarını kaldırma yaklaşımı, geliştiricilerin çalışma sayfalarının adlarını zaten bildikleri durumlar için iyi çalışır. Ancak, işte kaldırmak istediğiniz çalışma sayfasının adını bilmiyorsanız ne yapacaksınız?

İşte, böyle durumlarda, geliştiriciler, [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)) yönteminin adını kullanacağı çalışma sayfasının endeksini alarak bunun sayfa adı yerine çalışmasını sağlayan aşırı yüklenmiş bir sürümünü kullanabilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Gelişmiş Konular**
- [Sayfaları Etkinleştirme ve Çalışma Sayfasındaki Hücreyi Etkinleştirme](/cells/tr/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Çalışma Kitapları Arasında ve İçinde Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/java/copying-and-moving-worksheets/)
- [Çalışma Sayfasındaki Hücre Sayısını Sayma](/cells/tr/java/count-number-of-cells-in-the-worksheet/)
- [Boş Çalışma Sayfalarını Algılama](/cells/tr/java/detecting-empty-worksheets/)
- [Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma](/cells/tr/java/find-if-the-worksheet-is-dialog-sheet/)
- [Çalışma sayfası benzersiz kimliğini alın](/cells/tr/java/get-worksheet-unique-id/)
- [Excel'e Arka Plan Resmi Ekleme](/cells/tr/java/insert-background-image-to-excel/)
- [Çalışma Sayfalarından Senaryo Oluşturma, Hareketlendirme veya Kaldırma](/cells/tr/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Sayfa Sonlarını Yönetme](/cells/tr/java/managing-page-breaks/)
- [Sayfa Ayarı Özellikleri](/cells/tr/java/page-setup-features/)
- [Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle](/cells/tr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Aspose.Cells üzerinde Sheet.SheetId özelliğini kullanarak OpenXml'in faydalanılması](/cells/tr/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [ODS Dosyalarında Arkaplanla Çalışma](/cells/tr/java/working-with-background-in-ods-files/)
- [Çalışma Sayfası Görünümleri](/cells/tr/java/worksheet-views/)
