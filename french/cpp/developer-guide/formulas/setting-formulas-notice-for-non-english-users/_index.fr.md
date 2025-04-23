---
title: Configuration des formules  Avis aux utilisateurs non anglophones avec C++
linktitle: Définir des formules  Avis aux utilisateurs non anglophones
type: docs
weight: 10
url: /fr/cpp/setting-formulas-notice-for-non-english-users/
description: Apprenez à définir des formules dans Aspose.Cells for C++ avec le style anglais (US) pour les utilisateurs non anglophones.
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge la plupart des formules/fonctions qui font partie de Microsoft Excel. Les développeurs peuvent utiliser ces formules avec soit l'API, soit [les feuilles de calcul du concepteur](/cells/fr/cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporte un ensemble vaste de formules mathématiques, de chaînes, booléennes, de dates/horaires, statistiques, bases de données, recherche et références. Les formules doivent être spécifiées en style anglais (US).

{{% /alert %}} 

## **Avis aux utilisateurs non anglophones**
Il y a deux conseils que les utilisateurs non anglophones doivent suivre lors de la création de formules avec Aspose.Cells :

1. Les formules doivent être saisies en anglais. Par exemple, utilisez l'anglais "=SUM()" et pas l'allemand "=SUMME()".
1. Utilisez toujours une virgule (,) pour délimiter les paramètres de la fonction. Pour certaines options de langue ou paramètres, le délimiteur est un point-virgule, mais Aspose.Cells utilise la virgule selon le style anglais. Par exemple, utilisez "=IF (C5=0,0,C3/C4)" et non "=IF(C5=0;0;C3/C4)".
