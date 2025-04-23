---
title: Excel Verilerini DataTable a Aktar ve Karışık Veri Türünü Kontrol Et
type: docs
weight: 280
url: /tr/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Excel Verilerini DataTable a Aktarmayı ve Karışık Veri Türünü Kontrol Etme Aspose.Cells for .NET API si ile nasıl öğreneceğinizi öğrenin.
keywords: Excel Verilerini DataTable a Aktar ve Karışık Veri Türünü Kontrol Et, Çalışma Kitabı Verilerini DataTable a Aktar ve Karışık Veri Türünü Kontrol Et, Verileri DataTable a Aktar ve Karışık Veri Türünü Kontrol Et, Çalışsayı Verilerini DataTable a Aktar ve Karışık Veri Türünü Kontrol Et.
---

## **Olası Kullanım Senaryoları**
Bir sütun farklı türlerde veri içeriyorsa, verileri DataTable'a aktarırken program, bir tür istisnası atar. Varsayılan olarak, Aspose.Cells, değerlerin veri tipini, sütundaki ilk (hücre) değere dayanarak değerlendirir. Bu nedenle, değer sayıysa, sütunun veri tipinin mantıklı olan sayısal olacağı anlamına gelir. Eğer ilk değer sayı ise ancak sütunda alfasayısal veri veya değerler varsa, dize veri tipi atanmalıdır. Bu durumla başa çıkmak için, lütfen bir sütunda hem sayısal hem de dize değerler varsa [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) aşırı yüklemesini kullanın ve [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) içeren [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Boolean özniteliğini "true" olarak ayarlamayı deneyin.

## **Excel Verilerini DataTable'a Aktar ve Karışık Veri Türünü Kontrol Etme**

Aşağıdaki örnek, [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) özelliğini kullanarak excel verilerini data table'a aktarmayı açıklamaktadır. Lütfen [örnek Excel dosyası](sample.xlsx), ekran görüntüsü ve konsol çıktısı için bakınız.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Ekran Görüntüsü**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol hata ayıklama çıktısı aşağıda yer almaktadır

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
