---
title: Çalışsheet.XmlMapQuery yöntemini kullanarak XML Haritası Yoluyla Eşlenen Hücre Alanlarını Sorgulama
type: docs
weight: 60
url: /tr/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells kullanarak XML haritasına eşlenen hücre alanlarını sorgulayabilirsiniz [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) metodunu kullanarak. Yol varsa, XML haritası içindeki o yola ilişkin hücre alanlarının listesini döndürecektir. [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) metodunun ilk parametresi XML öğe yolunu, ikinci parametre ise sorgulamak istediğiniz bir XML haritasını belirtir.

## **Worksheet.XmlMapQuery yöntemini kullanarak XML Haritası Yoluna Eşlenmiş Hücre Alanlarını Sorgula**

Aşağıdaki ekran görüntüsü, kod içinde kullanılan [örnek Excel dosyası](55541790.xlsx) içindeki XML Haritasını gösteren Microsoft Excel'i göstermektedir. Kod, XML haritasını iki kez sorgular ve aşağıda gösterildiği gibi konsolda [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) metodu tarafından döndürülen hücre alanlarının listesini yazdırır.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **Liste Objesi / Tablo'dan XML Yolunu Al**

XML verileri çalışma sayfalarına alınabilir. Bazı durumlarda, çalışma sayfasının ListObjects'ından XML yoluna ihtiyaç duyulur. Bu özellik, Excel'de Şöyle bir ifade kullanılarak kullanılabilir: Sheet1.ListObjects(1).XmlMap.DataBinding.  Aynı özellik Aspose.Cells'de [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url) çağrısı yaparak kullanılabilir. Aşağıdaki örnek bu özelliği göstermektedir. Şablon dosyası ve diğer kaynak dosyalar aşağıdaki bağlantılardan indirilebilir:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
