---
title: Node.js kullanarak XML i Excel çalışma kitabına C++ ile aktarın
linktitle: XML Haritaları
type: docs
weight: 210
url: /tr/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: XML dosyalarından veriyi Excel e Aspose.Cells for Node.js via C++ kullanarak aktarın.
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-) yöntemi kullanılarak çalışma kitabı içindeki XML haritasını içe aktarmanıza olanak tanır. XML Map'i aşağıdaki adımlarla Microsoft Excel kullanarak içe aktarabilirsiniz:

- **Geliştirici** sekmesini seçin
- XML bölümünde **İçe Aktar**'ı tıklayın ve gerekli adımları izleyin.

İçe aktarma işlemini tamamlamak için XML verilerinizi sağlamanız gerekecektir. Test için kullanabileceğiniz [örnek XML verileri](5115037.txt) burada bulunmaktadır.

{{% /alert %}}

## **Microsoft Excel kullanarak XML Haritası İçe Aktarma**

Aşağıdaki ekran görüntüsü, Microsoft Excel kullanarak XML Haritası İçe Aktarma işlemini göstermektedir.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells for Node.js via C++ kullanarak XML Map içe aktarımı**

Aşağıdaki örnek kod, [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). faydalanmak için nasıl kullanılacağını göstermektedir. Bu, [çıktı excel dosyasını](5115036.xlsx) üretmektedir, bu, ekran görüntüsünde gösterilmiştir.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **İleri konular**
- [XmlMapCollection.add() yöntemi kullanarak çalışma kitabı içine XML Map ekleyin](/cells/tr/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Çalışma Kitabı içinde XML Haritasına bağlı XML Verilerini Dışa Aktar](/cells/tr/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XML Haritasının Kök Eleman Adını Bul](/cells/tr/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Hücreleri XML Haritası Elemanlarına Bağla](/cells/tr/nodejs-cpp/link-cells-to-xml-map-elements/)

