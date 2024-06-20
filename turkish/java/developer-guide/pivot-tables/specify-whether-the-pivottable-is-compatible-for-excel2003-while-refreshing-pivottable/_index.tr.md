---
title: PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 880
url: /tr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells, [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) özelliğini sağlar. Bu özellikle, pivot tablonun Excel2003 için yeniden oluşturulurken uyumlu olup olmadığını belirlemek için kullanılabilir. **true** ise, dize 255 karakterden küçük veya eşit olmalıdır, bu nedenle dize 255 karakterden daha büyükse kısaltılır. **false** ise, bir dize yukarıda bahsedilen kısıtlamaya sahip olmayacak. Varsayılan değer **true**'dur.

{{% /alert %}} 
## **PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin**
Aşağıdaki örnek kod, [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) özelliğinin nasıl kullanılacağını açıklar. Orijinal dize 383 karakter uzunluğundadır. Ancak [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) özelliği **true** olarak ayarlandığında ve pivot tablosu yeniden oluşturulduğunda, pivot tablosunun B5 hücresinin verisi kısaltılır ve 255 karakter uzunluğunda olur. Bununla birlikte, [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) özelliği **false** olarak ayarlandığında ve pivot tablosu tekrar yeniden oluşturulduğunda, pivot tablosunun B5 hücresinin verisi kısaltılmaz ve 383 karakter uzunluğunda kalır. Lütfen bu kodda kullanılan [örnek excel dosyasını](5472558.xlsx), onun tarafından oluşturulmuş [çıktı excel dosyasını](5472557.xlsx) ve referansınız için onun konsol çıktısını indirin. Lütfen ayrıca daha iyi anlamak için kod içindeki yorumları okuyun.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun verilen [örnek excel dosyası](5472558.xlsx) ile çalıştırıldığında konsol çıktısı şöyledir.



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
