---
title: Définition des formules - Avis pour les utilisateurs non anglophones
type: docs
weight: 20
url: /fr/java/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

 Aspose.Cells prend en charge la plupart des formules/fonctions qui font partie de Microsoft Excel. Les développeurs peuvent utiliser ces formules avec le API ou[feuilles de calcul de concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/). Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de base de données, de recherche et de référence. Les formules doivent être spécifiées en utilisant le style anglais (US).

Il existe deux conseils que les utilisateurs non anglophones doivent suivre lors de la création de formules avec Aspose.Cells :

1. Les formules doivent être saisies en anglais.
 Par exemple, utilisez l'anglais "=SUM()" et non l'allemand "=SUMME()".
1. Utilisez toujours une virgule (,) pour délimiter les paramètres de fonction.
Pour certaines options ou paramètres de langue, le délimiteur des paramètres de fonction est un point-virgule, mais Aspose.Cells utilise la virgule de style anglais. Par exemple, utilisez "=IF (C5=0,0,C3/C4)" et non "=IF(C5=0;0;C3/C4)"

{{% /alert %}}
