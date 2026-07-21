---
title: Golang ile C++ kullanarak Pivot Öğesinin Mutlak konumunu belirleme
linktitle: Pivot Öğesinin Mutlak Konumunu Belirtme
type: docs
weight: 50
url: /tr/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Aspose.Cells kullanarak C++ ta pivot öğelerinin mutlak konumunu nasıl belirteceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazen kullanıcıların pivot öğelerinin mutlak konumunu belirtmesi gerekir. Aspose.Cells API, bu ihtiyacı karşılamak için birkaç yeni özellik ve yöntem ortaya çıkardı.

- Tüm ebeveyn düğümün bağımsızında PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) özelliği eklendi. - Aynı ebeveyn düğümdeki PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) özelliği eklendi.
- PivotItem'i yukarı veya aşağı hareket ettirmek için sayım değerine göre `[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/)` yöntemi eklendi. Burada sayım, PivotItem'i yukarı veya aşağı hareket ettirmek için kaç pozisyon hareket edileceğini belirtir. Eğer sayım değeri sıfırdan küçükse, öğe yukarı taşınır; eğer sıfırdan büyükse, aşağı taşınır. Boolean tip `isSameParent` parametresi, hareket işleminin aynı ebeveyn düğümde olup olmayacağını belirtir.
- `PivotItem.Move(int count)` yöntemi kullanımdan kaldırılmıştır; bu nedenle, önerilen yeni yöntem [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) kullanılmasıdır.

{{% /alert %}}

Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından Pivot Öğeleri'nin konumlarını aynı ebeveyn düğümde belirtir. Referansınız için [kaynak Excel](5112632.xlsx) ve [çıktı Excel](5112619.xlsx) dosyalarını indirebilirsiniz. Çıktı Excel dosyasını açarsanız, Pivot Öğesi "4H12"'nin ebeveyn "K11" içinde 0. pozisyonda olduğunu ve "DIF400"'ün ise 3. pozisyonda olduğunu göreceksiniz. Benzer şekilde, CA32 1. pozisyonda ve AAA3 2. pozisyondadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Lütfen, `[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/)`, `[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)` özelliklerini ve `[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)` yöntemini kullanmadan önce `PivotTable.RefreshData` ve `PivotTable.CalculateData` yöntemlerini çağırmanız gerektiğini unutmayın.

{{% /alert %}}
