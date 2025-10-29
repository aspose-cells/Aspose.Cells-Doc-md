---
title: Convertir un fichier XLSX en format PDF avec Golang via C++
linktitle: Convertir un fichier XLSX au format PDF
type: docs
weight: 30
url: /fr/go-cpp/convert-xlsx-file-to-pdf-format/
description: Apprenez comment convertir des fichiers Excel en format PDF en utilisant Aspose.Cells for C++ avec une grande précision et exactitude.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) représente des documents indépendamment du logiciel, du matériel et du système d'exploitation utilisés pour créer ces documents. Un fichier PDF peut contenir une combinaison de texte, graphiques et images de manière indépendante du dispositif et de la résolution. Les fichiers PDF sont souvent compressés, ce qui leur permet de prendre moins d'espace que le fichier original.

Parfois, vous devez convertir un fichier Microsoft Excel en PDF. Pour cela, vous avez besoin d'une solution rapide, sécurisée, précise et fiable qui vous permet de distribuer des documents PDF dans le monde entier. Il existe de nombreux outils de conversion capables d'effectuer cette tâche. Mais vous devez vous assurer que la mise en page du document Excel original est conservée dans le fichier PDF de sortie. Les images, graphiques, formes, formats de données, polices, attributs, couleurs, paramètres de mise en page, orientation du texte, bordures, graphiques, etc., doivent être rendus avec précision et exactitude. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) assure une conversion fidèle.

Ce document est conçu pour fournir une compréhension complète de la façon dont un document Microsoft Excel (contenant des images, des graphiques, des formats, etc.) peut être converti en PDF. À cette fin, il montre comment créer une application console simple en C++ qui convertit un fichier Excel en PDF en utilisant l'API Aspose.Cells. La conversion est effectuée avec un haut degré de précision et d'exactitude.

{{% /alert %}}

## **Conversion d'Excel en PDF**

Cet exemple utilise un fichier Excel (SampleInput.xlsx) comme modèle. Le classeur contient des feuilles avec des graphiques et des images. Chaque feuille contient différents types de formats utilisant des polices, des attributs, des couleurs, des effets de shading, et des bordures. Il y a un graphique en colonnes sur la première feuille et une image sur la dernière.

### **Le fichier Excel modèle**

Le fichier modèle comporte trois feuilles, y compris des graphiques et des images en tant que médias. La première feuille comporte des graphiques, et la dernière une image, comme montré dans les captures d'écran ci-dessous.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|

### **Processus de conversion**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont affichées dans le PDF.

{{% /alert %}}

### **Résultat**

Lorsque le code ci-dessus est exécuté, un fichier PDF est créé dans le dossier Files de votre répertoire d'application.
Les captures d'écran suivantes montrent les pages PDF. Notez que les en-têtes et pieds de pages sont également conservés dans le fichier PDF de sortie.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|
