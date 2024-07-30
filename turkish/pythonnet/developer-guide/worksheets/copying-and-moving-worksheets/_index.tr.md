---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/python-net/copying-and-moving-worksheets/
description: Bu makale, Aspose.Cells for Python via .NET API si aracılığıyla çalışma tabloları arasında ve Excel çalışma kitapları arasında programatik olarak çalışma tablolarını kopyalama ve taşıma yöntemlerini içermektedir.
keywords: Python Excel Kütüphanesi, Python çalışma tablosu kopyalama, Python çalışma tablosu taşıma, Python Çalışma Kitapları Arasında Çalışma Tabloları Kopyalama, Python Çalışma Kitabı İçinde Çalışma Tabloları Taşıma, Python Çalışma Kitapları Arasında Çalışma Tabloları Kopyalama, Python Çalışma Kitapları İçinde Çalışma Tabloları Kopyalama.
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells for Python via .NET, çalışma tablolarını en yüksek hassasiyetle çalışma kitapları arasında veya içinde kopyalama ve taşıma işlemlerini destekler. Veriler, biçimlendirme, tablolar, matrisler, grafikler, görüntüler ve diğer nesneler ile birlikte çalışma tabloları en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Microsoft Excel kullanarak sayfaları Taşıma veya Kopyalama Nasıl**

Microsoft Excel'de çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama ve taşıma için gereken adımlar aşağıda listelenmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

## **Aspose.Cells for Python Excel Kütüphanesi ile Çalışma Kitabı içinde Çalışma Sayfalarını Nasıl Kopyalarsınız**

Aspose.Cells for Python via .NET, bir çalışma sayfasını koleksiyona eklemek ve mevcut bir çalışma sayfasından veri kopyalamak için kullanılan çok yüklü bir yöntem sunar. Yöntemin bir versiyonu kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer versiyon ise kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Çalışma Kitapları Arasında Çalışma Sayfalarını Nasıl Kopyalarsınız**

Aspose.Cells for Python via .NET, bir kaynak çalışma sayfasından veri ve biçimlendirmeyi başka bir çalışma sayfasına veya çalışma kitapları arasında kopyalamak için kullanılan bir yöntem sunar. Yöntem kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

Aşağıdaki örnek, bir çalışma kitabından başka bir çalışma kitabına bir çalışma sayfasını kopyalamayı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Çalışma Kitabı içinde Çalışma Sayfalarını Nasıl Taşırsınız**

Aspose.Cells for Python via .NET, çalışma sayfasını aynı elektronik tabloda başka bir konuma taşımak için kullanılan bir yöntem sunar. Yöntem hedef çalışma sayfası dizinini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
