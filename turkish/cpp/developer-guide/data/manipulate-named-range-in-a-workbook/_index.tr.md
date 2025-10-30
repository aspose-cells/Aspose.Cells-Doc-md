---
title: Bir İş Kitabındaki Adlandırılmış Aralığı Değiştirme
type: docs
weight: 90
url: /tr/cpp/manipulate-named-range-in-a-workbook/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells mevcut adlandırılmış aralıkların manipülasyonunu destekler. Tüm mevcut adlandırılmış aralıklara [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) koleksiyonundan erişilebilir. Adlandırılmış aralığa eriştikten sonra, [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) ve [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) gibi farklı yöntemlerini değiştirebilirsiniz.
## **Bir İş Kitabındaki Adlandırılmış Aralığı Değiştirme**
Aşağıdaki örnek kod, [kaynak excel dosyası](23167008.xlsx) içindeki ilk adlandırılmış-aralığı okur ve konsol üzerine [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) ve [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) özelliklerini yazdırır. Ardından `RefersTo` özelliğini değiştirir ve [çıktı excel dosyasını](23167009.xlsx) kaydeder.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Konsol Çıktısı**
Aşağıdaki konsol çıktısı, mevcut *Adlandırılmış Aralık* için [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) ve [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) üyelerinin değerlerini yazdırır.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
