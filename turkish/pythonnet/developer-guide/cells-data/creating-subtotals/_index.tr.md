---
title: Araltı Oluşturma
type: docs
weight: 800
url: /tr/python-net/creating-subtotals/
description: Aspose.Cells for Python via .NET API sını kullanarak bir elektronik tabloda herhangi bir tekrar eden değerler için aralık oluşturmayı öğrenin.
keywords: Python Excel Kütüphanesi, Aralık Uygula, Aralık Ayarla, Aralık Ekle, Aralık Oluştur, Çalışma sayfasına aralık ekleme 
---

{{% alert color="primary" %}}

Bir elektronik tabloda herhangi bir tekrar eden değerler için otomatik olarak aralık oluşturabilirsiniz. Aspose.Cells for Python via .NET, elektronik tablolara aralık eklemenize yardımcı olan API özelliklerini sağlar.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de aralık eklemek için:

1. İlk çalışma kitabının ilk çalışma sayfasında basit bir veri listesi oluşturun (aşağıdaki şekilde gösterildiği gibi) ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1. **Veri** menüsünden **Aralıklar**'ı seçin. Aralık iletişim kutusu görüntülenecektir. Kullanılacak işlevi ve aralıkların nereye yerleştirileceğini tanımlayın.

## **Aspose.Cells for Python via .NET API'sını Kullanarak**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınır sunar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. Sınıf çalışma sayfalarını ve diğer nesneleri yönetmek için geniş bir özellikler ve yöntemler yelpazesi sağlar. Her çalışma sayfası, bir [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundan oluşur. Bir çalışma sayfasına aralık eklemek için [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sınıfının [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) yöntemini kullanın. Yönteme parametre değerleri sağlayarak aralığın nasıl hesaplanacağını ve yerleştirileceğini belirtin.

Aşağıdaki örneklerde, Aspose.Cells for Python via .NET API'sını kullanarak şablon dosyanın (Book1.xls) ilk çalışma sayfasına aralıklar ekledik. Kod çalıştırıldığında, aralıklı bir çalışma sayfası oluşturulur.

Aşağıdaki kod parçaları, Aspose.Cells for Python via .NET ile bir çalışma sayfasına aralık eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **Gelişmiş Konular**
- [Aralık Uygulama ve Özet Satırların Yönünü Değiştirme ve Özetlerin Ayrıntıların Altında Oluşturulması](/cells/tr/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
{{< app/cells/assistant language="python-net" >}}
