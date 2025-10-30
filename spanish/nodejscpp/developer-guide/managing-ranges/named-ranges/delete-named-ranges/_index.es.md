---
title: Eliminar rangos con nombre con Node.js mediante C++
linktitle: Eliminar rangos con nombres
type: docs
weight: 90
url: /es/nodejs-cpp/Delete-named-ranges/
description: Puedes aprender cómo eliminar nombres definidos o rangos con nombre de archivos de Excel u OpenOffice con Aspose.Cells for Node.js via C++.
---

## **Introducción**
Si hay demasiados nombres definidos o rangos con nombre en los archivos de Excel, debemos eliminar algunos para que no se vuelvan a hacer referencia.

## **Eliminar rango con nombre en MS Excel**

Para eliminar un rango con nombre en Excel, siga estos pasos:
1. Abra Microsoft Excel y abra el libro que contiene el rango con nombre.
2. Vaya a la pestaña "Fórmulas" en la cinta de Excel.
3. Haga clic en el botón "Administrador de nombres" en el grupo "Nombres definidos". Esto abrirá la ventana de diálogo del Administrador de nombres.
4. En la ventana de diálogo del Administrador de nombres, seleccione el rango con nombre que desea eliminar.
5. Haga clic en el botón "Eliminar". Confirme la eliminación cuando se lo soliciten.
6. Haz clic en el botón "Cerrar" para cerrar el cuadro de diálogo del Administrador de nombres.
7. Guarda el libro para guardar los cambios.

## **Elimina rango con nombre usando Aspose.Cells for Node.js via C++**
Con Aspose.Cells for Node.js via C++, puedes eliminar rangos con nombre o nombres definidos por [texto](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) o [índice](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) en la lista.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Nota: si el nombre definido es referido por fórmulas, no se puede eliminar. Solo se puede eliminar la fórmula del nombre definido.

## **Eliminar algunos rangos con nombre**
Cuando eliminamos un nombre definido, debemos verificar si está referido por todas las fórmulas en el archivo.
Para mejorar el rendimiento al eliminar rangos con nombre, podemos eliminarlos algunos juntos.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Eliminar nombres definidos duplicados**
Algunos archivos de Excel se corrompen porque algunos nombres definidos están duplicados. Por lo tanto, podemos eliminar estos nombres duplicados para reparar el archivo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



{{< app/cells/assistant language="nodejs-cpp" >}}
