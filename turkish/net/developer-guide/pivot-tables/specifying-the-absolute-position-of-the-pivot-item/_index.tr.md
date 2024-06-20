---
title: Pivot Öğesinin Mutlak Konumunu Belirtme
type: docs
weight: 50
url: /tr/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Bazı durumlarda, kullanıcı pivot öğelerinin mutlak konumunu belirmek isteyebilir, Aspose.Cells API'sı, kullanıcı gereksinimini karşılamak için birkaç yeni özellik ve bir yöntem sunar.

- Tüm ebeveyn düğümün bağımsızında PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) özelliği eklendi. - Aynı ebeveyn düğümdeki PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) özelliği eklendi.
- PivotItem'ı yukarı veya aşağı hareket ettirmek için [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) metodu eklendi, burada sayım değeri tarafından yapılacak PivotItem'ın yukarı veya aşağı hareket etme sayısını belirtir; Eğer sayım değeri sıfırdan küçükse, öğe yukarı hareket ettirilecek, eğer sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, Boolean türünde olan isSameParent parametresi, hareket işleminin aynı ebeveyn düğümünde gerçekleştirilip gerçekleştirilmeyeceğini belirtir.
- *PivotItem.Move(int count)* yöntemi kullanım dışı bırakıldı bu nedenle tavsiye edilen, yerine yeniden eklenen yöntemi [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) kullanmaktır.

{{% /alert %}}

Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından aynı ebeveyn düğümdeki Pivot Öğelerinin konumlarını belirtir. Referansınız için [kaynak Excel](5112632.xlsx) ve [çıktı Excel](5112619.xlsx) dosyalarını indirebilirsiniz. Çıktı Excel dosyasını açarsanız, Pivot Öğesi "4H12"'nin "K11" üst ebeveynindeki 0. pozisyonda olduğunu ve "DIF400"'in 3. pozisyonda olduğunu göreceksiniz. Benzer şekilde, CA32 1. pozisyonda ve AAA3 2. pozisyonda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Lütfen dikkat, [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) özellikleri ve [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) metodu kullanmadan önce PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak gereklidir.

{{% /alert %}}
