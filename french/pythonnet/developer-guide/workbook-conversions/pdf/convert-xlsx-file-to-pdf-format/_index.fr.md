---
title: Convertir un fichier XLSX au format PDF
type: docs
weight: 30
url: /fr/python-net/convert-xlsx-file-to-pdf-format/
description: Apprenez comment convertir un fichier XLSX au format PDF avec Aspose.Cells pour l API Python via .NET.
keywords: Convertir un fichier XLSX au format PDF en Python, convertir xlsx en pdf en utilisant Python, xlsx en pdf avec Python, enregistrer xlsx en pdf en python, format xlsx en pdf en Python
---

{{% alert color="primary" %}}

PDF (Portable Document Format) représente des documents indépendamment du logiciel, du matériel et du système d'exploitation utilisé pour créer ces documents. Un fichier PDF peut être un document avec n'importe quelle combinaison de texte, de graphiques et d'images de manière indépendante de l'appareil et de la résolution. Les fichiers PDF sont souvent compressés, de sorte qu'ils occupent moins d'espace que le fichier d'origine.

Parfois, vous devez convertir un fichier Microsoft Excel en PDF. Pour cela, vous avez besoin d'une solution rapide, sécurisée, précise et fiable qui vous permet de distribuer des documents PDF dans le monde entier. Il existe de nombreux outils de conversion qui peuvent accomplir cette tâche. Mais vous devez vous assurer que la mise en page du document Excel d'origine est préservée dans le fichier PDF en sortie. Les images, les graphiques, les formes, la mise en forme des données, les polices, les attributs, les couleurs, les paramètres de configuration de la page, l'orientation du texte, les bordures, les graphiques, etc. doivent être rendus avec précision et précision. [Aspose.Cells pour Python via .NET](https://products.aspose.com/cells/python-net/) assure une conversion de haute qualité.

Ce document est conçu pour fournir une compréhension complète de la manière dont un document Microsoft Excel (contenant des images, des graphiques, une mise en forme, etc.) peut être converti en PDF. À cette fin, il montre comment créer une application console simple dans Visual Studio.Net qui convertit un fichier Excel en PDF en utilisant l'API Aspose.Cells pour Python via .NET. La conversion est effectuée avec un degré élevé de précision et d'exactitude.

{{% /alert %}}

## **Conversion d'Excel en PDF**

Cet exemple utilise un fichier Excel (SampleInput.xlsx) comme modèle. Le classeur contient des feuilles de calcul avec des graphiques et des images. Chaque feuille de calcul contient différents types de formats en utilisant des polices, des attributs, des couleurs, des effets de dégradé et des bordures. Il y a un graphique en colonnes sur la première feuille de calcul et une image sur la dernière.

### **Le fichier Excel modèle**

Le fichier modèle comporte trois feuilles de calcul, y compris des graphiques et une image comme média. La première feuille de calcul comporte des graphiques et la dernière feuille de calcul comporte une image comme indiqué ci-dessous dans les captures d'écran.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|

### **Processus de conversion**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. En procédant ainsi, vous vous assurez que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

### **Résultat**

Lorsque le code ci-dessus est exécuté, un fichier PDF est créé dans le dossier Files de votre répertoire d'application.
Les captures d'écran suivantes montrent les pages PDF. Notez que les en-têtes et pieds de pages sont également conservés dans le fichier PDF de sortie.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|
{{< app/cells/assistant language="python-net" >}}
