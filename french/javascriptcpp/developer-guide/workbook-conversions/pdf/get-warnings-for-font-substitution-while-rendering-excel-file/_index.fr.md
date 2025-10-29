---
title: Obtenir des avertissements pour la substitution de police lors du rendu d un fichier Excel avec JavaScript via C++
linktitle: Obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF
type: docs
weight: 230
url: /fr/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Apprendre comment obtenir des avertissements pour la substitution de police lors du rendu des fichiers Excel en PDF en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Parfois, lors du rendu d'un fichier Microsoft Excel en PDF, Aspose.Cells substitue des polices. Aspose.Cells propose une fonctionnalité qui permet aux développeurs de savoir quelle police particulière a été substituée en déclenchant un avertissement. Il s'agit d'une fonctionnalité utile qui peut vous aider à identifier pourquoi un PDF créé par Aspose.Cells semble différent du fichier Excel d'origine afin que vous puissiez prendre des mesures appropriées. Par exemple, installer les polices manquantes pour que les résultats du rendu soient identiques.

{{% /alert %}}  

Pour obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF, implémentez l'interface IWarningCallback et définissez la propriété PdfSaveOptions.warningCallback avec votre interface implémentée.

La capture d'écran ci-dessous montre un fichier Excel source que nous utiliserons dans le code suivant. Il contient du texte dans les cellules A6 et A7 dans des polices qui ne sont pas rendues correctement par Microsoft Excel.

|**Toutes les polices ne sont pas rendues correctement**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells va substituer les polices dans les cellules A6 et A7 par des polices appropriées comme indiqué ci-dessous.

|**Polices substituées**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Télécharger le fichier source et le PDF de sortie**  
Vous pouvez télécharger le fichier Excel source et le PDF de sortie à partir des liens suivants

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Code**  
Le code suivant implémente IWarningCallback et définit la propriété PdfSaveOptions.warningCallback avec l'interface implémentée. Désormais, chaque fois qu'une police sera substituée dans une cellule, Aspose.Cells générera un avertissement dans la méthode WarningCallback.Warning().

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **Sortie**  
Après avoir converti le fichier Excel source en PDF, les avertissements sont affichés dans la console de débogage comme ceci :

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode Workbook.calculateFormula juste avant de rendre la feuille de calcul au format PDF. Cela permettra de recalculer les valeurs dépendantes des formules et de rendre les bonnes valeurs dans le PDF.

{{% /alert %}}
