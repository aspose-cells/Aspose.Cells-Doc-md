---
title: Comment empêcher les utilisateurs d'imprimer un fichier Excel
type: docs
weight: 600
url: /fr/net/how-to-prevent-printing-excel/
description: Découvrez comment empêcher les utilisateurs d'imprimer Excel via le Aspose.Cells for .NET API.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **Scénarios d'utilisation possibles**
Dans notre travail quotidien, le fichier Excel peut contenir des informations importantes. Afin de protéger les données internes diffusées, l'entreprise ne nous autorise pas à les imprimer. Ce document vous expliquera comment empêcher les autres d'imprimer des fichiers Excel.

##  **Comment empêcher les utilisateurs d'imprimer un fichier dans MS-Excel**
Vous pouvez appliquer le code VBA suivant pour protéger votre fichier spécifique à imprimer.
1. Ouvrez votre classeur que vous n'autorisez pas les autres à imprimer.
1. Sélectionnez l'onglet "Développeur" dans le ruban Excel et cliquez sur le bouton "Afficher le code" dans la section "Contrôles". Vous pouvez également maintenir les touches ALT + F11 enfoncées pour ouvrir la fenêtre Microsoft Visual Basic pour Applications.
<br>
<img src="1.png" width=70% />
1. Et puis dans l'Explorateur de Projet de gauche, double-cliquez sur ThisWorkbook pour ouvrir le module et ajoutez quelques codes vba.
<br>
<img src="2.png" width=70% />
1. Ensuite, enregistrez et fermez ce code, puis revenez au classeur. Désormais, lorsque vous imprimerez le fichier d'exemple, son impression ne sera pas autorisée et vous obtiendrez la boîte d'avertissement suivante :
<br>
<img src="3.png" width=70% />

##  **Comment empêcher les utilisateurs d'imprimer un fichier Excel à l'aide de Aspose.Cells for .NET**

L'exemple de code suivant illustre comment empêcher les utilisateurs d'imprimer un fichier Excel :

1.  Chargez le[exemple de fichier](sample.xlsx).
1. Obtenez l'objet VbaModuleCollection à partir de la propriété VbaProject de Workbook.
1. Obtenez l'objet VbaModule via le nom "ThisWorkbook".
1. Définissez la propriété codes de VbaModule.
1.  Enregistrez le fichier exemple dans[format xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}