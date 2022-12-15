---
title: Bir Çalışma Kitabında Adlandırılmış Aralığı Yönetme
type: docs
weight: 90
url: /tr/cpp/manipulate-named-range-in-a-workbook/
---
## **Olası Kullanım Senaryoları**
 Aspose.Cells, mevcut adlandırılmış aralıkların işlenmesini destekler. Mevcut tüm adlandırılmış aralıklara şu adresten erişilebilir:[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) Toplamak. Adlandırılmış aralığa eriştiğinizde, çeşitli yöntemlerini değiştirebilirsiniz, örneğin[Tam Metin Al](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)ve[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Bir Çalışma Kitabında Adlandırılmış Aralığı Yönetme**
 Aşağıdaki örnek kod, içindeki ilk adlandırılmış aralığı okur.[kaynak excel dosyası](23167008.xlsx) ve yazdırır[Tam metin](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)ve[Referanslar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) konsoldaki özellikler. Bundan sonra, `RefersTo` özelliğini değiştirir ve kaydeder.[çıktı excel dosyası](23167009.xlsx).
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Konsol Çıkışı**
 Aşağıdaki konsol çıktısı şu değerleri yazdırır:[Tam metin](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)ve[Referanslar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) mevcut üyeler*Adlandırılmış Aralık*yukarıdaki kodda.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
