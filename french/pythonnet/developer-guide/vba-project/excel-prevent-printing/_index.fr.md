---
title: Comment empêcher les utilisateurs d imprimer un fichier Excel
type: docs
weight: 600
url: /fr/python-net/how-to-prevent-printing-excel/
description: Découvrez comment empêcher les utilisateurs d imprimer un Excel via l API Aspose.Cells pour Python via .NET.
keywords: impression excel, empêcher l impression excel, comment empêcher les utilisateurs d imprimer excel, excel empêcher l impression, empêcher l impression d un classeur, Empêcher les utilisateurs d imprimer l ensemble du classeur avec VBA. 
---

## **Scénarios d'utilisation possibles**
Dans notre travail quotidien, il peut y avoir des informations importantes dans le fichier Excel, afin de protéger la diffusion interne des données, l'entreprise ne nous permettra pas de les imprimer. Ce document vous indiquera comment empêcher les autres d'imprimer des fichiers Excel.

## **Comment empêcher les utilisateurs d'imprimer un fichier dans MS-Excel**
Vous pouvez appliquer le code VBA suivant pour protéger votre fichier spécifique contre l'impression.
1. Ouvrez votre classeur que vous ne permettez pas aux autres d'imprimer.
1. Sélectionnez l'onglet "Développeur" dans le ruban Excel et cliquez sur le bouton "Afficher le code" dans la section "Contrôles". Alternativement, vous pouvez maintenir les touches ALT + F11 enfoncées pour ouvrir la fenêtre Microsoft Visual Basic for Applications.
<br>
<img src="1.png" width=70% />
1. Puis dans l'Explorateur de projets à gauche, double-cliquez sur ThisWorkbook pour ouvrir le module, et ajoutez quelques codes VBA.
<br>
<img src="2.png" width=70% />
1. Enregistrez et fermez ce code, puis retournez au classeur. Maintenant, lorsque vous imprimez le fichier d'exemple, il ne sera pas autorisé à être imprimé et vous obtiendrez la boîte d'avertissement suivante :
<br>
<img src="3.png" width=70% />

## **Comment empêcher les utilisateurs d'imprimer un fichier Excel à l'aide d'Aspose.Cells pour Python via .NET**

Le code d'exemple suivant illustre comment empêcher les utilisateurs d'imprimer un fichier Excel :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenez l'objet VbaModuleCollection à partir de la propriété VbaProject de la classe Workbook.
1. Obtenez l'objet VbaModule via le nom "ThisWorkbook".
1. Définissez la propriété codes de VbaModule.
1. Enregistrez le fichier d'exemple au format [xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-Prevent-printing-excel.py" >}}

