---
title: Worksheet.XmlMapQuery yöntemi kullanılarak XML Eşleme Yoluna Eşlenen Alanlar Cell Sorgusu
type: docs
weight: 60
url: /tr/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells ile XML eşleme yoluna eşlenen hücre alanlarını sorgulayabilirsiniz.[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)yöntem. Yol varsa, XML haritası içinde o yolla ilgili hücre alanlarının listesini döndürür. nin ilk parametresi[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)yöntemi, XML öğesi yolunu belirtir ve ikinci parametre, sorgulamak istediğiniz bir XML eşlemesini belirtir.

## **Worksheet.XmlMapQuery yöntemi kullanılarak XML Eşleme Yoluna Eşlenen Alanlar Cell Sorgusu**

 Aşağıdaki ekran görüntüsü, içinde XML Eşlemesini görüntüleyen Microsoft Excel'i göstermektedir.[örnek excel dosyası](55541790.xlsx) kodunda kullanılır. Kod, XML haritasını iki kez sorgular ve XML tarafından döndürülen hücre alanlarının listesini yazdırır.[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)yöntem aşağıda gösterildiği gibi konsolda.

![yapılacaklar:resim_alternatif_metin](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Konsol Çıkışı**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Liste Nesnesinden/Tablodan XML yolunu al**

XML verileri çalışma sayfalarına alınabilir. Bazen çalışma sayfasının ListObjects öğesinden XML yolu gerekir. Bu özellik Excel'de Sheet1.ListObjects(1).XmlMap.DataBinding gibi bir ifade kullanılarak kullanılabilir. Aynı özellik Aspose.Cells aranarak mevcuttur.[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). Aşağıdaki örnek bu özelliği göstermektedir. Şablon dosyası ve diğer kaynak dosyalar aşağıdaki bağlantılardan indirilebilir:

1. [XML Verileri.xlsx](72417285.xlsx)
1. [Ülke Listesi.xml](72417287.xml)
1. [Yemek Listesi.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
