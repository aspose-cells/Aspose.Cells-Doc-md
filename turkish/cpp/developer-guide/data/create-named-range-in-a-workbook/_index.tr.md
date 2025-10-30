---
title: Bir İş Kitabında İsimlendirilmiş Aralık Oluşturma
type: docs
weight: 60
url: /tr/cpp/create-named-range-in-a-workbook/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells bir adlandırılmış aralık oluşturmayı destekler. Bir adlandırılmış aralık oluşturmanın farklı yolları vardır. En basit yollardan biri önce bir [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) nesnesi oluşturmak ve ardından [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) yöntemini kullanarak adını belirtmektir. Adlandırılmış aralıkların tümünü Microsoft Excel *Ad Yöneticisi* arayüzü üzerinden excel dosyanızın içinde görebilirsiniz.
## **Bir İş Kitabında Adlandırılmış Aralık Oluşturma**
Aşağıdaki örnek kod, Aspose.Cells üzerinden bir *Adlandırılmış Aralık* oluşturmayı açıklar. Bir kez *Adlandırılmış Aralık* oluşturulduktan sonra, [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) koleksiyonunun içinde görünür. Lütfen kod tarafından oluşturulan [çıktı excel dosyasını](23167006.xlsx) bir referans için görün.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Konsol Çıktısı**
Aşağıdaki konsol çıktısı, yukarıdaki kodda oluşturulan *Adlandırılmış Aralık* nesnesinin [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) ve [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) yöntemlerinin değerlerini yazdırır.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
