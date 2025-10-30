---  
title: XmlMapCollection.Add yöntemi kullanılarak XmlMap içeren çalışma kitabına XML Haritası ekleyin ve Node.js via C++ ile  
linktitle: XmlMapCollection.Add Yöntemi Kullanarak Çalışma Kitabının İçine XML Haritası Ekle  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: XmlMapCollection.Add yöntemi kullanarak çalışma kitabına XML Haritası eklemeyi öğrenin Aspose.Cells for Node.js via C++ ile.  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells, XML Haritasını kitap içine eklemek için kullanabileceğiniz [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) yöntemi sağlar.  

## **XmlMapCollection.Add yöntemini kullanarak İçine 'XmlMap' ekleyin**  

Aşağıdaki örnek kod, Kitap içine XML Haritası ekler ve [çıktı excel dosyasını](5115434.xlsx) olarak kaydeder. Ekran görüntüsü, [örnek.xml](5115433.xml) içinden alınan XML Haritasını gösterir.  

![add-xml-map](add-xml-map.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Add xml map found inside the sample.xml inside the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
