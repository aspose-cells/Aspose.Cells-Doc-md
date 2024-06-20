---
title: Araltı Oluşturma
type: docs
weight: 800
url: /tr/net/creating-subtotals/
description: Aspose.Cells for .NET API sini kullanarak elektronik tabloda tekrarlanan değerler için alt toplamlar oluşturmayı öğrenin.
keywords: Alt Toplamları Uygula, Alt Toplamları Ayarla, Alt toplamlar ekle, Alt Toplamlar Oluştur, Bir çalışma sayfasına alt toplamlar eklemek için nasıl 
---

{{% alert color="primary" %}}

Herhangi bir tekrarlanan değer için alt toplamları otomatik olarak oluşturabilirsiniz. Aspose.Cells, elektronik tablolara alt toplamlar eklemeye yardımcı olan API özellikleri sunar.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de aralık eklemek için:

1. İlk çalışma kitabının ilk çalışma sayfasında basit bir veri listesi oluşturun (aşağıdaki şekilde gösterildiği gibi) ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1. **Veri** menüsünden **Aralıklar**'ı seçin. Aralık iletişim kutusu görüntülenecektir. Kullanılacak işlevi ve aralıkların nereye yerleştirileceğini tanımlayın.

## **Aspose.Cells API Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. Sınıf çalışma sayfalarını ve diğer nesneleri yönetmek için geniş bir özellikler ve yöntemler yelpazesi sağlar. Her çalışma sayfası, bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonundan oluşur. Bir çalışma sayfasına aralık eklemek için [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) yöntemini kullanın. Yönteme parametre değerleri sağlayarak aralığın nasıl hesaplanacağını ve yerleştirileceğini belirtin.

Aşağıdaki örneklerde, Aspose.Cells API kullanarak şablon dosyasının (Book1.xls) ilk çalışma sayfasına ara toplamlar ekledik. Kod çalıştırıldığında, ara toplamlara sahip bir çalışma sayfası oluşturulur.

Aşağıda gelen kod parçaları, Aspose.Cells for .NET ile çalışma sayfasına ara toplamlar nasıl eklenir göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Gelişmiş Konular**
- [Aralık Uygulama ve Özet Satırların Yönünü Değiştirme ve Özetlerin Ayrıntıların Altında Oluşturulması](/cells/tr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
