---
title: XML in eine Excel Arbeitsmappe mit Node.js via C++ importieren
linktitle: XML Maps
type: docs
weight: 210
url: /de/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Daten aus XML Dateien in Excel mithilfe von Aspose.Cells for Node.js via C++ importieren.
---

{{% alert color="primary" %}}

Aspose.Cells erlaubt das Importieren der XML-Karte innerhalb des Arbeitsbuchs mit der [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-)-Methode. Sie können XML-Map mit Microsoft Excel mit den folgenden Schritten importieren:

- Wählen Sie den **Entwickler**-Tab
- Klicken Sie auf **Importieren** im XML-Bereich und befolgen Sie die erforderlichen Schritte.

Sie müssen Ihre XML-Daten bereitstellen, um den Import abzuschließen. Hier ist ein [Beispiel-XML-Daten](5115037.txt), das Sie für Tests verwenden können.

{{% /alert %}}

## **Importieren Sie eine XML-Map mit Microsoft Excel**

Der folgende Screenshot zeigt, wie man eine XML-Map mit Microsoft Excel importiert.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **XML-Map mit Aspose.Cells for Node.js via C++ importieren**

Der folgende Beispielcode zeigt, wie Sie die [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-) nutzen können. Es generiert die [Ausgabedatei Excel](5115036.xlsx) wie in diesem Screenshot gezeigt.

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

## **Erweiterte Themen**
- [XML-Map innerhalb der Arbeitsmappe mit der Methode XmlMapCollection.add() hinzufügen](/cells/de/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportieren Sie XML-Daten, die mit der XML-Map in der Arbeitsmappe verknüpft sind](/cells/de/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Finden Sie den Namen des Stammelements der XML-Map](/cells/de/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Zellen mit XML-Map-Elementen verknüpfen](/cells/de/nodejs-cpp/link-cells-to-xml-map-elements/)

