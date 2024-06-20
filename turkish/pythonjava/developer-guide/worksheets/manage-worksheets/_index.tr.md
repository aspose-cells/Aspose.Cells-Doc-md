---
title: Çalışsayfaları Yönet
type: docs
weight: 10
url: /tr/python-java/manage-worksheets/
---

Aspose.Cells for Python via Java kullanarak çalışsayfalarını yönetmek çok kolaydır. Bu makalede, Aspose.Cells API'sını kullanarak çalışsayfaları eklemeyi, erişmeyi ve kaldırmayı göstereceğiz.
## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**
Yeni bir Workbook oluşturmak için, [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) sınıfının bir nesnesini oluşturun. [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workboo) sınıfı bir Excel dosyasını temsil eder. Ardından [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) sınıfının [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) yöntemini kullanarak, yeni çalışsayfaları Excel dosyasına ekleyin. Son olarak, oluşturulan yeni Excel dosyasını kaydetmek için [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) sınıfının [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) yöntemini çağırın.

Aşağıdaki kod parçası, yeni bir Excel dosyası oluşturmayı ve ona bir çalışsayfa eklemeyi gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**
Bir tasarımcı tablosuna çalışsayfa eklemek, yeni bir Excel dosyasına çalışsayfa eklemekle tamamen aynıdır. Tek fark, yeni bir Excel dosyası oluşturmak yerine, [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) sınıfıyla mevcut bir dosyayı açmamızdır.

Aşağıdaki kod parçası, bir tasarımcı tablosuna çalışsayfa eklemeyi gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Sayfa Adını Kullanarak Çalışsayfalara Erişme**
Worksheet Adı Kullanarak Çalışsayfaları Erişme

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Çalışsayfaları Kaldırma**
Bazı sayfaların çalışma kitabından kaldırılması gereken durumlar olabilir. Bunun için API, [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) yöntemini sağlar. Kaldırılacak sayfa dizinini veya sayfa adını iletebilirsiniz. Aşağıdaki örnekler, sayfa dizinini ve sayfa adını kullanarak çalışma sayfalarını kaldırmayı gösterir.
### **Sayfa Dizini Kullanarak Çalışsayfaları Kaldırma**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
