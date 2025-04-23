---
title: Microsoft Excel dosyalarının çalışma sayfalarını yönetme.
linktitle: Çalışma Sayfaları
type: docs
weight: 90
url: /tr/net/manage-worksheets/
description: Aspose.Cells kullanarak çalışma sayfası ekleyebilir, çalışma sayfasını kaldırabilir ve etkin sayfayı ekleyebilirsiniz.
---


{{% alert color="primary" %}}

Geliştiriciler, Aspose.Cells'in esnek API'sini kullanarak Microsoft Excel dosyalarında programlı olarak çalışma sayfaları eklemek ve kaldırmak için yaklaşımlar sağlar. Bu konu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir {2} koleksiyonuna sahip olan bir {0} temsil eden bir Aspose.Cells sınıfını açıklar.

{{% /alert %}}

Aspose.Cells, bir Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonuna sahiptir.

Bir çalışma sayfası, bir [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir yelpazede özellikler ve yöntemler sağlar.

## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**

Programlı olarak yeni bir Excel dosyası oluşturmak için:

1. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının bir nesnesini oluşturun.
1. [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) methodunu [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) sınıfın serisine çağırın. Boş bir çalışma sayfası otomatik olarak Excel dosyasına eklenir. Yeni çalışma sayfasının dizinini [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonuna geçirerek referans alınabilir.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfalarında çalışma yapın.
1. Yeni çalışma sayfaları ile Excel dosyasını [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) methodunu çağırarak kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**

Tasarımcı bir e-tablosuna çalışma sayfaları eklemenin süreci, yeni bir çalışma sayfası eklemekle aynıdır. Tek fark, Excel dosyasının zaten mevcut olması ve çalışma sayfaları eklenmeden önce açılması gerektiği. Bir tasarımcı e-tablosu, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı tarafından açılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Sayfa Adını Kullanarak Çalışsayfalara Erişme**

Adını veya dizinini belirterek herhangi bir çalışma sayfasına erişin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**

Dosyadan çalışma sayfalarını kaldırmak için, [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) sınıfının [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) methodunu çağırın. Belirli bir çalışma sayfasını kaldırmak için [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) methoduna çalışma sayfasının adını geçirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**

Çalışma sayfalarını adı bilindiğinde adıyla kaldırmak iyi çalışır. Eğer çalışma sayfasının adını bilmiyorsanız, çalışma sayfasının adı yerine dizinini alan [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) methodunun aşırı yüklenmiş bir sürümünü kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Sayfaları Etkinleştirme ve Çalışma Sayfasında Aktif Bir Hücre Yapma**

Bazen, bir kullanıcı Excel'de bir Microsoft Excel dosyasını açtığında belirli bir çalışma sayfasının etkin ve görüntülenen olmasını istersiniz. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırmalı çubukların etkin hücreyi göstermesini isteyebilirsiniz.
Aspose.Cells, tüm bu görevleri yapabilir.

Bir **etkin sayfa**, üzerinde çalıştığınız bir sayfadır: sekmelerdeki etkin sayfanın adı varsayılan olarak kalın harfle yazılıdır.

Bir **etkin hücre**, seçilen hücredir, verinin başlatıldığı hücredir. Aynı zamanda yalnızca bir hücre etkindir. Etkin hücre, kalın bir kenarlıkla vurgulanır.

### **Sayfaları Aktifleştirme ve Bir Hücreyi Etkin Yapma**

Aspose.Cells, bir sayfayı ve bir hücreyi aktifleştirmek için özel API çağrıları sağlar. Örneğin, [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) özelliği, bir çalışma kitabında etkin sayfayı ayarlamak için kullanışlıdır.
Benzer şekilde, [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) özelliği, çalışma sayfasında etkin bir hücreyi ayarlamak ve almak için kullanılır.

Yatay veya dikey kaydırmalı çubukların belirli verileri göstermek istediğiniz satır ve sütun dizin konumuna geldiğinden emin olmak için, [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) ve [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn) özelliklerini kullanın.

Aşağıdaki örnek, bir çalışma sayfasını etkinleştirmenin ve üzerinde etkin bir hücre oluşturmanın nasıl yapıldığını gösterir. Oluşturulan çıktıda, kaydırmalı çubuklar, ilk görünür satır ve sütun olarak 2. satır ve 2. sütunu yapmak için kaydırılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Gelişmiş Konular**
- [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/net/copying-and-moving-worksheets/)
- [Çalışma Sayfasındaki Hücre Sayısını Sayma](/cells/tr/net/count-number-of-cells-in-the-worksheet/)
- [Boş Çalışma Sayfalarını Algılama](/cells/tr/net/detecting-empty-worksheets/)
- [Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma](/cells/tr/net/find-if-the-worksheet-is-dialog-sheet/)
- [Çalışma sayfası benzersiz kimliğini alın](/cells/tr/net/get-worksheet-unique-id/)
- [Çalışma Sayfalarından Senaryo Oluşturma, Hareketlendirme veya Kaldırma](/cells/tr/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Sayfa Sonlarını Yönetme](/cells/tr/net/managing-page-breaks/)
- [Sayfa Ayarı Özellikleri](/cells/tr/net/page-setup-features/)
- [Bir çalışma sayfasının birden fazla kopyasını yazdırma](/cells/tr/net/print-multiple-copies-of-a-worksheet/)
- [Aspose.Cells üzerinde Sheet.SheetId özelliğini kullanarak OpenXml'in faydalanılması](/cells/tr/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Çalışma Sayfası Görünümleri](/cells/tr/net/worksheet-views/)

{{< app/cells/assistant language="csharp" >}}
