---
title: Vérifiez si le projet VBA est protégé avec Node.js via C++
linktitle: Vérifier si le projet VBA est protégé
type: docs
weight: 20
url: /fr/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Vérifiez si le projet VBA est protégé dans Node.js**

Vous pouvez déterminer si le projet VBA (Visual Basic Applications) de votre fichier Excel est protégé ou non avec Aspose.Cells en utilisant la propriété [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--).

## **Code d'exemple**

Le code exemple suivant crée un classeur puis vérifie si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie de nouveau. Veuillez consulter la sortie de la console pour référence. Avant la protection, [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) retourne **faux**, mais après, il retourne **vrai**.

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access the VBA project of the workbook.
const vbaProj = wb.getVbaProject();

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - Before Protecting VBA Project: " + vbaProj.isProtected());

// Protect the VBA project.
vbaProj.protect(true, "11");

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - After Protecting VBA Project: " + vbaProj.isProtected());
```

## **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
