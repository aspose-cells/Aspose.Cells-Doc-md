---
title: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Tanıma göre, bir sayfa kesmesi, metin akışının bir sayfanın bittiği ve diğerinin başladığı yeridir. Microsoft Excel kullanıcılarına herhangi bir seçili hücreye sayfa kesmeleri eklemelerine izin verir.

Sayfa kesmesi eklenen hücrenin konumu, sayfa biter ve sayfa kesesinden sonraki tüm veri bir sonraki sayfada yazdırılır. Basılırken sayfa kesesi sonra çalışağı veri bölümlendirir. Basitçe, sayfa kesmeleri belirlemelerinize göre çalışma sayfanızı birden çok sayfaya böler. Aspose.Cells, geliştiricilere sayfa kesi eklemeleri . Yatay sayfa kesisi ve dikey sayfa kesisi ekleyebilirsiniz:

- Yatay sayfa kesmesi
- Dikey sayfa kesmesi

Tartışmanın geri kalanında, Aspose.Cells kullanarak çalışma sayfalarınıza yatay veya dikey sayfa kesme nasıl ekleyebileceğinizi açıklayacağız.

{{% /alert %}} 
## **Sayfa Sonları**
 Aspose.Cells, bir Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) koleksiyon içerir.

Sayfa, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için kullanılan geniş bir yöntem yelpazesi sağlar. Sayfa kesmelerini eklemek için [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet) sınıfının [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) yöntemini kullanın.
### **Sayfa Kesmeleri Eklemek**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
