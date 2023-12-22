---
title: Çalışma Kitabında Adlandırılmış Aralığı Değiştirme
type: docs
weight: 90
url: /tr/cpp/manipulate-named-range-in-a-workbook/
---
##  **Olası Kullanım Senaryoları**
 Aspose.Cells, mevcut adlandırılmış aralıkların değiştirilmesini destekler. Mevcut tüm adlandırılmış aralıklara şuradan erişilebilir:[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) Toplamak. Adlandırılmış aralığa eriştiğinizde, onun çeşitli yöntemlerini değiştirebilirsiniz; örn.[Tam Metin Al](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)Ve[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Çalışma Kitabında Adlandırılmış Aralığı Değiştirme**
 Aşağıdaki örnek kod, içindeki ilk adlandırılmış aralığı okur.[kaynak excel dosyası](23167008.xlsx) ve onu yazdırır[Tam metin](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)Ve[Şunu ifade eder:](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) Konsoldaki özellikler. Daha sonra `RefersTo` özelliğini değiştirerek kaydeder.[excel dosyasının çıktısını almak](23167009.xlsx).
##  **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Konsol Çıkışı**
 Aşağıdaki konsol çıktısı değerleri yazdırır:[Tam metin](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)Ve[Şunu ifade eder:](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) mevcut üyeler*Adlandırılmış Aralık*yukarıdaki kodda.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
