---
title: Enregistrer un fichier Excel
type: docs
weight: 20
url: /fr/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop,sauvegarder,fichier
description: Cet article présente comment enregistrer un fichier dans GridDesktop.
---

{{% alert color="primary" %}} 

En utilisant le contrôle Aspose.Cells.GridDesktop, les utilisateurs ne peuvent pas seulement créer de nouveaux fichiers Excel, mais aussi gérer les fichiers existants. Mais, dans les deux cas, il serait nécessaire d'enregistrer le contenu du Aspose.Cells.GridDesktop. C'est donc le sujet de notre discussion maintenant pour informer nos utilisateurs sur la manière dont ils peuvent enregistrer leur contenu de grille en tant que fichier Excel.

{{% /alert %}} 
## **Introduction**
Pour enregistrer le contenu du contrôle Aspose.Cells.GridDesktop en tant que fichier Excel, Aspose.Cells.GridDesktop fournit les méthodes suivantes.

1. **Enregistrer en tant que fichier**
1. **Enregistrer en tant que flux**
## **Enregistrer le fichier**
Créez une application de bureau et ajoutez deux boutons avec un contrôle GridControl au formulaire. Définissez les propriétés de texte des boutons comme **Enregistrer en tant que fichier** et **Enregistrer en tant que flux** respectivement.
### **Enregistrer sous forme de fichier**
Créez l'événement Click du bouton **Enregistrer sous un fichier** et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Un point important à discuter est que le contrôle Aspose.Cells.GridDesktop contient également une méthode nommée SaveToExcel, qui est également utilisée pour charger le contenu d'un fichier Excel dans la grille. Cependant, cette méthode est maintenant obsolète. Il est donc recommandé à tous les développeurs d'utiliser la méthode ExportExcelFile qui est plus robuste et efficace que l'ancienne.

{{% /alert %}} 
### **Enregistrement sous forme de flux**
Parfois, les développeurs peuvent être amenés à enregistrer le contenu de leur grille dans un flux (par exemple, MemoryStream). Pour faciliter cette tâche, le contrôle Aspose.Cells.GridDesktop prend également en charge l'enregistrement des données de la grille dans un flux. Créez l'événement Click du bouton **Enregistrer sous un flux** et collez le code suivant à l'intérieur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Microsoft Excel prend en charge des feuilles Excel pouvant contenir au maximum 65 536 lignes et 256 colonnes. Aspose.Cells.GridDesktop suit également les mêmes normes. Dans le contrôle Aspose.Cells.GridDesktop, les développeurs peuvent créer plus de lignes et de colonnes que la limite standard, mais lors de l'enregistrement des données de la grille dans un fichier Excel, une exception sera levée. Cela signifie que seules les données contenues dans les 65 536 lignes et 256 colonnes peuvent être enregistrées dans un fichier Excel à l'aide de Aspose.Cells.GridDesktop.

{{% /alert %}}
