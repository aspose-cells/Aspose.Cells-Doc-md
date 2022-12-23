---
title: Worksheet.XmlMapQuery yöntemi kullanılarak XML Eşleme Yoluna Eşlenen Alanlar Cell Sorgusu
type: docs
weight: 60
url: /tr/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Olası Kullanım Senaryoları**

XML eşleme yoluna eşlenen hücre alanlarını Aspose.Cells ile sorgulayabilirsiniz.[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) yöntem. Yol varsa, XML eşlemesi içinde o yolla ilgili hücre alanlarının listesini döndürür. ilk parametresi[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) yöntemi, XML öğesi yolunu belirtir ve ikinci parametre, sorgulamak istediğiniz bir XML eşlemesini belirtir.

## **Worksheet.XmlMapQuery yöntemi kullanılarak XML Eşleme Yoluna Eşlenen Alanlar Cell Sorgusu**

Aşağıdaki ekran görüntüsü, içinde XML Eşlemesini görüntüleyen Microsoft Excel'i göstermektedir.[örnek excel dosyası](55541818.xlsx)kodunda kullanılır. Kod, XML haritasını iki kez sorgular ve XML tarafından döndürülen hücre alanlarının listesini yazdırır.[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) yöntemi aşağıda gösterildiği gibi konsolda.

![yapılacaklar:resim_alternatif_metin](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Liste Nesnesinden/Tablodan XML yolunu al**

XML verileri çalışma sayfalarına alınabilir. Bazen çalışma sayfasının ListObjects öğesinden XML yolu gerekir. Bu özellik Excel'de Sheet1.ListObjects(1).XmlMap.DataBinding gibi bir ifade kullanılarak kullanılabilir. Aynı özellik Aspose.Cells aranarak mevcuttur.[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). Aşağıdaki örnek bu özelliği göstermektedir. Şablon dosyası ve diğer kaynak dosyalar aşağıdaki bağlantılardan indirilebilir:

1. [XMLData.xlsx](XMLData.xlsx)
1. [Ülke Listesi.xml](CountryList.xml)
1. [Yemek Listesi.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
