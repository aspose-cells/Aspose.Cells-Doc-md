---  
title: Actualizar días preservando el historial de registros de revisión en libro compartido con Node.js a través de C++  
linktitle: Actualizar días conservando el historial de registros de revisión en un libro compartido  
type: docs  
weight: 80  
url: /es/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Aprende cómo actualizar los días para preservar el historial del registro de revisiones en libros compartidos usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**

Cuando compartes un libro de trabajo, aparece una opción que dice ***Mantener el historial de cambios por N días*** como se muestra en la siguiente captura de pantalla. Puedes actualizar el número de días para preservar el historial usando Aspose.Cells for Node.js via C++ con la propiedad [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar Días de Conservación del Historial de Revisiones en Libro de Trabajo Compartido**

El siguiente código de muestra crea un libro de trabajo vacío, luego lo comparte y actualiza los días de registro de revisión para preservar el historial a 7 días, que normalmente son 30 días. Consulte el [archivo Excel de salida](60489773.xlsx) generado por el código como referencia.

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

