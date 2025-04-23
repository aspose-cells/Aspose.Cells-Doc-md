---
title: Herhangi bir Biçimlendirmeye Gerek Duymadan Excel Verilerini DataTable a Aktar
type: docs
weight: 280
url: /tr/net/export-excel-data-to-datatable-without-any-formatting/
description: Aspose.Cells for .NET API si aracılığıyla Herhangi bir Biçimlendirmeye Gerek Duymadan Excel Verilerini DataTable a Aktarmanın Nasıl Yapılacağını Öğrenin
keywords: Herhangi bir Biçimlendirmeye Gerek Duymadan Excel Verilerini DataTable a Aktar, Hücre Değer Biçimi Stratejisini Belirt, Verileri DataTable a Aktarırken Biçim Stratejisi Ekle 
---

{{% alert color="primary" %}}

Bazı durumlarda kullanıcılar, herhangi bir biçimlendirmeye gerek duymaksızın excel verilerini bir veri tablosuna aktarmak isteyebilir. Örneğin, bir hücrede değer 0.012345 olarak girilmiş ve bu değer iki ondalık basamaklı olarak biçimlendirilmişse, kullanıcı excel verilerini bir veri tablosuna aktardığında 0.012345 yerine 0.01 olarak aktarılacaktır. Bu sorunla başa çıkmak için Aspose.Cells, bu üç değerden birini alabilen [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) özelliğini sağlamıştır

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

Eğer [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy) olarak ayarlarsanız, o zaman verileri herhangi bir biçimlendirmeye gerek duymadan aktaracaktır

{{% /alert %}}

## Örnek Kod

Aşağıdaki örnek, excel verilerini [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) özelliğini kullanarak biçimlendirmesiz olarak bir veri tablosuna aktarmanın nasıl yapılacağını açıklar

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol hata ayıklama çıktısı aşağıda yer almaktadır

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
