---
title: Bloquear o desbloquear formas con Node.js vía C++
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/nodejs-cpp/lock-or-unlock-shapes/
description: Este artículo le muestra un código que explica cómo bloquear o desbloquear formas para protegerlas usando la biblioteca Aspose.Cells para Node.js vía C++.
keywords: Node.js Bloquear formas para protegerlas, Cómo bloquear o desbloquear formas usando Node.js vía C++, Bloquear o desbloquear formas para protegerlas en Node.js vía C++.
---

## **Escenarios de uso posibles**

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada. 

Bloquear formas en una hoja de cálculo o documento puede ser beneficioso por varias razones:
1. Prevenir cambios accidentales: bloquear formas asegura que no sean movidas, redimensionadas o eliminadas accidentalmente por los usuarios. Esto es especialmente importante en documentos complejos donde las formas pueden usarse para anotaciones, ilustraciones o como parte del diseño del documento.
1. Mantener el diseño y la estética: las formas a menudo juegan un papel crucial en el diseño y la apariencia visual de un documento. Bloquearlas preserva la apariencia deseada, asegurando que el documento se vea profesional y atractivo.
1. Integridad de datos: en hojas de cálculo, las formas pueden usarse para resaltar puntos de datos importantes, agregar comentarios o proporcionar explicaciones visuales. Bloquear estas formas garantiza que la información contextual que proporcionan permanezca precisa e intacta.
1. Consistencia en documentos compartidos: al colaborar en documentos, diferentes usuarios pueden tener diferentes niveles de experiencia. Bloquear formas ayuda a mantener la coherencia en todo el documento evitando alteraciones no intencionadas.
1. Seguridad: en documentos sensibles, bloquear formas puede ser parte de una estrategia más amplia para proteger la información. Por ejemplo, en informes financieros o documentos legales, las formas bloqueadas pueden usarse para salvaguardar anotaciones o puntos destacados críticos.

A veces, necesitas poder modificar ciertas formas en hojas de cálculo protegidas, en cuyo caso, necesitas desbloquear estas formas. Este artículo presentará en detalle cómo bloquear y desbloquear formas específicas.

## **Cómo bloquear formas para protegerlas en Excel**

Así puedes bloquear celdas en Microsoft Excel:

1. Abre tu archivo de Excel: abre el archivo de Excel que contiene las formas que deseas bloquear.

1. Selecciona la forma: haz clic en la forma que deseas bloquear. También puedes seleccionar varias formas manteniendo presionada la tecla Ctrl y haciendo clic en cada forma.

1. Abre el panel de formato de formas: haz clic derecho en la(s) forma(s) seleccionadas y elige "Tamaño y propiedades." Alternativamente, puedes ir a la pestaña "Formato" en la cinta de opciones, y en el grupo "Tamaño", hacer clic en el lanzador de diálogo (una pequeña flecha) para abrir el panel "Formato de forma".
1. Bloquea la forma: en el panel "Formato de forma", ve a la pestaña "Tamaño y propiedades" (el ícono parece un cuadrado con flechas). En la sección "Propiedades", marca la casilla de "Bloqueado."
<br>
<img src="1.png" width=60% />
1. Protege la hoja de trabajo: Ve a la pestaña "Revisar" en la cinta de opciones. Haz clic en "Proteger hoja". Establece una contraseña (opcional) y elige los permisos que deseas permitir (por ejemplo, seleccionar celdas bloqueadas, formatear celdas, etc.). Haz clic en "Aceptar".
<br>
<img src="2.png" width=60% />

## **Cómo bloquear todas las formas en una hoja especificada**

Para proteger todas las formas en una hoja de cálculo específica, usa el método `worksheet.protect(ProtectionType.Objects)`, como se muestra en el siguiente código de ejemplo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Cómo desbloquear formas específicas en una hoja de cálculo protegida**

Para desbloquear una forma específica en una hoja protegida, usa `shape.isLocked`, como se muestra en el siguiente código de ejemplo.

Nota: `shape.isLocked` solo tiene sentido cuando la hoja de cálculo está protegida.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
