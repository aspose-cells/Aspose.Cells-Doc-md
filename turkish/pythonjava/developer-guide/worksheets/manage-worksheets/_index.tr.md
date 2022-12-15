---
title: Çalışma Sayfalarını Yönet
type: docs
weight: 10
url: /tr/python-java/manage-worksheets/
---
Aspose.Cells for Python via Java'i kullanarak çalışma sayfalarını yönetmek çok kolaydır. Bu makalede, Aspose.Cells API'i kullanarak çalışma sayfalarına ekleme, çalışma sayfalarına erişim ve kaldırmayı göstereceğiz.
## **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**
 Yeni bir Çalışma Kitabı oluşturmak için, bir nesne oluşturun.[Çalışma kitabı](https://reference.aspose.com/cells/python/asposecells.api/Workbook) sınıf. bu[Çalışma kitabı](https://reference.aspose.com/cells/python/asposecells.api/Workbook) class bir Excel dosyasını temsil eder. Daha sonra kullanarak[Ekle](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) yöntemi[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , Excel dosyasına yeni çalışma sayfaları eklenir. Son olarak, yeni oluşturulan Excel dosyasını kaydetmek için[kaydetmek](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) yöntemi[Çalışma kitabı](https://reference.aspose.com/cells/python/asposecells.api/Workbook)sınıf.

Aşağıdaki kod parçacığı, yeni bir Excel dosyası oluşturmayı ve buna bir çalışma sayfası eklemeyi gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Tasarımcı Elektronik Tablosuna Çalışma Sayfaları Ekleme**
Bir tasarımcı elektronik tablosuna çalışma sayfası eklemek, çalışma sayfasını yeni bir Excel dosyasına eklemekle tamamen aynıdır. Tek fark, yeni bir Excel dosyası oluşturmak yerine, mevcut bir dosyayı açmamızdır.[Çalışma kitabı](https://reference.aspose.com/cells/python/asposecells.api/Workbook)sınıf.

Aşağıdaki kod parçacığı, bir tasarımcı elektronik tablosuna bir çalışma sayfası eklemeyi gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme**
Bir çalışma kitabı yükledikten sonra, geliştiriciler herhangi bir çalışma sayfasına dizinini veya adını kullanarak erişebilir. Aşağıdaki kod parçacığı, adını kullanarak bir çalışma sayfasına erişmeyi gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Çalışma Sayfalarını Kaldırma**
Bazı sayfaların çalışma kitabından kaldırılmak üzere buluştuğu zamanlar olabilir. Bunun için API,[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) yöntem. Sayfa dizinini veya kaldırılacak sayfanın sayfa adını iletebilirsiniz. Aşağıdaki örnekler, sayfa dizini ve sayfa adını kullanarak çalışma sayfalarını kaldırmayı göstermektedir.
### **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
