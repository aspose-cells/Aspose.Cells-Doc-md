---
title: Ara Toplamlar Oluşturma
type: docs
weight: 50
url: /tr/java/creating-subtotals/
---
{{% alert color="primary" %}}

Bir e-tablodaki yinelenen değerler için otomatik olarak ara toplamlar oluşturabilirsiniz. Aspose.Cells, e-tablolara programlı olarak alt toplamlar eklemenize yardımcı olan API özelliklerini sağlar.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de ara toplamlar oluşturmak için:

1. Çalışma kitabının ilk çalışma sayfasında (aşağıdaki şekilde gösterildiği gibi) basit bir veri listesi oluşturun ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1.  itibaren**Veri** menü, seç**ara toplamlar**.
 Alt toplamlar iletişim kutusu görüntülenir. Hangi işlevin kullanılacağını ve alt toplamların nereye yerleştirileceğini tanımlayın.

   **Alt toplamlar eklemek için bir veri aralığı seçme**

![yapılacaklar:resim_alternatif_Metin](creating-subtotals_1.png)

**Ara toplam iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](creating-subtotals_2.png)

## **Aspose.Cells API'i kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf. Sınıf, bir çalışma sayfasını ve diğer nesneleri yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Her çalışma sayfası bir[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. Bir çalışma sayfasında ara toplamlar oluşturmak için,[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)sınıfın alt toplam yöntemi. İstediğiniz sonucu elde etmek için yöntemin parametreleri için uygun değerleri sağlayın.

Aşağıdaki örnek, Aspose.Cells API kullanılarak şablon dosyasının (Book1.xls) ilk çalışma sayfasında alt toplamların nasıl oluşturulacağını gösterir.

Kod yürütüldüğünde, alt toplamları olan bir çalışma sayfası oluşturulur.

**ara toplamlar uygulanıyor** 

![yapılacaklar:resim_alternatif_Metin](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
