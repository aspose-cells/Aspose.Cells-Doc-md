---
title: Pivot Öğesinin Mutlak Konumunu Belirleme
type: docs
weight: 50
url: /tr/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Bazen, kullanıcının pivot öğelerinin mutlak konumunu belirtmesi gerekir, Aspose.Cells API birkaç yeni özelliği ve kullanıcı gereksinimini karşılamak için bir yöntemi kullanıma sunmuştur.

-  Katma[**Özet Öğe. Konum**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) üst düğümden bağımsız olarak tüm PivotItem'lerdeki konum dizinini belirtmek için kullanılabilen özellik. Katma[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) aynı üst düğüm altındaki PivotItems içindeki konum dizinini belirtmek için kullanılabilen özellik.
-  Katma[**PivotItem.Move(int sayısı, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)count değerine göre öğeyi yukarı veya aşağı taşımak için kullanılan yöntem; burada count, PivotItem'i yukarı veya aşağı hareket ettirmek için konum sayısıdır. Sayım değeri sıfırdan küçükse, öğe yukarı taşınır, burada sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, Boolean tipi isSameParent parametresi, taşıma işleminin aynı üst düğümde gerçekleştirilip gerçekleştirilmeyeceğini belirtir. ya da değil.
-  Eskimiş*PivotItem.Move(int sayısı)* yöntemi bu nedenle yeni eklenen yöntemin kullanılması önerilir.[**PivotItem.Move(int sayısı, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) yerine.

{{% /alert %}}

 Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından aynı üst düğümdeki Pivot Öğeleri konumlarını belirtir. indirebilirsiniz[kaynak Excel](5112632.xlsx) ve[Excel çıktısı](5112619.xlsx) referansınız için dosyalar. Çıktı Excel dosyasını açarsanız, "4H12" Pivot Öğesinin "K11" ebeveyninde 0. konumda ve "DIF400" 3. konumda olduğunu göreceksiniz. Benzer şekilde, CA32 1 konumunda ve AAA3 2 konumunda

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Lütfen unutmayın, kullanmadan önce PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak gerekir.[**Özet Öğe. Konum**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) özellikler ve[**PivotItem.Move(int sayısı, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) yöntem.

{{% /alert %}}
