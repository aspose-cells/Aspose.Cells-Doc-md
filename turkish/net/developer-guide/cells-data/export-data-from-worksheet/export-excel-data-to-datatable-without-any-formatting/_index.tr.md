---
title: Excel Verilerini Formatlamadan DataTable'a Aktarın
type: docs
weight: 280
url: /tr/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

Bazen kullanıcılar excel verilerini herhangi bir biçimlendirme olmadan bir veri tablosuna aktarmak ister. Örneğin, bir hücre 0.012345 değerine sahipse ve iki ondalık basamak gösterecek şekilde biçimlendirilmişse, kullanıcı excel verilerini bir veri tablosuna aktaracağında, 0.012345 olarak değil 0.01 olarak dışa aktarılacaktır. Bu sorunu çözmek için Aspose.Cells sağladı[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) Bu üç değerden birini alabilen özellik

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 olarak ayarlayacaksanız[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), ardından verileri herhangi bir biçimlendirme olmadan dışa aktarır.

{{% /alert %}}

## Basit kod

 Aşağıdaki örnek, kullanımını açıklar[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)Excel verilerini herhangi bir biçimlendirme ile ve biçimlendirme olmadan dışa aktarma özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Konsol Çıkışı**

Aşağıda, yukarıdaki örnek kodun konsol hata ayıklama çıktısı bulunmaktadır.

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
