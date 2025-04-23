---
title: Çalışsheet.XmlMapQuery yöntemini kullanarak XML Haritası Yoluyla Eşlenen Hücre Alanlarını Sorgulama
type: docs
weight: 60
url: /tr/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Olası Kullanım Senaryoları**

XML haritası yoluna göre haritalanan hücre alanlarını sorgulamak için Aspose.Cells for Python via .NET'nin [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) metodunu kullanabilirsiniz. Yol varsa, XML haritası içindeki bu yola ait hücre alanlarının listesi döner. [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) metodunun ilk parametresi XML öğe yolunu, ikinci parametre ise sorgulamak istediğiniz XML haritasını belirtir.

## **Worksheet.XmlMapQuery yöntemini kullanarak XML Haritası Yoluna Eşlenmiş Hücre Alanlarını Sorgula**

Aşağıdaki ekran görüntüsü, kod içinde kullanılan [örnek Excel dosyası](55541790.xlsx) içindeki XML Haritasını gösteren Microsoft Excel'i göstermektedir. Kod, XML haritasını iki kez sorgular ve aşağıda gösterildiği gibi konsolda [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) metodu tarafından döndürülen hücre alanlarının listesini yazdırır.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

XML verisi çalışma sayfalarına içe aktarılabilir. Bazen, çalışma sayfasının ListObjects yapısından XML yolu gerekebilir. Bu özellik, Sheet1.ListObjects(1).XmlMap.DataBinding gibi bir ifade kullanılarak Excel'de kullanılabilir. Aynı özellik Aspose.Cells for Python via .NET'de [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url) çağrılarak erişilebilir. Bu özelliğin örneği aşağıda gösterilmiştir. Şablon dosyası ve diğer kaynak dosyaları aşağıdaki bağlantılardan indirilebilir.

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

