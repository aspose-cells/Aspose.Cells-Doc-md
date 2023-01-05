---
title: Microsoft Excel dosyalarının Çalışma Sayfalarını yönetin.
linktitle: çalışma sayfaları
type: docs
weight: 90
url: /tr/net/manage-worksheets/
description: Aspose.Cells'i kullanarak çalışma sayfası ekleyin, çalışma sayfasını ve etkin Sayfayı kaldırın.
---
{{% alert color="primary" %}}

Geliştiriciler, Microsoft Excel dosyalarındaki çalışma sayfalarını programlı olarak Aspose.Cells' esnek API'i kullanarak kolayca oluşturabilir ve yönetebilir. Bu konu, Microsoft Excel dosyalarına çalışma sayfası ekleme ve kaldırma yaklaşımlarını açıklamaktadır.

{{% /alert %}}

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar.

## **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**

Programlı olarak yeni bir Excel dosyası oluşturmak için:

1.  Şunun bir nesnesini oluşturun:[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf.
1.  Ara[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) yöntemi[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) sınıf. Excel dosyasına otomatik olarak boş bir çalışma sayfası eklenir. Yeni çalışma sayfasının sayfa dizini şuraya geçirilerek başvurulabilir:[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Toplamak.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfaları üzerinde çalışma gerçekleştirin.
1.  Çağırarak yeni Excel dosyasını yeni çalışma sayfalarıyla kaydedin.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**Kayıt etmek**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Tasarımcı Elektronik Tablosuna Çalışma Sayfaları Ekleme**

 Bir tasarımcı elektronik tablosuna çalışma sayfası ekleme işlemi, Excel dosyasının zaten mevcut olması ve çalışma sayfaları eklenmeden önce açılması gerektiği dışında, yeni bir çalışma sayfası ekleme işlemiyle aynıdır. Bir tasarımcı e-tablosu şu şekilde açılabilir:[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme**

Adını veya dizinini belirterek herhangi bir çalışma sayfasına erişin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**

Çalışma sayfalarını bir dosyadan kaldırmak için,[**KaldırAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) yöntemi[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) sınıf. Sayfa adını şuraya iletin:[**KaldırAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)belirli bir çalışma sayfasını kaldırma yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**

 Çalışma sayfalarını ada göre kaldırmak, çalışma sayfasının adı bilindiğinde işe yarar. Çalışma sayfasının adını bilmiyorsanız, aşırı yüklenmiş bir sürümünü kullanın.[**KaldırAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)çalışma sayfasının sayfa adı yerine sayfa dizinini alan yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Sayfaları Etkinleştirme ve Çalışma Sayfasında Cell Etkinleştirme**

Bazen, bir kullanıcı bir Microsoft Excel dosyasını Excel'de açtığında belirli bir çalışma sayfasının etkin olması ve görüntülenmesi gerekir. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırma çubuklarını etkin hücreyi gösterecek şekilde ayarlamak isteyebilirsiniz.
Aspose.Cells tüm bu görevleri yapabilecek kapasitededir.

 Bir**etkin sayfa** üzerinde çalıştığınız bir sayfadır: sekmedeki etkin sayfanın adı varsayılan olarak kalındır.

 Bir**aktif hücre** seçili bir hücredir, yazmaya başladığınızda verilerin girildiği hücredir. Aynı anda yalnızca bir hücre etkindir. Etkin hücre kalın bir kenarlıkla vurgulanır.

### **Sayfaları Etkinleştirme ve Cell Etkinleştirme**

Aspose.Cells, bir sayfa ve hücreyi etkinleştirmek için özel API çağrıları sağlar. Örneğin,[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)özelliği, bir çalışma kitabındaki etkin sayfayı ayarlamak için kullanışlıdır.
Benzer şekilde,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)özelliği, çalışma sayfasında etkin bir hücre ayarlamak ve almak için kullanılır.

Yatay veya dikey kaydırma çubuklarının, belirli verileri göstermek istediğiniz satır ve sütun dizini konumunda olduğundan emin olmak için,[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) ve[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)özellikler.

Aşağıdaki örnek, bir çalışma sayfasının nasıl etkinleştirileceğini ve içinde etkin bir hücrenin nasıl oluşturulacağını gösterir. Oluşturulan çıktıda, kaydırma çubukları kaydırılarak 2. sıra ve 2. sütun ilk görünür satır ve sütunları olur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **ileri konular**
- [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/net/copying-and-moving-worksheets/)
- [Çalışma Sayfasındaki hücre sayısını sayın](/cells/tr/net/count-number-of-cells-in-the-worksheet/)
- [Boş Çalışma Sayfalarını Algılama](/cells/tr/net/detecting-empty-worksheets/)
- [Çalışma Sayfasının İletişim Sayfası olup olmadığını bulun](/cells/tr/net/find-if-the-worksheet-is-dialog-sheet/)
- [Çalışma sayfası benzersiz kimliğini al](/cells/tr/net/get-worksheet-unique-id/)
- [Çalışma Sayfalarından Senaryolar Oluşturun, Yönetin veya Kaldırın](/cells/tr/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Sayfa Sonlarını Yönetme](/cells/tr/net/managing-page-breaks/)
- [Sayfa Düzeni Özellikleri](/cells/tr/net/page-setup-features/)
- [Bir çalışma sayfasının birden çok kopyasını yazdırma](/cells/tr/net/print-multiple-copies-of-a-worksheet/)
- [Aspose.Cells kullanarak OpenXml'nin Sheet.SheetId özelliğini kullanın](/cells/tr/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Çalışma Sayfası Görünümleri](/cells/tr/net/worksheet-views/)

