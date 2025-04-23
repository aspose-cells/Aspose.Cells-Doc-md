---  
title: Obtenez ou définissez l identifiant de classe de l objet OLE incorporé avec Node.js via C++  
linktitle: Obtenir ou définir l identifiant de classe de l objet OLE incorporé  
type: docs  
weight: 200  
url: /fr/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Apprenez à obtenir ou définir l identifiant de classe des objets OLE incorporés dans Node.js en utilisant Aspose.Cells via C++.  
---  

## **Scénarios d'utilisation possibles**  
Aspose.Cells offre la propriété [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--) que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe d'un objet OLE incorporé. Les identifiants de classe des objets OLE sont en réalité des GUID, c'est-à-dire des Identifiants Uniques Globaux. Le GUID a toujours une longueur de 16 octets ; par conséquent, les identifiants de classe font également 16 octets. Ils se trouvent souvent dans le Registre Windows et fournissent des informations à l'application hôte sur la façon d'ouvrir les objets OLE incorporés contenant diverses ressources intégrées dans l'application cliente.

## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**  
La capture d'écran suivante montre l'identifiant de classe de l'objet OLE, c'est-à-dire le GUID, qui a été lu à partir du [fichier Excel d'exemple](5115190.xls) contenant l'objet OLE PowerPoint incorporé.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Code d'exemple**  
Veuillez consulter le code exemple suivant exécuté avec le [fichier Excel d'exemple](5115190.xls) et sa sortie console qui affiche l'identifiant de classe de l'objet OLE, c'est-à-dire le GUID. Le GUID imprimé est exactement le même que celui montré dans la capture d'écran.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **Sortie console**  
Voici la sortie console du code exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

