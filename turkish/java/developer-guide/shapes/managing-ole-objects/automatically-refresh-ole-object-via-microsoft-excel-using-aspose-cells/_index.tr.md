---
title: Aspose.Cells kullanarak Microsoft Excel üzerinden OLE nesnesini otomatik olarak yenileyin
type: docs
weight: 730
url: /tr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel'de excel dosyası açıldığında Ole nesnesini yenilemek için [OleObject.AutoLoad](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#AutoLoad) özelliğini sağlar. Bu özellik sayesinde, excel tarafından oluşturulan doğru Ole görüntüsü Ole nesnesinde görüntülenecektir.

{{% /alert %}} 
## **Microsoft Excel kullanarak Aspose.Cells ile Çalışmayan Elemanı Otomatik Yenileme**
Aşağıdaki örnek kod, gerçek dışı bir Ole görüntüsü bulunduran [örnek excel dosyasını](5473423.xlsx) yükler. Ole nesnesi aslında bir Microsoft Word belgesidir, ancak örnek excel dosyası Microsoft Word görüntüsü yerine hayvan görüntüsünü gösterir. Ancak [çıkış excel dosyasını](5473429.xlsx) açarsanız, Microsoft Excel'in doğru Ole görüntüsünü görüntülediğini görebilirsiniz.

Aşağıdaki ekran görüntüsü, Microsoft Excel'de açıldığında [örnek excel dosyasının](5473423.xlsx) nasıl göründüğünü göstermektedir.

![todo:image_alt_text](automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells_1.png)

Aşağıdaki ekran görüntüsü, Microsoft Excel'de açıldığında [çıkış excel dosyasının](5473429.xlsx) nasıl göründüğünü göstermektedir.

![todo:image_alt_text](automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AutomaticallyrefreshOLEobject-AutomaticallyrefreshOLEobject.java" >}}
{{< app/cells/assistant language="java" >}}
