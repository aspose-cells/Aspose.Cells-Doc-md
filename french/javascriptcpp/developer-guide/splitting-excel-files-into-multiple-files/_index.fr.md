---
title: Fractionnement de fichiers Excel en plusieurs fichiers
linktitle: Fractionnement de fichiers Excel en plusieurs fichiers
description: Aspose.Cells for JavaScript via C++ est une bibliothèque JavaScript via C++ pour travailler avec des fichiers de feuille de calcul, qui prend en charge le fractionnement d'un seul fichier Excel en plusieurs fichiers. Cet article présentera comment fractionner les fichiers Excel en copiant chaque feuille de calcul dans un classeur distinct et en copiant des plages de cellules spécifiques vers d'autres classeurs.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ bibliothèque, feuille de calcul, fractionner le fichier Excel, copier la feuille de calcul, copier la plage, plusieurs classeurs, enregistrer en fichiers séparés
type: docs
weight: 195
url: /fr/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ prend en charge le fractionnement d'un seul fichier Excel en plusieurs fichiers. Il existe deux méthodes principales : (1) copier chaque feuille de calcul du classeur source dans un nouveau classeur et enregistrer chaque classeur en tant que fichier distinct, et (2) copier une plage de cellules spécifique d’une feuille de calcul vers un nouveau classeur. Les deux approches sont utiles lorsqu’il faut distribuer des sous‑ensembles de données, créer des rapports plus petits pour différents destinataires ou isoler des données pour un traitement individuel.
{{% /alert %}}

## **Introduction**
De nombreux scénarios réels obligent un développeur à découper un fichier Excel unique en plusieurs fichiers plus petits. Par exemple, un classeur peut contenir une feuille de calcul par département, et chaque responsable de département doit recevoir uniquement sa propre feuille. Dans d’autres cas, il peut être nécessaire d’extraire un tableau ou un bloc de données particulier d’une feuille et de l’envoyer sous forme de fichier autonome par courriel, sans révéler le reste du classeur. Les classeurs consolidés de grande taille peuvent également devoir être découpés en morceaux plus petits pour faciliter la manipulation, accélérer le chargement ou permettre le traitement en aval par d’autres systèmes.  
Aspose.Cells for JavaScript via C++ propose deux approches flexibles pour cette tâche. La première parcourt chaque feuille de calcul du classeur source et copie son contenu dans une toute nouvelle instance de `Workbook`, en enregistrant chaque instance en tant que fichier distinct. La seconde se concentre sur une plage de cellules précise au sein d’une feuille et ne copie que cette plage dans un nouveau classeur. Dans les deux cas, le flux général est identique : charger le classeur source avec la classe `Workbook`, accéder aux données via les objets `Worksheet` et `Cells`, transférer le contenu vers un `Workbook` de destination, puis enregistrer le classeur de destination sur le disque.

## **Fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur**

### **Vue d'ensemble de l'approche**
Dans cette approche, le classeur source est ouvert une seule fois, puis pour chaque `Worksheet` de sa collection `Worksheets`, un nouveau classeur de destination est créé. Le contenu de la feuille source est alors copié dans la première feuille du classeur de destination, et le classeur de destination est enregistré sous un nom dérivé du nom de la feuille source. Le résultat est un fichier de sortie par feuille, chaque fichier contenant les données d’une seule feuille source.  
Cette méthode convient lorsque chaque feuille du classeur source représente une unité d’information logiquement indépendante (département, région, mois ou ligne de produit) et que vous souhaitez livrer ou traiter chaque unité séparément.

### **Étapes**
Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur :
1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` et en transmettant le chemin du fichier à son constructeur.  
2. Parcourez la collection `Workbook.Worksheets` à l’aide d’une boucle `for` ou `for...of` afin de traiter chaque `Worksheet` du fichier source.  
3. À l’intérieur de la boucle, créez une nouvelle instance de `Workbook` (un classeur vide) pour la feuille courante.  
4. Copiez le contenu de la feuille source dans la feuille de destination. Cela peut être fait en parcourant les cellules de la collection `Cells` de la feuille source et en écrivant leurs valeurs dans les cellules correspondantes de la feuille de destination, ou en utilisant la méthode `Cells.Copy` pour transférer toute une plage en une seule opération.  
5. Construisez un chemin de fichier de sortie incluant le nom de la feuille source (par exemple `dataDir + worksheet.Name + ".xls"`), de façon à ce que chaque fichier généré possède un nom unique.  
6. Appelez la méthode `Workbook.Save` du classeur de destination pour écrire le fichier sur le disque.  
7. Répétez les étapes 3 à 6 pour chaque feuille suivante jusqu’à ce que toutes les feuilles aient été traitées.

### **Exemple de code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

Le résultat attendu est un ensemble de nouveaux fichiers dans le répertoire de données, un fichier par feuille du classeur source. Chaque fichier porte le nom de la feuille correspondante et contient les données (et éventuellement la mise en forme) de cette seule feuille.

## **Fractionner un fichier Excel en copiant une plage dans un nouveau classeur**

### **Vue d'ensemble de l'approche**
Parfois, les données à fractionner ne correspondent pas à une feuille entière, mais à une région rectangulaire précise d’une feuille, comme `A1:D10` ou une plage nommée représentant un tableau particulier. Dans ces cas‑ci, copier des feuilles entières est superflu, et une approche plus précise est requise : identifier la plage source, copier uniquement cette plage dans un nouveau classeur, puis enregistrer le nouveau fichier.  
Cette approche est idéale lorsque vous devez extraire un seul tableau, un bloc de rapport ou une zone de données d’une feuille plus grande tout en ignorant le contenu non pertinent. Elle est également utile pour exporter des régions sélectionnées par l’utilisateur sous forme de fichiers autonomes.

### **Étapes**
Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant une plage spécifique dans un nouveau classeur :
1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` avec le chemin du fichier.  
2. Récupérez la `Worksheet` cible contenant la plage à copier, soit par indice (par exemple la première feuille), soit par nom dans la collection `Worksheets`.  
3. Identifiez la plage à copier. Il peut s’agir d’une plage codée en dur comme `A1:C10`, d’une plage nommée obtenue via la collection `Worksheet.Cells`, ou d’une plage créée avec `Worksheet.Cells.CreateRange`.  
4. Créez une nouvelle instance de `Workbook` de destination.  
5. Accédez à la première `Worksheet` du classeur de destination (la feuille par défaut).  
6. Copiez la plage source dans la feuille de destination, généralement à partir de la cellule `A1`. La méthode `Cells.Copy` de la collection `Cells` de destination peut être utilisée pour copier toute la plage, ou vous pouvez parcourir les cellules de la plage source et écrire leurs valeurs dans les cellules de destination avec `PutValue`. Des `CopyOptions` optionnels peuvent être fournis pour contrôler ce qui est transféré (valeurs uniquement, valeurs et styles, formules, etc.).  
7. Enregistrez le classeur de destination vers un nouveau chemin de fichier sur le disque à l’aide de la méthode `Workbook.Save`.

### **Exemple de code**
Le résultat attendu est un seul nouveau fichier dans le répertoire de données contenant uniquement les valeurs (et éventuellement la mise en forme) de la plage spécifiée extraite du classeur source. Le fichier de destination n’a aucune relation avec les autres données du fichier source ; il ne contient que la plage extraite, commençant à la cellule `A1` de sa première feuille.

## Related Articles
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)
- [Modifier la mise en page des champs de page dans le tableau croisé dynamique](/cells/fr/javascript-cpp/change-page-field-layout/)
- [Convertir Sparkline en image et HTML dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}