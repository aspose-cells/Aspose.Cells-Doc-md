---
title: Çalışma Kitabında Adlandırılmış Aralık Oluşturma
type: docs
weight: 60
url: /tr/cpp/create-named-range-in-a-workbook/
---
##  **Olası Kullanım Senaryoları**
 Aspose.Cells, adlandırılmış bir aralığın oluşturulmasını destekler. Adlandırılmış bir aralık oluşturmanın farklı yolları vardır. En basit yollardan biri ilk önce oluşturmaktır.[Menzil](https://reference.aspose.com/cells/cpp/aspose.cells/range) nesneyi kullanın ve ardından kullanarak adını ayarlayın.[Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) yöntem. Excel dosyanızdaki tüm adlandırılmış aralıkları Microsoft Excel aracılığıyla görebilirsiniz.*İsim Yöneticisi*arayüz.
##  **Çalışma Kitabında Adlandırılmış Aralık Oluşturma**
 Aşağıdaki örnek kod, nasıl oluşturulacağını açıklamaktadır.*Adlandırılmış Aralık* Aspose.Cells aracılığıyla.*Adlandırılmış Aralık* oluşturulduğundan içeriden görülebilir.[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) Toplamak. Lütfen bkz[excel dosyasının çıktısını almak](23167006.xlsx) referans için kod tarafından oluşturulur.
##  **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Konsol Çıkışı**
 Aşağıdaki konsol çıktısı değerleri yazdırır:[Tam Metin Al](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) Ve[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) oluşturulan yöntemler*Adlandırılmış Aralık*yukarıdaki kodda.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
