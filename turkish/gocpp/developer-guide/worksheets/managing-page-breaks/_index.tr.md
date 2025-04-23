---
title: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

Tanıma göre, bir sayfa kesmesi, metin akışının bir sayfanın bittiği ve diğerinin başladığı yeridir. Microsoft Excel kullanıcılarına herhangi bir seçili hücreye sayfa kesmeleri eklemelerine izin verir.

Sayfa kesmesi eklenen hücrenin konumu, sayfa biter ve sayfa kesesinden sonraki tüm veri bir sonraki sayfada yazdırılır. Basılırken sayfa kesesi sonra çalışağı veri bölümlendirir. Basitçe, sayfa kesmeleri belirlemelerinize göre çalışma sayfanızı birden çok sayfaya böler. Aspose.Cells, geliştiricilere sayfa kesi eklemeleri . Yatay sayfa kesisi ve dikey sayfa kesisi ekleyebilirsiniz:

- Yatay sayfa kesmesi
- Dikey sayfa kesmesi

Tartışmanın geri kalanında, Aspose.Cells kullanarak çalışma sayfalarınıza yatay veya dikey sayfa kesme nasıl ekleyebileceğinizi açıklayacağız.

{{% /alert %}}

## **Sayfa Sonları**

Aspose.Cells, Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. Bu [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her sayfa öğesine erişim sağlayan [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunu içerir.

Bir sayfa öğesi [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, sayfa yönetimi için kullanılan çok çeşitli yöntemler sağlar. Sayfa kırıntıları eklemek için [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) yöntemini kullanın.

### **Sayfa Kesmeleri Eklemek**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
