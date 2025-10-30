---
title: Microsoft Excel dosyalarının çalışma sayfalarını yönetme.
linktitle: Çalışma Sayfaları
type: docs
weight: 90
url: /tr/python-net/manage-worksheets/
description: Bu makale, Aspose.Cells for Python via .NET API ile Microsoft Excel dosyalarının Çalışma Sayfalarını Yönetmeyi göstermektedir.
keywords: Python Excel Kütüphanesi, Python ile Microsoft Excel dosyalarının Çalışma Sayfalarını Yönetme, Python da Çalışma Sayfası Ekleme, Python da Çalışma Sayfası Kaldırma, Python da Yeni Bir Excel Dosyasına Çalışma Sayfası Ekleme, Python da Tasarımcı Elektronik Tablo için Çalışma Sayfası Ekleme, Python da Sayfa Adı kullanarak Çalışma Sayfalarına Erişme, Python da Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma, Python da Sayfa İndeksini Kullanarak Çalışma Sayfalarını Kaldırma, Python da Sayfaları Etkinleştirme ve Bir Hücreyi Etkin Yapma.
---


{{% alert color="primary" %}}

Geliştiriciler, Aspose.Cells'in esnek API'sini kullanarak Microsoft Excel dosyalarında programlı olarak çalışma sayfaları eklemek ve kaldırmak için yaklaşımlar sağlar. Bu konu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir {2} koleksiyonuna sahip olan bir {0} temsil eden bir Aspose.Cells sınıfını açıklar.

{{% /alert %}}

Aspose.Cells, bir Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonuna sahiptir.

Bir çalışma sayfası, bir [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir yelpazede özellikler ve yöntemler sağlar.

## **Yeni bir Excel Dosyasına Çalışma Sayfaları Ekleme**

Programlı olarak yeni bir Excel dosyası oluşturmak için:

1. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının bir nesnesini oluşturun.
1. [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) methodunu [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) sınıfın serisine çağırın. Boş bir çalışma sayfası otomatik olarak Excel dosyasına eklenir. Yeni çalışma sayfasının dizinini [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonuna geçirerek referans alınabilir.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfalarında çalışma yapın.
1. Yeni çalışma sayfaları ile Excel dosyasını [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) methodunu çağırarak kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Tasarımcı Elektronik Tablo için Çalışma Sayfaları Ekleme**

Tasarımcı bir e-tablosuna çalışma sayfaları eklemenin süreci, yeni bir çalışma sayfası eklemekle aynıdır. Tek fark, Excel dosyasının zaten mevcut olması ve çalışma sayfaları eklenmeden önce açılması gerektiği. Bir tasarımcı e-tablosu, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı tarafından açılabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Sayfa Adı kullanarak Çalışma Sayfalarına Erişme**

Adını veya dizinini belirterek herhangi bir çalışma sayfasına erişin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**

Dosyadan çalışma sayfalarını kaldırmak için, [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) sınıfının [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) methodunu çağırın. Belirli bir çalışma sayfasını kaldırmak için [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) methoduna çalışma sayfasının adını geçirin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Sayfa İndeksini Kullanarak Çalışma Sayfalarını Kaldırma**

Çalışma sayfasının adı bilindiğinde çalışır. Sayfa adını bilmiyorsanız, sayfa adı yerine çalışma sayfasının sayfa indeksini alan [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) yöntemini kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Sayfaları Etkinleştirme ve Çalışma Sayfasında Etkin Bir Hücre Yapma**

Bazen, bir kullanıcı Excel'de bir Microsoft Excel dosyasını açtığında belirli bir çalışma sayfasının etkin ve görüntülenen olmasını istersiniz. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırmalı çubukların etkin hücreyi göstermesini isteyebilirsiniz.
Aspose.Cells, tüm bu görevleri yapabilir.

Bir **etkin sayfa**, üzerinde çalıştığınız bir sayfadır: sekmelerdeki etkin sayfanın adı varsayılan olarak kalın harfle yazılıdır.

Bir **etkin hücre**, seçilen hücredir, verinin başlatıldığı hücredir. Aynı zamanda yalnızca bir hücre etkindir. Etkin hücre, kalın bir kenarlıkla vurgulanır.

### **Sayfaları Etkinleştirme ve Bir Hücreyi Etkin Yapma**

Aspose.Cells, bir sayfayı ve bir hücreyi aktifleştirmek için özel API çağrıları sağlar. Örneğin, [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) özelliği, bir çalışma kitabında etkin sayfayı ayarlamak için kullanışlıdır.
Benzer şekilde, [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) özelliği, çalışma sayfasında etkin bir hücreyi ayarlamak ve almak için kullanılır.

Yatay veya dikey kaydırmalı çubukların belirli verileri göstermek istediğiniz satır ve sütun dizin konumuna geldiğinden emin olmak için, [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) ve [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/) özelliklerini kullanın.

Aşağıdaki örnek, bir çalışma sayfasını etkinleştirmenin ve üzerinde etkin bir hücre oluşturmanın nasıl yapıldığını gösterir. Oluşturulan çıktıda, kaydırmalı çubuklar, ilk görünür satır ve sütun olarak 2. satır ve 2. sütunu yapmak için kaydırılır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
