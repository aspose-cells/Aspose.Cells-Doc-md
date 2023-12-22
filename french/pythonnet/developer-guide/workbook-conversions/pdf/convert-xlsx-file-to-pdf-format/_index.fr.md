---
title: Convertir le fichier XLSX au format PDF
type: docs
weight: 30
url: /fr/python-net/convert-xlsx-file-to-pdf-format/
description: Apprenez à convertir un fichier XLSX au format PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

PDF (Portable Document Format) représente les documents indépendamment du logiciel, du matériel et du système d'exploitation utilisés pour créer ces documents. Un fichier PDF peut être constitué de documents contenant n'importe quelle combinaison de texte, de graphiques et d'images, indépendamment du périphérique et de la résolution. Les fichiers PDF sont souvent compressés et occupent donc moins d'espace que le fichier d'origine.

 Parfois, vous devez convertir un fichier Excel Microsoft en PDF. Pour cela, vous avez besoin d'une solution rapide, sécurisée, précise et fiable qui vous permet de distribuer des documents PDF dans le monde entier. Il existe de nombreux outils de conversion qui peuvent effectuer cette tâche. Mais vous devez vous assurer que la mise en page du document Excel d'origine est conservée dans le fichier de sortie PDF. Les images, graphiques, formes, formatage des données, polices, attributs, couleurs, paramètres de mise en page, orientation du texte, bordures, graphiques, etc. doivent être rendus avec exactitude et précision.[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) assure une conversion haute fidélité.

Ce document est conçu pour fournir une compréhension complète de la façon dont un document Excel Microsoft (contenant des images, des graphiques, un formatage, etc.) peut être converti en PDF. À cette fin, il montre comment créer une application console simple dans Visual Studio.Net qui convertit un fichier Excel vers PDF en utilisant Aspose.Cells for Python via .NET API. La conversion est effectuée avec un haut degré de précision et d'exactitude.

{{% /alert %}}

##  **Conversion d'Excel en PDF**

Cet exemple utilise un fichier Excel (SampleInput.xlsx) comme modèle. Le classeur contient des feuilles de calcul avec des graphiques et des images. Chaque feuille de calcul contient différents types de formats utilisant des polices, des attributs, des couleurs, des effets d'ombrage et des bordures. Il y a un histogramme sur la première feuille de calcul et une image sur la dernière.

###  **Le fichier Excel modèle**

Le fichier modèle comporte trois feuilles de calcul, dont des graphiques et une image en tant que média. La première feuille de calcul contient des graphiques et la dernière feuille de calcul contient une image, comme indiqué ci-dessous dans les captures d'écran.

|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| La première feuille de travail**(Prévisions de ventes)**| La deuxième feuille de travail**(Rapport des ventes)**|
|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| La troisième feuille de travail**(La saisie des données)**| La dernière feuille de travail**(Image)**|

###  **Processus de conversion**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

###  **Résultat**

Lorsque le code ci-dessus a été exécuté, un fichier PDF est créé dans le dossier Fichiers de votre répertoire d'application.
Les captures d'écran suivantes montrent les pages PDF. Notez que les en-têtes et pieds de page sont également conservés dans le fichier de sortie PDF.

|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| La première feuille de travail**(Prévisions de ventes)**| La deuxième feuille de travail**(Rapport des ventes)**|
|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![tâche : image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| La troisième feuille de travail**(La saisie des données)**| La dernière feuille de travail**(Image)**|
