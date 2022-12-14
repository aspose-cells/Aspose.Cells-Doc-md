---
title: Çalışma Kitabında Adlandırılmış Aralık Oluşturma
type: docs
weight: 60
url: /tr/cpp/create-named-range-in-a-workbook/
---
## **Olası Kullanım Senaryoları**
 Aspose.Cells, adlandırılmış bir aralığın oluşturulmasını destekler. Adlandırılmış bir aralık oluşturmanın farklı yolları vardır. En basit yollardan biri, önce oluşturmaktır.[IR Aralığı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) nesne ve ardından kullanarak adını ayarlayın[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) yöntem. Microsoft Excel üzerinden tüm adlandırılmış aralıkları excel dosyanızda görebilirsiniz.*Ad Yöneticisi*arayüz.
## **Çalışma Kitabında Adlandırılmış Aralık Oluşturma**
 Aşağıdaki örnek kod, nasıl oluşturulacağını açıklar.*Adlandırılmış Aralık* Aspose.Cells aracılığıyla.*Adlandırılmış Aralık* oluşturulur, içinde görünür[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) Toplamak. Lütfen bkz[çıktı excel dosyası](23167006.xlsx) referans için kod tarafından oluşturulur.
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Konsol Çıkışı**
 Aşağıdaki konsol çıktısı şu değerleri yazdırır:[Tam Metin Al](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) ve oluşturulan `GetRefersTo` yöntemleri*Adlandırılmış Aralık*yukarıdaki kodda.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
