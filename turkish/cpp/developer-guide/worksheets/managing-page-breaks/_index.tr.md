---
title: Sayfa Sonlarını Yönetme
type: docs
weight: 30
url: /tr/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Tanıma göre sayfa sonu, bir metin akışında bir sayfanın bittiği ve bir sonrakinin başladığı bir yerdir. Microsoft Excel, kullanıcıların bir çalışma sayfasının seçilen herhangi bir hücresine sayfa sonları eklemesine izin verir.

Yazdırma sırasında sayfa sonunun eklendiği, sayfanın sonlandırıldığı ve sayfa sonundan sonra kalan tüm verilerin bir sonraki sayfada yazdırıldığı hücrenin konumu. Basit bir ifadeyle, sayfa sonları, çalışma sayfanızı belirtimlerinize göre birden çok sayfaya böler. Aspose.Cells'i kullanarak çalışma zamanında çalışma sayfalarınıza da sayfa sonları ekleyebilirsiniz. Aspose.Cells, geliştiricilerin iki tür sayfa sonu eklemesine olanak tanır:

- Yatay sayfa sonu
- Dikey sayfa sonu

Tartışmanın geri kalanında, Aspose.Cells'i kullanarak çalışma sayfalarınıza nasıl yatay veya dikey sayfa sonları ekleyebileceğinizi açıklayacağız.

{{% /alert %}} 
## **Sayfa Sonları**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Bu bir Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)class, bir çalışma sayfasını yönetmek için kullanılan çok çeşitli yöntemler sağlar. Sayfa sonlarını eklemek için[Sayfa Sonları Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) yöntemi[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)sınıf.
### **Sayfa Sonları Ekleme**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
