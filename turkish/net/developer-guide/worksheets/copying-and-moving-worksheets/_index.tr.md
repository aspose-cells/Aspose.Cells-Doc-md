---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/net/copying-and-moving-worksheets/
description: Bu makale, C# API veya .NET Kütüphanesi kullanarak bir Excel çalışma kitabının içinde ve arasında çalışsayfalarını programlı olarak kopyalamak ve taşımak için örnek kodları içerir.
keywords: kopya çalışsayfa c#, taşı çalışsayfa c#
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells, çalışma kitapları içinde veya arasında çalışma sayfalarını kopyalama ve taşıma desteği sağlar. Veri, biçimlendirme, tablolar, matrisler, grafikler, görüntüler ve diğer nesnelerle birlikte, en yüksek hassasiyetle kopyalanan çalışma sayfaları.

{{% /alert %}}

## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**

Microsoft Excel'de çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama ve taşıma için gereken adımlar aşağıda listelenmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

### **Aspose.Cells ile Bir Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**

Aspose.Cells, mevcut bir çalışma sayfasından veri kopyalamak için kullanılan ve çalışma sayfasının bir kopyasını eklemek için kullanılan [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index) adlı aşırı yüklü bir yöntem sağlar. Yöntemin bir sürümü, kaynak çalışma sayfasının endeksini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **Çalışma Kitapları Arasında Çalışma Sayfalarını Kopyalama**

 Aspose.Cells, çalışma kitapları arasında veya içinde bir kaynak çalışma sayfasından diğer çalışma sayfasına veri ve biçimlendirmeyi kopyalamak için kullanılan [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) yöntemini sağlar. Yöntem, kaynak çalışma sayfası nesnesini bir parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

Aşağıdaki örnek, bir çalışma kitabından başka bir çalışma kitabına bir çalışma sayfasını kopyalamayı göstermektedir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **Çalışma Kitabı İçinde Sayfaları Taşıma**

 Aspose.Cells, aynı elektronik tablo içinde bir çalışma sayfasını başka bir konuma taşımak için kullanılan [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) yöntemini sağlar. Yöntem, hedef çalışma sayfası dizinini bir parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
