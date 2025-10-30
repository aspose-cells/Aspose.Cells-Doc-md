---
title: Başındaki Boş Satır ve Sütunları CSV ye aktarırken kırpın Golang ile C++ kullanarak
linktitle: Başlangıçta Boş Satır ve Sütunları Kırparak
type: docs
weight: 100
url: /tr/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for C++ kullanarak spreadsheet leri CSV formatına dışa aktarırken başlangıçta boş satırları ve sütunları nasıl kırpacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızda başlangıçta boş sütunlar veya satırlar bulunur. Örneğin, bu satırı düşünün:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells, kaydederken önde gelen boş sütunları ve satırları atmaz, ancak Microsoft Excel gibi onları kaldırmak istiyorsanız, Aspose.Cells [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) özelliğini sağlar. Lütfen onu **true** olarak ayarlayın ve tüm önde gelen boş satırlar ve sütunlar kaydederken atılacaktır.

{{% alert color="primary" %}}

Aspose.Cells for C++ 20.4 sürümünden önce, [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) varsayılan değeri **false** idi. 20.4 sürümünden sonra, [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) varsayılan değeri **true**. 

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, [örnek Excel dosyasını](sampleTrimBlankColumns.xlsx) yükler, iki önde gelen boş sütunu bulunan Excel dosyasını önce herhangi bir değişiklik yapmadan CSV formatında kaydeder ve sonra [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) özelliğini **true** olarak ayarlar ve tekrar kaydeder. Ekran görüntüsü, [örnek Excel dosyası](sampleTrimBlankColumns.xlsx), önde gelen boş sütunları kırpmadan oluşturulan [çıktı CSV dosyası](outputWithoutTrimBlankColumns.csv) ve kırparak oluşturulan [çıktı CSV dosyası](outputTrimBlankColumns.csv)'ı gösterir.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
