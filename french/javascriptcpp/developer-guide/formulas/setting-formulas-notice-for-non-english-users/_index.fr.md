---
title: Définir des formules  Avis pour les utilisateurs non anglophones avec JavaScript via C++
linktitle: Définir des formules  Avis aux utilisateurs non anglophones
type: docs
weight: 10
url: /fr/javascript-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells supporte la plupart des formules/fonctions qui font partie de Microsoft Excel. Les développeurs peuvent utiliser ces formules avec l'API ou [les feuilles de calcul de conception](/cells/fr/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporte un vaste ensemble de formules mathématiques, de chaînes de caractères, booléennes, de date/heure, statistiques, base de données, recherche et références. Les formules doivent être spécifiées en utilisant le style anglais (US).

{{% /alert %}} 

## **Avis aux utilisateurs non anglophones**
Il y a deux conseils que les utilisateurs non anglophones doivent suivre lors de la création de formules avec Aspose.Cells :

1. Les formules doivent être saisies en anglais. Par exemple, utilisez l'anglais "=SUM()" et pas l'allemand "=SUMME()".
1. Utilisez toujours une virgule (,) pour délimiter les paramètres de la fonction. Pour certaines options de langue ou paramètres, le délimiteur est un point-virgule, mais Aspose.Cells utilise la virgule selon le style anglais. Par exemple, utilisez "=IF (C5=0,0,C3/C4)" et non "=IF(C5=0;0;C3/C4)".
