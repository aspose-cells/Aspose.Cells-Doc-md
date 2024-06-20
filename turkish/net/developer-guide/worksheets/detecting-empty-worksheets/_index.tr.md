---
title: Boş Çalışsayfası Bulma
type: docs
weight: 410
url: /tr/net/detecting-empty-worksheets/
description: Bu makalede, C# API ve .NET kitaplığını kullanarak Excel çalışma kitabının boş çalışma sayfalarını nasıl programlı olarak algılayacağınızı açıklayan kodu gösterir.
keywords: c# ile boş çalışma sayfası algılama, boş excel çalışma sayfası c# bulma
---

## **Doldurulmuş Hücreleri Kontrol Etme**

Çalışma sayfaları bir veya daha fazla hücre değeriyle doldurulabilir ve bir değer basit (metin, sayısal, tarih/saat) veya bir formül veya formül tabanlı bir değer olabilir. Bu durumda, verilen çalışma sayfasının boş olup olmadığını tespit etmek kolaydır. Yapmamız gereken tek şey, [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) veya [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) özelliklerini kontrol etmektir. Yukarıdaki özelliklerden herhangi biri sıfır veya pozitif değerler döndürürse, bir veya daha fazla hücre dolmuş demektir, ancak bu özelliklerden herhangi biri -1 döndürürse, verilen çalışma sayfasında hiçbir hücre dolmamış demektir.

{{% alert color="primary" %}}

Satır ve sütun koleksiyonları sıfırdan başlayan dizinlere sahiptir, bu nedenle 0. satır ve 0. sütuna sahip bir hücre, çalışma sayfasındaki ilk hücre anlamına gelir, yani A1.

{{% /alert %}}

## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**

Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışma sayfasının yalnızca biçimlendirmesi uygulanan hücreleri olabilir. Bu senaryoda, [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) veya [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) özellikleri, başlatılmış hücrelerin yokluğunu gösteren -1 değerini döndürecektir, ancak bu yaklaşım kullanılarak başlatılmış boş hücrelerin algılanamayacağını gösterir. Bir çalışma sayfasının boş başlatılmış hücrelere sahip olup olmadığını kontrol etmek için [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonundan alınan numaralandırıcı üzerinde IEnumerator.MoveNext yöntemini kullanmanız önerilir. IEnumerator.MoveNext yöntemi **true** döndürürse, verilen çalışma sayfasında bir veya daha fazla başlatılmış hücre olduğu anlamına gelir.

## **Şekilleri Kontrol Etme**

Verilen bir çalışma sayfasının doldurulmuş hücreleri olmayabilir, ancak denetimler, grafikler, resimler vb. gibi şekiller ve nesneler içerebilir. Bir çalışma sayfasının herhangi bir şekil içerip içermediğini kontrol etmemiz gerekiyorsa, [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) özelliğini inceleyerek yapabiliriz. Herhangi bir pozitif değer, çalışma sayfasında şekil(l)in varlığını gösterir.

## **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
