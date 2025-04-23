---
title: Pivot Öğesinin Mutlak Konumunu Belirtme
type: docs
weight: 50
url: /tr/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Bazen, kullanıcı pivot öğelerinin mutlak konumunu belirtmek ister, Aspose.Cells for Node.js via C++ API, kullanıcının bu ihtiyacını karşılamak için birkaç yeni özellik ve yöntem ortaya koymuştur.

- Tüm ebeveyn düğümün bağımsızında PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) özelliği eklendi. - Aynı ebeveyn düğümdeki PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) özelliği eklendi.
- PivotItem'ı yukarı veya aşağı hareket ettirmek için [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) metodu eklendi, burada sayım değeri tarafından yapılacak PivotItem'ın yukarı veya aşağı hareket etme sayısını belirtir; Eğer sayım değeri sıfırdan küçükse, öğe yukarı hareket ettirilecek, eğer sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, Boolean türünde olan isSameParent parametresi, hareket işleminin aynı ebeveyn düğümünde gerçekleştirilip gerçekleştirilmeyeceğini belirtir.
- *PivotItem.move(int count)* metodunun kullanımı kullanımdan kaldırıldı, bunun yerine yeni eklenen [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) metodunun kullanılması önerilir.

{{% /alert %}}

Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından aynı ebeveyn düğümdeki Pivot Öğelerinin konumlarını belirtir. Referansınız için [kaynak Excel](5112632.xlsx) ve [çıktı Excel](5112619.xlsx) dosyalarını indirebilirsiniz. Çıktı Excel dosyasını açarsanız, Pivot Öğesi "4H12"'nin "K11" üst ebeveynindeki 0. pozisyonda olduğunu ve "DIF400"'in 3. pozisyonda olduğunu göreceksiniz. Benzer şekilde, CA32 1. pozisyonda ve AAA3 2. pozisyonda.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Lütfen dikkat, [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-), [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) özellikleri ve [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) metodu kullanmadan önce PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak gereklidir.

{{% /alert %}}

