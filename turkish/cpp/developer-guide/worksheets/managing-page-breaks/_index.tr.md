---
title: Sayfa Sonlarını Yönetme
type: docs
weight: 30
url: /tr/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Tanıma göre sayfa sonu, metin akışında bir sayfanın bitip diğerinin başladığı yerdir. Microsoft Excel, kullanıcıların çalışma sayfasının seçilen herhangi bir hücresine sayfa sonları eklemesine olanak tanır.

Yazdırma sırasında sayfa sonunun eklendiği, sayfanın bittiği ve sayfa sonundan sonraki tüm verilerin bir sonraki sayfaya yazdırıldığı hücrenin konumu. Basit bir ifadeyle sayfa sonları, çalışma sayfanızı spesifikasyonlarınıza göre birden fazla sayfaya böler. Ayrıca çalışma zamanında Aspose.Cells'i kullanarak çalışma sayfalarınıza sayfa sonları ekleyebilirsiniz. Aspose.Cells, geliştiricilerin iki tür sayfa sonu eklemesine olanak tanır:

- Yatay sayfa sonu
- Dikey sayfa sonu

Tartışmanın geri kalanında Aspose.Cells'i kullanarak çalışma sayfalarınıza nasıl yatay veya dikey sayfa sonları ekleyebileceğinizi açıklayacağız.

{{% /alert %}} 
##  **Sayfa Sonları**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) bu bir Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)class, bir çalışma sayfasını yönetmek için kullanılan çok çeşitli yöntemler sağlar. Sayfa sonlarını eklemek için şunu kullanın:[Sayfa Sonu Ekle](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)sınıf.
###  **Sayfa Sonu Ekleme**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
