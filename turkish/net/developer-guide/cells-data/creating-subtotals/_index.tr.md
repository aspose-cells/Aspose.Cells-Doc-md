---
title: Alt Toplamlar Oluşturma
type: docs
weight: 800
url: /tr/net/creating-subtotals/
description: Aspose.Cells for .NET API numaralı telefonu kullanarak bir e-tabloda yinelenen değerler için alt toplamları nasıl oluşturacağınızı öğrenin.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

Bir e-tabloda yinelenen değerler için otomatik olarak alt toplamlar oluşturabilirsiniz. Aspose.Cells, e-tablolara program aracılığıyla alt toplamlar eklemenize yardımcı olan API özellikleri sağlar.

{{% /alert %}}

##  **Microsoft Excel'i kullanma**

Microsoft Excel'de alt toplamlar eklemek için:

1. Çalışma kitabının ilk çalışma sayfasında (aşağıdaki şekilde gösterildiği gibi) basit bir veri listesi oluşturun ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1.  itibaren**Veri** menüsünde *Alt Toplamlar**'ı seçin. Alt Toplamlar iletişim kutusu görüntülenecektir. Hangi işlevin kullanılacağını ve alt toplamların nereye yerleştirileceğini tanımlayın.

##  **Aspose.Cells API'i kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. Sınıf, çalışma sayfalarını ve diğer nesneleri yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Her çalışma sayfası bir[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak. Bir çalışma sayfasına alt toplamlar eklemek için[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sınıf'[**ara toplam**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)yöntem. Alt toplamın nasıl hesaplanıp yerleştirilmesi gerektiğini belirtmek için yönteme parametre değerleri sağlayın.

Aşağıdaki örneklerde şablon dosyasının (Kitap1.xls) ilk çalışma sayfasına Aspose.Cells API kodunu kullanarak alt toplamlar ekledik. Kod çalıştırıldığında alt toplamların bulunduğu bir çalışma sayfası oluşturulur.

Aşağıdaki kod parçacıkları, Aspose.Cells for .NET numaralı çalışma sayfasına alt toplamların nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **İleri konular**
- [Alt Toplamın Uygulanması ve Detayın Altındaki Anahat Özeti Satırlarının Yönünün Değiştirilmesi](/cells/tr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
