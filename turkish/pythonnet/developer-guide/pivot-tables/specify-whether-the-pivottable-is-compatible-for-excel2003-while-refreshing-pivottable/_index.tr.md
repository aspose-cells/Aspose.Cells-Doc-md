---
title: PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 80
url: /tr/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Bu makale, Aspose.Cells for Python via .NET ile PivotTablo yeniden tazeleme sırasında Excel2003 için uyumlu olup olmadığını belirtmeyi göstermektedir.
keywords: Aspose.Cells for Python Excel, Excel Python kütüphanesi, PivotTablo yeniden tazeleme sırasında Excel2003 için uyumlu olup olmadığını belirtin
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, pivot tablosunu yeniden tazeleme sırasında Excel2003 için uyumlu olup olmadığını belirtmek için [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) özelliğini sağlar. true ise, bir dize 255 karakterden az olmalıdır, bu nedenle dize 255 karakterden fazla ise kısaltılacaktır. **false**, bir dizenin yukarıda bahsedilen kısıtlamaya sahip olmayacaktır. Varsayılan değer **true**'dir.

{{% /alert %}}

## **PivotTablo yeniden tazeleme sırasında Excel2003 için uyumlu olup olmadığını belirtme**

Aşağıdaki örnek kod, [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) özelliğinin kullanımını açıklar. Orijinal dize 383 karakter uzunluğundadır. Fakat [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) özelliği **true** olarak ayarlandığında ve pivot tablosu yeniden tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılır ve 255 karakter uzunluğuna gelir. Ancak [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) özelliği **false** olarak ayarlandığında ve pivot tablosu tekrar tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılmaz ve 383 karakter uzunluğunda kalır. Bu özelliğin daha iyi anlaşılması için kod içindeki yorumları okuyun lütfen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
