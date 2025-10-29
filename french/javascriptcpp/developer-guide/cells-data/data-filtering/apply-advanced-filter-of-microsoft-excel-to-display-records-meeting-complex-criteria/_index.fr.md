---
title: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 280
url: /fr/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Apprenez comment appliquer un filtre avancé dans Microsoft Excel pour afficher les enregistrements correspondant à des critères complexes en utilisant le script Aspose.Cells for Java via API C++.
keywords: Appliquer un Filtre Avancé en JavaScript via C++, Définir un Filtre Avancé en JavaScript via C++, Ajouter un Filtre Avancé en JavaScript via C++, Créer un Filtre Avancé en JavaScript via C++, Comment ajouter un Filtre Avancé à une plage en JavaScript via C++
---

## **Scénarios d'utilisation possibles**  

Microsoft Excel vous permet d'appliquer le *Filtre avancé* sur les données de la feuille pour afficher les enregistrements répondant à des critères complexes. Vous pouvez appliquer le filtre avancé via la commande *Données > Avancé* comme montré dans cette capture d'écran.  

![todo:image_alt_text](1.png)  

Le script Aspose.Cells for Java via C++ permet également d'appliquer le Filtre Avancé en utilisant la méthode [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Tout comme Microsoft Excel, il accepte les paramètres suivants.  

**isFilter**  

Indique s'il y a filtrage de la liste sur place.  

**plageListe**  

La plage de liste.  

**criteriaRange**  

La plage de critères.  

**copyTo**  

La plage où copier les données.  

**uniqueRecordOnly**  

Afficher ou copier uniquement les lignes uniques.  

## **Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes**  

Le code exemple suivant applique le filtre avancé sur le [Fichier Excel d'exemple](48496692.xlsx) et génère le [Fichier Excel de sortie](48496691.xlsx). La capture d'écran montre les deux fichiers pour comparaison. Comme vous pouvez le voir dans la capture, les données ont été filtrées dans le fichier Excel de sortie selon des critères complexes.  

![todo:image_alt_text](2.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
