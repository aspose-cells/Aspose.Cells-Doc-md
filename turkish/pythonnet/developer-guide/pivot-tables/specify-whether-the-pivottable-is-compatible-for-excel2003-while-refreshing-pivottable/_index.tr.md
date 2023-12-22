---
title: PivotTable'ı yenilerken PivotTable'ın Excel2003 ile uyumlu olup olmadığını belirtme
type: docs
weight: 80
url: /tr/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Bu makale, PivotTable'ı Aspose.Cells for Python via .NET ile yenilerken PivotTable'ın Excel2003 ile uyumlu olup olmadığının nasıl belirleneceğini gösterir.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET şunları sağlar[**PivotTable.is_excel_2003_uyumlu**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) PivotTable'ı yenilerken PivotTable'ın Excel2003 ile uyumlu olup olmadığını belirtmek için kullanabileceğiniz özellik. Doğruysa, bir dizenin 255 karakterden küçük veya ona eşit olması gerekir; dolayısıyla dize 255 karakterden büyükse kesilecektir. *yanlış** ise, bir dize yukarıda belirtilen kısıtlamaya sahip olmayacaktır. Varsayılan değer *true**'dur.

{{% /alert %}}

##  **PivotTable'ı yenilerken PivotTable'ın Excel2003 ile uyumlu olup olmadığını belirtme**

 Aşağıdaki örnek kod, kullanımını açıklamaktadır.[**PivotTable.is_excel_2003_uyumlu**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) mülk. Orijinal dize 383 karakter uzunluğundadır. Ama ne zaman[**PivotTable.is_excel_2003_uyumlu**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) özellik ayarlandı**doğru** ve pivot tablo yenilenir, pivot tablonun B5 hücresindeki veriler kesilir ve 255 karakter uzunluğunda olur. Ancak ne zaman[**PivotTable.is_excel_2003_uyumlu**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) özellik ayarlandı**YANLIŞ**ve pivot tablo yeniden yenilenir, pivot tablonun B5 hücresindeki veriler kesilmez ve 383 karakter uzunluğunda kalır. Bu özelliğin daha iyi anlaşılması için lütfen kodun içindeki yorumları okuyun.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
