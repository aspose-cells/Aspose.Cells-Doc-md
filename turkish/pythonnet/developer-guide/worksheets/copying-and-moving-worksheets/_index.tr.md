---
title: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/python-net/copying-and-moving-worksheets/
description: Bu makale örnek kod içerir ve Aspose.Cells for Python via .NET API kullanarak bir Excel çalışma kitabındaki ve çalışma kitapları arasındaki sayfaları programlama yoluyla nasıl kopyalayıp taşıyacağınızı anlatır.
keywords: Python Excel Kütüphanesi, Python ile sayfa kopyalama, Python ile sayfa taşıma, Python ile Çalışma Kitapları arasında Sayfa Kopyalama, Python ile Çalışma Kitaplarında Sayfa Taşıma, Python ile Çalışma Kitapları arasında Sayfa Kopyalama, Python ile Bir Çalışma Kitabında Sayfa Kopyalama.
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells for Python via .NET, çalışma kitapları içinde veya arasında sayfaların kopyalanmasını ve taşınmasını destekler. Sayfa, veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerle birlikte en yüksek kesinlikle kopyalanır.

{{% /alert %}}

## **Microsoft Excel kullanarak Sayfaları Taşıma veya Kopyalama**

Microsoft Excel'de çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama ve taşıma için gereken adımlar aşağıda listelenmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

## **Bir Çalışma Kitabını Kopyalama Aspose.Cells for Python Excel Kütüphanesi ile nasıl yapılır**

Aspose.Cells for Python via .NET, veri kopyalamak ve biçimlendirmeyi başka bir çalışma sayfasına kopyalamak için [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str) adlı aşırı yüklenmiş bir yöntem sağlar. Bu yöntemden biri, kaynak çalışma sayfası indeksini parametre olarak alır. Diğeri ise kaynak çalışma sayfasının adını kullanır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Çalışma Kitapları Arasında Sayfaları Kopyalama**

Aspose.Cells for Python via .NET, kaynak çalışma sayfasından başka bir çalışma sayfasına veya başka çalışma kitapları arasında veri ve biçimlendirmeyi kopyalamak için [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet) yöntemini sağlar. Bu yöntem, kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

Aşağıdaki örnek, bir çalışma kitabından başka bir çalışma kitabına bir çalışma sayfasını kopyalamayı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Çalışma Kitabı İçinde Sayfaları Taşıma**

Aspose.Cells for Python via .NET, aynı elektronik tabloda başka bir konuma sayfa taşımak için [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) yöntemini sağlar. Bu yöntem, hedef çalışma sayfası indeksini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
