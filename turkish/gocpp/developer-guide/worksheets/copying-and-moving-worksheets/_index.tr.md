---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/go-cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells, çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşımayı destekler. Bir çalışma sayfası, veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerle birlikte en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**

Microsoft Excel'de çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşımanın dahil olduğu adımlar aşağıda verilmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

### **Aspose.Cells ile Bir Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**

Aspose.Cells, aşırı yüklenmiş [AddCopy()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/addcopy_string/) yöntemini sağlar. Bu yöntem, bir çalışma sayfasını koleksiyona eklemek ve mevcut bir çalışma sayfasından veri kopyalamak için kullanılır. Bir versiyon, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer versiyon ise kaynak çalışma sayfasının adını kullanır. Aşağıdaki örnek, bir çalışma kitabı içindeki mevcut bir çalışma sayfasını nasıl kopyalayacağınızı gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyWorksheetsWithinWorkbook.go" >}}

### **Çalışma Kitabı İçinde Sayfaları Taşıma**

Aspose.Cells, aynı elektronik tablodaki başka bir konuma sayfa öğesi [MoveTo()](https://reference.aspose.com/cells/go-cpp/worksheet/moveto/) yönlendirme yöntemini sağlar. Bu yöntem, hedef sayfa indeksi parametresi alır. Aşağıdaki örnek, bir sayfa öğesini çalışma kitabı içinde başka bir konuma nasıl taşıyacağınızı gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MoveWorksheetsWithinWorkbook.go" >}}
