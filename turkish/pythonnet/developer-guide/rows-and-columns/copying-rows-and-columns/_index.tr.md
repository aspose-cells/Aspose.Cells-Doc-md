---
title: Satır ve Sütunları Kopyalama
type: docs
weight: 40
url: /tr/python-net/copying-rows-and-columns/
description: Bu makale, Aspose.Cells for Python via .NET API sini kullanarak Satırların ve Sütunların nasıl kopyalanacağını göstermektedir.
keywords: Python Excel Kütüphanesi, Python Satırların ve Sütunların Nasıl Kopyalanır, Python da Satırları Kopyalama, Python da Sütunların Kopyalanması, Aspose.Cells for Python via .NET Kullanarak Satırların ve Sütunların Kopyalanması, Python Çoklu Satır ve Sütunlarının Yapıştırılması, Python da Tek Satır veya Sütunun Nasıl Kopyalandığı ve Yapıştırıldığı.
---

## **Giriş**

Bazen, bir çalışma sayfasında tüm çalışma sayfasını kopyalamadan satır ve sütunları kopyalamanız gerekir. Aspose.Cells ile, çalışma kitapları arasında veya içinde satır ve sütunları kopyalamak mümkündür.
Bir satır (veya sütun) kopyalandığında, içindeki veriler, güncellenmiş referanslarla formülleri - ve değerleri, yorumları, biçimlendirmeyi, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini içeren veriler de kopyalanır.

## **Microsoft Excel ile Satırları ve Sütunları Nasıl Kopyalanır**

1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1. Satır veya sütunları kopyalamak için **Standart** araç çubuğunda **Kopyala**'yı tıklayın veya **CTRL**+**C**'ye basın.
1. Kopyalamak istediğiniz seçimin altında veya sağındaki bir satır veya sütunu seçin.
1. Satır veya sütunları kopyalarken, **Ekle** menüsünde **Kopyalanan Hücreler**'i tıklayın.

{{% alert color="primary" %}}

Hedef hücrelerin içeriği herhangi bir içeriği Çıkar veya tıklamak yerine **Standart** araç çubuğunda **Yapıştır**'ı tıklarsanız değiştirilir.

{{% /alert %}}

## **Microsoft Excel ile Yapıştırma Seçenekleri Kullanarak Satır ve Sütunları Nasıl Yapıştırılır**

1. Kopyalamak istediğiniz veri veya diğer özelliklere sahip hücreleri seçin.
1. Ana sekmede **Kopyala**'yı tıklayın.
1. Kopyaladığınız şeyi yapıştırmak istediğiniz alanın ilk hücresine tıklayın.
1. Ana sekmede **Yapıştır**'ın yanındaki oku tıklayın ve ardından **Yapıştırma**'yı seçin.
1. İstediğiniz **seçenekleri** seçin.

## **Aspose.Cells for .NET Kullanarak Satır ve Sütunları Nasıl Kopyalanır**

## **Tek Satırları Nasıl Kopyalanır**

Aspose.Cells, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sınıfının [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) yöntemini sağlar. Bu yöntem, formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri de dahil olmak üzere tüm türde verileri kaynaktan hedefe kopyalar.

[**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) yöntemi aşağıdaki parametreleri alır:

- kaynak [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) nesnesi
- kaynak satır endeksi, ve
- hedef satır endeksi.

Bu yöntemi bir sayfa içinde bir satırı, veya başka bir sayfaya kopyalamak için kullanın. [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) yöntemi, örneğin Microsoft Excel'de olduğu gibi benzer şekilde çalışır. Bu nedenle, örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yok, o değer de kopyalanır.

Aşağıdaki örnek, bir çalışsayfasında bir satır kopyalamayı gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veri, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı çalışsayfadaki 12. satıra yapıştırır.

[**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int) yöntemi kullanarak kaynak satırın yüksekliğini almayı ve ardından hedef satırın yüksekliğini ayarlamayı dikkate almanız gerekmez, çünkü [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) yöntemi otomatik olarak satır yüksekliği hakkında da ilgilenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingRows-1.py" >}}

{{% alert color="primary" %}}

Satırları kopyalarken, ilgili resimler, grafikler veya diğer çizim nesnelerinin Microsoft Excel ile aynı olduğu gibi dikkate alınması önemlidir:

1. Kaynak satır dizini 5 ise, resim, grafik vb., başlangıç satır dizini 4 ve bitiş satır dizini 6 içinde bulunduruluyorsa kopyalanır.
1. Var olan resimler, grafikler vb. hedef satırdan silinmez.

{{% /alert %}}

## **Birden Fazla Satırın Nasıl Kopyalanacağı**

Ayrıca, ek bir tamsayı parametresi alarak yeni bir hedefe birden fazla satır kopyalarken [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) yöntemini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleRows-1.py" >}}


## **Sütunları Kopyalamak**

Aspose.Cells, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sınıfının [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) yöntemini sağlar, bu yöntem formüller, güncellenmiş referanslar içeren değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm türde verileri kaynaktan hedefe kopyalar.

[**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) yöntemi aşağıdaki parametreleri alır:

- kaynak [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) nesnesi
- kaynak sütun indeksi ve
- hedef sütun indeksi.

Bir çalışma sayfası içinde bir sütunu kopyalamak veya başka bir çalışma sayfasına kopyalamak için [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) yöntemini kullanın.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingColumns-1.py" >}}

## **Birden Çok Sütun Nasıl Kopyalanır**

[**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) yöntemine benzer şekilde, Aspose.Cells API'leri ayrıca birden çok kaynak sütunu yeni bir konuma kopyalamak için [**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/) yöntemini sağlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleColumns-1.py" >}}


## **Yapıştırma Seçenekleri ile Satır ve Sütunların Nasıl Yapıştırılacağı**

Aspose.Cells şimdi, [**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions) işlevler [**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions) ve [**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions) kullanırken uygun yapıştırma seçeneğini Excel ile benzer şekilde ayarlamayı sağlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.py" >}}

