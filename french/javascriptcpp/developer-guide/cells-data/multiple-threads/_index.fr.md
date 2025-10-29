---
title: Lecture des valeurs de cellule dans plusieurs threads simultanément
linktitle: Plusieurs threads
type: docs
weight: 1800
url: /fr/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Apprenez à lire les valeurs de cellule en plusieurs threads simultanément via l API Aspose.Cells for JavaScript en C++.
keywords: Lire les valeurs de cellule en plusieurs threads simultanément en JavaScript via C++, Aspose.Cells C++ Multithreads, Lecture de données en plusieurs threads
---

{{% alert color="primary" %}}

La nécessité de lire les valeurs de cellule dans plusieurs threads simultanément est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

Pour lire les valeurs des cellules dans plus d’un thread simultanément, définissez [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) sur **true**. Sinon, vous risquez d’obtenir des mauvaises valeurs de cellules.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Crée ensuite deux threads qui lisent simultanément les valeurs de cellules aléatoires.
   Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, un message est affiché.

Si vous commentez cette ligne :

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

alors le message suivant est affiché :

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Multi-Threading Read Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        let testWorkbook;

        const threadLoop = () => {
            const random = Math.random;
            while (true) {
                const row = Math.floor(random() * 10000);
                const col = Math.floor(random() * 100);
                const s = testWorkbook.worksheets.get(0).cells.get(row, col).stringValue;
                if (s !== "R" + row + "C" + col) {
                    console.log("This message will show up when cells read values are incorrect.");
                }
            }
        };

        const testMultiThreadingRead = () => {
            testWorkbook = new Workbook();
            testWorkbook.worksheets.clear();
            testWorkbook.worksheets.add("Sheet1");

            for (let row = 0; row < 10000; row++) {
                for (let col = 0; col < 100; col++) {
                    testWorkbook.worksheets.get(0).cells.get(row, col).value = "R" + row + "C" + col;
                }
            }

            // Uncommenting this line will enable multi-threaded reading    
            //testWorkbook.worksheets.get(0).cells.setMultiThreadReading(true);

            const myThread1 = setInterval(threadLoop, 0);
            const myThread2 = setInterval(threadLoop, 0);

            setTimeout(() => {
                clearInterval(myThread1);
                clearInterval(myThread2);
                document.getElementById('result').innerHTML = '<p style="color: green;">Multi-threading read test completed.</p>';
            }, 5 * 1000);
        };

        document.getElementById('runExample').addEventListener('click', async () => {
            await readyPromise;
            document.getElementById('result').innerHTML = '<p style="color: green;">Starting multi-threading read test. This will run for 5 seconds.</p>';
            testMultiThreadingRead();
        });
    </script>
</html>
```
