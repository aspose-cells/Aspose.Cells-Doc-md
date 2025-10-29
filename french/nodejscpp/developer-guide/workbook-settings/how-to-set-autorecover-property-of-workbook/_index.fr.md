---  
title: Comment définir la propriété AutoRecover du classeur avec Node.js via C++  
linktitle: Comment définir la propriété AutoRecover du classeur  
type: docs  
weight: 220  
url: /fr/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Apprenez comment définir la propriété AutoRecover d’un classeur en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** dans un classeur, Microsoft Excel désactive la sauvegarde automatique (AutoRecover) sur ce fichier Excel.  

Aspose.Cells fournit la propriété [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) pour activer ou désactiver cette option.  
{{% /alert %}}  

Le code suivant explique comment utiliser la propriété [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) du classeur. Le code lit d’abord la valeur par défaut de cette propriété qui est **true**, puis la définit comme **false** et enregistre le classeur. Ensuite, il relit le classeur et lit la valeur de cette propriété, qui est alors **false**.  

## Code Node.js pour définir la propriété AutoRecover du classeur  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Sortie**  

Voici la sortie de la console du code d'exemple ci-dessus.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
