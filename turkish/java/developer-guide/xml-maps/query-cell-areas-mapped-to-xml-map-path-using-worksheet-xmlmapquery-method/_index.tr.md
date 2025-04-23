---
title: Çalışsheet.XmlMapQuery yöntemini kullanarak XML Haritası Yoluyla Eşlenen Hücre Alanlarını Sorgulama
type: docs
weight: 60
url: /tr/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells kullanarak XML haritası yoluna eşlenen hücre alanlarını sorgulayabilirsiniz. Path varsa, XML haritası içinde o yola ilişkin hücre alanları listesini döndürecektir. [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-) yönteminin ilk parametresi XML öğe yolu, ikinci parametresi sorgulamak istediğiniz XML haritasını belirtir.

## **Worksheet.XmlMapQuery yöntemini kullanarak XML Haritası Yoluna Eşlenmiş Hücre Alanlarını Sorgula**

Aşağıdaki ekran görüntüsü, kodda kullanılan [örnek Excel dosyasını](55541818.xlsx) göstermekte ve kod, XML haritasını iki kez sorgular ve [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-) yöntemi tarafından döndürülen hücre alanları listesini konsolda aşağıda gösterildiği gibi yazdırır.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Konsol Çıktısı**

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

XML verileri çalışsayfalarına içe aktarılabilir. Bazen çalışsayfanın ListeObjelerinden XML yolu gereklidir. Bu özellik, Excel'de Sheet1.ListObjects(1).XmlMap.DataBinding gibi bir ifade kullanılarak elde edilir. Aynı özellik, Aspose.Cells'de [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url) çağrılarak kullanılabilir. Aşağıdaki örnek bu özelliği göstermektedir. Şablon dosyası ve diğer kaynak dosyalar aşağıdaki bağlantılardan indirilebilir:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
{{< app/cells/assistant language="java" >}}
