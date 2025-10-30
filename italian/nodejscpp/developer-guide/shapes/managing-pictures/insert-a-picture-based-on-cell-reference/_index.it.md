---
title: Inserisci un immagine basata sulla cella di riferimento con Node.js tramite C++
linktitle: Inserisci un immagine basata sul riferimento della cella
type: docs
weight: 150
url: /it/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Impara come inserire un’immagine in un foglio di lavoro basata su una cella di riferimento usando Aspose.Cells for Node.js via C++. Mostra i dati della cella in un’immagine.
---

{{% alert color="primary" %}}
A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento nella Barra delle formule. Aspose.Cells supporta questa funzionalità (Microsoft Excel 2010).
{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells for Node.js via C++ supporta la visualizzazione del contenuto di una cella di un foglio di lavoro in una forma grafica. Puoi collegare l’immagine alla cella che contiene i dati che desideri visualizzare. Poiché la cella o l'intervallo di celle sono collegati all’oggetto grafico, le modifiche apportate ai dati di quella cella o intervallo vengono automaticamente visualizzate nel grafico. Aggiungi un’immagine al foglio di lavoro chiamando il metodo [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) della collezione [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (incapsulato nell’oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Specifica l'intervallo di celle usando l'attributo [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) dell’oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).

### Esempio di codice

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
