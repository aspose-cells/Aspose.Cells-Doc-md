---
title: PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 80
url: /tr/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++, PivotTable'ı Excel2003 ile uyumlu hale getirip getirmediğini belirlemek için [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) özelliğini sağlar. Eğer true ise, bir dizenin 255 karakterden az veya eşit olması gerekir, eğer dize 255 karakterden fazlaysa, bu dize kesilir. **False** ise, dizenin bu sınırlaması olmaz. Varsayılan değer **true**'dır.

{{% /alert %}}

## **PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin**

Aşağıdaki örnek kod, [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) özelliğinin kullanımını açıklar. Orijinal dize 383 karakter uzunluğundadır. Fakat [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) özelliği **true** olarak ayarlandığında ve pivot tablosu yeniden tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılır ve 255 karakter uzunluğuna gelir. Ancak [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) özelliği **false** olarak ayarlandığında ve pivot tablosu tekrar tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılmaz ve 383 karakter uzunluğunda kalır. Bu özelliğin daha iyi anlaşılması için kod içindeki yorumları okuyun lütfen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

