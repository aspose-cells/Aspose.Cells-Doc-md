---
title: Boş Çalışsayfası Bulma
type: docs
weight: 410
url: /tr/python-net/detecting-empty-worksheets/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi kullanarak Excel çalışma kitaplarındaki boş çalışma sayfalarını programlı olarak nasıl tespit edeceğinizi açıklayan kod örneği gösterir.
keywords: Python Excel Kütüphanesi, python kullanarak boş çalışma sayfasını tespit et, python ile boş excel çalışma sayfasını bul.
---

## **Doldurulmuş Hücreleri Kontrol Etme**

Çalışma sayfaları bir veya daha fazla hücre değeriyle doldurulabilir ve bir değer basit (metin, sayısal, tarih/saat) veya bir formül veya formül tabanlı bir değer olabilir. Bu durumda, verilen çalışma sayfasının boş olup olmadığını tespit etmek kolaydır. Yapmamız gereken tek şey, [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) veya [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) özelliklerini kontrol etmektir. Yukarıdaki özelliklerden herhangi biri sıfır veya pozitif değerler döndürürse, bir veya daha fazla hücre dolmuş demektir, ancak bu özelliklerden herhangi biri -1 döndürürse, verilen çalışma sayfasında hiçbir hücre dolmamış demektir.

{{% alert color="primary" %}}

Satır ve sütun koleksiyonları sıfırdan başlayan dizinlere sahiptir, bu nedenle 0. satır ve 0. sütuna sahip bir hücre, çalışma sayfasındaki ilk hücre anlamına gelir, yani A1.

{{% /alert %}}

## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**

Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışma sayfasında yalnızca biçimlendirme uygulanmış hücreler olabilir. Bu durumda, [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) veya [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) özellikleri -1 döndürür ve bu da hiçbir doldurulmuş değerin olmadığını gösterir, ancak biçimlendirilmiş hücreler bu yaklaşımla algılanamaz. Bir çalışma sayfasında boş başlatılmış hücrelerin olup olmadığını kontrol etmek için, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundan alınan enumeratör üzerinde IEnumerator.MoveNext metodunun kullanılması önerilir. Eğer IEnumerator.MoveNext **true** dönerse, bu, verilen çalışma sayfasında bir veya daha fazla başlatılmış hücrenin olduğu anlamına gelir.

## **Şekilleri Kontrol Etme**

Veri ile doldurulmamış herhangi bir çalışma sayfası olabileceği gibi, şekiller ve nesneleri de içerebilir, örneğin, kontroller, grafikler, resimler ve benzeri. Bir çalışma sayfasında herhangi bir şekil olup olmadığını kontrol etmemiz gerekiyorsa, [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) öğelerini inceleyerek bunu yapabiliriz. Pozitif bir değer, çalışma sayfasında şekil(s) olduğunu gösterir.

## **Programlama Örneği**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
