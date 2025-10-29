---
title: Protéger ou déprotéger par mot de passe le classeur partagé avec Node.js via C++
linktitle: Protéger par mot de passe ou désactiver la protection de la feuille de calcul partagée
type: docs
weight: 10
url: /fr/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Scénarios d'utilisation possibles**

Vous pouvez protéger ou déprotéger le classeur partagé avec Microsoft Excel comme indiqué dans la capture d'écran suivante. Aspose.Cells for Node.js via C++ prend également en charge cette fonctionnalité avec les méthodes [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) et [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Protéger par mot de passe ou désactiver la protection de la feuille de calcul partagée**

Le code d'exemple suivant crée un classeur et le protège tout en activant le partage, puis le sauvegarde en tant que [fichier Excel de sortie](55541777.xlsx). La capture d'écran montre que lorsque vous essayez de le déprotéger, Microsoft Excel vous invite à entrer le mot de passe pour le déprotéger.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
