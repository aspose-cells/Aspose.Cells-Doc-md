---
title: Boş Çalışsayfası Bulma
type: docs
weight: 410
url: /tr/python-net/detecting-empty-worksheets/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesini kullanarak Excel çalışma kitaplarının programlı olarak boş çalışma sayfalarını nasıl tespit edeceğinizi açıklayan kodları gösterir.
keywords: Python Excel Kütüphanesi, python kullanarak boş çalışma sayfası tespiti, python da boş excel çalışma sayfası bulma.
---

## **Doldurulmuş Hücreleri Kontrol Etme**

Çalışma sayfaları bir veya daha fazla hücre değeriyle doldurulabilir ve bir değer basit (metin, sayısal, tarih/saat) veya bir formül veya formül tabanlı bir değer olabilir. Bu durumda, verilen çalışma sayfasının boş olup olmadığını tespit etmek kolaydır. Yapmamız gereken tek şey, [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) veya [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) özelliklerini kontrol etmektir. Yukarıdaki özelliklerden herhangi biri sıfır veya pozitif değerler döndürürse, bir veya daha fazla hücre dolmuş demektir, ancak bu özelliklerden herhangi biri -1 döndürürse, verilen çalışma sayfasında hiçbir hücre dolmamış demektir.

{{% alert color="primary" %}}

Satır ve sütun koleksiyonları sıfırdan başlayan dizinlere sahiptir, bu nedenle 0. satır ve 0. sütuna sahip bir hücre, çalışma sayfasındaki ilk hücre anlamına gelir, yani A1.

{{% /alert %}}

## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**

Değerlere sahip tüm hücreler otomatik olarak başlatılır, ancak bir çalışma sayfasının sadece biçimlendirme uygulanan hücreleri olabileceği bir olasılık vardır. Bu senaryoda, [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) veya [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) özellikleri, başlatılmış hücrelerin olmamasını ancak başlatılmış hücrelere sahip hücrelerin bu yaklaşımla algılanamayacağını belirten -1 değerini döndürecektir. Bir çalışma sayfasının boş başlatılmış hücreleri olup olmadığını kontrol etmek için, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundan elde edilen numaralandırıcı üzerinde IEnumerator.MoveNext yönteminin kullanılması tavsiye edilir. Eğer IEnumerator.MoveNext yöntemi **true** döndürürse, bu, verilen çalışma sayfasında bir veya daha fazla başlatılmış hücre olduğu anlamına gelir.

## **Şekilleri Kontrol Etme**

Belirli bir çalışma sayfasının hiçbir dolu hücreyi içermediği ancak kontroller, grafikler, resimler gibi şekiller ve nesneler içerebileceği bir olasılık vardır. Bir çalışma sayfasının herhangi bir şekil içerip içermediğini kontrol etmemiz gerekiyorsa, [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) öğelerini inceleyerek yapabiliriz. Herhangi bir pozitif değer, çalışma sayfasında şekil(ler) bulunduğunu gösterecektir.

## **Programlama Örneği**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
