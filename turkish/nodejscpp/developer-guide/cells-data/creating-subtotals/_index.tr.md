---
title: Araltı Oluşturma
type: docs
weight: 800
url: /tr/nodejs-cpp/creating-subtotals/
description: Bir elektronik tablolarda herhangi bir tekrar eden değerler için toplamlar nasıl oluşturulacağını Aspose.Cells for Node.js via C++ API sini kullanarak öğrenin.
keywords: Alt Toplamları Uygula, Alt Toplamları Ayarla, Alt toplamlar ekle, Alt Toplamlar Oluştur, Bir çalışma sayfasına alt toplamlar eklemek için nasıl 
---

{{% alert color="primary" %}}

Bir elektronik tablodaki tekrar eden tüm değerler için otomatik olarak toplamlar oluşturabilirsiniz. Aspose.Cells for Node.js via C++, elektronik tablolar üzerinde toplamlar eklemenize yardımcı olan API özellikleri sağlar.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de aralık eklemek için:

1. İlk çalışma kitabının ilk çalışma sayfasında basit bir veri listesi oluşturun (aşağıdaki şekilde gösterildiği gibi) ve dosyayı Book1.xls olarak kaydedin.
1. Listenizdeki herhangi bir hücreyi seçin.
1. **Veri** menüsünden **Aralıklar**'ı seçin. Aralık iletişim kutusu görüntülenecektir. Kullanılacak işlevi ve aralıkların nereye yerleştirileceğini tanımlayın.

## **Aspose.Cells for Node.js via C++ API'sini kullanarak**

Aspose.Cells for Node.js via C++, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişmenizi sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. Sınıf çalışma sayfalarını ve diğer nesneleri yönetmek için geniş bir özellikler ve yöntemler yelpazesi sağlar. Her çalışma sayfası, bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundan oluşur. Bir çalışma sayfasına aralık eklemek için [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) sınıfının [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) yöntemini kullanın. Yönteme parametre değerleri sağlayarak aralığın nasıl hesaplanacağını ve yerleştirileceğini belirtin.

Aşağıdaki örneklerde, Aspose.Cells for Node.js via C++ API'sini kullanarak [şablon dosyası](book1.xlsx) ilk çalışma sayfasına toplamlar ekledik. Kod çalıştırıldığında, toplamlı bir çalışma sayfası oluşturulur.

Aşağıdaki kod parçacıkları, Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfasına toplamlar nasıl eklenir gösterir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
