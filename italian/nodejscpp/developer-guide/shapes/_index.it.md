---  
title: Inserisci immagini e forme di file Excel con Node.js tramite C++  
linktitle: Forme  
type: docs  
weight: 140  
url: /it/nodejs-cpp/insert-shapes/  
description: Gestisci immagini, oggetti OLE e forme nei file Excel utilizzando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A volte è necessario inserire alcune forme necessarie nel foglio di lavoro. Potresti dover inserire la stessa forma in posizioni diverse del foglio di lavoro. Oppure devi inserire in batch forme nel foglio di lavoro.  
Non preoccuparti! [Aspose.Cells](https://products.aspose.com/cells/) supporta tutte queste operazioni.  
{{% /alert %}}  

Le forme in Excel sono principalmente suddivise nei seguenti tipi:  
- **Immagini**  
- **Oggetti OLE**  
- **Linee**  
- **Rettangoli**  
- **Forme di base**  
- **Frecce a blocco**  
- **Forme di equazione**  
- **Diagrammi di flusso**  
- **Stelle e striscioni**  
- **Callout**  

Questo documento guida selezionerà una o due forme da ciascun tipo per creare dei campioni. Attraverso questi esempi, imparerai come usare [Aspose.Cells](https://products.aspose.com/cells/) per inserire la forma specificata nel foglio di lavoro.  

## **Aggiungi immagini nel foglio di lavoro Excel usando Node.js**  

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:  
Basta chiamare il metodo [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) della raccolta [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Il metodo [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) accetta i seguenti parametri:  

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.  
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.  
- **Nome del file immagine**, il nome del file immagine, completo di percorso.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Inserisci oggetti OLE nel foglio di lavoro Excel usando Node.js**  

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells ha la classe [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), usata per aggiungere un nuovo oggetto OLE alla lista di raccolta. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), rappresenta un oggetto OLE. Ha alcuni membri importanti:  

- La proprietà [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.  
- La proprietà [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) specifica i dati dell'oggetto sotto forma di array di byte. Questi dati verranno visualizzati nel loro programma correlato quando fai doppio clic sull'icona dell'oggetto OLE.  

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Inserisci una linea nel foglio di lavoro Excel usando Node.js**  

La forma della linea appartiene alla categoria **lines**.  

***In Microsoft Excel (ad esempio 2007):***  

- Selezionare la cella dove si desidera inserire la linea  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Quindi, seleziona la linea tra le 'Forme recentemente usate' o 'Linee'  

![](line.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una linea nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

Il seguente esempio mostra come inserire una linea in un foglio di lavoro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](line2.png)  

## **Inserisci una freccia con linea nel foglio di lavoro Excel usando Node.js**  

La forma della freccia della linea appartiene alla categoria **Linee**. È un caso speciale di linea.  

***In Microsoft Excel (ad esempio 2007):***  

- Selezionare la cella dove si desidera inserire la freccia di linea  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona la freccia della linea da 'Forme usate di recente' o 'Linee'  

![](line_arrow1.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una freccia di linea nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire una freccia di linea in un foglio di lavoro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](line_arrow2.png)  

## **Inserire un Rettangolo in un Foglio di Excel utilizzando Node.js**  

La forma del rettangolo appartiene alla categoria **Rettangoli**.  

***In Microsoft Excel (ad esempio 2007):***  

- Selezionare la cella in cui si desidera inserire il rettangolo  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il rettangolo da 'Forme usate di recente' o 'Rettangoli'  

![](rectangle.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire un rettangolo nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un rettangolo in un foglio di lavoro.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](rectangle2.png)  

## **Inserire un Cubo in un Foglio di Excel utilizzando Node.js**  

La forma del cubo appartiene alla categoria **Forme di base**.  

***In Microsoft Excel (ad esempio 2007):***  

- Selezionare la cella in cui si desidera inserire il cubo  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il Cubo da **Forme di base**  

![](cube.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire un cubo nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un cubo in un foglio di lavoro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](cube2.png)  

## **Inserire una freccia di testo in stile callout in un Foglio di Excel utilizzando Node.js**  

La forma della freccia di testo appartiene alla categoria **Freccie di blocco**.  

***In Microsoft Excel (ad esempio 2007):***  

- Seleziona la cella in cui desideri inserire la freccia quadrupla di chiamata  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona la freccia di testo da **Freccie di blocco**  

![](callout_quad_arrow.png)  

***Utilizzando Aspose.Cells***  

Puoi utilizzare il seguente metodo per inserire una freccia quadrupla di chiamata nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire una freccia di testo in uno worksheet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](callout_quad_arrow2.png)  

## **Inserire un simbolo di moltiplicazione in un Foglio di Excel utilizzando Node.js**  

La forma del simbolo di moltiplicazione appartiene alla categoria **Forme di equazione**.  

***In Microsoft Excel (ad esempio 2007):***  

- Seleziona la cella in cui desideri inserire il segno di moltiplicazione  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il simbolo di moltiplicazione da **Forme di equazione**  

![](multiplication_sign.png)  

***Utilizzando Aspose.Cells***  

Puoi utilizzare il seguente metodo per inserire un segno di moltiplicazione nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un simbolo di moltiplicazione in uno worksheet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](multiplication_sign2.png)  

## **Inserire un multidocumento in un Foglio di Excel utilizzando Node.js**  

La forma del multidocumento appartiene alla categoria **FlowCharts**.  

***In Microsoft Excel (ad esempio 2007):***  

- Selezionare la cella in cui si desidera inserire il multidocumento  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Poi, seleziona il multidocumento da **FlowCharts**  

![](multidocument.png)  

***Utilizzando Aspose.Cells***  

Puoi utilizzare il seguente metodo per inserire un multidocumento nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'esempio seguente mostra come inserire un multidocumento in uno worksheet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](multidocument2.png)  

## **Inserire una stella a cinque punte in un Foglio di Excel utilizzando Node.js**  

La forma della stella a cinque punte appartiene alla categoria **Stelle e Bandiere**.  

***In Microsoft Excel (ad esempio 2007):***  

- Seleziona la cella in cui desideri inserire la stella a cinque punte  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Quindi, seleziona la stella a cinque punte da **Stelle e Bandiere**  

![](star_5_points.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una stella a cinque punte nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Il seguente esempio mostra come inserire una stella a cinque punte in un foglio di lavoro.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](star_5_points2.png)  

## **Inserire una nuvola di pensieri nel foglio di lavoro Excel usando Node.js**  

La forma della nuvola di pensieri appartiene alla categoria **Callouts**.  

***In Microsoft Excel (ad esempio 2007):***  

- Seleziona la cella in cui desideri inserire la nuvola a forma di fumetto  
- Fai clic sul menu Inserisci e seleziona Forme.  
- Quindi, seleziona la nuvola di pensieri da **Callouts**  

![](thought_bubble_cloud.png)  

***Utilizzando Aspose.Cells***  

È possibile utilizzare il seguente metodo per inserire una nuvola di pensiero nel foglio di lavoro.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Il seguente esempio mostra come inserire una nuvola di pensieri nel foglio di lavoro.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Eseguendo il codice precedente, otterrai i seguenti risultati:  

![](thought_bubble_cloud2.png)  

## **Argomenti avanzati**  
- [Modifica dei valori di regolazione della forma](/cells/it/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Copia delle forme tra i fogli di lavoro](/cells/it/nodejs-cpp/copy-shapes-between-worksheets/)  
- [Dati in forma non primitiva](/cells/it/nodejs-cpp/data-in-non-primitive-shape/)  
- [Ricerca della posizione assoluta della forma all'interno del foglio di lavoro](/cells/it/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Ottieni punti di connessione dalla forma](/cells/it/nodejs-cpp/get-connection-points-from-shape/)  
- [Gestione dei controlli](/cells/it/nodejs-cpp/managing-controls/)  
- [Aggiungi icone al foglio di lavoro](/cells/it/nodejs-cpp/insert-svg-to-excel/)  
- [Gestione di oggetti OLE](/cells/it/nodejs-cpp/managing-ole-objects/)  
- [Gestione delle immagini](/cells/it/nodejs-cpp/managing-pictures/)  
- [Gestisci Smart Art](/cells/it/nodejs-cpp/managing-smartart/)  
- [Gestione casella di testo](/cells/it/nodejs-cpp/managing-textbox-of-excel/)  
- [Aggiungere un'immagine WordArt al foglio di lavoro](/cells/it/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Aggiornamento dei valori delle forme collegate](/cells/it/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Invia la forma avanti o indietro all'interno del foglio di lavoro](/cells/it/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Gestire le opzioni di forma](/cells/it/nodejs-cpp/managing-shape-options/)  
- [Gestire le opzioni di testo di forma](/cells/it/nodejs-cpp/managing-shape-text-options/)  
- [Estensioni Web - Componenti aggiuntivi di Office](/cells/it/nodejs-cpp/web-extensions-office-add-ins/)  


