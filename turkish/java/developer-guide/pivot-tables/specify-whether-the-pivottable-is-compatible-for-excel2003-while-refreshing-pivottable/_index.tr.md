---
title: PivotTable'ı yenilerken PivotTable'ın Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 880
url: /tr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells şunları sağlar:[PivotTable.IsExcel2003Uyumlu](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)PivotTable'ı yenilerken PivotTable'ın Excel2003 ile uyumlu olup olmadığını belirtmek için kullanabileceğiniz özellik. Eğer**doğru** , bir dize 255 karakterden küçük veya eşit olmalıdır, bu nedenle dize 255 karakterden büyükse kesilecektir. Eğer**YANLIŞ** , bir dize yukarıda belirtilen kısıtlamaya sahip olmayacaktır. varsayılan değer**doğru**.

{{% /alert %}} 
## **PivotTable'ı yenilerken PivotTable'ın Excel2003 için uyumlu olup olmadığını belirtin**
 Aşağıdaki örnek kod, kullanımını açıklar[PivotTable.IsExcel2003Uyumlu](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) Emlak. Orijinal dize 383 karakter uzunluğundadır. Ama ne zaman[PivotTable.IsExcel2003Uyumlu](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) özellik şu şekilde ayarlandı:**doğru** ve pivot tablo yenilendiğinde, pivot tablonun B5 hücresinin verileri kesilir ve 255 karakter uzunluğunda olur. Ancak, ne zaman[PivotTable.IsExcel2003Uyumlu](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) özellik ayarlandı**YANLIŞ** ve pivot tablo tekrar yenilendiğinde, pivot tablonun B5 hücresinin verileri kesilmez ve 383 karakter uzunluğunda kalır. Lütfen indirin[örnek excel dosyası](5472558.xlsx) Bu kodda kullanılan[çıktı excel dosyası](5472557.xlsx) referansınız için onun tarafından oluşturulan konsol çıktısı. Bu özelliği daha iyi anlamak için lütfen kodun içindeki yorumları da okuyun.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Konsol Çıkışı**
Verilen ile yürütüldüğünde yukarıdaki örnek kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
