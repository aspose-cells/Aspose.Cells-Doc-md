---
title: Çalışma Sayfalarını Yönet
linktitle: çalışma sayfaları
type: docs
weight: 60
url: /tr/java/manage-worksheets/
---
{{% alert color="primary" %}}

Geliştiriciler, esnek API veya Aspose.Cells'i kullanarak programlı olarak Excel dosyalarında çalışma sayfalarını kolayca oluşturabilir ve yönetebilir. Bu konuda, Excel dosyalarına çalışma sayfası eklemek ve kaldırmak için bazı yaklaşımları tartışacağız.

{{% /alert %}}

Aspose.Cells'i kullanarak çalışma sayfalarını yönetmek ABC kadar kolaydır. Bu bölümde, şunları nasıl yapabileceğimizi açıklayacağız:

1. Sıfırdan yeni bir Excel dosyası oluşturun ve ona bir çalışma sayfası ekleyin
1. Tasarımcı elektronik tablolarına çalışma sayfaları ekleyin
1. Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme
1. Sayfa adını kullanarak bir çalışma sayfasını bir Excel dosyasından kaldırın
1. Sayfa dizinini kullanarak bir çalışma sayfasını bir Excel dosyasından kaldırın

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Bu bir Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bu temel API kümesinden nasıl yararlanabileceğimizi görelim.

## **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**

 Programlı olarak yeni bir Excel dosyası oluşturmak için geliştiricilerin bir nesne oluşturması gerekir.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bir Excel dosyasını temsil eden sınıf. Ardından geliştiriciler arayabilir[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) yöntemi[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . aradığımızda[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) yönteminde, Excel dosyasına otomatik olarak boş bir çalışma sayfası eklenir ve buna yeni eklenen çalışma sayfasının sayfa dizini Excel'e iletilerek başvurulabilir.[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Çalışma sayfası referansı alındıktan sonra, geliştiriciler kendi gereksinimlerine göre çalışma sayfaları üzerinde çalışabilirler. Çalışma sayfalarında iş bittikten sonra, geliştiriciler yeni oluşturulan Excel dosyalarını yeni çalışma sayfalarıyla kaydedebilir.[**kayıt etmek**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Tasarımcı Elektronik Tablosuna Çalışma Sayfaları Ekleme**

Bir tasarımcı elektronik tablosuna çalışma sayfaları ekleme işlemi, Excel dosyasının zaten oluşturulmuş olması ve bir çalışma sayfası eklemeden önce bu Excel dosyasını açmamız gerekmesi dışında, yukarıdaki yaklaşımla tamamen aynıdır. Başlatılırken dosya yolu veya akışı geçirilerek bir tasarımcı elektronik tablosu açılabilir.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme**

Geliştiriciler, adını veya dizinini belirterek herhangi bir çalışma sayfasına erişebilir veya alabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**

 Bazen, geliştiricilerin mevcut Excel dosyalarından çalışma sayfalarını kaldırmaları gerekebilir ve bu görev çağrılarak gerçekleştirilebilir.[**kaldırAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) yöntemi[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Toplamak. Sayfa adını şuraya geçirebiliriz:[**kaldırAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) belirli bir çalışma sayfasını kaldırma yöntemi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**

Geliştiriciler silinecek çalışma sayfalarının sayfa adlarını zaten biliyorsa, yukarıdaki çalışma sayfalarını kaldırma yaklaşımı işe yarar. Ancak, Excel dosyanızdan kaldırmak istediğiniz çalışma sayfasının sayfa adını bilmiyorsanız ne olur?

 Eh, bu gibi durumlarda, geliştiriciler aşırı yüklenmiş bir sürümünü kullanabilirler.[**kaldırAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)çalışma sayfasının sayfa adı yerine sayfa dizinini alan yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **ileri konular**
- [Sayfaları Etkinleştirme ve Çalışma Sayfasında Cell'i Etkinleştirme](/cells/tr/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Çalışma Sayfalarını Çalışma Kitapları İçinde ve Çalışma Kitapları Arasında Kopyalama ve Taşıma](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/java/copying-and-moving-worksheets/)
- [Çalışma Sayfasındaki hücre sayısını sayın](/cells/tr/java/count-number-of-cells-in-the-worksheet/)
- [Boş Çalışma Sayfalarını Algılama](/cells/tr/java/detecting-empty-worksheets/)
- [Çalışma Sayfasının İletişim Sayfası olup olmadığını bulun](/cells/tr/java/find-if-the-worksheet-is-dialog-sheet/)
- [Çalışma sayfası benzersiz kimliğini al](/cells/tr/java/get-worksheet-unique-id/)
- [Arka Plan Resmini Excel'e Ekle](/cells/tr/java/insert-background-image-to-excel/)
- [Çalışma Sayfalarından Senaryolar Oluşturun, Yönetin veya Kaldırın](/cells/tr/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Sayfa Sonlarını Yönetme](/cells/tr/java/managing-page-breaks/)
- [Sayfa Düzeni Özellikleri](/cells/tr/java/page-setup-features/)
- [Bir çalışma sayfasındaki boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelleyin](/cells/tr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Aspose.Cells kullanarak OpenXml'nin Sheet.SheetId özelliğini kullanın](/cells/tr/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [ODS Dosyalarında Arka Planla Çalışma](/cells/tr/java/working-with-background-in-ods-files/)
- [Çalışma Sayfası Görünümleri](/cells/tr/java/worksheet-views/)
