---
title: Ara Toplamlar Oluşturma
type: docs
weight: 800
url: /tr/net/creating-subtotals/
---
{{% alert color="primary" %}}

Bir e-tablodaki yinelenen değerler için otomatik olarak ara toplamlar oluşturabilirsiniz. Aspose.Cells, elektronik tablolara programlı olarak ara toplamlar eklemenize yardımcı olan API özelliklerini sağlar.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de ara toplamlar eklemek için:

1. Çalışma kitabının ilk çalışma sayfasında (aşağıdaki şekilde gösterildiği gibi) basit bir veri listesi oluşturun ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1.  itibaren**Veri** menü, seç**ara toplamlar**. Alt toplamlar iletişim kutusu görüntülenecektir. Hangi işlevin kullanılacağını ve alt toplamların nereye yerleştirileceğini tanımlayın.

## **Aspose.Cells API'i kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. Sınıf, çalışma sayfalarını ve diğer nesneleri yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Her çalışma sayfası bir[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. Bir çalışma sayfasına ara toplamlar eklemek için,[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıf'[**ara toplam**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)yöntem. Ara toplamın nasıl hesaplanıp yerleştirileceğini belirtmek için yönteme parametre değerleri sağlayın.

Aşağıdaki örneklerde, şablon dosyasının (Kitap1.xls) ilk çalışma sayfasına Aspose.Cells API kullanarak alt toplamlar ekledik. Kod yürütüldüğünde, ara toplamları olan bir çalışma sayfası oluşturulur.

Aşağıdaki kod parçacıkları, Aspose.Cells for .NET ile bir çalışma sayfasına alt toplamların nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **ileri konular**
- [Ayrıntı altındaki Anahat Özeti Satırlarının Ara Toplamını Uygulama ve Yönünü Değiştirme](/cells/tr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
