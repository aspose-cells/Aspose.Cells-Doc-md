---
title: Excel Verilerini DataTable'a Aktarın ve Karışık Veri Türünü Kontrol Edin
type: docs
weight: 280
url: /tr/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Aspose.Cells for .NET API numaralı telefondan Excel Verilerini DataTable'a nasıl aktaracağınızı ve Karışık Veri Türünü Kontrol Etmeyi öğrenin.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Olası Kullanım Senaryoları**
Bir sütun çeşitli türlerde veriler içeriyorsa, program verileri bir DataTable'a aktarırken bir tür istisnası oluşturacaktır. Veri tablosunu dışa aktarmak için varsayılan olarak Aspose.Cells, sütundaki ilk (hücre) değere dayalı olarak değerlere ilişkin veri türünü değerlendirir. Yani değerin sayı olması, sütunun veri tipinin sayısal olacağı anlamına gelir ki bu da mantıklıdır. İlk değer sayı ise ancak sütunda alfasayısal veriler veya değerler varsa, bir dize veri türü atanmalıdır. Bununla başa çıkmak için lütfen kullanın[ExportDataTable'da aşırı yükleme](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) bu içerir[Veri Tablosunu Dışa Aktarma Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) ve ayarlamayı deneyin[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Bir sütunda hatadan kaçınmak için hem sayısal hem de dize değerleri varsa Boolean niteliğini "true" olarak ayarlayın.

##  **Excel Verilerini DataTable'a Aktarın ve Karışık Veri Türünü Kontrol Edin**

 Aşağıdaki örnek kullanımını açıklamaktadır[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Excel verilerini veri tablosuna aktarma özelliği. Lütfen bkz[örnek Excel dosyası](sample.xlsx)referans olması açısından ekran görüntüsü ve konsol çıktısı.

###  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Ekran görüntüsü**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Konsol Çıkışı**

Yukarıdaki örnek kodun konsol hata ayıklama çıktısı aşağıdadır

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
