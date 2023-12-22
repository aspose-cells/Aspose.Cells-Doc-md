---
title: Excel Verilerini herhangi bir Biçimlendirme olmadan DataTable'a aktarma
type: docs
weight: 280
url: /tr/net/export-excel-data-to-datatable-without-any-formatting/
description: Aspose.Cells for .NET API numaralı telefondan Excel Verilerini herhangi bir Formatlama olmadan DataTable'a nasıl aktaracağınızı öğrenin.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

Bazen kullanıcılar excel verilerini herhangi bir biçimlendirme olmadan bir veri tablosuna aktarmak isterler. Örneğin, bir hücre 0,012345 değerine sahipse ve iki ondalık basamağı görüntüleyecek şekilde biçimlendirilmişse, kullanıcı excel verilerini bir veri tablosuna aktardığında, bu 0,012345 olarak değil 0,01 olarak dışa aktarılacaktır. Bu sorunla başa çıkmak için Aspose.Cells sağlandı[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) Bu üç değerden birini alabilen özellik

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 Eğer bunu ayarlayacaksan[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), ardından verileri herhangi bir biçimlendirme olmadan dışa aktarır.

{{% /alert %}}

##  Basit kod

 Aşağıdaki örnek kullanımını açıklamaktadır[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)Excel verilerini herhangi bir biçimlendirmeyle veya biçimlendirme olmadan dışa aktarma özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **Konsol Çıkışı**

Yukarıdaki örnek kodun konsol hata ayıklama çıktısı aşağıdadır

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
