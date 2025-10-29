---
title: Obtenir ou définir l’identifiant de classe de l’objet OLE incorporé avec JavaScript via C++
linktitle: Obtenir ou définir l identifiant de classe de l objet OLE incorporé
type: docs
weight: 200
url: /fr/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Apprenez à obtenir ou à définir l’identifiant de classe des objets OLE incorporés en JavaScript en utilisant Aspose.Cells via C++.
---

## **Scénarios d'utilisation possibles**  
Aspose.Cells fournit la propriété [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) que vous pouvez utiliser pour obtenir ou définir l’identifiant de classe d’un objet OLE incorporé. Les identifiants de classe d’objets OLE sont en réalité des GUID, c’est-à-dire des identifiants uniques globaux. Un GUID fait toujours 16 octets; par conséquent, les identifiants de classe font également 16 octets. Ils se trouvent souvent dans le Registre Windows et fournissent des informations à l’application hôte sur la façon d’ouvrir les objets OLE incorporés contenant diverses ressources intégrées dans l’application cliente.

## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**  
La capture d'écran suivante montre l'identifiant de classe de l'objet OLE, c'est-à-dire le GUID, qui a été lu à partir du [fichier Excel d'exemple](5115190.xls) contenant l'objet OLE PowerPoint incorporé.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Code d'exemple**  
Veuillez consulter le code exemple suivant exécuté avec le [fichier Excel d'exemple](5115190.xls) et sa sortie console qui affiche l'identifiant de classe de l'objet OLE, c'est-à-dire le GUID. Le GUID imprimé est exactement le même que celui montré dans la capture d'écran.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **Sortie console**  
Voici la sortie console du code exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
