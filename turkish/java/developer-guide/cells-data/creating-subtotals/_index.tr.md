---
title: Araltı Oluşturma
type: docs
weight: 50
url: /tr/java/creating-subtotals/
---

{{% alert color="primary" %}}

Herhangi bir tekrar eden değer için alt toplamlar otomatik olarak oluşturabilirsiniz. Aspose.Cells, elektronik tablolara alt toplamlar eklemenize yardımcı olan API özellikleri sunar.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de alt toplamlar oluşturmak için:

1. İlk çalışma kitabının ilk çalışma sayfasında basit bir veri listesi oluşturun (aşağıdaki şekilde gösterildiği gibi) ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1. **Veri** menüsünden **Alt Toplamlar**'ı seçin.
   Alt Toplam iletişim kutusu görüntülenir. Hangi işlevin kullanılacağını ve alt toplamların nereye konulacağını tanımlayın.

   **Alt toplamlar eklemek için veri aralığı seçme**

![todo:image_alt_text](creating-subtotals_1.png)

**Alt Toplam İletişim Kutusu** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Aspose.Cells API'si Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. Sınıf, bir çalışma sayfasını ve diğer nesneleri yönetmek için geniş bir yelpaze sunar. Her bir çalışma sayfası bir [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundan oluşur. Bir çalışma sayfasında alt toplamlar oluşturmak için [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) sınıfının subtotal methodunu kullanın. Methodun parametreleri için uygun değerleri sağlayarak istediğiniz sonucu elde edin.

Aşağıdaki örnek, Aspose.Cells API'sını kullanarak şablon dosyasının (Book1.xls) ilk çalışma sayfasında alt toplamlar oluşturmayı göstermektedir.

Kod çalıştırıldığında, alt toplamları olan bir çalışma sayfası oluşturulur.

**Alt Toplamları Uygulama** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
