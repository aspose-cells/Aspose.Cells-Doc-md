---
title: Comment insérer une image dans une cellule
type: docs
weight: 130
url: /fr/javascript-cpp/how-to-insert-picture-in-cell/
description: Apprenez à insérer une image dans une cellule avec le Script Aspose.Cells for Java via C++.
keywords: Comment insérer une image dans une cellule, insérer une image sur des cellules, placer une image dans une cellule, placer une image sur des cellules, comment placer une image dans une cellule, comment placer une image sur des cellules, passer de l image dans la cellule à l image sur les cellules, passer de l emplacement dans la cellule à l emplacement sur les cellules.
---

## **Scénarios d'utilisation possibles**
L'image ajoute une touche de luminosité à votre feuille de calcul et fournit une représentation visuelle du contenu. Elles facilitent également la compréhension des données et l'émergence d'informations. Bien que vous ayez pu utiliser des images dans Excel depuis de nombreuses années, Excel a récemment activé la fonctionnalité permettant aux images de devenir de véritables valeurs de cellules. Même si la mise en page du dessin est modifiée, il restera toujours attaché aux données. Vous pouvez l'utiliser dans des tableaux, le trier, le filtrer, l'inclure dans des formules, etc.

## **Comment insérer une image dans une cellule en utilisant Excel**
Pour insérer une image dans une cellule d'Excel, suivez ces étapes :

1. Allez dans l'onglet Insertion et cliquez sur l'option Images.
2. Sélectionnez **Placer dans la cellule**. Choisissez l'une des sources suivantes dans le menu déroulant Insérer une image à partir de (**Cet appareil**, **Images stockées** et **Images en ligne**). Cet appareil pour insérer une image depuis votre appareil. Images stockées pour insérer une image à partir d'images stockées. Images en ligne pour insérer une image depuis le web.
<br>
<img src="1.png" width=60% />
3. Sélectionnez l'image et insérez-la dans une cellule.
<br>
<img src="8.png" width=60% />

## **Comment insérer une image sur des cellules en utilisant Excel**
Pour insérer une image sur des cellules dans Excel, suivez ces étapes :

1. Allez dans l'onglet Insertion et cliquez sur l'option Images.
2. Sélectionnez **Placer sur des cellules**. Choisissez l'une des sources suivantes dans le menu déroulant Insérer une image à partir de (**Cet appareil**, **Images stockées** et **Images en ligne**). Cet appareil pour insérer une image depuis votre appareil. Images stockées pour insérer une image à partir d'images stockées. Images en ligne pour insérer une image depuis le web.
<br>
<img src="2.png" width=60% />
3. Sélectionnez l'image et insérez-la sur des cellules.
<br>
<img src="3.png" width=60% />

## **Comment passer de l'image dans la cellule à l'image sur les cellules en utilisant Excel**
Vous pouvez facilement passer de **l'image dans la cellule** à **l'image sur les cellules**. Veuillez suivre ces étapes :
1. Cliquez avec le bouton droit sur la cellule et sélectionnez **Image dans la cellule** > **Placer sur des cellules**. 
<br>
<img src="4.png" width=60% />
2. Le résultat après le changement est le suivant :
<br>
<img src="5.png" width=60% />

## **Comment passer de l'image sur les cellules à l'image dans la cellule en utilisant Excel**
Vous pouvez facilement passer de **l'image sur les cellules** à **l'image dans la cellule**. Veuillez suivre ces étapes :
1. Cliquez avec le bouton droit sur l'image et sélectionnez **Placer dans la cellule**. 
<br>
<img src="6.png" width=60% />
2. Le résultat après le changement est le suivant :
<br>
<img src="7.png" width=60% />

## **Comment insérer une image dans une cellule en utilisant le Script Aspose.Cells for Java via C++**
Insérer une image dans une cellule en utilisant Aspose.Cells. Veuillez consulter le code d'exemple suivant. Après avoir exécuté l'exemple de code, une image sera insérée dans une cellule.
1. Instancier un objet Workbook. 
2. Obtenez la cellule où vous souhaitez insérer l'image.
3. Définissez la propriété Cell.EmbeddedImage. 
4. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). 

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
