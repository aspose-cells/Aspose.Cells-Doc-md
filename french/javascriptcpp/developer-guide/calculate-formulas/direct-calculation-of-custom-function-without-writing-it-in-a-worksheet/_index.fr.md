---
title: Calcul direct d une fonction personnalisée sans l écrire dans une feuille de calcul avec JavaScript via C++
linktitle: Calcul direct de fonction personnalisée sans l écrire dans une feuille de calcul
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer directement des fonctions personnalisées dans Microsoft Excel sans écrire la fonction dans une feuille de calcul en utilisant JavaScript via C++. Charger un fichier Excel existant ou en créer un nouveau, calculer la fonction personnalisée, et sauvegarder le fichier modifié.
keywords: Aspose.Cells, Excel, fonctions personnalisées, calculs directs, JavaScript via C++, pas besoin d écrire, feuilles de calcul
type: docs
weight: 90
url: /fr/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul**

Ce sujet explique comment vous pouvez calculer directement vos fonctions personnalisées sans les écrire d’abord dans une feuille de calcul. Veuillez utiliser la méthode [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) à cette fin.

Veuillez consulter le code d'exemple suivant qui illustre l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée nommée MyCompany.CustomFunction() et nous calculons sa valeur comme "Aspose.Cells." par nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1 qui est "Bienvenue à " par le moteur de calcul, et la valeur calculée finale retourne comme "Bienvenue à Aspose.Cells.". Comme vous pouvez le voir dans le code, nous n'avons pas écrit notre fonction personnalisée nulle part dans une feuille de calcul et elle est calculée directement par notre propre logique personnalisée.

### **Exemple de programmation**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

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

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Article connexe**

{{% alert color="primary" %}}

[Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
